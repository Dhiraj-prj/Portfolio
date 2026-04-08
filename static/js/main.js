// Custom cursor
const cursor = document.getElementById('cursor');
const follower = document.getElementById('cursor-follower');
let mx = 0, my = 0, fx = 0, fy = 0;

document.addEventListener('mousemove', e => {
  mx = e.clientX; my = e.clientY;
  cursor.style.left = mx + 'px';
  cursor.style.top = my + 'px';
});

function animateFollower() {
  fx += (mx - fx) * 0.12;
  fy += (my - fy) * 0.12;
  follower.style.left = fx + 'px';
  follower.style.top = fy + 'px';
  requestAnimationFrame(animateFollower);
}
animateFollower();

// Nav scroll effect
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 60);
});

// Reveal on scroll
const reveals = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 80);
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });
reveals.forEach(el => revealObserver.observe(el));

// Hero name animation on load
document.querySelectorAll('.name-line').forEach((el, i) => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(40px)';
  el.style.transition = `opacity 0.8s ease ${i * 0.15 + 0.2}s, transform 0.8s ease ${i * 0.15 + 0.2}s`;
  setTimeout(() => {
    el.style.opacity = '1';
    el.style.transform = 'translateY(0)';
  }, 100);
});
