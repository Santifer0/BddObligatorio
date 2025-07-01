import React, { useContext,useState } from "react";
import './css/home.css';
import { UserContext } from "../context/UserContext";
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";
import fondoLogin from '../src/assets/fondo-login.jpg';

const Home = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const [userName] = useState(location.state?.userName || "Usuario Anónimo");
  const [Permiso] = useState(location.state?.Permiso || false);
  const [userPassword] = useState(location.state?.userPassword || "");

  const IngresarGestion = () => {
    navigate("/Gestion" , { state: { userName, Permiso, userPassword} });
  };

  const IngresarRegistro = () => {
    navigate("/Registro" , { state: { userName, Permiso, userPassword} });
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
        <h2>¡Bienvenido {userName}!</h2>
        <button onClick={IngresarGestion}>
          Gestion
        </button>
        <br />
        <button onClick={IngresarRegistro}>
          Registros
        </button>
      </div>
    </div>
  );
};

export default Home;