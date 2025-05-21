document.addEventListener("DOMContentLoaded", function () {
    const showDetailsButtons = document.querySelectorAll(".show-details-btn");
    const detailCards = document.querySelectorAll(".job-details");

    showDetailsButtons.forEach(button => {
        button.addEventListener("click", function () {
            detailCards.forEach(card => {
                card.style.display = "none";
            });

            const jobId = this.id.replace("btn-", "");
            const detailCard = document.getElementById(`details-${jobId}`);
            if (detailCard) {
                detailCard.style.display = "block";
                detailCard.classList.add("page-fade-in");
            }
        });
    });

    const fadeIns = document.querySelectorAll(".page-fade-in");
    fadeIns.forEach((el, i) => {
        el.style.animationDelay = `${i * 100}ms`;
    });
});

document.addEventListener('DOMContentLoaded', function() {
  var applyModal = document.getElementById('applyModal');
  applyModal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget;
    var jobId = button.getAttribute('data-job-id');
    document.getElementById('modalJobId').value = jobId;
  });
});