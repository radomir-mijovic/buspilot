import styles from "./RequestDemoMobileCard.module.scss";
import brandLogo from "../../icons/buspilot-favicon.svg";
import RequestDemoForm from "./RequestDemoForm";
import { useState } from "react";

const RequestDemoMobileCard = () => {
  const [response, setResponse] = useState("");

  return (
    <div className={styles.mobileCard}>
      <div className={styles.cardHeader}>
        <img src={brandLogo} alt="" width={20} height={20} />
        <h3 className="font-display">
          <a className={styles.logoA} href="/">BusPilot</a>
        </h3>
      </div>
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
          <div className={styles.lowerPWrapper}>
            <p>We'll get back to you within one business day.</p>
            <p>
              Already have an account? <a href="/login">Sign in</a>
            </p>
          </div>
        </>
      )}
    </div>
  );
};

export default RequestDemoMobileCard;
