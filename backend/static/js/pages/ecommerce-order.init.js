var orderList = new List("orderList", {
  valueNames: ["id", "customer_name", "product_name", "type", "amount", "payment"],
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

document.addEventListener("click", function (e) {
  var btn = e.target.closest(".delete-vehicle-btn");
  if (!btn) return;
  e.stopPropagation();
  e.preventDefault();
  var vehicleId = btn.dataset.vehicleId;
  var deleteUrl = btn.dataset.deleteUrl;
  Swal.fire({
    html: '<div class="mt-3"><lord-icon src="https://cdn.lordicon.com/gsqxdxog.json" trigger="loop" colors="primary:#f7b84b,secondary:#f06548" style="width:100px;height:100px"></lord-icon><div class="mt-4 pt-2 fs-15 mx-5"><h4>Da li ste sigurni?</h4><p class="text-muted mx-4 mb-0">Da li ste sigurni da želite obrisati ovo vozilo?</p></div></div>',
    showCancelButton: true,
    customClass: {
      confirmButton: "btn btn-primary w-xs me-2 mb-1",
      cancelButton: "btn btn-danger w-xs mb-1",
    },
    confirmButtonText: "Da, obriši!",
    cancelButtonText: "Otkaži",
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
