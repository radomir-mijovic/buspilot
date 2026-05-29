import styles from "./HeaderLinks.module.scss"
import header_links from "../../utils/header_links.js";

const HeaderLinks = () => {
  return (
    <div className={styles.headerLinkWrapper}>
      {header_links.map((link) => (
        <h5 className={styles.headerLinkH5} key={link.id}>{link.title}</h5>
      ))}
    </div>
  );
};

export default HeaderLinks;
