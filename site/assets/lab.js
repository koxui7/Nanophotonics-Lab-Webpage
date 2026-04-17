const filterLinks = document.querySelectorAll('[data-filter]');
const filterItems = document.querySelectorAll('.portfolio-items > div');

for (const link of filterLinks) {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const target = link.dataset.filter || '*';

    for (const candidate of filterLinks) {
      candidate.classList.remove('active');
    }

    link.classList.add('active');

    for (const item of filterItems) {
      if (target === '*' || item.classList.contains(target.replace('.', ''))) {
        item.style.display = '';
      } else {
        item.style.display = 'none';
      }
    }
  });
}
