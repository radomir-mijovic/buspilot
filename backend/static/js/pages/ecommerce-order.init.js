var orderList = new List("orderList", {
  valueNames: ["id", "customer_name", "product_name", "type", "amount", "payment"],
  item: '<tr><td class="id"></td><td class="customer_name"></td><td class="product_name"></td><td class="type"></td><td class="amount"></td><td class="payment"></td></tr>',
}).on("updated", function (e) {
  var noresult = document.getElementsByClassName("noresult")[0];
  noresult.style.display = e.matchingItems.length === 0 ? "block" : "none";
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

function _t(key, fallback) {
  return (window.appTranslations && window.appTranslations[key]) || fallback;
}

document.addEventListener("click", function (e) {
  var btn = e.target.closest(".delete-vehicle-btn");
  if (!btn) return;
  e.stopPropagation();
  e.preventDefault();
  var vehicleId = btn.dataset.vehicleId;
  var deleteUrl = btn.dataset.deleteUrl;
  Swal.fire({
    html:
      '<div class="mt-3"><lord-icon src="https://cdn.lordicon.com/gsqxdxog.json" trigger="loop" colors="primary:#f7b84b,secondary:#f06548" style="width:100px;height:100px"></lord-icon>' +
      '<div class="mt-4 pt-2 fs-15 mx-5"><h4>' + _t("t-are-you-sure", "Da li ste sigurni?") + "</h4>" +
      '<p class="text-muted mx-4 mb-0">' + _t("t-vehicle-delete-confirm", "Vozilo će biti trajno obrisano.") + "</p></div></div>",
    showCancelButton: true,
    customClass: {
      confirmButton: "btn btn-danger w-xs me-2 mb-1",
      cancelButton: "btn btn-primary w-xs mb-1",
    },
    confirmButtonText: _t("t-yes-delete", "Da, Obriši!!"),
    cancelButtonText: _t("t-cancel", "Otkaži"),
    buttonsStyling: false,
    showCloseButton: true,
  }).then(function (result) {
    if (!result.isConfirmed) return;
    var csrfToken = (document.cookie.match(/csrftoken=([^;]+)/) || [])[1] || "";
    fetch(deleteUrl, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
        "HX-Request": "true",
      },
    }).then(function (response) {
      if (response.ok) {
        var row = document.getElementById("row-" + vehicleId);
        if (row) row.remove();
        orderList.reIndex();
      }
    });
  });
}, true);
