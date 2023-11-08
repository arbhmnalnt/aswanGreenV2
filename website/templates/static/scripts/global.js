const navToggler = document.querySelector(".nav-toggler");
const navbarNav = document.querySelector(".navbar__nav");
const navClose = document.querySelector(".nav__close");
const overlay = document.createElement("div");
overlay.classList.add("overlay");

navToggler.addEventListener("click", () => {
  navbarNav.classList.toggle("active");

  if (overlay.parentElement === document.body) {
    overlay.remove();
  } else {
    document.body.appendChild(overlay);
  }
});

overlay.addEventListener("click", () => {
  navbarNav.classList.remove("active");
  overlay.remove();
});

navClose.addEventListener("click", () => {
  navbarNav.classList.remove("active");
  overlay.remove();
});

window.addEventListener("load", () => {
  const preloader = document.querySelector(".preloader");

  if (preloader !== null) {
    preloader.remove();
  }
});
