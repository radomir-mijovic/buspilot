import { useState } from "react";
import styles from "./Expiring.module.scss";
import alertRedIcon from "../../../icons/alert-circle-red.svg";
import alertGreyIcon from "../../../icons/alert-triangle-grey.svg";
import { MdClose } from "react-icons/md";

const tabs = [
  { id: 1, title: "Vozila" },
  { id: 2, title: "Vozači" },
];

const Expiring = ({
  expiringVehiclesDocs,
  expiringDriversDocs,
  setExpiring,
  setAdminDropdown,
}) => {
  const [isActive, setIsActive] = useState(1);
  const [expiringDocs, setExpiringDocs] = useState(expiringVehiclesDocs);

  const mapExpiringDocs = (object, tabId) => {
    setIsActive(tabId);
    if (object === "Vozila") {
      setExpiringDocs(expiringVehiclesDocs);
    } else {
      setExpiringDocs(expiringDriversDocs);
    }
  };

  return (
    <div className={styles.cardWrapper}>
      <div className={styles.cardTop}>
        <div onClick={() => setExpiring(false)} className={styles.closeIcon}>
          <MdClose />
        </div>
        <h4>Dokumenti koji brzo ističu!</h4>
        <div className={styles.tabs}>
          {tabs.map((tab) => {
            return (
              <h6
                onClick={() => mapExpiringDocs(tab.title, tab.id)}
                key={tab.id}
                className={
                  isActive === tab.id ? styles.tabActive : styles.tabInactive
                }
              >
                {tab.title}
              </h6>
            );
          })}
        </div>
      </div>
      <div className={styles.cardBottom}>
        {expiringDocs.slice(0, 3).map((doc) => {
          return (
            <div key={doc.id} className={styles.textWrapper}>
              <img src={alertRedIcon} alt="" />
              <div className={styles.textInnerWrapper}>
                <h5>
                  {doc.title.toUpperCase()} za {doc.related_object}
                  <span> ističe </span> u narednih mjesec dana!
                </h5>
                <div className={styles.smallTextWrapper}>
                  <img src={alertGreyIcon} alt="" width={15} height={15} />
                  <p>Ističe za {doc.days_to_expire} dana</p>
                </div>
              </div>
            </div>
          );
        })}
        <div className={styles.buttonWrapper}>
          <button type="button">
            <a
              onClick={() => setAdminDropdown(false)}
              href="/expiring-documents"
            >
              Pregledaj dokumente
            </a>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Expiring;
