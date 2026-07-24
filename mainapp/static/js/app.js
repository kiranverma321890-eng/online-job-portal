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
// AUTH FORM VALIDATION & PASSWORD UI 
(function(){
  document.querySelectorAll('.toggle-password').forEach(function(toggle){
    toggle.addEventListener('click',function(){
      const input=document.getElementById(toggle.dataset.target);
      const icon=toggle.querySelector('i');
      if(input.type==='password'){input.type='text';icon.classList.replace('bi-eye-slash-fill','bi-eye-fill');}
      else{input.type='password';icon.classList.replace('bi-eye-fill','bi-eye-slash-fill');}
    });
  });

  const regPassword=document.getElementById('regPassword');
  const strengthFill=document.getElementById('passwordStrengthFill');
  const strengthText=document.getElementById('passwordStrengthText');
  if(regPassword){
    regPassword.addEventListener('input',function(){
      const val=regPassword.value;
      let score=0;
      if(val.length>=8)score++;
      if(/[A-Z]/.test(val)&&/[a-z]/.test(val))score++;
      if(/[0-9]/.test(val)&&/[^A-Za-z0-9]/.test(val))score++;
      strengthFill.className='password-strength-fill';
      if(score<=1){strengthFill.classList.add('weak');strengthText.textContent='Weak password';}
      else if(score===2){strengthFill.classList.add('medium');strengthText.textContent='Medium strength';}
      else{strengthFill.classList.add('strong');strengthText.textContent='Strong password';}
    });
  }

  const confirmPassword=document.getElementById('regConfirmPassword');
  if(confirmPassword){
    confirmPassword.addEventListener('input',function(){
      confirmPassword.setCustomValidity(confirmPassword.value!==regPassword.value?'mismatch':'');
    });
  }

  document.querySelectorAll('.needs-validation').forEach(function(form){
    form.addEventListener('submit',function(e){
      if(!form.checkValidity()){e.preventDefault();e.stopPropagation();}
      form.classList.add('was-validated');
    },false);
  });
})();