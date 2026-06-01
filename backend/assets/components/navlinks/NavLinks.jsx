import { useState } from "react";
import nav_links from "../../utils/nav_links";
import styles from "./NavLinks.module.scss";

const NavLinks = () => {
  const [activeSublink, setActiveSublink] = useState(0);

  return (
    <div className={styles.navlinksWrapper}>
      <ul className={styles.links}>
        {nav_links.map((link) => {
          const LinkIcon = link.icon
          return (
            <div key={link.id}>
              <li
                onMouseEnter={() => setActiveSublink(link.id)}
                className={styles.link}
                key={link.id}
              >
                <LinkIcon/>
                <a href={link.href}>{link.title}</a>
                {link.sublinkId === activeSublink && (
                  <div className={styles.sublinks}>
                    {link.sublinks.map((sublink) => {
                      const SubIcon = sublink.icon;
                      return (
                        <a href={sublink.href}>
                          <div className={styles.innerDiv} key={sublink.id}>
                            {SubIcon && (
                              <div className={styles.iconWrapper}>
                                <SubIcon className={styles.icon} size={20} />
                              </div>
                            )}
                            <p>{sublink.subtitle}</p>
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
