document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".slides img");
    const nextBtn = document.querySelector(".next-btn");
    const prevBtn = document.querySelector(".prev-btn");
    
    let currentIndex = 0;
    let slideInterval;
    const intervalTime = 5000; // Tempo em milissegundos para mudar de slide (5 segundos)

    // Função que altera a imagem ativa
    const changeSlide = (index) => {
        // Remove o estado ativo de todas as imagens
        slides.forEach(slide => slide.classList.remove("active"));
        
        // Garante o loop dos índices caso passe do limite
        if (index >= slides.length) {
            currentIndex = 0;
        } else if (index < 0) {
            currentIndex = slides.length - 1;
        } else {
            currentIndex = index;
        }

        // Adiciona a classe ativa no slide correto
        slides[currentIndex].classList.add("active");
    };

    // Função para avançar o slide automaticamente
    const startAutoSlide = () => {
        slideInterval = setInterval(() => {
            changeSlide(currentIndex + 1);
        }, intervalTime);
    };

    // Para o timer e reinicia (evita bugs se o usuário clicar muito rápido)
    const resetInterval = () => {
        clearInterval(slideInterval);
        startAutoSlide();
    };

    // Eventos dos botões
    nextBtn.addEventListener("click", () => {
        changeSlide(currentIndex + 1);
        resetInterval();
    });

    prevBtn.addEventListener("click", () => {
        changeSlide(currentIndex - 1);
        resetInterval();
    });

    // Inicia o carrossel automático ao carregar a página
    startAutoSlide();
});