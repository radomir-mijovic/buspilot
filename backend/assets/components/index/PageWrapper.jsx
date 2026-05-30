import Capabilities from "./capabilities/Capabilities";
import Header from "./header/Header";
import Hero from "./hero/Hero";
import style from "./PageWrapper.module.css";
import Platform from "./platform/Platform";
import Switch from "./switch/Switch";

const PageWrapper = () => {
  return (
    <div className={style.pageWrapper}>
      <Header />
      <Hero />
      <Platform />
      <Capabilities />
      <Switch />
    </div>
  );
};

export default PageWrapper;
