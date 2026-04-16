// script.js
console.log("✅ Script.js loaded successfully!");

document.addEventListener('DOMContentLoaded', function () {

    console.log("✅ DOM fully loaded");

    const section = document.querySelector('.philosophy-div');
    const image = document.querySelector('.image-content');
    const text = document.querySelector('.text-content');
    const checkItems = document.querySelectorAll('.check-item');

    if (!section) console.error("❌ .philosophy-div not found");
    if (!image) console.error("❌ .image-content not found");
    if (!text) console.error("❌ .text-content not found");
    if (checkItems.length === 0) console.warn("⚠️ No .check-item found");

    if (!section || !image || !text) {
        console.error("❌ Animation stopped - missing elements");
        return;
    }

    // Force hide initially
    image.style.opacity = 0;
    image.style.transform = 'translateX(-80px)';
    text.style.opacity = 0;
    text.style.transform = 'translateX(80px)';

    // Simple Scroll Listener (more reliable for now)
    function checkScroll() {
        const rect = section.getBoundingClientRect();
        if (rect.top <= window.innerHeight * 0.7) {
            console.log("✅ Section is in view - Starting animation");

            // Image first
            setTimeout(() => {
                image.style.transition = 'all 0.8s ease';
                image.style.opacity = 1;
                image.style.transform = 'translateX(0)';
            }, 100);

            // Text second
            setTimeout(() => {
                text.style.transition = 'all 0.8s ease';
                text.style.opacity = 1;
                text.style.transform = 'translateX(0)';
            }, 500);

            // Check items
            checkItems.forEach((item, i) => {
                setTimeout(() => {
                    item.style.transition = 'all 0.6s ease';
                    item.style.opacity = 1;
                    item.style.transform = 'translateY(0)';
                }, 900 + i * 250);
            });

            window.removeEventListener('scroll', checkScroll); // Run once
        }
    }

    window.addEventListener('scroll', checkScroll);
    checkScroll(); // Check immediately in case it's already in view
});




// About Section Staggered Animation
document.addEventListener('DOMContentLoaded', function () {

    const aboutSection = document.querySelector('.about-section');
    const cards = document.querySelectorAll('.card');

    if (!aboutSection || cards.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateAboutCards();
                observer.disconnect(); // Run only once
            }
        });
    }, {
        threshold: 0.25,
        rootMargin: "-80px 0px"
    });

    observer.observe(aboutSection);

    function animateAboutCards() {
        cards.forEach((card, index) => {
            setTimeout(() => {
                card.classList.add('visible');
            }, 100 + (index * 180)); // Nice staggered delay
        });
    }
});