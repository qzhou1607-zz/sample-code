var page = 1;
var total = 0;
while (true) {
    var products;
    $.ajax({
        async:false,
        dataType:'json',
        url:'http://shopicruit.myshopify.com/products.json?page=' + page,
        success: function(data) {
            var subtotal = 0;
            products = data.products;
            if (products.length > 0) {
                $.each(products,function(i,product) {
                                 tags = product.tags;
                                 if (tags.indexOf('Clock') != -1 || tags.indexOf('Watch') != -1) {
                                      variants = product.variants;
                                      $.each(variants, function(j,variant) {
                                            $('ul').append('<li>'
                                                + tags.join(', ') + ' '
                                                + j +':' + variant.price 
                                                + '</li>');
                                            subtotal += variant.price*1
                                      });
                                 }
                             });
                total += subtotal;
                $('span').html('Total: ' + total);
            }
        }   
    });
    if (products.length === 0) {
        break;
    }
    page = page + 1;
}   




