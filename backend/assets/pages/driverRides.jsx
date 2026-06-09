import DriverNavbar from "../components/driverNavbar/DriverNavbar";
import DriverRides from "../components/driverRides/DriverRides";
import DriverWidgets from "../components/driverWidget/DriverWidgets";
import "../styles/fonts.css";
import ReactDOM from "react-dom/client";
import {DriverProvider} from "../contexts/DriverContext"
import RidesDates from "../components/driverRides/RidesDates";

const driverRidesPage = document.getElementById("driverRidesPage");

if (driverRidesPage) {
  ReactDOM.createRoot(driverRidesPage).render(
    <DriverProvider>
      <DriverNavbar title="Moje vožnje" />
      <DriverWidgets />
      <RidesDates/>
      <DriverRides />
    </DriverProvider>,
  );
}
