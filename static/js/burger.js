document.addEventListener("DOMContentLoaded", function() {
    const burgerButton = document.getElementById("burgerButton");
    const nav = document.querySelector('.navbarNav');
    console.log(nav)
    const bar1 = document.getElementById("bar1");
    const bar2 = document.getElementById("bar2");
    const bar3 = document.getElementById("bar3");

    burgerButton.addEventListener("click", function() {
        // Toggle the menu
        console.log(burgerButton)
        console.log(nav)
        nav.classList.toggle("hidden");

        // Rotate bars into a cross
        bar1.classList.toggle("rotate-45");
        bar2.classList.toggle("opacity-0");
        bar3.classList.toggle("-rotate-45");

        // Toggle the aria-expanded attribute
        const isExpanded = burgerButton.getAttribute("aria-expanded") === "true";
        burgerButton.setAttribute("aria-expanded", !isExpanded);
    });
});
