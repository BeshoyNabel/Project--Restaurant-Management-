const searchInput = document.getElementById("search-input");
if (localStorage.getItem("search_cutomer")) {
  searchInput.value = localStorage.getItem("search_cutomer");
}
searchInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        let value = searchInput.value.trim().replace(/\s+/g, "").toLowerCase();
        localStorage.setItem("search_cutomer",searchInput.value)
        window.location.href = `/customers/search/?name=${encodeURIComponent(value)}`;
    }
});
document.addEventListener("DOMContentLoaded", function() {
            localStorage.clear();
        });