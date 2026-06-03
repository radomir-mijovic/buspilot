import { useState } from "react";
import nav_links from "../../utils/nav_links";
import styles from "./MobileNavbar.module.scss";
import { isBrowser } from "react-device-detect";
import { FiChevronUp, FiChevronDown } from "react-icons/fi";

const MobileNavbar = ({ setIsMobileMenu }) => {
  if (isBrowser) {
    return;
  }

  const currentPath =
    typeof window !== "undefined" ? window.location.pathname : "";

  const initialOpen = nav_links.filter(
    (l) => l.has_sublinks && l.sublinks.some((s) => s.href === currentPath),
  );

  const [openIds, setOpenIds] = useState(initialOpen);

  const toggle = (id) => {
    setOpenIds((prev) =>
      prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id],
    );
  };

  const isActive = (href) => currentPath === href;
  const isSectionActive = (link) =>
    (link.href && isActive(link.href)) ||
    (link.has_sublinks && link.sublinks.some((s) => isActive(s.href)));

  return (
    <nav className={styles.navWrapper}>
      {nav_links.map((link) => {
        const Icon = link.icon;
        const open = openIds.includes(link.id);
        const sectionActive = isSectionActive(link);

        if (!link.has_sublinks) {
          return (
            <a
              href={link.href}
              key={link.id}
              onClick={() => setIsMobileMenu(false)}
              className={`${styles.item} ${sectionActive ? styles.active : ""}`}
            >
              <Icon size={20} className={styles.icon} />
              <span className={styles.title}>{link.title}</span>
            </a>
          );
        }

        return (
          <div key={link.id}>
            <button
              type="button"
              onClick={() => toggle(link.id)}
              className={`${styles.item} ${sectionActive ? styles.active : ""}`}
            >
              <Icon size={20} className={styles.icon} />
              <span className={styles.title}>{link.title}</span>
              {open ? (
                <FiChevronUp className={styles.chevron} />
              ) : (
                <FiChevronDown className={styles.chevron} />
              )}
            </button>

            {open && (
              <ul className={styles.sublinks}>
                {link.sublinks.map((sub) => {
                  return (
                    <li key={sub.id}>
                      <a
                        href={sub.href}
                        onClick={() => setIsMobileMenu(false)}
                        className={`${styles.subitem} ${isActive(sub.href) ? styles.active : ""}`}
                      >
                        <span className={styles.dot} />
                        <span>{sub.subtitle}</span>
                      </a>
                    </li>
                  );
                })}
              </ul>
            )}
          </div>
        );
      })}
    </nav>
  );
};
export default MobileNavbar;
