document.addEventListener("DOMContentLoaded", function () {
    try {
        const showJobDetailsButtons = document.querySelectorAll(".show-details-btn");
        const detailCards = document.querySelectorAll(".job-details");
        showJobDetailsButtons.forEach((button) => {
            button.addEventListener("click", function () {
                // const jobId = this.getAttribute("data-job-id");
                // const jobDetails = document.querySelector(`.job-details-${jobId}`);
                // if (jobDetails) {
                //     jobDetails.classList.toggle("hidden");
                // }

                detailCards.forEach((card) => {
                    card.style.display = "none";
                });
                console.log("Button clicked");
                const jobId = button.id;
                const jobDetails = document.getElementById('details-' + jobId);
                if (jobDetails) {
                    jobDetails.style.display = "block";
                }
            });
        });
    }

    catch {

    }
});