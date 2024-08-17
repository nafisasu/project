// This script will handle any JavaScript interactions
document.querySelectorAll('.product button').forEach(button => {
    button.addEventListener('click', () => {
        alert('Item added to cart!');
    });
});