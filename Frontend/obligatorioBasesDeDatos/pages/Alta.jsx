import React, { useState } from "react";
import './css/gestion.css';
import fondoLogin from '../src/assets/fondo-login.jpg';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

const Alta = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const userName = location.state?.userName || "Usuario Anónimo";
    const Permiso = location.state?.Permiso || false;
    const modal = location.state?.modal || "Item";
    const accion = location.state?.accion || "Alta";

    const [nombre, setNombre] = useState("");
    const [contacto, setContacto] = useState("");
    const [precio, setPrecio] = useState("");
    const [id, setId] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        const data = {
            nombre,
            contacto,
            precio,
            id
        };
        console.log(`${accion} de ${modal}:`, data);

        alert(`${accion} de ${modal} realizada exitosamente!`);

        // Limpiar campos
        setNombre("");
        setContacto("");
        setPrecio("");
        setDescripcion("");
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
                <h2>{accion} de {modal}</h2>
                <input
                    className="nombre"
                    type="text"
                    placeholder="Ingrese el nombre"
                    value={nombre}
                    onChange={(e) => setNombre(e.target.value)}
                    required
                />
                <input
                    className="input-modal"
                    type="text"
                    placeholder="Ingrese el contacto"
                    value={contacto}
                    onChange={(e) => setContacto(e.target.value)}
                />
                <input
                    className="input-modal"
                    type="number"
                    placeholder="Ingrese el precio"
                    value={precio}
                    onChange={(e) => setPrecio(e.target.value)}
                />
                <input
                    className="input-modal"
                    type="text"
                    placeholder={`Ingrese id del proveedor`}
                    value={id}
                    onChange={(e) => setId(e.target.value)}
                />
                
                <br />
                <button type="submit">
                    Confirmar {accion}
                </button>
                <button type="button" onClick={volverAGestion}>
                    Volver a Gestión
                </button>
            </div>
        </div>
    );
};

export default Alta;