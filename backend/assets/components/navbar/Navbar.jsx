import styles from "./Navbar.module.scss";
import brandLogo from "../../icons/buspilot-favicon.svg";
import mneFlagIcon from "../../icons/flag-montenegrin.svg";
import Expiring from "./expiring/Expiring";
import { useState, useEffect } from "react";
import { FaAngleDown } from "react-icons/fa6";
import { isMobile, isBrowser } from "react-device-detect";
import AdminDropdown from "./admin/AdminDropdown";

const Navbar = () => {
  const [isExpiring, setExpiring] = useState(false);
  const [isAdminDropdown, setIsAdminDropdown] = useState(false);
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

  const handleAdminDropdown = () => {
    setIsAdminDropdown((prev) => !prev);
    setExpiring(false);
  };

  const handleExpiringDropdown = () => {
    setExpiring((prev) => !prev);
    setIsAdminDropdown(false);
  };

  return (
    <nav className={styles.nav}>
      <a href="/calendar">
        <div className={styles.logoWrapper}>
          <img src={brandLogo} alt="" width={30} height={30} />
          {isBrowser && <h3>BusPilot</h3>}
        </div>
      </a>

      <div className={styles.utilsWrapper}>
        <div>
          <button
            onClick={handleExpiringDropdown}
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
          {isExpiring && totalInDanger > 0 && (
            <Expiring
              setExpiring={setExpiring}
              expiringVehiclesDocs={expiringVehiclesDocs}
              expiringDriversDocs={expiringDriversDocs}
            />
          )}
        </div>
        <div className={styles.languageWrapper}>
          <img src={mneFlagIcon} alt="" width={25} height={25} />
          <FaAngleDown />
        </div>
        <div className={styles.line} />
        <div onClick={handleAdminDropdown} className={styles.adminWrapper}>
          <div className={styles.letter}>
            <h5>A</h5>
          </div>
          {isBrowser && (
            <>
              <h4>
                Admin <span>korisnik</span>
              </h4>
              <FaAngleDown />
            </>
          )}
        </div>
        {isAdminDropdown && (
          <AdminDropdown setIsAdminDropdown={setIsAdminDropdown} />
        )}
      </div>
    </nav>
  );
};

export default Navbar;
