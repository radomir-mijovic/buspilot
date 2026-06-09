import styles from "./DriverRide.module.scss";
import getCookie from "../../utils/get_cookie";
import { useDriver } from "../../contexts/DriverContext";

const DriverRide = ({ ride }) => {
  const { setIsRideChanged } = useDriver();

  const confirmUrl = (isRideConfirmed) => {
    if (isRideConfirmed === true) {
      return "/api/driver-portal/cancel-ride/";
    } else {
      return "/api/driver-portal/confirm-ride/";
    }
  };

  const handeRideConfirmations = async () => {
    try {
      await fetch(confirmUrl(ride.is_confirmed), {
        method: "PATCH",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ ride_id: ride.id }),
      });
      setIsRideChanged((prev) => !prev);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className={styles.rideWrapper}>
      <div className={styles.upperWrapper}>
        <p>{ride.start_date}</p>
      </div>
      <div className={styles.upperTextWrapper}>
        <div className={styles.timeWrapper}>
          <h2>{ride.start_time}</h2>
          <p>polazak</p>
        </div>
        <div className={styles.infoWrapper}>
          <h4>{ride.title}</h4>
          <h5>
            <span>Tip</span> {ride.ride_type}
          </h5>
          <h5>
            <span>polazak</span> {ride.start_location}
          </h5>
          <h5>
            <span>Agencija</span> {ride.agency}
          </h5>
          <h5>
            <span>Vodic</span>{" "}
            {ride.guides
              .map((guide) => `${guide.first_name} ${guide.last_name}`)
              .join(", ")}
          </h5>
        </div>
      </div>
      <div className={styles.lowerTextWrapper}>
        <p
          className={`${ride.is_confirmed ? styles.ridePConfirmed : styles.ridePNotConfirmed}`}
        >
          {ride.is_confirmed ? "Potvrđeno" : "Čeka tvoju potvrdu"}
        </p>
        <button
          onClick={handeRideConfirmations}
          className={`${styles.button} ${ride.is_confirmed ? styles.buttonCancel : styles.buttonConfirm}`}
          type="button"
        >
          {ride.is_confirmed ? "Vožnja potvrđena" : "Potvrdi vožnju"}
        </button>
      </div>
    </div>
  );
};

export default DriverRide;
