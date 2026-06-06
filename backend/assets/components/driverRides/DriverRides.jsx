import { useEffect, useState } from "react";
import styles from "./DriverRides.module.scss";
import DriverRide from "./DriverRide";
import { useDriver } from "../../contexts/DriverContext";

const DriverRides = () => {
  const [rides, setRides] = useState([]);
  const [loading, setLoading] = useState(true);
  const { isRideChanged, filterDate } = useDriver();

  let backendFilterDate = "";

  if (filterDate) {
    const [day, month, year] = filterDate.split(".");
    backendFilterDate = `20${year}-${month}-${day}`;
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch(
          `/api/driver-rides/?start_date=${backendFilterDate}`,
        );

        if (!res.ok) {
          throw new Error(`HTTP Error! Status ${res.status}`);
        }

        const data = await res.json();
        setRides(data);
        setLoading(false);
      } catch (err) {
        console.log(err);
      }
    };
    fetchData();
  }, [isRideChanged, filterDate]);

  if (loading) {
    return <h1>Loading rides...</h1>;
  }

  return (
    <div className={styles.ridesWrapper}>
      {rides.map((ride) => {
        return <DriverRide key={ride.id} ride={ride} />;
      })}
    </div>
  );
};

export default DriverRides;
