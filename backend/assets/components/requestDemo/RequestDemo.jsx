import styles from "./RequestDemo.module.scss";
import RequestDemoCard from "./RequestDemoCard";
import RequestDemoMobileCard from "./RequestDemoMobileCard";

const RequestDemo = () => {
  return (
    <div className={styles.pageWrapper}>
      <RequestDemoCard />
      <RequestDemoMobileCard />
    </div>
  );
};

export default RequestDemo;
