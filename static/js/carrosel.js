document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".slide");
    const dots = document.querySelectorAll(".dot");
    const prevBtn = document.querySelector(".prev-btn");
    const nextBtn = document.querySelector(".next-btn");
    const carousel = document.querySelector(".carousel");
    
    let currentSlide = 0;
    let slideInterval;

    // Função para atualizar a exibição dos slides e dots
    function showSlide(index) {
        // Remove a classe active de todos
        slides.forEach(slide => slide.classList.remove("active"));
        dots.forEach(dot => dot.classList.remove("active"));

        // Ativa o slide e o dot corretos
        slides[index].classList.add("active");
        if (dots[index]) dots[index].classList.add("active");
        
        currentSlide = index;
    }

    function nextSlide() {
        let index = (currentSlide + 1) % slides.length;
        showSlide(index);
    }

    function prevSlide() {
        let index = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(index);
    }

    // Controles dos botões
    nextBtn.addEventListener("click", nextSlide);
    prevBtn.addEventListener("click", prevSlide);

    // Controle pelas bolinhas (dots)
    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => {
            showSlide(index);
        });
    });

    // Auto-play (Passar sozinho a cada 4 segundos)
    function startAutoPlay() {
        slideInterval = setInterval(nextSlide, 4000);
    }

    function stopAutoPlay() {
        clearInterval(slideInterval);
    }

    // Inicia o auto-play
    startAutoPlay();

    // Pausa o carrossel quando o mouse estiver em cima
    carousel.addEventListener("mouseenter", stopAutoPlay);
    carousel.addEventListener("mouseleave", startAutoPlay);
});