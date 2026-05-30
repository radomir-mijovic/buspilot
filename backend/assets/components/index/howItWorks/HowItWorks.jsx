import how_it_works from "../../../utils/how_it_works";
import styles from "./HowItWorks.module.scss";

const HowItWorks = () => {
  return (
    <section className={styles.sectionContainer}>
      <h4>How it works</h4>
      <h2>
        Simple workflow. Better operations.
      </h2>
      <div className={styles.cardsWrapper}>
        {how_it_works.map(item => {
          return <div className={styles.cardWrapper} key={item.id}>
            <h2>0{item.id}</h2>
            <h3>{item.title}</h3>
            <p>{item.text}</p>
          </div>
        })}
      </div>
    </section>
  );
};

export default HowItWorks;
