import Built from "./built/Built";
import Capabilities from "./capabilities/Capabilities";
import Footer from "./footer/Footer";
import Header from "./header/Header";
import Hero from "./hero/Hero";
import HowItWorks from "./howItWorks/HowItWorks";
import Modernize from "./modernize/Modernize";
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
      <HowItWorks />
      <Built />
      <Modernize />
      <Footer />
    </div>
  );
};

export default PageWrapper;
