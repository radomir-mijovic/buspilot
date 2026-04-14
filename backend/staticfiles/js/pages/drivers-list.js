var driversList = new List("drivers-list", {
  valueNames: ["name"],
  item: '<tr><td class="name"></td></tr>',
});

document
  .getElementById("deleteDriverModal")
  .addEventListener("show.bs.modal", function (event) {
    var deleteUrl = event.relatedTarget.getAttribute("data-delete-url");
    var driverId = event.relatedTarget
      .closest("tr")
      .getAttribute("id")
      .replace("row-", "");
    var confirmBtn = document.getElementById("deleteDriverConfirm");
    confirmBtn.setAttribute("hx-post", deleteUrl);
    confirmBtn.setAttribute("hx-target", "#row-" + driverId);
    htmx.process(confirmBtn);
  });
