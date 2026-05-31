import styles from "./Navbar.module.scss";
import brandLogo from "../../icons/buspilot-favicon.svg";
import Expiring from "./expiring/Expiring";
import { useState, useEffect } from "react";

const Navbar = () => {
  const [isExpiring, setExpiring] = useState(false);
  const [expiringVehiclesDocs, setExpiringVehiclesDocs] = useState([]);
  const [expiringDriversDocs, setExpiringDriversDocs] = useState([]);
  const totalInDanger =
    expiringDriversDocs.length + expiringVehiclesDocs.length;

  useEffect(() => {
    const featchData = async () => {
      const [vehiclesRes, driversRes] = await Promise.all([
        fetch("/api/vehicles/expiring-documents"),
        fetch("/api/drivers/expiring-documents"),
      ]);
      setExpiringVehiclesDocs(await vehiclesRes.json());
      setExpiringDriversDocs(await driversRes.json());
    };
    featchData();
  }, []);

  return (
    <nav className={styles.nav}>
      <div className={styles.logoWrapper}>
        <img src={brandLogo} alt="" width={30} height={30} />
        <h3>BusPilot</h3>
      </div>

      <div className={styles.utilsWrapper}>
        <button
          onClick={() => setExpiring((prev) => !prev)}
          className={styles.iconbtn}
          type="button"
          aria-label="Notifications"
        >
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.7"
          >
            <path d="M18 8a6 6 0 0 0-12 0c0 7-3 8-3 8h18s-3-1-3-8" />
            <path d="M13.7 21a2 2 0 0 1-3.4 0" />
          </svg>
          {totalInDanger > 0 && (
            <span className={styles.badge}>{totalInDanger}</span>
          )}
        </button>
        <div className={styles.languageWrapper}>
          {isExpiring && totalInDanger > 0 && (
            <Expiring
              setExpiring={setExpiring}
              expiringVehiclesDocs={expiringVehiclesDocs}
              expiringDriversDocs={expiringDriversDocs}
            />
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
