$(document).ready(function() {
    $("#time").slider({
        id: "slider",
        min: 0,
        max: 10,
        range: true,
        value: [3,7]
    });
});