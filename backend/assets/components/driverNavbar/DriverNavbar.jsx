import styles from "./DriverNavbar.module.scss";

const DriverNavbar = () => {
  return (
    <div className={styles.navbarWrapper}>
      <h6>Vozač portal</h6>
      <div className={styles.textWrapper}>
        <h4>Moje vožnje</h4>
        <div className={styles.initialsWrapper}>RM</div>
      </div>
      <p>Radomir Mijović</p>
    </div>
  );
};

export default DriverNavbar;
