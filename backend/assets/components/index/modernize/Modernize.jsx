import styles from "./Modernize.module.scss";

const Modernize = () => {
  return (
    <section className={styles.sectionContainer}>
      <div className={styles.cardWrapper}>
        <h4>Get started</h4>
        <h2>Ready to modernize your fleet operations?</h2>
        <h5>
          Manage your transport business more efficiently with one centralized
          platform designed for real operational workflows. Save time, stay
          organized, and keep your entire fleet under control.
        </h5>
        <a href="/request-demo">
          <button className={styles.button} type="button">
            Request a Demo
          </button>
        </a>
      </div>
    </section>
  );
};

export default Modernize;
