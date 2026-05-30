import switchs from "../../../utils/switchs";
import styles from "./Switch.module.scss";

const Switch = () => {
  return (
    <section className={styles.sectionContainer}>
      <div className={styles.sectionWrapper}>
        <div className={styles.textWrapper}>
          <h4>why teams switch</h4>
          <h2>
            Simplify daily <br /> operations
          </h2>
          <h6>
            Designed to reduce complexity and help transport <br /> businesses
            run more efficiently.
          </h6>
        </div>
        <div className={styles.cardsWrapper}>
          {switchs.map((item) => {
            console.log(item.id);
            return (
              <div className={styles.cardWrapper} key={item.id}>
                <div className={styles.iconWrapper}>
                  <img src={item.icon} alt="" />
                </div>
                <div className={styles.innerTextWrapper}>
                  <h3>{item.title}</h3>
                  <p>{item.text}</p>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Switch;
