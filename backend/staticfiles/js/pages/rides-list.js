document
  .querySelectorAll(".nav-tabs .nav-link[data-filter]")
  .forEach(function (tab) {
    tab.addEventListener("click", function () {
      document.querySelectorAll(".nav-tabs .nav-link").forEach(function (t) {
        t.classList.remove("active");
      });
      this.classList.add("active");

      var filter = this.getAttribute("data-filter");
      console.log(filter, "filter");
      document.querySelectorAll("#orderTable tbody tr").forEach(function (row) {
        if (filter === "all" || row.getAttribute("data-ride-type") === filter) {
          row.style.display = "";
        } else {
          row.style.display = "none";
        }
      });
    });
  });

document
  .getElementById("deleteRideModal")
  .addEventListener("show.bs.modal", function (event) {
    var deleteUrl = event.relatedTarget.getAttribute("data-delete-url");
    var rideId = event.relatedTarget
      .closest("tr")
      .getAttribute("id")
      .replace("row-", "");
    var confirmBtn = document.getElementById("deleteRideConfirm");
    confirmBtn.setAttribute("hx-post", deleteUrl);
    confirmBtn.setAttribute("hx-target", "#row-" + rideId);
    htmx.process(confirmBtn);
  });
