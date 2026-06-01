import "../styles/fonts.css";
import ReactDOM from "react-dom/client";
import NavLinks from "../components/navlinks/NavLinks";

const navlinks = document.getElementById("navLinksReact");

if (navlinks) {
  ReactDOM.createRoot(navlinks).render(<NavLinks />);
}
