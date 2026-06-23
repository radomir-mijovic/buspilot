import { useEffect, useState } from "react";
import styles from "./RequestDemoForm.module.scss";

const RequestDemoForm = ({ setResponse }) => {
  const [company, setCompany] = useState("");
  const [contactNumber, setContactNumber] = useState("");
  const [country, setCountry] = useState("");
  const [email, setEmail] = useState("");
  const [countries, setCountries] = useState([]);
  const [responseError, setResponseError] = useState("")

  useEffect(() => {
    const fetchCountries = async () => {
      try {
        const res = await fetch("/api/request-demo", {
          method: "OPTIONS",
        });

        if (!res.ok) {
          throw new Error("HTTP Error!");
        }

        const data = await res.json();
        setCountries(data);
      } catch (err) {
        console.log(err);
      }
    };
    fetchCountries();
  }, []);

  const submitHandler = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("/api/request-demo", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: email,
          country: country,
          company: company,
          contact_number: contactNumber,
        }),
      });

      if (!res.ok) {
        const error_data = await res.json()
        setResponseError(error_data.email[0])
        throw new Error("HTTP Error!");
      }

      const data = await res.json();
      setResponse(data.details);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <form onSubmit={(e) => submitHandler(e)} className={styles.formWrapper}>
      <div className={styles.innerWrapper}>
        <label htmlFor="company">Company</label>
        <input
          placeholder="e.g. Adriatic Transport d.o.o."
          value={company}
          onChange={(e) => setCompany(e.target.value)}
          id="company"
          name="company"
          type="text"
        />
      </div>

      <div className={styles.innerWrapper}>
        <label htmlFor="contactNumber">Contact Number</label>
        <input
          value={contactNumber}
          onChange={(e) => setContactNumber(e.target.value)}
          id="contactNumber"
          name="contactNumber"
          type="text"
        />
      </div>

      <div className={styles.innerWrapper}>
        <label htmlFor="country">Country</label>
        <select
          onChange={(e) => setCountry(e.target.value)}
          name="country"
          id="country"
        >
          {countries?.map((country) => {
            return (
              <option key={country.name[0]} value={country.name[0]}>
                {country.name[1]}
              </option>
            );
          })}
        </select>
      </div>

      <div className={styles.innerWrapper}>
        <label htmlFor="email">Email</label>
        <p className={styles.pError}>{responseError}</p>
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          id="email"
          name="email"
          type="email"
        />
      </div>
      <button type="submit">Request Demo</button>
    </form>
  );
};

export default RequestDemoForm;
