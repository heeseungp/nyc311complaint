// initialize the map
var map = L.map('map', {zoomControl:false}).setView([40.7128, -74.0059], 11);

L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
{
  maxZoom: 15,
  minZoom: 11
}).addTo(map);

// LOADING ZIPCODES
var nyczipcodefile = "static/zipcode/nyczipcodes.geojson";
$.getJSON(nyczipcodefile, function(data) {
  geojsonlayer = L.geoJson(data, {
    style: { color: "#000000", fillColor: "#f7f7f7", weight: 2 },
    onEachFeature: onEachFeatureZipCode
  }).addTo(map);
  geojsonlayer.bringToFront();
});

function onEachFeatureZipCode(feature, layer) {
  layer.on('click', function(e) {
    selected_zip = feature.properties.postalCode;
    console.log(selected_zip);
  });
}

var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent(selected_zip)
        .openOn(map);
}

map.on('click', onMapClick);



//first initial
var complaint = $('input[name=complaint]:checked').val();
var month = document.getElementById("monthSlider").value;
var normalized_path = "";
if($('input[name=toggleType]:checked').val() == "UnNormalized") normalized_path = "unnormalized";
  else normalized_path = "normalized";

console.log(complaint);
console.log(month);
console.log(normalized_path);

var imgPath = 'static/img/mapimg/' +  "unnormalized" + '/' + complaint + '/' + complaint + '_' + month + '.png';
var imageUrl = imgPath;
var imageBounds = [[40.484300, -74.275076], [40.915760, -73.695027]]; //working
  // imageBounds = [[40.495628, -74.255819], [40.913253, -73.700065]]; //min and max
var finalimage = L.imageOverlay(imageUrl, imageBounds);
map.addLayer(finalimage);

//change imagelayer from radiobutton
function checkComplaint(complaint) {
  document.getElementById('dropDownTitle').innerHTML = complaint;
  document.getElementById('dropDownTitle').style.backgroundColor = "#e6e6e6";
  if(map.hasLayer(finalimage)) {
    map.removeLayer(finalimage);
  }

  month = document.getElementById("monthSlider").value; 
  if($('input[name=toggleType]:checked').val() == "UnNormalized") normalized_path = "unnormalized";
  else normalized_path = "normalized";

  imgPath = 'static/img/mapimg/' + normalized_path + '/' + complaint + '/' + complaint + '_' + month + '.png';
  imageUrl = imgPath;
  ImageBounds = [[40.484300, -74.275076], [40.915760, -73.695027]]; //working
    // imageBounds = [[40.495628, -74.255819], [40.913253, -73.700065]]; //min and max
  finalimage = L.imageOverlay(imageUrl, imageBounds).addTo(map);
  finalimage.bringToBack();
}


//change imagelayer from toggle
function checkToggle(value) {
  if(map.hasLayer(finalimage)) {
    map.removeLayer(finalimage);
  }
  
  complaint = $('input[name=complaint]:checked').val();
  month = document.getElementById("monthSlider").value;
  if(value == "Normalized") normalized_path = "normalized";
  else normalized_path = "unnormalized";

  imgPath = 'static/img/mapimg/' + normalized_path + '/' + complaint + '/' + complaint + '_' + month + '.png';
  imageUrl = imgPath;
  ImageBounds = [[40.484300, -74.275076], [40.915760, -73.695027]]; //working
    // imageBounds = [[40.495628, -74.255819], [40.913253, -73.700065]]; //min and max
  finalimage = L.imageOverlay(imageUrl, imageBounds).addTo(map);
  finalimage.bringToBack();      
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//change imagelyer from slider
var monthNames = ["January", "Februrary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var yr = "";
var whichmonth = "";
var combo_yrMonth = "";
$('#monthSlider').slider({
  formatter: function(value) {
    return 'Current value: ' + value;
  }
});    

$("#monthSlider").on("slide", function(slideEvt) {
  whichmonth = (slideEvt.value% 12) + 1;
  yr = Math.floor(slideEvt.value/12);

  // just the display
  $("#timeValue1").text(monthNames[whichmonth-1] + " 201" + yr);

  if(whichmonth < 10) {
    whichmonth = "0" + whichmonth;
  }
  combo_yrMonth = "201" + yr + "-" + whichmonth + "-00" + " 00:00:00";

  // post data
  $("#from").val(combo_yrMonth);

  //check if the finalimage layer is on leaflet
  if(map.hasLayer(finalimage)) {
    map.removeLayer(finalimage);
  }

  //grabbing the which complaint
  complaint = $('input[name=complaint]:checked').val();
  //grabbing which month
  month = slideEvt.value;
  //check if toggleType is unnormalized
  if($('input[name=toggleType]:checked').val() == "UnNormalized") normalized_path = "unnormalized";
  else normalized_path = "normalized";
  //set imgpath
  imgPath = 'static/img/mapimg/' + normalized_path + '/' + complaint + '/' + complaint + '_' + month + '.png';
  imageUrl = imgPath;
  ImageBounds = [[40.484300, -74.275076], [40.915760, -73.695027]]; //working
    // imageBounds = [[40.495628, -74.255819], [40.913253, -73.700065]]; //min and max

  finalimage = L.imageOverlay(imageUrl, imageBounds).addTo(map);
  finalimage.bringToBack();
});