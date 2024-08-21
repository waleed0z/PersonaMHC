 const navbarToggle = document.querySelector('#menu-bars');
const navbarLinks = document.querySelectorAll('.navbar a');

navbarToggle.addEventListener('click', () => {
    navbarLinks.forEach(link => link.classList.toggle('show'));
    const closeIcon = document.querySelector('#close');
    if (closeIcon) {
        closeIcon.classList.toggle('show');
        navbarToggle.classList.toggle('fa-bars');
    }
});