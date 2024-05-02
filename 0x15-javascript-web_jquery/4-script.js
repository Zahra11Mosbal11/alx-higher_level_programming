// Add a click event listener to the DIV#toggle_header element
$('DIV#toggle_header').click(function () {
  // Toggle the classes 'red' and 'green' on the <header> element
  $('header').toggleClass('red green');
});
