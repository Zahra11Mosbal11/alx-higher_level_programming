// Add item to the list
$('DIV#add_item').click(function () {
  const newItem = $('<li>Item</li>');
  $('UL.my_list').append(newItem);
});

// Remove item from the list
$('DIV#remove_item').click(function () {
  $('UL.my_list li:last-child').remove();
});

// Clear the list
$('DIV#clear_list').click(function () {
  $('UL.my_list').empty();
});
