import DriverNavbar from "../components/driverNavbar/DriverNavbar";
import "../styles/fonts.css";
import ReactDOM from "react-dom/client";
import { DriverProvider } from "../contexts/DriverContext";
import DriverPassRides from "../components/driverPassRides/DriverPassRides";

const driverRidesPage = document.getElementById("driverPassRidesPage");

if (driverRidesPage) {
  ReactDOM.createRoot(driverRidesPage).render(
    <DriverProvider>
      <DriverNavbar title="Prošle vožnje" />
      <DriverPassRides />
    </DriverProvider>,
  );
}
