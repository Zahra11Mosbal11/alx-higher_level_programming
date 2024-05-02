// Add a click event listener to the DIV#add_item element
$('DIV#add_item').click(function () {
  const element = '<li>Item</li>';
  $('ul.my_list').append(element);
});
