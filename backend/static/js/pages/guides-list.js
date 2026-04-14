var guidesList = new List("guides-list", {
  valueNames: ["name"],
  item: '<tr><td class="name"></td></tr>',
});

document
  .getElementById("deleteguideModal")
  .addEventListener("show.bs.modal", function (event) {
    var deleteUrl = event.relatedTarget.getAttribute("data-delete-url");
    var guideId = event.relatedTarget
      .closest("tr")
      .getAttribute("id")
      .replace("row-", "");
    var confirmBtn = document.getElementById("deleteguideConfirm");
    confirmBtn.setAttribute("hx-post", deleteUrl);
    confirmBtn.setAttribute("hx-target", "#row-" + guideId);
    htmx.process(confirmBtn);
  });
