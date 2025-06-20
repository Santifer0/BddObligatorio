import React, { useContext, useState } from "react";
import './css/login.css';
import { UserContext } from "../context/UserContext";
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";
import fondoLogin from '../src/assets/fondo-login.jpg';

const Login = () => {
  const { userName, setUserName } = useContext(UserContext);
  const [contraseña, setContraseña] = useState("");
  const navigate = useNavigate();

  const Ingresar = () => {
    // Aquí podrías validar el login con backend
    // Si es correcto:
    if (userName === "" || contraseña === "") {
      alert("Por favor, complete todos los campos.");
      return;
    }
    if (userName === "admin") {
      navigate("/Home", { state: { userName, Permiso: true } });
    } else {
      navigate("/Home", { state: { userName, Permiso: false } });
    }
  };

  return (
    <div
      className="modal-background"
      style={{
        backgroundImage: `url(${fondoLogin})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        minHeight: '100vh',
        minWidth: '100vw',
        position: 'fixed',
        top: 0,
        left: 0,
        zIndex: 1,
      }}
    >
      <div className="modal">
        <h2>Ingresar</h2>
        <input
          placeholder="Ingrese su usuario"
          value={userName}
          onChange={e => setUserName(e.target.value)}
        />
        <input
          type="password"
          placeholder="Ingrese su contraseña"
          value={contraseña}
          onChange={e => setContraseña(e.target.value)}
        />
        <button className="login-button" onClick={Ingresar}>
          Ingresar
        </button>
      </div>
    </div>
  );
};

export default Login;