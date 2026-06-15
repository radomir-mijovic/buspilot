import styles from "./RequestDemoCard.module.scss";
import { BsCheckAll } from "react-icons/bs";
import brandLogo from "../../icons/buspilot-favicon.svg";
import RequestDemoForm from "./RequestDemoForm";
import { useState } from "react";

const RequestDemoCard = () => {
  const [response, setResponse] = useState("");

  return (
    <div className={styles.cardWrapper}>
      <div className={styles.rightSide}>
        <a href="/">
          <div className={styles.logoWrapper}>
            <img src={brandLogo} alt="" width={40} height={40} />
            <h3>BusPilot</h3>
          </div>
        </a>
        <div className={styles.textWrapper}>
          <h5>Fleet management, simplified</h5>
          <h2>Run your entire transport operation from one dashboard.</h2>
          <p>
            Vehicles, drivers, rides, schedules, agencies and documents —
            organized, clear, and under control.
          </p>
          <div className={styles.infoWrapper}>
            <h6>
              <span>
                <BsCheckAll />
              </span>
              Personalized 30-minute walkthrough
            </h6>
            <h6>
              <span>
                <BsCheckAll />
              </span>
              Tailored to your fleet & workflows
            </h6>
            <h6>
              <span>
                <BsCheckAll />
              </span>
              No commitment, no setup required
            </h6>
          </div>
          <div className={styles.lowerPWrapper}>
            <p>We'll get back to you within one business day.</p>
            <p>
              Already have an account? <a href="/login">Sign in</a>
            </p>
          </div>
        </div>
      </div>
      <div className={styles.leftSide}>
        {response ? (
          <>
            <h4>{response}</h4>
            <a href="/">Go to website</a>
          </>
        ) : (
          <>
            <div className={styles.lowerTextWrapper}>
              <h5>request a demo</h5>
              <h2>See BusPilot in action</h2>
              <p>
                Tell us a bit about your company and we'll set up a personalized
                walkthrough.
              </p>
            </div>
            <RequestDemoForm setResponse={setResponse} />
          </>
        )}
      </div>
    </div>
  );
};

export default RequestDemoCard;
