import { useEffect, useState } from "react";
import styles from "./DriverDefects.module.scss";
import getCookie from "../../utils/get_cookie";

const DriverDefects = () => {
  const [vehicles, setVehicles] = useState([]);
  const [vehicleId, setVehicleId] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    const fetchVehicles = async () => {
      try {
        const res = await fetch("/api/driver-portal/defect-vehicles");

        if (!res.ok) {
          throw new Error("HTTP Error!");
        }

        const data = await res.json();
        setVehicles(data);
        setVehicleId("");
        setDescription("");
      } catch (err) {
        console.log(err);
      }
    };
    fetchVehicles();
  }, []);

  console.log(vehicles);

  const handleFromSubmit = async (e) => {
    e.preventDefault();

    try {
      await fetch("/api/driver-portal/report-defects/", {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({
          vehicle: vehicleId,
          description: description,
        }),
      });
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className={styles.pageWrapper}>
      <p className={styles.title}>
        Prijavi kvar ili problem na vozilu. Tim za održavanje će biti
        obaviješten.
      </p>
      <form onSubmit={(e) => handleFromSubmit(e)}>
        <select
          className={styles.select}
          id="vehicle"
          value={vehicleId}
          onChange={(e) => setVehicleId(e.target.value)}
        >
          <option value="">Izaberite vozilo</option>
          {vehicles.map((vehicle) => {
            return (
              <option value={vehicle.id} key={vehicle.id}>
                {vehicle.brand} {vehicle.model} {vehicle.licence_number}
              </option>
            );
          })}
        </select>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className={styles.textarea}
          type=""
          placeholder="Opiši problem - npr.  čudan zvuk iz motora, ne radi klima, oštećena guma..."
        />
        <button
          disabled={description === "" || vehicleId === ""}
          className={styles.button}
          type="submit"
        >
          Prijavi kvar
        </button>
      </form>
    </div>
  );
};

export default DriverDefects;
