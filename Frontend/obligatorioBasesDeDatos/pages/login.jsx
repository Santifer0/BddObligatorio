import React, { useContext, useState } from "react";
import './css/login.css';
import { UserContext } from "../context/UserContext";
import { useNavigate } from "react-router-dom";
import fondoLogin from '../src/assets/fondo-login.jpg';

const Login = () => {
  const { userName, setUserName } = useContext(UserContext);
  const [contraseña, setContraseña] = useState("");
  const navigate = useNavigate();

  const Ingresar = async () => {
    if (userName === "" || contraseña === "") {
      alert("Por favor, complete todos los campos.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include", // ¡ESTO ES CRUCIAL!
        body: JSON.stringify({ nombre: userName, contrasenia: contraseña }),
      });

      const data = await response.json();

      if (response.ok) {
        navigate("/Home", { state: { userName: data.userName, Permiso: data.Permiso, userPassword: contraseña } });
      } else {
        alert("Usuario o contraseña incorrectos.");
      }
    } catch (error) {
      console.error("Error al intentar iniciar sesión:", error);
      alert("Hubo un problema al intentar iniciar sesión.");
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