import RequestDemo from "../components/requestDemo/RequestDemo";
import "../styles/fonts.css";
import ReactDOM from "react-dom/client";

const requestDemo = document.getElementById("requestDemo");

if (requestDemo) {
  ReactDOM.createRoot(requestDemo).render(<RequestDemo/>);
}
