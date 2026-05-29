import Header from "./header/Header";
import Hero from "./hero/Hero";
import style from "./PageWrapper.module.css";
import Platform from "./platform/Platform";

const PageWrapper = () => {
  return (
    <div className={style.pageWrapper}>
      <Header />
      <Hero />
      <Platform />
    </div>
  );
};

export default PageWrapper;
