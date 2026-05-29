import "../styles/fonts.css";
import ReactDOM from "react-dom/client";
import Navbar from "../components/navbar/Navbar";

const navbar = document.getElementById("navbarReact");

if (navbar) {
  ReactDOM.createRoot(navbar).render(<Navbar />);
}
