import styles from "./RequestDemo.module.scss";
import RequestDemoCard from "./RequestDemoCard";

const RequestDemo = () => {
  return (
    <div className={styles.pageWrapper}>
      <RequestDemoCard />
    </div>
  );
};

export default RequestDemo;
