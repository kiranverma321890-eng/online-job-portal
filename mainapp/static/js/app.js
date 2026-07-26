// STATISTICS COUNTER
document.addEventListener("DOMContentLoaded", function () {

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const updateCounter = () => {

            const target = +counter.dataset.target;
            const current = +counter.innerText.replace(/\D/g, '');

            const increment = target / 100;


            if (current < target) {

                counter.innerText =
                    Math.ceil(current + increment) +
                    (target === 98 ? "%" : "+");

                setTimeout(updateCounter, 20);

            }
            else {

                counter.innerText =
                    target +
                    (target === 98 ? "%" : "+");

            }

        };


        updateCounter();

    });

});
// STATISTICS COUNTER END

// FAQ SEARCH
document.addEventListener("DOMContentLoaded", () => {
    const search = document.getElementById("faqSearch");
    if (!search) return;

    const items = document.querySelectorAll(".faq-item");

    search.addEventListener("keyup", function () {
        const value = this.value.toLowerCase();

        items.forEach(item => {
            const text = item.innerText.toLowerCase();
            item.style.display = text.includes(value) ? "block" : "none";
        });
    });
});
document.querySelectorAll(".faq-category").forEach(card => {
    card.addEventListener("mouseenter", () => card.classList.add("shadow-lg"));
    card.addEventListener("mouseleave", () => card.classList.remove("shadow-lg"));
});
// CONTACT FORM VALIDATION 
(function () {
    const form = document.getElementById('contactForm');
    if (!form) return;
    const successMsg = document.getElementById('formSuccessMsg');
    form.addEventListener('submit', function (e) {
        if (!form.checkValidity()) {
            e.preventDefault(); e.stopPropagation();
        } else {
            // AJAX submission point - replace with fetch to Django view if not using full page POST
            // e.preventDefault();
            successMsg.classList.remove('d-none');
        }
        form.classList.add('was-validated');
    }, false);
})();