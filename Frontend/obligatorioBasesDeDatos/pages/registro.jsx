import React, { useState } from "react";
import './css/registro.css';
import fondoLogin from '../src/assets/fondo-login.jpg';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

const apiEndpoints = {
  "Máquinas": "/api/registro/alquiler",
  "Técnicos": "/api/registro/consumo/reporte",
  "Clientes": "/api/registro/mantenimientos-tecnico",
  "Insumos": "/api/registro/maquinas-cliente"
};

const infoModals = {
  "Máquinas": {
    title: "Alquiler mensual de máquinas por cliente"
  },
  "Técnicos": {
    title: "Total a cobrar por cliente"
  },
  "Clientes": {
    title: "Total de mantenimientos por técnico"
  },
  "Insumos": {
    title: "Máquinas por cliente"
  }
};

function Registro() {
  const [modal, setModal] = useState(null);
  const [modalData, setModalData] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();
  const userName = location.state?.userName || "Usuario Anónimo";
  const Permiso = location.state?.Permiso || false;
  const userPassword = location.state?.userPassword || "";

  async function handleOpenModal(nombre) {
    setModal(nombre);
    setLoading(true);
    setModalData("");
    try {
      const endpoint = apiEndpoints[nombre];
      console.log(`Intentando conectar a: ${endpoint}`);
      if (endpoint) {
        const fullUrl = `http://localhost:5000${endpoint}`;
        console.log(`URL completa: ${fullUrl}`);
        const res = await fetch(fullUrl, {
          method: 'GET',
          credentials: 'include',
          headers: {
            'Content-Type': 'application/json',
          }
        });
        console.log(`Respuesta status: ${res.status}`);
        if (res.ok) {
          const data = await res.json();
          console.log('Datos recibidos:', data);
          setModalData(data);
        } else {
          console.error(`Error en la respuesta: ${res.status}`);
          setModalData(null);
        }
      } else {
        console.error('No hay endpoint definido para:', nombre);
        setModalData(null);
      }
    } catch (e) {
      console.error('Error en la petición:', e);
      setModalData(null);
    }
    setLoading(false);
  }

  function handleCloseModal() {
    setModal(null);
    setModalData("");
  }

  function renderTable(nombre, data) {
    console.log(`Renderizando tabla para ${nombre} con datos:`, data);
    if (!data) return <p style={{ color: 'black' }}>No hay datos para mostrar.</p>;
    let rows = [];
    let headers = [];

    if (nombre === "Máquinas" && data.alquileres) {
      headers = ["Cliente", "Total Alquiler ($)"];
      if (Array.isArray(data.alquileres) && data.alquileres.length > 0) {
        rows = data.alquileres.map(([cliente, total]) => [cliente, total]);
      } else {
        return <p style={{ color: 'black' }}>No hay alquileres registrados.</p>;
      }
    } else if (nombre === "Técnicos" && data.totales) {
      headers = ["Cliente", "Alquiler Total ($)", "Insumos Total ($)", "Total a Cobrar ($)"];
      if (Array.isArray(data.totales) && data.totales.length > 0) {
        rows = data.totales.map(([cliente, alquiler, insumos, total]) => [cliente, alquiler, insumos, total]);
      } else {
        return <p style={{ color: 'black' }}>No hay totales calculados.</p>;
      }
    } else if (nombre === "Clientes" && data.mantenimientos) {
      headers = ["Técnico", "Total Mantenimientos"];
      if (Array.isArray(data.mantenimientos) && data.mantenimientos.length > 0) {
        rows = data.mantenimientos.map(([tecnico, total]) => [tecnico, total]);
      } else {
        return <p style={{ color: 'black' }}>No hay mantenimientos registrados.</p>;
      }
    } else if (nombre === "Insumos" && data.maquinas) {
      headers = ["Cliente", "Total Máquinas", "Modelos"];
      if (Array.isArray(data.maquinas) && data.maquinas.length > 0) {
        rows = data.maquinas.map(([cliente, total, modelos]) => [cliente, total, modelos]);
      } else {
        return <p style={{ color: 'black' }}>No hay máquinas registradas.</p>;
      }
    } else {
      return <p style={{ color: 'black' }}>Error: Formato de datos no reconocido para {nombre}.</p>;
    }

    return (
      <table className="tabla-modal" style={{ color: 'black' }}>
        <thead>
          <tr>
            {headers.map((h, i) => <th key={i} style={{ color: 'black' }}>{h}</th>)}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, i) => (
            <tr key={i}>
              {row.map((cell, j) => <td key={j} style={{ color: 'black' }}>{cell}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    );
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
      <div className="modal main-modal">
        <h2>Registro</h2>
        <button onClick={() => navigate("/RegistroConsumo", { state: { userName, Permiso, userPassword } })}>
          consumo de Insumos
        </button>
        <button onClick={() => handleOpenModal("Máquinas")}>alquiler mensual de máquinas por cliente</button>
        <button onClick={() => handleOpenModal("Técnicos")}>total a cobrar por cliente</button>
        <button onClick={() => handleOpenModal("Clientes")}>total de mantenimientos por ci_tecnico</button>
        <button onClick={() => handleOpenModal("Insumos")}>maquinas por cliente</button>
        <button className="back" onClick={() => navigate("/Home", { state: { userName, Permiso, userPassword } })}>
          back
        </button>
      </div>
      {modal && (
        <div className="custom-modal-overlay">
          <div className="custom-modal-content" style={{ background: 'white', borderRadius: '10px', padding: '2rem', minWidth: '320px', maxWidth: '90vw', color: 'black' }}>
            <h3 style={{ color: 'black' }}>{infoModals[modal]?.title || "Información"}</h3>
            {loading ? <p style={{ color: 'black' }}>Cargando...</p> : renderTable(modal, modalData)}
            <button onClick={handleCloseModal} style={{ color: 'white', backgroundColor: '#333', border: 'none', padding: '10px 20px', borderRadius: '5px', cursor: 'pointer' }}>Cerrar</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Registro;