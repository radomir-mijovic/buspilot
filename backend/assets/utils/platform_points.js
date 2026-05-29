import busIcon from "../icons/fleet-bus.svg";
import driverIcon from "../icons/driver-user.svg";
import shieldIcon from "../icons/reduce-errors-shield.svg";
import routeIcon from "../icons/rides-route.svg";
import agencyIcon from "../icons/agency.svg";
import calendarIcon from "../icons/calendar.svg";

const platform_points = [
  {
    id: 1,
    title: "Manage buses, mini buses, vans, and company vehicles",
    icon: busIcon,
  },
  {
    id: 2,
    title: "Organize drivers and staff documentation",
    icon: driverIcon,
  },
  { id: 3, title: "Store company documents securely", icon: shieldIcon },
  { id: 4, title: "Track daily and monthly rides", icon: routeIcon },
  { id: 5, title: "Manage agencies and tour guides", icon: agencyIcon },
  {
    id: 6,
    title: "Visualize schedules with an integrated calendar",
    icon: calendarIcon,
  },
];

export default platform_points;
