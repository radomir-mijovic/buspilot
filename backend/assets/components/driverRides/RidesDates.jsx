import { useEffect, useState } from "react";
import styles from "./RidesDates.module.scss";
import { useDriver } from "../../contexts/DriverContext";

const RidesDates = () => {
  const [rides, setRides] = useState([]);
  const { setFilterDate } = useDriver();

  useEffect(() => {
    const fetchDates = async () => {
      try {
        const res = await fetch("/api/driver-rides/");

        if (!res.ok) {
          throw new Error("HTTP Error!");
        }
        const data = await res.json();
        setRides(data);
      } catch (err) {
        console.log(err);
      }
    };
    fetchDates();
  }, []);

  const uniqueDates = [...new Set(rides.map((ride) => ride.start_date))];

  return (
    <div className={styles.datesWrapper}>
      {uniqueDates.map((date) => {
        return (
          <div onClick={() => setFilterDate(date)} key={date} className={styles.dateWrapper}>
            <p>{date}</p>
          </div>
        );
      })}
    </div>
  );
};

export default RidesDates;
