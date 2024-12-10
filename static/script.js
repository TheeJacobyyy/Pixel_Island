document.addEventListener("DOMContentLoaded", () => {
  const carousel = document.querySelector(".carousel");
  const items = document.querySelectorAll(".carousel-item");
  const prevButton = document.querySelector(".carousel-control.prev");
  const nextButton = document.querySelector(".carousel-control.next");

  let currentIndex = 0;
  const totalItems = items.length;

  function updateCarousel() {
    const offset = -currentIndex * 100; // Calculate the offset for sliding
    carousel.style.transform = `translateX(${offset}%)`;
  }

  // Event listeners for next and previous buttons
  prevButton.addEventListener("click", () => {
    currentIndex = (currentIndex - 1 + totalItems) % totalItems; // Wrap around to the last item
    updateCarousel();
  });

  nextButton.addEventListener("click", () => {
    currentIndex = (currentIndex + 1) % totalItems; // Wrap around to the first item
    updateCarousel();
  });

  // Auto-slide every 3 seconds
  setInterval(() => {
    currentIndex = (currentIndex + 1) % totalItems;
    updateCarousel();
  }, 5000);
});
