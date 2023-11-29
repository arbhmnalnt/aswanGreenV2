const contactUsForm = document.querySelector(".contact-us__form");
const submitBtn = document.querySelector(".contact-us__form button");
const successMsg = document.querySelector(".success-message");

contactUsForm.addEventListener("submit", (e) => {
  e.preventDefault();

  submitBtn.classList.add("btn--loading");

  setTimeout(() => {
    contactUsForm.classList.add("hidden");
    successMsg.classList.remove("hidden");
  }, 1500);
});
