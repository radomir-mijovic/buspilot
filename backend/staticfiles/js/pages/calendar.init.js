document.addEventListener("DOMContentLoaded", function () {
  var calendarEl = document.getElementById("calendar");
  var vehicleId = calendarEl.dataset.vehicleId;
  var modal = new bootstrap.Modal(document.getElementById("event-modal"));
  var updateModal = new bootstrap.Modal(document.getElementById("event-modal"));

  window.buspilotCalendar = new FullCalendar.Calendar(calendarEl, {
    timeZone: "local",
    initialView: "dayGridMonth",
    editable: false,
    selectable: true,
    navLinks: false,
    themeSystem: "bootstrap",
    headerToolbar: {
      left: "prev,next today",
      center: "title",
      right: "newRide",
    },
    customButtons: {
      newRide: {
        text: "+ Nova vožnja",
        click: function () {
          modal.show();
        },
      },
    },
    events: function (fetchInfo, successCallback, failureCallback) {
      fetch(`/api/vehicles/${vehicleId}/calendar-events`)
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          successCallback(data);
        })
        .then(function () {
          failureCallback();
        });
    },
    dateClick: function (info) {
      var startDate = document.getElementById("start_date");
      if (startDate) startDate.value = info.dateStr;
      modal.show();
    },
    eventClick: function (info) {
      console.log(info, "info");
      info.jsEvent.preventDefault();
      updateModal.show();
      //if (info.event.id) {
      //  window.location.href = "/rides-update/" + info.event.id + "/";
      //}
    },
  });

  window.buspilotCalendar.render();
  document
    .getElementById("form-event")
    .addEventListener("submit", function (e) {
      e.preventDefault();

      const form = e.target;
      const formData = new FormData(form);

      fetch("/api/rides/", {
        method: "POST",
        body: formData,
        credentials: "include",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
      }).then(function (response) {
        if (response.ok) {
          modal.hide();
          window.buspilotCalendar.refetchEvents();
        }
      });
    });
});

function getCookie(name) {
  let cookieValue = null;

  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");

    for (let cookie of cookies) {
      cookie = cookie.trim();

      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }

  return cookieValue;
}
