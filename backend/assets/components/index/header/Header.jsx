import styles from "./Header.module.css";
import brandLogo from "../../../icons/buspilot-favicon.svg";
import RequestDemoButton from "../../buttons/RequestDemoButton";
import LoginButton from "../../buttons/LoginButton";

const Header = () => {
  return (
    <div className={styles.main}>
      <div className={styles.headerLogo}>
        <img src={brandLogo} alt="" width={20} height={20} />
        <h3 className="font-display">BusPilot</h3>
      </div>
      <div className={styles.buttonWrapper}>
        <LoginButton />
        <RequestDemoButton />
      </div>
    </div>
  );
};

export default Header;
