import platform_points from "../../../utils/platform_points";
import styles from "./Platform.module.scss";
const Platform = () => {
  return (
    <section className={styles.platformWrapper}>
      <h4>the platform</h4>
      <h2>
        Everything your team needs. <br /> One centralized system.
      </h2>
      <h5>
        Stop managing operations across spreadsheets, papers, and disconnected
        tools.
      </h5>
      <h6>
        Our platform gives transport companies a complete operational overview —
        helping teams <br /> stay organized, reduce manual work, and manage
        fleets more efficiently every day.
      </h6>
      <div className={styles.pointsContainer}>
        <div className={styles.pointsWrapper}>
          {platform_points.map((item) => {
            return (
              <div className={styles.pointItems} key={item.id}>
                <img src={item.icon} width={20} height={20} alt="" />
                <p>{item.title}</p>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Platform;
