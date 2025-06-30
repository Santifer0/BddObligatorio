import React, { useState } from "react";
import './css/alta.css';
import fondoLogin from '../src/assets/fondo-login.jpg';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

const Baja = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const userName = location.state?.userName || "Usuario Anónimo";
    const Permiso = location.state?.Permiso || false;
    const modal = location.state?.modal || "Item";


    const [id, setId] = useState("");
    const [ci, setCi] = useState("");


    const Confirmar= () => {
        alert(`Baja de ${modal} realizada exitosamente!`);
        // Aquí podrías agregar la lógica para enviar los datos al backend o realizar alguna acción adicional
    };

    const volverAGestion = () => {
        navigate("/Gestion", { state: { userName, Permiso } });
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
                <h2>Baja de {modal}</h2>
                <input
                    className={`Id${modal == "Técnicos" ? " invisible" : ""}`}
                    type="text"
                    placeholder="ID"
                    value={id}
                    onChange={e => setId(e.target.value)}
                />
                <input
                    className={`Ci${modal !== "Técnicos" ? " invisible" : ""}`}
                    type="number"
                    placeholder="CI"
                    value={ci}
                    onChange={e => setCi(e.target.value)}
                />
                <br />
                <button type="button" onClick={Confirmar}>
                    Confirmar Baja
                </button>
                <button type="button" onClick={volverAGestion}>
                    Volver a Gestión
                </button>
            </div>
        </div>
    );
};

export default Baja;