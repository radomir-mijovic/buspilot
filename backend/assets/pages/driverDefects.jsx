import DriverNavbar from "../components/driverNavbar/DriverNavbar";
import "../styles/fonts.css";
import ReactDOM from "react-dom/client";
import { DriverProvider } from "../contexts/DriverContext";
import DriverDefects from "../components/driverDefects/DriverDefects";

const driverDefectsPage = document.getElementById("driverDefectsPage");

if (driverDefectsPage) {
  ReactDOM.createRoot(driverDefectsPage).render(
    <DriverProvider>
      <DriverNavbar title="Prijavi kvar" />
      <DriverDefects />
    </DriverProvider>,
  );
}
