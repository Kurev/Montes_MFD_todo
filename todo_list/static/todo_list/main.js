document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.btn');
  buttons.forEach((button) => {
    button.addEventListener('mouseenter', () => {
      button.classList.add('shadow-sm');
    });
    button.addEventListener('mouseleave', () => {
      button.classList.remove('shadow-sm');
    });
  });
});
