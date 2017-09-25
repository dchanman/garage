"use strict";

function toggleClicked() {
    console.log("Clicked!");
    var req = new XMLHttpRequest();
    req.onreadystatechange = function () {
        if (req.readyState === 4 && req.status === 200) {
            console.log("success");
        }
    };
    req.open("GET", "api/toggle", true);
    req.send(null);
}

window.onload = function () {
    var toggle = document.getElementById("toggle");
    toggle.addEventListener("click", toggleClicked);
};