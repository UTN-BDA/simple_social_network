import { createContext, useContext, useState } from "react";

const UserContext = createContext(null);


export const useUser = () => useContext(UserContext);


export const UserProvider = ({ children }) => {
  const [usuario, setUsuario] = useState(null);

  return (
    <UserContext.Provider value={{ usuario, setUsuario }}>
      {children}
    </UserContext.Provider>
  );
};
