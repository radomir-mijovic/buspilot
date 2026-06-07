import { useEffect, useState } from "react";
import styles from "./DriverNavbar.module.scss";

const DriverNavbar = () => {
  const [driver, setDriver] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDriverDetails = async () => {
      try {
        const res = await fetch("/api/driver-rides/driver-details/");

        if (!res.ok) {
          throw new Error("HTTP Error!");
        }

        const data = await res.json();
        setDriver(data);
        setLoading(false);
      } catch (err) {
        console.log(err);
      }
    };

    fetchDriverDetails();
  }, []);

  if (loading) {
    return <h2>Loading driver data...</h2>;
  }

  return (
    <div className={styles.navbarWrapper}>
      <h6>Vozač portal</h6>
      <div className={styles.textWrapper}>
        <h4>Moje vožnje</h4>
        <div className={styles.initialsWrapper}>
          {driver.first_name[0]}
          {driver.last_name[0]}
        </div>
      </div>
      <p>
        {driver.first_name} {driver.last_name}
      </p>
    </div>
  );
};

export default DriverNavbar;
