import driver_menu_link from "../../utils/driver_menu_links";
import styles from "./DriverMenu.module.scss";

const DriverMenu = () => {
  return (
    <div className={styles.menuWrapper}>
      {driver_menu_link.map((link) => (
        <a href={link.href} key={link.id}>
          {link.title}
        </a>
      ))}
    </div>
  );
};

export default DriverMenu;
