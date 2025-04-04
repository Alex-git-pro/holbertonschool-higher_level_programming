document.getElementById('toggle_header').addEventListener('click', function() {
    const header = document.querySelector('header');
    // Toggle the classes between red and green
    if (header.classList.contains('red')) {
      header.classList.replace('red', 'green');
    } else {
      header.classList.replace('green', 'red');
    }
  });
