import styles from "./RequestDemoButton.module.scss";

const RequestDemoButton = ({ large }) => {
  return (
    <button className={`${styles.button} ${styles[large]}`} type="button">
      Request Demo
    </button>
  );
};
export default RequestDemoButton;
