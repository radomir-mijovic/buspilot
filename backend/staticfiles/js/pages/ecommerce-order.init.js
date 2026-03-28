var perPage = 8,
  options = {
    valueNames: ["id", "customer_name", "product_name", "type", "amount", "payment"],
    page: perPage,
    pagination: true,
    plugins: [ListPagination({ left: 2, right: 2 })],
  },
  orderList = new List("orderList", options).on("updated", function (e) {
    var noresult = document.getElementsByClassName("noresult")[0];
    var paginationWrap = document.querySelector(".pagination-wrap");
    var paginationPrev = document.querySelector(".pagination-prev");
    var paginationNext = document.querySelector(".pagination-next");

    if (e.matchingItems.length === 0) {
      noresult.style.display = "block";
    } else {
      noresult.style.display = "none";
    }

    if (paginationPrev) paginationPrev.classList.toggle("disabled", e.i === 1);
    if (paginationNext) paginationNext.classList.toggle("disabled", e.i > e.matchingItems.length - e.page);
    if (paginationWrap) paginationWrap.style.display = e.matchingItems.length <= perPage ? "none" : "flex";
  });

var tabEl = document.querySelectorAll('a[data-bs-toggle="tab"]');

function filterOrder(t) {
  orderList.filter(function (item) {
    return t === "All" || item.values().type === t;
  });
  orderList.update();
}

Array.from(tabEl).forEach(function (e) {
  e.addEventListener("shown.bs.tab", function (e) {
    filterOrder(e.target.id);
  });
});

function SearchData() {
  var s = document.querySelector(".search");
  if (s) orderList.search(s.value);
}

var paginationNext = document.querySelector(".pagination-next");
var paginationPrev = document.querySelector(".pagination-prev");

if (paginationNext) {
  paginationNext.addEventListener("click", function () {
    var active = document.querySelector(".pagination.listjs-pagination .active");
    if (active && active.nextElementSibling) active.nextElementSibling.children[0].click();
  });
}

if (paginationPrev) {
  paginationPrev.addEventListener("click", function () {
    var active = document.querySelector(".pagination.listjs-pagination .active");
    if (active && active.previousSibling) active.previousSibling.children[0].click();
  });
}
