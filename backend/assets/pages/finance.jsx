import ReactDOM from "react-dom/client";
import InvoicesHeader from "../components/invoicesHeader";

const root = document.getElementById("finance-page")

if (root) {
    ReactDOM.createRoot(root).render(
        <InvoicesHeader />
    )
}
