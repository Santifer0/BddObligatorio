import React, { useState } from "react";
import './css/gestion.css';
import fondoLogin from '../src/assets/fondo-login.jpg';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

const Registro = () => {
  const [modal, setModal] = useState(null);
  const navigate = useNavigate();
  const location = useLocation();
  const userName = location.state?.userName || "Usuario Anónimo";


  function handleOpenModal(nombre) {
    setModal(nombre);
  }
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
        <button onClick={() => handleOpenModal("Insumos")}>
          consumo de Insumos
        </button>
        <button onClick={() => handleOpenModal("Máquinas")}>
          alquiler mensual de máquinas por cliente
        </button>
        <button onClick={() => handleOpenModal("Técnicos")}>
          total a cobrar por cliente
        </button>
        <button onClick={() => handleOpenModal("Clientes")}>
          total de mantenimientos por ci_tecnico
        </button>
        <button onClick={() => handleOpenModal("Insumos")}>
          maquinas por cliente
        </button>

      </div>
    </div>
  );
};

export default Registro;