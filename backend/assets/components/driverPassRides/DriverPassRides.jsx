import styles from "./DriverPassRides.module.scss";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { useEffect, useState } from "react";
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import { IoCheckmarkDone } from "react-icons/io5";
import { format } from "date-fns";
import { srLatn } from "date-fns/locale";
import { RiProgress5Line } from "react-icons/ri";

const DriverPassRides = () => {
  const [date, setDate] = useState();
  const [passRides, setPassRides] = useState([]);

  const yesterday = new Date();
  yesterday.setDate(yesterday.getDate() - 1);
  const initialDate = yesterday.toISOString().split("T")[0];

  useEffect(() => {
    const fetchRides = async () => {
      try {
        const res = await fetch(
          `/api/driver-rides/pass-rides?filter_date=${date ? date : initialDate}`,
        );

        if (!res.ok) {
          throw new Error("HTTP Error!");
        }

        const data = await res.json();
        setPassRides(data);
      } catch (err) {
        console.log(err);
      }
    };
    fetchRides();
  }, [date]);

  console.log(passRides);

  return (
    <div className={styles.pageWrapper}>
      <LocalizationProvider adapterLocale={srLatn} dateAdapter={AdapterDateFns}>
        <DatePicker
          maxDate={new Date(Date.now() - 24 * 60 * 60 * 1000)}
          format="dd/MM/yyyy"
          label="Izaberite datum"
          onAccept={(value) => {
            if (value) {
              setDate(format(value, "yyyy-MM-dd"));
            }
          }}
        />
      </LocalizationProvider>
      <div className={styles.ridesWrapper}>
        {passRides.length === 0 ? (
          <h3>Nema voznji</h3>
        ) : (
          <>
            <h3>Završene vožnje</h3>
            {passRides.map((ride) => {
              return (
                <div key={ride.id} className={styles.rideCard}>
                  <div>
                    <h4>{ride.title}</h4>
                    <div className={styles.cardText}>
                      <p
                        className={
                          ride.ride_type === "Excursion"
                            ? styles.excursion
                            : ride.ride_type === "Line"
                              ? styles.line
                              : ride.ride_type === "Transfer"
                                ? styles.transfer
                                : ride.ride_type === "Round Tour"
                                  ? styles.roundTour
                                  : ""
                        }
                      >
                        {ride.ride_type}
                      </p>
                      <div className={styles.dot} />
                      <p>{ride.agency}</p>
                      <div className={styles.dot} />
                      <p>{ride.start_date}</p>
                    </div>
                  </div>
                  {ride.in_progress ? (
                    <RiProgress5Line size={20} color={"#A46435"}/>
                  ) : (
                    <IoCheckmarkDone size={20} color={"#338A68"} />
                  )}
                </div>
              );
            })}
          </>
        )}
      </div>
    </div>
  );
};

export default DriverPassRides;
