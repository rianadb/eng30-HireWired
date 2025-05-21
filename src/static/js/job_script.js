document.addEventListener("DOMContentLoaded", function () {
    // Job Details
    const showDetailsButtons = document.querySelectorAll(".show-details-btn");
    const detailCards = document.querySelectorAll(".job-details");

    showDetailsButtons.forEach(button => {
        button.addEventListener("click", function () {
            detailCards.forEach(card => card.style.display = "none");
            const jobId = this.id.replace("btn-", "");
            const detailCard = document.getElementById(`details-${jobId}`);
            if (detailCard) {
                detailCard.style.display = "block";
                detailCard.classList.add("page-fade-in");
            }
        });
    });

    // Animation delay
    document.querySelectorAll(".page-fade-in").forEach((el, i) => {
        el.style.animationDelay = `${i * 100}ms`;
    });

    // Apply modal job id
    const applyModal = document.getElementById('applyModal');
    if (applyModal) {
        applyModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;
            const jobId = button.getAttribute('data-job-id');
            document.getElementById('modalJobId').value = jobId;
        });
    }

    // Salary min update
    const salaryInput = document.getElementById('jobSalary');
    const rateType = document.getElementById('rateType');

    if (salaryInput && rateType) {
        const updateMinSalary = () => {
            const isDayRate = rateType.value === 'day';
            salaryInput.setAttribute('min', isDayRate ? 610 : 0);
            if (isDayRate && parseFloat(salaryInput.value) < 610) {
                salaryInput.value = 610;
            }
        };

        // Initial and on change
        updateMinSalary();
        rateType.addEventListener('change', updateMinSalary);
    }
});

