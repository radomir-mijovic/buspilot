import driver_menu_link from "../../utils/driver_menu_links";
import styles from "./DriverMenu.module.scss";
import { IoCloseOutline } from "react-icons/io5";

const DriverMenu = ({ setMenu }) => {
  return (
    <div className={styles.menuWrapper}>
      {driver_menu_link.map((link) => (
        <a href={link.href} key={link.id}>
          {link.title}
        </a>
      ))}
      <IoCloseOutline
        style={{ position: "absolute", right: 10, top: 10 }}
        size={25}
        color={"#8A8F96"}
        onClick={() => setMenu(false)}
      />
    </div>
  );
};

export default DriverMenu;
