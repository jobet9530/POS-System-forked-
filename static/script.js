$(document).ready(function() {
  function fetchProducts(){
    $.ajax({
      url: '/product',
      type: 'GET',
      dataType: 'xml'
      success: function(data) {
          displayProducts(data);
      },
      error: function(error){
        console.error('Error fetching products:', error);
      }
    });
  }
  function displayProducts(data) {
      var productHTML = '<h2>Product List</h2><ul>';
      $(xmlData).find('product').each(function(){
        var product = $(this);
        productHTML += '<li>' +
          'ID: ' + product.find('product_id').text() +
          ', Name: ' + product.find('product_name').text() +
          ', Price: $' + product.find('price').text() +
          ', Stock Quantity: ' + product.find('stock_quantity').text() +
          '</li>';
      });
    productHTML += '</ul>';
    $('#product-list').html(productHTML);
  }

  window.updateProduct = function(productId, newPrice) {
    $.ajax({
      url: '/product/' + productId,
      type: 'PUT',
      contentType: 'application/json',
      data: JSON.stringify({ price: newPrice }),
      success: function(data) {
        console.log('Product updated successfully:', data);
      },
      error: function(error) {
        console.error('Error updating product:', error);
      }
    });
  };

  window.deleteProduct = function(productId) {
    $.ajax({
      url: '/product/' + productId,
      type: 'DELETE',
      success: function(data) {
        console.log('Product deleted successfully:', data);
      },
      error: function(error) {
        console.error('Error deleting product:', error);
      }
    });
  };
  window.addProduct = function(productName, price, stockQuantity) {
    $.ajax({
      url: '/product',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ product_name: productName, price: price, stock_quantity: stockQuantity }),
      success: function(data) {
        console.log('Product added successfully:', data);
      },
      error: function(error) {
        console.error('Error adding product:', error);
      }
    });
  };
  function isValidInput(productId, newProductName){
    return productId !== null && productId !== undefined && productId !== '' && newProductName !== null && newProductName !== undefined && newProductName !== '';
  }
}