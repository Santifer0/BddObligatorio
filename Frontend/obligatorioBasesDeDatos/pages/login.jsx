import React, { useContext, useState } from "react";
import './css/login.css';
import { UserContext } from "../context/UserContext";
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";
import fondoLogin from '../src/assets/fondo-login.jpg';
import apiService from '../src/services/apiService';

const Login = () => {
  const { userName, setUserName } = useContext(UserContext);
  const [contraseña, setContraseña] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const Ingresar = async () => {
    if (userName === "" || contraseña === "") {
      alert("Por favor, complete todos los campos.");
      return;
    }

    setLoading(true);
    try {
      const response = await apiService.login(userName, contraseña);
      
      if (response.success) {
        // Login exitoso, redirigir según permisos
        navigate("/Home", { 
          state: { 
            userName, 
            Permiso: response.es_administrador 
          } 
        });
      }
    } catch (error) {
      console.error('Error en login:', error);
      alert(error.message || "Error al intentar iniciar sesión. Verifique sus credenciales.");
    } finally {
      setLoading(false);
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
        <button 
          className="login-button" 
          onClick={Ingresar}
          disabled={loading}
        >
          {loading ? "Ingresando..." : "Ingresar"}
        </button>
      </div>
    </div>
  );
};

export default Login;