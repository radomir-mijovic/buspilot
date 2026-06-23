import styles from "./RequestDemoButton.module.scss";

const RequestDemoButton = ({ large }) => {
  return (
    <a href="/request-demo">
      <button className={`${styles.button} ${styles[large]}`} type="button">
        Request Demo
      </button>
    </a>
  );
};
export default RequestDemoButton;
