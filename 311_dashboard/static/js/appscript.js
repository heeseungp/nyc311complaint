var mymap = L.map('mapid').setView([40.730610,-73.935242], 10);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiYXNoYWgwMDAiLCJhIjoiY2oxenV3Y2J2MDMzdTMzbnV3d2lsNTN1eiJ9.npr294JoMyA4_TmC8f-4hQ', {
		maxZoom: 18,
		id: 'mapbox.streets'
	}).addTo(mymap);