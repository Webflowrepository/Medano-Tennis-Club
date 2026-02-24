// Las librerías Lenis, gsap, ScrollTrigger y SplitType se cargan globalmente desde el HTML.
gsap.registerPlugin(ScrollTrigger);

// 1. Lenis Initialization
const lenis = new Lenis({
  lerp: 0.1,
  smoothWheel: true,
});

// Sincronización crítica
lenis.on('scroll', ScrollTrigger.update);

gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});

gsap.ticker.lagSmoothing(0);

// 2. Global Animations Setup
document.addEventListener("DOMContentLoaded", () => {
  // Mobile Menu Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navbar = document.querySelector('.navbar');

  if (mobileToggle && navbar) {
    const hamburgerIcon = mobileToggle.querySelector('.hamburger-icon');
    const closeIcon = mobileToggle.querySelector('.close-icon');

    mobileToggle.addEventListener('click', () => {
      navbar.classList.toggle('menu-open');
      if (navbar.classList.contains('menu-open')) {
        if (hamburgerIcon) hamburgerIcon.style.display = 'none';
        if (closeIcon) closeIcon.style.display = 'block';
        mobileToggle.setAttribute('aria-expanded', 'true');
        lenis.stop(); // Detiene scroll del fondo
      } else {
        if (hamburgerIcon) hamburgerIcon.style.display = 'block';
        if (closeIcon) closeIcon.style.display = 'none';
        mobileToggle.setAttribute('aria-expanded', 'false');
        lenis.start(); // Restaura scroll
      }
    });

    // Navbar Scrolled State - Mobile Only Toggle was incorrectly restricting Desktop
  }

  // Hero Text Animation (Fade-in suave similar a la imagen)
  const heroTitle = document.querySelector('.hero-title');
  if (heroTitle) {
    // Ya no usamos SplitType para dividir por caracteres
    gsap.from('.hero-content', {
      y: 40, // Desplazamiento menor, más sutil
      opacity: 0,
      duration: 1.5, // Duración más larga, como el fade del background
      ease: "power2.out",
      delay: 0.3
    });
  }
  // Hero Slider Logic (4s intervals)
  const sliderImages = document.querySelectorAll('.hero-slider__image');
  if (sliderImages.length > 0) {
    let currentImageIndex = 0;

    // Activa la primera
    sliderImages[currentImageIndex].classList.add('is-active');

    setInterval(() => {
      // Oculta actual
      sliderImages[currentImageIndex].classList.remove('is-active');

      // Siguiente indice
      currentImageIndex = (currentImageIndex + 1) % sliderImages.length;

      // Muestra nueva
      sliderImages[currentImageIndex].classList.add('is-active');
    }, 4000); // 4 Segundos
  }

  // ===    Section 'El Club' - Staggered scroll animation (imagen + texto) ===
  const sectionClub = document.querySelector('.section-club');
  if (sectionClub) {
    const clubImage = sectionClub.querySelector('div:first-child');
    const clubText = sectionClub.querySelector('div:last-child');

    // Imagen: entra desde la izquierda cuando la sección llega a pantalla
    if (clubImage) {
      gsap.from(clubImage, {
        scrollTrigger: {
          trigger: sectionClub,
          start: "top bottom", // dispara cuando el top de la sección toca el fondo del viewport
          once: true,
        },
        x: -60,
        opacity: 0,
        duration: 1.2,
        ease: "power3.out",
      });
    }

    // Texto: entra desde la derecha, con un pequeño delay
    if (clubText) {
      gsap.from(clubText, {
        scrollTrigger: {
          trigger: sectionClub,
          start: "top bottom",
          once: true,
        },
        x: 60,
        opacity: 0,
        duration: 1.2,
        delay: 0.2,
        ease: "power3.out",
      });
    }
  }

  // Generic ScrollTrigger fade-in-up for remaining sections
  const fadeUpElements = document.querySelectorAll('.fade-up:not(.section-club)');
  fadeUpElements.forEach((el) => {
    gsap.from(el, {
      scrollTrigger: {
        trigger: el,
        start: "top bottom",
        once: true,
      },
      y: 40,
      opacity: 0,
      duration: 0.8,
      ease: "power3.out",
    });
  });

  // Re-calcular posiciones de ScrollTrigger después de que la page cargue completamente
  window.addEventListener('load', () => {
    ScrollTrigger.refresh();
  });
});
