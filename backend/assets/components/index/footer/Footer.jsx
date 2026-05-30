import styles from "./Footer.module.scss";

const Footer = () => {
  return (
    <footer className={styles.footerContainer}>
      <h5>Fleet & Ride Management Software for Transport Companies.</h5>
      <h6>
        Manage vehicles, rides, drivers, schedules, and documents from one
        modern dashboard.
      </h6>
      <p>© 2026 BusPilot. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
