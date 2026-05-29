import LoginButton from "../../buttons/LoginButton";
import RequestDemoButton from "../../buttons/RequestDemoButton";
import BuiltFor from "./BuiltFor";
import styles from "./Hero.module.scss";
import heroImage from "../../../images/hero-image.png"

const Hero = () => {
  return (
    <section className={styles.heroWrapper}>
      <div className={styles.textWrapper}>
        <BuiltFor />
        <h1>Manage your entire transport operation from one dashboard</h1>
        <h6>
          Organize vehicles, drivers, rides, schedules, agencies, and company
          documents in one powerful fleet management platform.
        </h6>
        <p>
          Built for bus operators, shuttle services, tourism transport
          companies, and travel agencies that need clarity, organization, and
          control.
        </p>
      </div>
      <div className={styles.buttonWrapper}>
        <RequestDemoButton large="large" />
        <LoginButton large="large" />
      </div>
      <p className={styles.lowerP}>
        Trusted by modern transport operations to simplify daily management.
      </p>
      <div className={styles.imageWrapper}>
        <img src={heroImage} alt="" />
      </div>
    </section>
  );
};

export default Hero;
