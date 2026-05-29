import Header from "./header/Header";
import Hero from "./hero/Hero";
import style from "./PageWrapper.module.css";

const PageWrapper = () => {
  return (
    <div className={style.pageWrapper}>
      <Header />
      <Hero />
    </div>
  );
};

export default PageWrapper;
