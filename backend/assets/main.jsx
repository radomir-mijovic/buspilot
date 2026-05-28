import ReactDOM from "react-dom/client";
import TestComponent from "./components/testComponent";

const root = document.getElementById("test-component");

if (root) {
    ReactDOM.createRoot(root).render(
        <TestComponent />
    );
}
