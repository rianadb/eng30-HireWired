document.addEventListener("DOMContentLoaded", function () {
    const categories = [
        { icon: "fas fa-tools", title: "Skilled Work", description: "Explore skilled work categories." },
        { icon: "fas fa-truck", title: "Logistics", description: "Opportunities in transportation and logistics." },
        { icon: "fas fa-hard-hat", title: "Construction", description: "Construction-related job openings." },
        { icon: "fas fa-user-cog", title: "Technical Support", description: "Jobs in maintenance and technical support." },
        { icon: "fas fa-tractor", title: "Agriculture and Groundskeeping", description: "Farming, landscaping, and outdoor maintenance positions." },
        { icon: "fas fa-broom", title: "Building and Grounds Maintenance", description: "Facility upkeep and property maintenance roles." }
    ];

    
    const carousel = document.getElementById("carousel");
    const prevBtn = document.querySelector(".prev");
    const nextBtn = document.querySelector(".next");
    let currentIndex = 0;
    const visibleCount = 4;

    function renderCarousel() {
        carousel.innerHTML = "";
        for (let i = 0; i < visibleCount; i++) {
            const index = (currentIndex + i) % categories.length;
            const item = categories[index];
            const categoryElement = document.createElement("div");
            categoryElement.classList.add("category-item");
            if (i === visibleCount - 1) {
                categoryElement.classList.add("blur");
            }

            // Setting up the category item HTML
            categoryElement.innerHTML = `
                <i class="${item.icon}"></i>
                <h3 class="category-text">${item.title}</h3>
                <p class="category-description">${item.description}</p>
            `;

            // Initially hide the description
            categoryElement.querySelector(".category-description").style.display = "none";

            // Event listener for hover effect
            categoryElement.addEventListener("mouseenter", function () {
                const titleElement = categoryElement.querySelector(".category-text");
                const descriptionElement = categoryElement.querySelector(".category-description");
                
                // Hide title and show description
                titleElement.style.display = "none";
                descriptionElement.style.display = "block";
            });

            categoryElement.addEventListener("mouseleave", function () {
                const titleElement = categoryElement.querySelector(".category-text");
                const descriptionElement = categoryElement.querySelector(".category-description");
                
                // Show title and hide description
                titleElement.style.display = "block";
                descriptionElement.style.display = "none";
            });

            carousel.appendChild(categoryElement);
        }
    }

    function nextItem() {
        currentIndex = (currentIndex + 1) % categories.length;
        renderCarousel();
    }

    function prevItem() {
        currentIndex = (currentIndex - 1 + categories.length) % categories.length;
        renderCarousel();
    }

    nextBtn.addEventListener("click", nextItem);
    prevBtn.addEventListener("click", prevItem);

    renderCarousel();
});
