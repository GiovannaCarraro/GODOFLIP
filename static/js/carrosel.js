// espera a página carregar completamente
document.addEventListener("DOMContentLoaded", () => {

    // pega todos os slides do carrossel
    const slides = document.querySelectorAll(".slide");

    // pega todas as bolinhas indicadoras
    const dots = document.querySelectorAll(".dot");

    // pega os botões de navegação
    const prevBtn = document.querySelector(".prev-btn");
    const nextBtn = document.querySelector(".next-btn");

    // pega o container do carrossel
    const carousel = document.querySelector(".carousel");

    // controla qual slide está ativo
    let currentSlide = 0;

    // guarda o intervalo do autoplay
    let slideInterval;

    // atualiza o slide exibido
    function showSlide(index) {

        // remove a classe active de todos os slides
        slides.forEach(slide => slide.classList.remove("active"));

        // remove a classe active de todas as bolinhas
        dots.forEach(dot => dot.classList.remove("active"));

        // ativa o slide atual
        slides[index].classList.add("active");

        // ativa a bolinha correspondente
        if (dots[index]) dots[index].classList.add("active");

        // atualiza o indice atual
        currentSlide = index;
    }

    // avança para o próximo slide
    function nextSlide() {

        let index = (currentSlide + 1) % slides.length;

        showSlide(index);
    }

    // volta para o slide anterior
    function prevSlide() {

        let index = (currentSlide - 1 + slides.length) % slides.length;

        showSlide(index);
    }

    // evento do botão próximo
    nextBtn.addEventListener("click", nextSlide);

    // evento do botão anterior
    prevBtn.addEventListener("click", prevSlide);

    // permite trocar de slide pelas bolinhas
    dots.forEach((dot, index) => {

        dot.addEventListener("click", () => {

            showSlide(index);

        });

    });

    // inicia a troca automática dos slides
    function startAutoPlay() {

        slideInterval = setInterval(nextSlide, 2000);

    }

    // para a troca automática
    function stopAutoPlay() {

        clearInterval(slideInterval);

    }

    // inicia o carrossel automático
    startAutoPlay();

    // pausa quando o mouse estiver sobre o carrossel
    carousel.addEventListener("mouseenter", stopAutoPlay);

    // volta a funcionar quando o mouse sair
    carousel.addEventListener("mouseleave", startAutoPlay);

});