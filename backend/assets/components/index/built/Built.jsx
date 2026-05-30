import styles from "./Built.module.scss";

const pills = [
  "Bus companies",
  "Shuttle services",
  "Tourism transportation",
  "Airport transfer companies",
  "Travel agencies",
  "Corporate transport",
];

const Built = () => {
  return (
    <section className={styles.sectionContainer}>
      <h4>Who it's for</h4>
      <h2>Built for modern transport businesses</h2>
      <div className={styles.pillsContainer}>
        <div className={styles.pillsWrapper}>
          {pills.map((item, index) => <div className={styles.pill} key={index}>
            <div className={styles.blueDot}/>
            <h3>{item}</h3>
          </div>)}
        </div>
      </div>
    </section>
  );
};

export default Built;
