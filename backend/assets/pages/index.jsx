import "../styles/fonts.css";
import ReactDOM from "react-dom/client";
import PageWrapper from "../components/index/PageWrapper";

const index = document.getElementById("index");

if (index) {
  ReactDOM.createRoot(index).render(<PageWrapper />);
}
