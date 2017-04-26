queue()
    .defer(d3.json, "/data")
    .await(makeGraphs);

function makeGraphs(error, recordsJson) {

}
