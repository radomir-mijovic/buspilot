import styles from "./DriverWidget.module.scss";

const DriverWidget = ({ count, title, isDanger }) => {
  return (
    <div className={styles.driverWidget}>
      <h3 className={isDanger ? styles.danger : ""}>{count}</h3>
      <p>{title}</p>
    </div>
  );
};

export default DriverWidget;
