import { createContext, useContext, useState } from "react";

const DriverContext = createContext();

export const DriverProvider = ({ children }) => {
  const [isRideChanged, setIsRideChanged] = useState(false);
  const [filterDate, setFilterDate] = useState("");

  return (
    <DriverContext.Provider
      value={{ isRideChanged, setIsRideChanged, filterDate, setFilterDate }}
    >
      {children}
    </DriverContext.Provider>
  );
};

export const useDriver = () => {
  return useContext(DriverContext);
};
