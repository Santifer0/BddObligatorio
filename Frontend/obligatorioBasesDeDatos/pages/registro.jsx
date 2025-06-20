import React, { useContext } from "react";
import './css/home.css';
import { UserContext } from "../context/UserContext";
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

import fondoLogin from '../src/assets/fondo-login.jpg';

const IngresarGestion = () => {
    // Aquí podrías validar el login con backend
    // Si es correcto:
    navigate("/Home");
  };

const IngresarRegistro = () => {
    // Aquí podrías validar el login con backend
    // Si es correcto:
    navigate("/Home");
  };


const Registro = () => {

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
        <h2>Registro</h2>
        <button className="button" onClick={IngresarGestion}>
          Gestion
        </button>
        <br></br>
        <button className="button" onClick={IngresarRegistro}>
          Registros
        </button>
      </div>
    </div>
  );
};

export default Registro;