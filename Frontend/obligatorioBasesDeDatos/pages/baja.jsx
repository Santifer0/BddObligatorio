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
    const userPassword = location.state?.userPassword || "";
    const modal = location.state?.modal || "Item";


    const [id, setId] = useState("");
    const [ci, setCi] = useState("");

    const Confirmar= async () => {
        // Usar la sesión establecida en el login
        let endpoint = "";
        let body = {};

        if (modal === "Insumos") {
            endpoint = "http://localhost:5000/api/insumos/baja";
            body = { id };
        } else if (modal === "Técnicos") {
            endpoint = "http://localhost:5000/api/tecnicos/baja";
            body = { ci };
        } else if (modal === "Clientes") {
            endpoint = "http://localhost:5000/api/clientes/baja";
            body = { id };
        } else if (modal === "Empresas") {
            endpoint = "http://localhost:5000/api/empresas/baja";
            body = { id };
        } else if (modal === "Locales") {
            endpoint = "http://localhost:5000/api/locales/baja";
            body = { id };
        } else if (modal === "Proveedores") {
            endpoint = "http://localhost:5000/api/proveedores/baja";
            body = { id };
        } else if (modal === "Usuarios") {
            endpoint = "http://localhost:5000/api/usuarios/baja";
            body = { id };
        } else if (modal === "Máquinas") {
            endpoint = "http://localhost:5000/api/maquinas/baja";
            body = { id };
        } else if (modal === "Mantenimientos") {
            endpoint = "http://localhost:5000/api/mantenimientos/baja";
            body = { id };
        } else if (modal === "Registro_Consumo") {
            endpoint = "http://localhost:5000/api/registro_consumo/baja";
            body = { id };
        } else {
            endpoint = "http://localhost:5000/api/insumos/baja";
            body = { id };
        }

        try {
            const response = await fetch(endpoint, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: "include",
                body: JSON.stringify(body),
            });
            if (response.ok) {
                const data = await response.json();
                if (data.status === "ok") {
                    alert("Baja realizada con éxito.");
                    navigate("/Gestion", { state: { userName, Permiso, userPassword } });
                } else {
                    alert("Error al realizar la baja: " + data.message);
                }
            } else {
                const errorData = await response.json();
                alert("Error: " + errorData.message);
            }
        } catch (error) {
            console.error("Error en la solicitud:", error);
            alert("Hubo un problema al realizar la baja.");
        }
    };

    const volverAGestion = () => {
        navigate("/Gestion", { state: { userName, Permiso, userPassword } });
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
