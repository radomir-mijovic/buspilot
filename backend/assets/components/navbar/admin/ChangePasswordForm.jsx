import { useState } from "react";
import getCookie from "../../../utils/get_cookie";
import styles from "./ChangePasswordForm.module.scss";

const ChangePasswordForm = () => {
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [oldPasswordError, setOldPasswordError] = useState("");
  const [newPasswordError, setNewPasswordError] = useState("");

  const onSubmitHandler = async (e) => {
    e.preventDefault();
    setOldPasswordError("");
    setNewPasswordError("");

    try {
      const res = await fetch("/api/auth/change-password", {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({
          old_password: oldPassword,
          new_password: newPassword,
        }),
      });

      if (!res.ok) {
        const errorData = await res.json();
        setOldPasswordError(errorData.old_password);
        setNewPasswordError(errorData.new_password);
        return;
      }

      if (res.ok) {
        window.location.href = "/login";
      }
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <form className={styles.formWrapper} onSubmit={onSubmitHandler}>
      <div>
        {oldPasswordError && (
          <h6 style={{ color: "red" }}>{oldPasswordError}</h6>
        )}
        <input
          onChange={(e) => setOldPassword(e.target.value)}
          type="password"
          name="old_password"
          placeholder="Stari password"
        />
      </div>
      <div>
        {newPasswordError && (
          <h6 style={{ color: "red" }}>{newPasswordError}</h6>
        )}
        <input
          onChange={(e) => setNewPassword(e.target.value)}
          type="password"
          name="new_password"
          placeholder="Novi password"
        />
      </div>
      <button type="submit">Promijeni lozinku</button>
    </form>
  );
};

export default ChangePasswordForm;
