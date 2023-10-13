import React, { createContext, useState } from 'react';

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  const handleLogin = async (username, password) => {
  
  };

  const handleSignup = async (username, password) => {
 
  };

  const handleLogout = () => {
 
  };

  return (
    <AuthContext.Provider value={{ user, setUser, handleLogin, handleSignup, handleLogout }}>
      {children}
    </AuthContext.Provider>
  );
}