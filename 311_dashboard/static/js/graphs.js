queue()
    .defer(d3.json, "/data")
    .await(makeGraphs);

function makeGraphs(error, recordsJson) {

    var records = recordsJson;
//    var parseTime = d3.timeParse("%Y-%m-%d");
    var dateFormat = d3.time.format("%Y-%m-%d")

    records.forEach(d => {
//        console.log(typeof(d["CreatedDate"]));
//        d["CreatedDate"] = parseTime(d["CreatedDate"]);
        d["CreatedDate"] = dateFormat.parse(d["CreatedDate"])
        d["Longitude"] = JSON.parse(d["Longitude"]);
        d["Latitude"] = JSON.parse(d["Latitude"]);
    });

    // Create a crossfilter instance
    var cf = crossfilter(records);

    // Define dimensions (the columns in the table)
    var complaintTypeDim = cf.dimension(d => d.ComplaintType);
    var dateDim = cf.dimension(d => d.CreatedDate);
    var boroughDim = cf.dimension(d => d.Borough);
    var agencyDim = cf.dimension(d => d.Agency);
    var allDim = cf.dimension(d => d);

    // Group Data
    var numRecordsByDate = dateDim.group().reduceSum(d => d.Latitude.length);
//    var complaintTypeGroup = complaintTypeDim.group();
    var complaintTypeGroup = complaintTypeDim.group().reduceSum(d => d.Latitude.length);
    var boroughGroup = boroughDim.group();
    var agencyGroup = agencyDim.group();
    var all = cf.groupAll();

    // Define min and max dates to be used in charts
    var minDate = dateDim.bottom(1)[0]["CreatedDate"];
    console.log('minDate is ' + minDate);
    var maxDate = dateDim.top(1)[0]["CreatedDate"];
    console.log('maxDate is ' + maxDate);

    // Charts
    var complaintChart = dc.rowChart("#complaint-type-box");
    var timeChart = dc.barChart("#time-chart-box");


    // chart specifications
    timeChart
        .width(650)
        .height(140)
        .margins({top:10, right:50, bottom: 20, left:60})
        .dimension(dateDim)
        .group(numRecordsByDate)
        .transitionDuration(500)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .elasticY(true)
        .yAxis().ticks(4);

    complaintChart
        .width(300)
        .height(200)
        .dimension(complaintTypeDim)
        .group(complaintTypeGroup)
        .elasticX(true)
        .xAxis().ticks(4);

    var map = L.map('map-box');

    var drawMap = function() {
        map.setView([40.730610, -73.935242], 11);
		mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
		L.tileLayer(
			'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
				attribution: '&copy; ' + mapLink + ' Contributors',
				maxZoom: 15,
			}).addTo(map);

		//HeatMap
		var geoData = [];
		_.each(allDim.top(Infinity), function (d) {
//            console.log(d);
//           console.log(d["Latitude"]);
//            console.log(d["Longitude"]);
            var zipped = _.zip(d["Latitude"], d["Longitude"]);
            _.map(zipped, function(coord) {
                geoData.push([coord[0], coord[1], ]);
            });
	      });
		var heat = L.heatLayer(geoData,{
			radius: 10,
			blur: 20,
			maxZoom: 1,
		}).addTo(map);
    };

    drawMap();

    //Update the heatmap if any dc chart get filtered
	dcCharts = [complaintChart,timeChart];

	_.each(dcCharts, function (dcChart) {
		dcChart.on("filtered", function (chart, filter) {
			map.eachLayer(function (layer) {
				map.removeLayer(layer)
			});
			drawMap();
		});
	});

	dc.renderAll();
};
