/*
 the script mus be loaded after the map div is defined.
 otherwise this will not work (we would need a listener to
 wait for the DOM to be fully loaded).

 Just put the script tag below the map div.

 The source code below is the example from the leaflet start page.
 */

var map = L.map("map", { minZoom: 2, maxZoom: 6 }).setView([0, 0], 3);

L.tileLayer("https://{s}.tile.osm.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

L.marker([51.5, -0.09])
  .addTo(map)
  .bindPopup("HAHAHAHA I AM TEH 2ND ONE")
  .openPopup();

L.marker([5, -0.08])
  .addTo(map)
  .bindPopup("A pretty CSS3 popup.<br> Easily customizable.");

// var popup = L.popup()
//     .setLatLng([51.513, -0.09])
//     .setContent("I am a standalone popup.")
//     .openOn(map); // andles automatic closing of a previously opened popup when opening a new one
