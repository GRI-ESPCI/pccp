// Mobile navbar
function toggleNavbar() {
    var nav = document.getElementById('nav');
    if(nav.className === "nav") {
        nav.className += " navresponsive";
    } else {
        nav.className = "nav"
    }
}

var toggle = document.getElementById("toggle");
toggle.addEventListener("click", toggleNavbar);
