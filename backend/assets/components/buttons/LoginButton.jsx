import styles from "./LoginButton.module.scss";

const LoginButton = ({ large }) => {
  return (
    <a href="/login">
      <button className={`${styles.button} ${styles[large]}`}>Login</button>
    </a>
  );
};

export default LoginButton;
