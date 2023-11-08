document.addEventListener("DOMContentLoaded", () => {
  new Splide(".hero-carousel", {
    direction: "rtl",
    breakpoints: { 767: { arrows: !1 } },
  }).mount();

  new Splide(".our-activities__slider", {
    direction: "rtl",
    perPage: 3,
    drag: "free",
    gap: "1rem",
    arrows: false,
    pagination: false,
    breakpoints: { 767: { perPage: 1, gap: "0.5rem" }, 992: { perPage: 2 } },
  }).mount();

  const statsSection = document.querySelector(".stats-section");
  const statsNumber = document.querySelectorAll(".stats__number");

  new IntersectionObserver(
    (entries) => {
      entries.forEach((el) => {
        el.isIntersecting &&
          statsNumber.forEach((number) => {
            const animate = () => {
              const value = +number.dataset.value;
              const data = +number.textContent;
              const speed = value / 500;

              data < value
                ? ((number.textContent = Math.ceil(data + speed)),
                  setTimeout(animate, 1))
                : (number.textContent = value);
            };
            animate();
          });
      });
    },
    { threshold: 0.5 }
  ).observe(statsSection);
});

const imagesOptions = {
  margin: "100px",
};

const lazyLoad = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    else {
      const src = entry.target.getAttribute("data-src");

      if (src !== null) {
        entry.target.src = src;
      } else {
        const backgroundImage = entry.target.getAttribute("data-background");
        entry.target.style.backgroundImage = `url(${backgroundImage})`;
      }

      lazyLoad.unobserve(entry.target);
    }
  });
}, imagesOptions);

const images = document.querySelectorAll("[data-src]");
images.forEach((img) => lazyLoad.observe(img));

const carouselItems = document.querySelectorAll("[data-background]");
carouselItems.forEach((item) => lazyLoad.observe(item));

const animationOptions = {
  threshold: 0.3,
};
const animationObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    entry.target.classList.toggle("show", entry.isIntersecting);
  });
}, animationOptions);

const animationElements = document.querySelectorAll(".animate");

animationElements.forEach((el) => animationObserver.observe(el));
