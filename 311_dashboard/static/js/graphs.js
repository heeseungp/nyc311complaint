queue()
    .defer(d3.json, "/data")
    .await(makeGraphs);

function makeGraphs(error, recordsJson) {

    var records = recordsJson;
    var dateFormat = d3.timeFormat("%Y-%m-%d");

    records.forEach(d => {
        d["CreatedDate"] = dateFormat.parse(d["CreatedDate"]);
        d["Longitude"] = +d["Longitude"];
        d["Latitude"] = +d["Latitude"];
    });

    // Create a crossfilter instance
    var cf = crossfilter(records);

    // Define dimensions (the columns in the table)
    var complaintTypeDim = cf.dimension(d => d.ComplaintType);
    var dateDim = cf.dimension(d => d.CreatedDate);
    var boroughDim = cf.dimension(d => d.Borough);
    var agencyDim = cf.dimension(d => d.Agency);
    var latDim = cf.dimension(d => d.Latitude);
    var longDim = cf.dimension(d => d.Longitude);
    var allDim = cf.dimension(d => d);

    // Group Data
    var numRecordsByDate = dateDim.group();
    var complaintTypeGroup = complaintTypeDim.group();
    var boroughGroup = boroughDim.group();
    var agencyGroup = agencyDim.group();
    var all = cf.groupAll();

    // Define min and max dates to be used in charts
    var minDate = dateDim.bottom(1)[0]["CreatedDate"];
    var maxDate = dateDim.top(1)[0]["CreatedDate"];

    console.log(minDate);
    console.log(maxDate);
}
