// Carousel
var carousel = document.getElementById("carousel");
var slides = carousel.getElementsByClassName("slide");
var dots = document.getElementById("dots-container").getElementsByClassName("dot");
var nbrSlides = slides.length;
var currentSlide = 0;

function updateSlide() {
    currentSlide += 1;
    if(currentSlide == nbrSlides) {
        currentSlide = 0;
    }
    showSlide(currentSlide);
}

function showSlide(x) {
    Array.prototype.forEach.call(slides, (slide) => {
        slide.className = "slide";
    });
    Array.prototype.forEach.call(dots, (dot) => {
        dot.className = "dot";
    });
    slides[x].className = "slide slide-active";
    dots[x].className = "dot dot-active";
}

setInterval(updateSlide, 5000);

Array.prototype.forEach.call(dots, (dot, i) => {
    dot.addEventListener("click", () => {
        showSlide(i);
    });
});
