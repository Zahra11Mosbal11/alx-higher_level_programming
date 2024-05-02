// Fetches translation from the provided URL and updates the content of div#hello

let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.get(url, function (data) {
  let translation = data.hello;
  $('div#hello').text(translation);
});
