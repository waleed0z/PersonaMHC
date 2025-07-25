document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const menuList = document.getElementById('menuList');
    const navOverlay = document.getElementById('navOverlay');
    const nav = document.getElementById('navbar');
    const MOBILE_WIDTH = 700;

    function isMobile() {
        return window.innerWidth <= MOBILE_WIDTH;
    }

    function openMenu() {
        menuList.classList.add('open');
        navOverlay.classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
        menuList.classList.remove('open');
        navOverlay.classList.remove('open');
        document.body.style.overflow = '';
    }

    menuToggle.addEventListener('click', function() {
        if (isMobile()) {
            if (!menuList.classList.contains('open')) {
                openMenu();
            } else {
                closeMenu();
            }
        }
    });

    navOverlay.addEventListener('click', function() {
        closeMenu();
    });

    // Close menu on link click (mobile)
    menuList.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href && href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    closeMenu();
                    setTimeout(() => {
                        target.scrollIntoView({behavior: 'smooth'});
                    }, 100); // Wait for menu to close
                }
            } else {
                closeMenu();
            }
        });
    });

    // Responsive: close menu if resizing to desktop
    window.addEventListener('resize', function() {
        if (!isMobile()) {
            closeMenu();
        }
    });

    // Navbar shadow on scroll
    window.addEventListener('scroll', function() {
        if(window.scrollY > 60) nav.classList.add('scrolled');
        else nav.classList.remove('scrolled');
    });

    // Carousel functionality for all carousels
    function setupCarousel(carouselId) {
        const container = document.getElementById(carouselId);
        if (!container) return;
        const slides = container.querySelectorAll('.quote-slide');
        let current = 0;
        let timer = null;

        function showSlide(idx) {
            slides.forEach((slide, i) => {
                slide.classList.toggle('active', i === idx);
            });
            current = idx;
        }

        function nextSlide() {
            showSlide((current + 1) % slides.length);
        }

        function prevSlide() {
            showSlide((current - 1 + slides.length) % slides.length);
        }

        // Button controls
        container.querySelectorAll('.carousel-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                if (btn.dataset.dir === 'next') nextSlide();
                else prevSlide();
                resetTimer();
            });
        });

        // Auto-advance every 7s
        function resetTimer() {
            if (timer) clearInterval(timer);
            timer = setInterval(nextSlide, 7000);
        }
        resetTimer();

        // Pause on hover (desktop)
        container.addEventListener('mouseenter', () => { if (timer) clearInterval(timer); });
        container.addEventListener('mouseleave', resetTimer);
    }

    // Setup all carousels
    ['carousel-1','carousel-2','carousel-3','carousel-4'].forEach(setupCarousel);

    // Smooth scroll for anchor links (for browsers that don't support scroll-behavior)
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href && href.length > 1) {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({behavior: 'smooth'});
                }
            }
        });
    });

    // Animate sections on scroll (fade-in)
    function revealOnScroll() {
        const reveals = document.querySelectorAll(
            '.section-visual, .hero-section, .blog-section, .quote-carousel-container'
        );
        const windowHeight = window.innerHeight;
        reveals.forEach(function(section) {
            const sectionTop = section.getBoundingClientRect().top;
            if (sectionTop < windowHeight * 0.92) {
                section.classList.add('visible');
            }
        });
    }
    window.addEventListener('scroll', revealOnScroll);
    window.addEventListener('resize', revealOnScroll);
    revealOnScroll();

    // Animate team members in sequence when team section is visible
    function animateTeamMembers() {
        const teamSection = document.querySelector('.team-section');
        if (!teamSection) return;
        const teamMembers = teamSection.querySelectorAll('.team-member.team-animate');
        if (!teamSection.classList.contains('visible')) return;
        teamMembers.forEach((member, i) => {
            setTimeout(() => member.classList.add('visible'), 200 + i * 200);
        });
    }
    // Observe team section visibility
    function onScrollTeam() {
        const teamSection = document.querySelector('.team-section');
        if (teamSection && teamSection.classList.contains('visible')) {
            animateTeamMembers();
            window.removeEventListener('scroll', onScrollTeam);
        }
    }
    window.addEventListener('scroll', onScrollTeam);
    onScrollTeam();
});
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const closeIcon = document.getElementById('closeIcon');
    const menuList = document.getElementById('menuList');
    const navOverlay = document.getElementById('navOverlay');
    const nav = document.getElementById('navbar');
    const MOBILE_WIDTH = 700;

    function isMobile() {
        return window.innerWidth <= MOBILE_WIDTH;
    }

    function openMenu() {
        menuList.classList.add('open');
        navOverlay.classList.add('open');
        document.body.style.overflow = 'hidden';
        menuToggle.style.display = 'none';
        closeIcon.style.display = 'block';
    }

    function closeMenu() {
        menuList.classList.remove('open');
        navOverlay.classList.remove('open');
        document.body.style.overflow = '';
        menuToggle.style.display = 'block';
        closeIcon.style.display = 'none';
    }

    menuToggle.addEventListener('click', openMenu);
    closeIcon.addEventListener('click', closeMenu);

    navOverlay.addEventListener('click', function() {
        closeMenu();
    });

    // Close menu on link click (mobile)
    menuList.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href && href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    closeMenu();
                    setTimeout(() => {
                        target.scrollIntoView({behavior: 'smooth'});
                    }, 100); // Wait for menu to close
                }
            } else {
                closeMenu();
            }
        });
    });

    // Responsive: close menu if resizing to desktop
    window.addEventListener('resize', function() {
        if (!isMobile()) {
            closeMenu();
        }
    });

    // Navbar shadow on scroll
    window.addEventListener('scroll', function() {
        if(window.scrollY > 60) nav.classList.add('scrolled');
        else nav.classList.remove('scrolled');
    });

    // Carousel functionality for all carousels
    function setupCarousel(carouselId) {
        const container = document.getElementById(carouselId);
        if (!container) return;
        const slides = container.querySelectorAll('.quote-slide');
        let current = 0;
        let timer = null;

        function showSlide(idx) {
            slides.forEach((slide, i) => {
                slide.classList.toggle('active', i === idx);
            });
            current = idx;
        }

        function nextSlide() {
            showSlide((current + 1) % slides.length);
        }

        function prevSlide() {
            showSlide((current - 1 + slides.length) % slides.length);
        }

        // Button controls
        container.querySelectorAll('.carousel-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                if (btn.dataset.dir === 'next') nextSlide();
                else prevSlide();
                resetTimer();
            });
        });

        // Auto-advance every 7s
        function resetTimer() {
            if (timer) clearInterval(timer);
            timer = setInterval(nextSlide, 7000);
        }
        resetTimer();

        // Pause on hover (desktop)
        container.addEventListener('mouseenter', () => { if (timer) clearInterval(timer); });
        container.addEventListener('mouseleave', resetTimer);
    }

    // Setup all carousels
    ['carousel-1','carousel-2','carousel-3','carousel-4'].forEach(setupCarousel);

    // Smooth scroll for anchor links (for browsers that don't support scroll-behavior)
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href && href.length > 1) {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({behavior: 'smooth'});
                }
            }
        });
    });

    // Animate sections on scroll (fade-in)
    function revealOnScroll() {
        const reveals = document.querySelectorAll(
            '.section-visual, .hero-section, .blog-section, .quote-carousel-container'
        );
        const windowHeight = window.innerHeight;
        reveals.forEach(function(section) {
            const sectionTop = section.getBoundingClientRect().top;
            if (sectionTop < windowHeight * 0.92) {
                section.classList.add('visible');
            }
        });
    }
    window.addEventListener('scroll', revealOnScroll);
    window.addEventListener('resize', revealOnScroll);
    revealOnScroll();

    // Animate team members in sequence when team section is visible
    function animateTeamMembers() {
        const teamSection = document.querySelector('.team-section');
        if (!teamSection) return;
        const teamMembers = teamSection.querySelectorAll('.team-member.team-animate');
        if (!teamSection.classList.contains('visible')) return;
        teamMembers.forEach((member, i) => {
            setTimeout(() => member.classList.add('visible'), 200 + i * 200);
        });
    }
    // Observe team section visibility
    function onScrollTeam() {
        const teamSection = document.querySelector('.team-section');
        if (teamSection && teamSection.classList.contains('visible')) {
            animateTeamMembers();
            window.removeEventListener('scroll', onScrollTeam);
        }
    }
    window.addEventListener('scroll', onScrollTeam);
    onScrollTeam();
});