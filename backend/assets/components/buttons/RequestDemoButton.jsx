import styles from "./RequestDemoButton.module.scss";

const RequestDemoButton = ({ large }) => {
  return (
    <button className={`${styles.button} ${styles[large]}`} type="button">
      <a href="/request-demo">Request Demo</a>
    </button>
  );
};
export default RequestDemoButton;
