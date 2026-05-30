import capabilities from "../../../utils/capabilities";
import styles from "./Capabilities.module.scss";
import RequestDemoButton from "../../buttons/RequestDemoButton"

const Capabilities = () => {
  return (
    <section className={styles.sectionContainer}>
      <h4>Capabilities</h4>
      <h2>
        Powerful features built <br /> for transport companies
      </h2>
      <div className={styles.featureContainer}>
        <div className={styles.featureWrapper}>
          {capabilities.map((item) => {
            return (
              <div className={styles.itemContainer} key={item.id}>
                <div className={styles.iconWrapper}>
                  <img src={item.icon} alt="" />
                </div>

                <h3>{item.title}</h3>
                <p>{item.text}</p>
              </div>
            );
          })}
          <div className={styles.requestContainer}>
            <h3>See it on your own fleet</h3>
            <p>Book a walkthrough and we'll map BusPilot to your operation.</p>
            <RequestDemoButton large="large"/>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Capabilities;
