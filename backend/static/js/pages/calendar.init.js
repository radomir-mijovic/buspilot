document.addEventListener("DOMContentLoaded", function () {
  var calendarEl = document.getElementById("calendar");
  var vehicleId = calendarEl.dataset.vehicleId;
  var modal = new bootstrap.Modal(document.getElementById("event-modal"));
  var updateModal = new bootstrap.Modal(
    document.getElementById("event-update-modal"),
  );
  var currentRideId = null;

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
      var startDate = document.getElementById("start_date");
      if (startDate) startDate.value = info.dateStr;
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
          form.querySelector("[name='start_date']").value =
            ride.start_date || "";
          form.querySelector("[name='end_date']").value = ride.end_date || "";
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
