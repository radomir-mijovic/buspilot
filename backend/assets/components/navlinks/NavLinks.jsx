import { useState } from "react";
import nav_links from "../../utils/nav_links";
import styles from "./NavLinks.module.scss";
import { isMobile } from "react-device-detect";

const NavLinks = () => {
  const [activeSublink, setActiveSublink] = useState(0);

  if (isMobile) {
    return;
  }

  const currentPath =
    typeof window !== "undefined" ? window.location.pathname : "";

  return (
    <div className={styles.navlinksWrapper}>
      <ul className={styles.links}>
        {nav_links.map((link) => {
          const LinkIcon = link.icon;
          return (
            <div key={link.id}>
              <li
                onMouseEnter={() => setActiveSublink(link.id)}
                className={styles.link}
                key={link.id}
              >
                <LinkIcon />
                <a
                  className={styles.active}
                  href={link.href}
                >
                  {link.title}
                </a>
                {link.sublinkId === activeSublink && (
                  <div onMouseLeave={() => setActiveSublink(false)} className={styles.sublinks}>
                    {link.sublinks.map((sublink) => {
                      const SubIcon = sublink.icon;
                      return (
                        <a key={sublink.id} href={sublink.href}>
                          <div className={styles.innerDiv} key={sublink.id}>
                            {SubIcon && (
                              <div className={styles.iconWrapper}>
                                <SubIcon className={styles.icon} size={20} />
                              </div>
                            )}
                            <p
                              className={`${sublink.href === currentPath ? styles.active : ""}`}
                            >
                              {sublink.subtitle}
                            </p>
                          </div>
                        </a>
                      );
                    })}
                  </div>
                )}
              </li>
            </div>
          );
        })}
      </ul>
    </div>
  );
};

export default NavLinks;
