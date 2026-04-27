let currentYear = new Date().getFullYear();
let currentMonth = new Date().getMonth() + 1;
let rideType = "";

function buildHeader(year, month) {
  const daysInMonth = new Date(year, month, 0).getDate();
  const tr = document.createElement("tr");

  tr.appendChild(document.createElement("th"));

  const days = (window.appTranslations && window.appTranslations["t-days"]) || [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun",
  ];

  for (let day = 1; day <= daysInMonth; day++) {
    const th = document.createElement("th");

    const date = new Date(year, month - 1, day);
    const dayIndex = (date.getDay() + 6) % 7;

    const dayNum = document.createElement("div");
    dayNum.textContent = day;
    const dayLabel = document.createElement("div");
    dayLabel.textContent = days[dayIndex];

    th.appendChild(dayNum);
    th.appendChild(dayLabel);
    tr.appendChild(th);
  }

  return tr;
}

function parseDate(str) {
  const [y, m, d] = str.split("-").map(Number);
  return new Date(y, m - 1, d);
}

function buildRideRow(ride, year, month) {
  const daysInMonth = new Date(year, month, 0).getDate();
  const tr = document.createElement("tr");
  tr.style.height = "36px";

  const label = document.createElement("td");
  label.textContent = ride.title;
  label.style.whiteSpace = "nowrap";
  label.style.paddingRight = "8px";
  label.className = ride.class_name;
  tr.appendChild(label);

  const startDate = parseDate(ride.start_date);
  const endDate = parseDate(ride.end_date || ride.start_date);

  const startDay =
    startDate.getFullYear() === year && startDate.getMonth() + 1 === month
      ? startDate.getDate()
      : 1;
  const endDay =
    endDate.getFullYear() === year && endDate.getMonth() + 1 === month
      ? endDate.getDate()
      : daysInMonth;

  for (let i = 1; i < startDay; i++) {
    tr.appendChild(document.createElement("td"));
  }

  const td = document.createElement("td");
  td.colSpan = endDay - startDay + 1;
  td.textContent = ride.agency;
  td.className = ride.class_name;
  td.style.color = "black";
  td.style.borderRadius = "4px";
  td.style.padding = "4px 6px";
  td.style.fontSize = "12px";
  td.style.overflow = "hidden";
  td.style.whiteSpace = "nowrap";
  tr.appendChild(td);

  for (let i = endDay + 1; i <= daysInMonth; i++) {
    tr.appendChild(document.createElement("td"));
  }

  return tr;
}

async function render(year, month, type) {
  document.getElementById("month-label").textContent = new Date(
    year,
    month - 1,
  ).toLocaleString("default", { month: "long" });

  const table = document.getElementById("calendar-table");
  table.innerHTML = "";

  const thead = document.createElement("thead");
  thead.appendChild(buildHeader(year, month));
  table.appendChild(thead);

  const tbody = document.createElement("tbody");

  try {
    const response = await fetch(
      `/api/rides/?month=${month}&year=${year}&type=${type}`,
    );
    const rides = await response.json();
    const daysInMonth = new Date(year, month, 0).getDate();
    const firstOfMonth = new Date(year, month - 1, 1);
    const lastOfMonth = new Date(year, month - 1, daysInMonth);

    const filtered = rides.filter((ride) => {
      const start = parseDate(ride.start_date);
      const end = parseDate(ride.end_date || ride.start_date);
      return start <= lastOfMonth && end >= firstOfMonth;
    });

    filtered.forEach((ride) =>
      tbody.appendChild(buildRideRow(ride, year, month)),
    );
  } catch (e) {
    console.error(e);
  }

  table.appendChild(tbody);
}

document
  .getElementById("filter-buttons")
  .addEventListener("click", async (event) => {
    let type = "";
    if (event.target.id === "lines") {
      type = 1;
    } else if (event.target.id === "transfers") {
      type = 2;
    } else if (event.target.id === "excursions") {
      type = 3;
    } else if (event.target.id === "round") {
      type = 4;
    }

    render(currentYear, currentMonth, type);
  });

document.getElementById("prev").addEventListener("click", () => {
  currentMonth--;
  if (currentMonth === 0) {
    currentMonth = 12;
    currentYear--;
  }
  render(currentYear, currentMonth, rideType);
});

document.getElementById("next").addEventListener("click", () => {
  currentMonth++;
  if (currentMonth === 13) {
    currentMonth = 1;
    currentYear++;
  }
  render(currentYear, currentMonth, rideType);
});

render(currentYear, currentMonth, rideType);
