import { useEffect, useState } from "react";
import styles from "./DriverWidgets.module.scss";
import DriverWidget from "./DriverWidget";
import { useDriver } from "../../contexts/DriverContext";

const DriverWidgets = () => {
  const [upcomingRides, setUpcomingRides] = useState(0);
  const [notConfirmed, setNotConfirmed] = useState(0);
  const [confirmed, setConfirmed] = useState(0);
  const { isRideChanged } = useDriver();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch("/api/driver-rides/rides-count/");
        if (!res.ok) {
          throw new Error(`HTTP Error! status: ${res.status}`);
        }

        const data = await res.json();

        setUpcomingRides(data.upcoming);
        setNotConfirmed(data.not_confirmed_rides);
        setConfirmed(data.confirmed_rides);
      } catch (err) {
        console.log(err);
      }
    };
    fetchData();
  }, [isRideChanged]);

  return (
    <div className={styles.widgetWrapper}>
      <DriverWidget count={upcomingRides} title="Predstojeće" />
      <DriverWidget count={notConfirmed} title="Čeka potvrdu" isDanger={true} />
      <DriverWidget count={confirmed} title="Potvrđeno" />
    </div>
  );
};

export default DriverWidgets;
