var customerName;
var customerPhone;
var orderDetails = {};
var totalPrice = 0;
const Menu = JSON.parse(document.getElementById("menu").textContent);
const order = JSON.parse(document.getElementById("order").textContent);

orderDetails = order.items;
customerName = order.customer_name;
customerPhone = order.customer_phone;
totalPrice = parseFloat(order.total_price);

for (const item of Menu) {
  if (orderDetails[item.item_name] !== undefined) {
    var quantity = document.querySelector("#quantity_" + item.id);
    quantity.value = "" + orderDetails[item.item_name];
  }
}


$(document).ready(function () {
  var current_fs, next_fs, previous_fs; //fieldsets
  var opacity;

  $(".remove").click(function () {
    var itemId = $(this).attr("id");
    var quantityInput = $("#quantity_" + itemId);
    menu = Menu.find((c) => c.id === parseInt(itemId));
    if (orderDetails[menu.item_name] !== undefined) {
      quantityInput.val(parseInt(quantityInput.val()) - 1);
      if (parseInt(quantityInput.val()) <= 0) {
        quantityInput.val(0);
        delete orderDetails[menu.item_name];
      } else {
        orderDetails[menu.item_name] = parseInt(quantityInput.val());
      }
      totalPrice -= parseFloat(menu.price);
    }
  });

  $(".add").click(function () {
    var itemId = $(this).attr("id");
    var quantityInput = $("#quantity_" + itemId);
    menu = Menu.find((c) => c.id === parseInt(itemId));
    quantityInput.val(parseInt(quantityInput.val()) + 1);
    orderDetails[menu.item_name] = parseInt(quantityInput.val());
    totalPrice += parseFloat(menu.price);
  });

  $(".next").click(function () {
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    if (current_fs.find("#order_summary")) {
      if (Object.keys(orderDetails).length === 0) {
        alert("Please add items to your order.");
        return;
      }
      var summaryHtml = `
        <h2 class="fs-title">Order Summary</h2>
        <br />
        <span style="display: flex; justify-content: space-between;">
            <h2 class="fs-title" style="text-align: left;">${customerName}</h2>
            <h2 class="fs-title" style="text-align: right;">${customerPhone}</h2>
        </span>
        <br /><table class="fixed_header">
            <thead>
                <tr>
                    <th>Item</th>
                    <th>Quantity</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
            ${Object.keys(orderDetails).map(
              (itemName) => `
                <tr>
                    <th>${itemName}</th>
                    <th>${orderDetails[itemName]}</th>
                    <th>$${(
                      orderDetails[itemName] *
                      Menu.find((m) => m.item_name === itemName).price
                    ).toFixed(2)}</th>
                </tr>
            `
            )}
            </tbody>
        </table>
        <h2 class="fs-title">Total Price: $${totalPrice.toFixed(2)}</h2>`;
      next_fs.find("#order_summary").html(summaryHtml);
      next_fs.find("#order").val(
        JSON.stringify({
          customer_name: customerName,
          customer_phone: customerPhone,
          items: orderDetails,
        })
      );
    }
    //Add Class Active
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate(
      { opacity: 0 },
      {
        step: function (now) {
          // for making fielset appear animation
          opacity = 1 - now;

          current_fs.css({
            display: "none",
            position: "relative",
          });
          next_fs.css({ opacity: opacity });
        },
        duration: 600,
      }
    );
  });

  $(".previous").click(function () {
    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    //Remove class active
    $("#progressbar li")
      .eq($("fieldset").index(current_fs))
      .removeClass("active");

    //show the previous fieldset
    previous_fs.show();

    //hide the current fieldset with style
    current_fs.animate(
      { opacity: 0 },
      {
        step: function (now) {
          // for making fielset appear animation
          opacity = 1 - now;

          current_fs.css({
            display: "none",
            position: "relative",
          });
          previous_fs.css({ opacity: opacity });
        },
        duration: 600,
      }
    );
  });
});