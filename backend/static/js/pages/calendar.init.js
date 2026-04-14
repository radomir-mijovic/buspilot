document.addEventListener("DOMContentLoaded", function () {
  var calendarEl = document.getElementById("calendar");
  var vehicleId = calendarEl.dataset.vehicleId;
  var modal = new bootstrap.Modal(document.getElementById("event-modal"));
  var updateModal = new bootstrap.Modal(
    document.getElementById("event-update-modal"),
  );
  var currentRideId = null;

  var fpOpts = { dateFormat: "Y-m-d", altInput: true, altFormat: "d/m/Y", allowInput: true };
  var fpCreateStart = flatpickr(document.querySelector("#form-event [name='start_date']"), fpOpts);
  var fpCreateEnd = flatpickr(document.querySelector("#form-event [name='end_date']"), fpOpts);
  var fpUpdateStart = flatpickr(document.querySelector("#form-update-event [name='start_date']"), fpOpts);
  var fpUpdateEnd = flatpickr(document.querySelector("#form-update-event [name='end_date']"), fpOpts);

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
        text: "+ " + (window.appTranslations && window.appTranslations["t-new-ride"] || "Nova vožnja"),
        click: function () {
          modal.show();
        },
      },
    },
    events: function (fetchInfo, successCallback, failureCallback) {
      fetch("/api/vehicles/" + vehicleId + "/calendar-events")
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          successCallback(data);
        })
        .catch(function () {
          failureCallback();
        });
    },
    dateClick: function (info) {
      fpCreateStart.setDate(info.dateStr);
      modal.show();
    },
    eventClick: function (info) {
      info.jsEvent.preventDefault();
      currentRideId = info.event.id;

      fetch("/api/rides/" + currentRideId + "/")
        .then(function (response) {
          return response.json();
        })
        .then(function (ride) {
          var form = document.getElementById("form-update-event");
          form.querySelector("[name='title']").value = ride.title || "";
          var rideTypeSelect = form.querySelector("[name='ride_type']");
          rideTypeSelect.value = String(ride.ride_type || "");
          rideTypeSelect.dispatchEvent(new Event("change"));
          fpUpdateStart.setDate(ride.start_date || "");
          fpUpdateEnd.setDate(ride.end_date || "");
          form.querySelector("[name='start_time']").value =
            ride.start_time || "";
          form.querySelector("[name='end_time']").value = ride.end_time || "";
          form.querySelector("[name='start_location']").value =
            ride.start_location || "";
          form.querySelector("[name='end_location']").value =
            ride.end_location || "";
          form.querySelector("[name='agency']").value = String(ride.agency || "");

          Array.from(form.querySelector("[name='drivers']").options).forEach(
            function (opt) {
              opt.selected = ride.drivers.includes(parseInt(opt.value));
            },
          );

          Array.from(form.querySelector("[name='guides']").options).forEach(
            function (opt) {
              opt.selected = ride.guides.includes(parseInt(opt.value));
            },
          );

          updateModal.show();
        });
    },
  });

  window.buspilotCalendar.render();

  window.addEventListener("translationsLoaded", function (e) {
    var btn = document.querySelector(".fc-newRide-button");
    if (btn) btn.textContent = "+ " + (e.detail["t-new-ride"] || "Nova vožnja");
  });

  document
    .getElementById("form-event")
    .addEventListener("submit", function (e) {
      e.preventDefault();
      const formData = new FormData(e.target);

      fetch("/api/rides/", {
        method: "POST",
        body: formData,
        credentials: "include",
        headers: { "X-CSRFToken": getCookie("csrftoken") },
      }).then(function (response) {
        if (response.ok) {
          modal.hide();
          window.buspilotCalendar.refetchEvents();
        }
      });
    });

  document
    .getElementById("form-update-event")
    .addEventListener("submit", function (e) {
      e.preventDefault();
      const formData = new FormData(e.target);

      fetch("/api/rides-update/" + currentRideId + "/", {
        method: "PATCH",
        body: formData,
        credentials: "include",
        headers: { "X-CSRFToken": getCookie("csrftoken") },
      }).then(function (response) {
        if (response.ok) {
          updateModal.hide();
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
