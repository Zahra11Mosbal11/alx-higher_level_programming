#!/usr/bin/node
exports.converter = function (base) {
  return function convert (num) {
    if (num === 0) {
      return '';
    } else {
      return convert(Math.floor(num / base)) + (num % base).toString(base).toUpperCase();
    }
  };
};
