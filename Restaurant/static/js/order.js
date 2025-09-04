const searchInput = document.getElementById("search-input");
if (localStorage.getItem("search_customer_order")) {
  searchInput.value = localStorage.getItem("search_customer_order");
}
searchInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        let value = searchInput.value.trim().replace(/\s+/g, "").toLowerCase();
        localStorage.setItem("search_customer_order", searchInput.value);
        window.location.href = `/orders/search/?name=${encodeURIComponent(value)}`;
    }
});
 document.addEventListener("DOMContentLoaded", function() {
            localStorage.clear();
        });