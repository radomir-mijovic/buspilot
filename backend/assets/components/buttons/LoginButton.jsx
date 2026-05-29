import styles from "./LoginButton.module.scss";

const LoginButton = ({ large }) => {
  return (
    <button className={`${styles.button} ${styles[large]}`}>
      <a href="/login">Login</a>
    </button>
  );
};

export default LoginButton;
