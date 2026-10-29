import styles from "./AdminDropdown.module.scss";
import logoutIcon from "../../../icons/logout.svg";
import { MdClose } from "react-icons/md";
import { useState } from "react";
import ChangePasswordForm from "./ChangePasswordForm";

const AdminDropdown = ({ setIsAdminDropdown }) => {
  const [isPasswordChange, setIsPasswordChange] = useState(false);

  return (
    <div
      className={styles.dropdown}
    >
      <div
        onClick={() => setIsAdminDropdown(false)}
        className={styles.closeIcon}
      >
        <MdClose />
      </div>
      <p>
        Dobrodošli <span>Admin</span>!
      </p>
      <h6 onClick={() => setIsPasswordChange(prev => !prev)}>Promijeni lozinku</h6>
      {isPasswordChange && <ChangePasswordForm />}
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
