const searchInput = document.getElementById("search-input");
if (localStorage.getItem("search_item")) {
  searchInput.value = localStorage.getItem("search_item");
}
searchInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        let value = searchInput.value.trim().replace(/\s+/g, "").toLowerCase();
        localStorage.setItem("search_item",searchInput.value)
        window.location.href = `/menu/search/?name=${encodeURIComponent(value)}`;
    }
});
document.addEventListener("DOMContentLoaded", function() {
            localStorage.clear();
        });