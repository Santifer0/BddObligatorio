<<<<<<< HEAD
=======
import React, { useState } from "react";
import './css/alta.css';
import './css/gestion.css';
import './css/baja.css';
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
    const [showModal, setShowModal] = useState(false);
    const [listData, setListData] = useState([]);
    const [loading, setLoading] = useState(false);

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

    const obtenerLista = async () => {
        setLoading(true);
        setShowModal(true);
        
        try {
            let endpoint = "";
            
            if (modal === "Insumos") {
                endpoint = "http://localhost:5000/api/insumos";
            } else if (modal === "Técnicos") {
                endpoint = "http://localhost:5000/api/tecnicos";
            } else if (modal === "Clientes") {
                endpoint = "http://localhost:5000/api/clientes";
            } else if (modal === "Proveedores") {
                endpoint = "http://localhost:5000/api/proveedores";
            } else if (modal === "Usuarios") {
                endpoint = "http://localhost:5000/api/usuarios";
            } else if (modal === "Máquinas") {
                endpoint = "http://localhost:5000/api/maquinas";
            } else if (modal === "Mantenimientos") {
                endpoint = "http://localhost:5000/api/mantenimientos";
            }

            const response = await fetch(endpoint, {
                method: "GET",
                credentials: "include"
            });

            if (response.ok) {
                const data = await response.json();
                setListData(data);
            } else {
                alert("Error al obtener la lista");
            }
        } catch (error) {
            console.error("Error:", error);
            alert("Error al conectar con el servidor");
        } finally {
            setLoading(false);
        }
    };

    const seleccionarElemento = (elemento) => {
        if (modal === "Técnicos") {
            setCi(elemento.ci || elemento.CI);
        } else {
            setId(elemento.id || elemento.ID);
        }
        setShowModal(false);
    };

    const cerrarModal = () => {
        setShowModal(false);
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
                <button type="button" onClick={obtenerLista}>
                    Ver Lista de {modal}
                </button>
                <button type="button" onClick={Confirmar}>
                    Confirmar Baja
                </button>
                <button type="button" onClick={volverAGestion}>
                    Volver a Gestión
                </button>
            </div>

            {/* Modal de lista */}
            {showModal && (
                <div className="modal-content">
                    <h3>Lista de {modal}</h3>
                    {loading ? (
                        <p>Cargando...</p>
                    ) : (
                        <div>
                            {listData.length === 0 ? (
                                <p>No hay elementos disponibles</p>
                            ) : (
                                <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                                    <thead>
                                        <tr style={{ borderBottom: '2px solid #ccc' }}>
                                            <th style={{ padding: '10px', textAlign: 'left' }}>
                                                {modal === "Técnicos" ? "CI" : "ID"}
                                            </th>
                                            <th style={{ padding: '10px', textAlign: 'left' }}>Nombre</th>
                                            <th style={{ padding: '10px', textAlign: 'left' }}>Datos</th>
                                            <th style={{ padding: '10px', textAlign: 'left' }}>Acción</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {listData.map((elemento, index) => (
                                            <tr key={index} style={{ borderBottom: '1px solid #eee' }}>
                                                <td style={{ padding: '8px' }}>
                                                    {modal === "Técnicos" ? (elemento.ci || elemento.CI) : (elemento.id || elemento.ID)}
                                                </td>
                                                <td style={{ padding: '8px' }}>
                                                    {elemento.nombre || elemento.Nombre || elemento.modelo || elemento.nombre_publico || "N/A"}
                                                </td>
                                                <td style={{ padding: '8px' }}>
                                                    {modal === "Insumos" && `$${elemento.precio}`}
                                                    {modal === "Clientes" && elemento.telefono}
                                                    {modal === "Técnicos" && elemento.apellido}
                                                    {modal === "Proveedores" && elemento.contacto}
                                                    {modal === "Usuarios" && (elemento.permisos === 1 ? "Admin" : "User")}
                                                    {modal === "Máquinas" && elemento.ubicacionCliente}
                                                    {modal === "Mantenimientos" && elemento.tipo}
                                                </td>
                                                <td style={{ padding: '8px' }}>
                                                    <button 
                                                        onClick={() => seleccionarElemento(elemento)}
                                                        style={{
                                                            backgroundColor: '#dc3545',
                                                            color: 'white',
                                                            border: 'none',
                                                            padding: '5px 10px',
                                                            borderRadius: '3px',
                                                            cursor: 'pointer'
                                                        }}
                                                    >
                                                        Seleccionar
                                                    </button>
                                                </td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            )}
                            <div style={{ marginTop: '20px', textAlign: 'center' }}>
                                <button className="cerrar" onClick={cerrarModal}>
                                    Cerrar
                                </button>
                            </div>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default Baja;
>>>>>>> 27b333fd7684ad9edb2c1c713af5bcf51a3ed8dd
