import busIcon from "../icons/fleet-bus.svg";
import routeIcon from "../icons/rides-route.svg";
import calendarIcon from "../icons/calendar.svg";
import driverIcon from "../icons/driver-user.svg";
import agencyIcon from "../icons/agency.svg";
import documentIcon from "../icons/document.svg";
import dashboarIcon from "../icons/dashboard-chart.svg";

const capabilities = [
  {
    id: 1,
    title: "Fleet Management",
    text: "Keep all company vehicles organized in one place. Manage buses, mini buses, vans, availability, and operational details with ease.",
    icon: busIcon,
  },
  {
    id: 2,
    title: "Ride Planning & Tracking",
    text: "Track daily operations and monthly ride activity with a clear and structured overview of your transport schedules.",
    icon: routeIcon,
  },
  {
    id: 3,
    title: "Smart Calendar System",
    text: "View schedules, assignments, and ride planning using a modern calendar interface designed for operational teams.",
    icon: calendarIcon,
  },
  {
    id: 4,
    title: "Driver Management",
    text: "Store driver information, licenses, contracts, and important documents securely and access them anytime.",
    icon: driverIcon,
  },
  {
    id: 5,
    title: "Agency & Guide Management",
    text: "Manage partner agencies, tour guides, contacts, and related documentation in one organized system.",
    icon: agencyIcon,
  },
  {
    id: 6,
    title: "Company Document Center",
    text: "Centralize registrations, insurance files, permits, contracts, and company documents to avoid lost paperwork and delays.",
    icon: documentIcon,
  },
  {
    id: 7,
    title: "Operational Dashboard",
    text: "Monitor your business activity with a clean and modern dashboard that helps your team stay informed and efficient.",
    icon: dashboarIcon,
  },
];

export default capabilities;
