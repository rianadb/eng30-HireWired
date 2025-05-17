const illustrations = [
    "/static/images/illustration1.png",
    "/static/images/illustration2.png",
    "/static/images/illustration3.png"
];
let currentIndex = 0;

// Load the first illustration on page load
window.onload = function() {
    const illustration = document.getElementById("illustration");
    illustration.src = illustrations[currentIndex];
};

function changeIllustration() {
    currentIndex = (currentIndex + 1) % illustrations.length;
    const illustration = document.getElementById("illustration");
    illustration.src = illustrations[currentIndex];
}

setInterval(changeIllustration, 3000);