// Simple tab filter for product categories
document.addEventListener('DOMContentLoaded', () => {
  const tabs = document.querySelectorAll('.tab-btn');
  const cards = document.querySelectorAll('.product-card');

  // Shared filter function used by tabs and pagination
  const filterByCategory = (cat) => {
    // Sync tab buttons
    tabs.forEach(t => {
      t.classList.toggle('active', t.getAttribute('data-cat') === cat);
    });
    // Sync pagination
    document.querySelectorAll('.page-link[data-cat]').forEach(p => {
      p.classList.toggle('active', p.getAttribute('data-cat') === cat);
    });
    // Filter cards
    cards.forEach(card => {
      if (cat === 'all' || card.getAttribute('data-cat') === cat) {
        card.style.display = 'flex';
        card.style.opacity = '0';
        requestAnimationFrame(() => { card.style.transition = 'opacity .3s'; card.style.opacity = '1'; });
      } else {
        card.style.display = 'none';
      }
    });
  };

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const cat = tab.getAttribute('data-cat');
      filterByCategory(cat);
    });
  });

  // Pagination links also trigger category filter
  document.querySelectorAll('.page-link[data-cat]').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const cat = link.getAttribute('data-cat');
      filterByCategory(cat);
      // Smooth scroll back to product grid top on mobile
      const grid = document.querySelector('.category-tabs');
      if (grid) grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  // Hero slider auto-play + dots
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dots .dot');
  if (slides.length > 1) {
    let cur = 0;
    const go = (i) => {
      slides[cur].classList.remove('active');
      dots[cur].classList.remove('active');
      cur = (i + slides.length) % slides.length;
      slides[cur].classList.add('active');
      dots[cur].classList.add('active');
    };
    dots.forEach((d, i) => d.addEventListener('click', () => go(i)));
    setInterval(() => go(cur + 1), 5500);
  }

  // Smooth-reveal header on scroll
  const header = document.querySelector('.site-header');
  let lastY = window.scrollY;
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    if (y > 80) header.style.boxShadow = '0 2px 16px rgba(0,0,0,0.06)';
    else header.style.boxShadow = '0 1px 0 rgba(0,0,0,0.05)';
    lastY = y;
  });
});

// Product detail gallery thumbnail switcher
function changeImg(thumb, mainImgId) {
  const mainImg = document.getElementById(mainImgId);
  if (!mainImg) return;
  const fullSrc = thumb.getAttribute('data-full');
  if (!fullSrc) return;
  mainImg.style.opacity = '0.6';
  setTimeout(() => {
    mainImg.src = fullSrc;
    mainImg.alt = thumb.alt;
    mainImg.style.opacity = '1';
  }, 150);
  // Update active state on thumbs
  const thumbs = thumb.parentElement.querySelectorAll('.thumb');
  thumbs.forEach(t => t.classList.remove('active'));
  thumb.classList.add('active');
}
