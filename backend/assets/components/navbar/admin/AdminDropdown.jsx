import styles from "./AdminDropdown.module.scss";
import logoutIcon from "../../../icons/logout.svg";
import { MdClose } from "react-icons/md";

const AdminDropdown = ({ setIsAdminDropdown }) => {
  return (
    <div className={styles.dropdown}>
      <div
        onClick={() => setIsAdminDropdown(false)}
        className={styles.closeIcon}
      >
        <MdClose />
      </div>
      <p>
        Dobrodošli <span>Admin</span>!
      </p>
      <h6>Promijeni lozinku</h6>
      <div className={styles.logoutWrapper}>
        <img src={logoutIcon} width={15} height={15} alt="" />
        <a href="/logout">
          <h6>Odjava</h6>
        </a>
      </div>
    </div>
  );
};

export default AdminDropdown;
