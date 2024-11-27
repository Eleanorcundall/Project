document.addEventListener("DOMContentLoaded", function() {
    const burgerButton = document.getElementById("burgerButton");
    const nav = document.querySelector('.navbarNav');

    burgerButton.addEventListener("click", function() {

        // Rotate bars if the menu is closed
        Array.from(burgerButton.children).forEach((bar, index) => {
            if (nav.classList.contains("burgerBarClosed")) {
                if (index === 0) {
                    bar.classList.toggle("-rotate-45");
                    bar.classList.toggle("origin-[75%]");
                } else if (index === 1) {
                    bar.classList.toggle("hidden");
                } else if (index === 2) {
                    bar.classList.toggle("rotate-45");
                    bar.classList.toggle("origin-[70%]");
                }
            } else if (nav.classList.contains("burgerBarOpen")) {
                if (index === 0) {
                bar.classList.remove("-rotate-45", "origin-[75%]"); 
                } else if (index === 1) {
                    bar.classList.remove("hidden");
                } else if (index === 2) {
                    bar.classList.remove("rotate-45", "origin-[70%]");
                }
            }
        });

        // Toggle the menu
        if (nav.classList.contains("burgerBarClosed")) {
            nav.classList.remove("burgerBarClosed");
            nav.classList.add("burgerBarOpen");
            nav.classList.remove("hidden"); 
        } else {
            nav.classList.remove("burgerBarOpen");
            nav.classList.add("burgerBarClosed");
            nav.classList.add("hidden");
        }

        // Toggle the aria-expanded attribute
        const isExpanded = burgerButton.getAttribute("aria-expanded") === "true";
        burgerButton.setAttribute("aria-expanded", !isExpanded);
    });
});
