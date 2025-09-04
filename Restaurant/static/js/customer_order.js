const searchInput = document.getElementById("search-input");
if (localStorage.getItem("search_customer")) {
  searchInput.value = localStorage.getItem("search_customer");
}
searchInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        let value = searchInput.value.trim().replace(/\s+/g, "").toLowerCase();
        localStorage.setItem("search_customer",searchInput.value)
        window.location.href = `/customers/search_customer_orders/?name=${encodeURIComponent(value)}`;
    }
});
document.addEventListener("DOMContentLoaded", function() {
            localStorage.clear();
        });