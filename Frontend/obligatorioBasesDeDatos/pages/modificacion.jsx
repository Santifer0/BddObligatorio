import React, { useState } from "react";
import './css/alta.css';
import './css/gestion.css';
import './css/modificacion.css';
import fondoLogin from '../src/assets/fondo-login.jpg';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

const Modificacion = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const userName = location.state?.userName || "Usuario Anónimo";
    const Permiso = location.state?.Permiso || false;
    const userPassword = location.state?.userPassword || "";
    const modal = location.state?.modal || "Item";

    const [id, setId] = useState("");
    const [nombre, setNombre] = useState("");
    const [contacto, setContacto] = useState("");
    const [precio, setPrecio] = useState("");
    const [idProveedor, setIdProveedor] = useState("");
    const [direccion, setDireccion] = useState("");
    const [telefono, setTelefono] = useState("");
    const [correo, setCorreo] = useState("");
    const [modelo, setModelo] = useState("");
    const [id_cliente, setIdCliente] = useState("");
    const [ubicacion_cliente, setUbicacionCliente] = useState("");
    const [costo_alquiler_mensual, setCostoAlquilerMensual] = useState("");
    const [ci, setCi] = useState("");
    const [apellido, setApellido] = useState("");
    const [id_maquina, setIdMaquina] = useState("");
    const [ci_tecnico, setCiTecnico] = useState("");
    const [tipo, setTipo] = useState("");
    const [fecha, setFecha] = useState("");
    const [observaciones, setObservaciones] = useState("");
    const [nombre_publico, setNombrePublico] = useState("");
    const [contrasenia, setContrasenia] = useState("");
    const [id_insumo, setIdInsumo] = useState("");
    const [cantidad, setCantidad] = useState("");
    const [permisos, setPermisos] = useState("");
    const [showModal, setShowModal] = useState(false);
    const [listData, setListData] = useState([]);
    const [loading, setLoading] = useState(false);

    const Confirmar= async () => {
        // Usar la sesión establecida en el login
        let endpoint = "";
        let body = {};

        if (modal === "Insumos") {
            endpoint = "http://localhost:5000/api/insumos/modificacion";
            body = { id, nombre, precio, idProveedor };
        } else if (modal === "Técnicos") {
            endpoint = "http://localhost:5000/api/tecnicos/modificacion";
            body = { ci, telefono };
        } else if (modal === "Clientes") {
            endpoint = "http://localhost:5000/api/clientes/modificacion";
            body = { id, nombre, direccion, telefono, correo };
        } else if (modal === "Empresas") {
            endpoint = "http://localhost:5000/api/empresas/modificacion";
            body = { id, nombre, telefono, correo };
        } else if (modal === "Locales") {
            endpoint = "http://localhost:5000/api/locales/modificacion";
            body = { id, nombre, direccion, telefono, correo };
        } else if (modal === "Proveedores") {
            endpoint = "http://localhost:5000/api/proveedores/modificacion";
            body = { id, nombre, contacto };
        } else if (modal === "Usuarios") {
            endpoint = "http://localhost:5000/api/usuarios/modificacion";
            body = { id, nombre_publico, nombre, contrasenia, permisos };
        } else if (modal === "Máquinas") {
            endpoint = "http://localhost:5000/api/maquinas/modificacion";
            body = { id, modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual };
        } else if (modal === "Mantenimientos") {
            endpoint = "http://localhost:5000/api/mantenimientos/modificacion";
            body = { id, id_maquina, ci_tecnico, tipo, fecha, observaciones };
        } else if (modal === "Registro_Consumo") {
            endpoint = "http://localhost:5000/api/registro_consumo/modificacion";
            body = { id, id_maquina, id_insumo, fecha, cantidad };
        }

        try {
            const response = await fetch(endpoint, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: "include",
                body: JSON.stringify(body),
            });

            const result = await response.json();

            if (response.ok) {
                alert(`Modificación de ${modal} realizada exitosamente!`);
                navigate("/Gestion", { state: { userName, Permiso, userPassword } });
            } else {
                alert(`Error: ${result.message || "Error al realizar la modificación"}`);
            }
        } catch (error) {
            console.error("Error en la solicitud:", error);
            alert("Hubo un problema al realizar la modificación.");
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
            setTelefono(elemento.telefono || "");
        } else {
            setId(elemento.id || elemento.ID);
            if (modal === "Insumos") {
                setNombre(elemento.nombre || "");
                setPrecio(elemento.precio || "");
                setIdProveedor(elemento.idProveedor || "");
            } else if (modal === "Clientes") {
                setNombre(elemento.nombre || "");
                setDireccion(elemento.direccion || "");
                setTelefono(elemento.telefono || "");
                setCorreo(elemento.correo || "");
            } else if (modal === "Proveedores") {
                setNombre(elemento.nombre || "");
                setContacto(elemento.contacto || "");
            } else if (modal === "Usuarios") {
                setNombrePublico(elemento.nombre_publico || "");
                setNombre(elemento.nombre || "");
                setPermisos(elemento.permisos || "");
            } else if (modal === "Máquinas") {
                setModelo(elemento.modelo || "");
                setIdCliente(elemento.idCliente || "");
                setUbicacionCliente(elemento.ubicacionCliente || "");
                setCostoAlquilerMensual(elemento.costo_alquiler || "");
            }
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
                <h2>Modificacion de {modal}</h2>
                <input
                    className={`Id${modal == "Técnicos" ? " invisible" : ""}`}
                    type="text"
                    placeholder="ID"
                    value={id}
                    onChange={e => setId(e.target.value)}
                />
                <input
                    className={`ci${modal !== "Técnicos" ? " invisible" : ""}`}
                    type="text"
                    placeholder="CI"
                    value={ci}
                    onChange={e => setCi(e.target.value)}
                />
                <input
                    className={`nombre${!['Insumos','Clientes','Proveedores','Usuarios'].includes(modal) ? " invisible" : ""}`}
                    type="text"
                    placeholder="Nombre"
                    value={nombre}
                    onChange={e => setNombre(e.target.value)}
                />
                <input
                    className={`precio${modal !== "Insumos" ? " invisible" : ""}`}
                    type="number"
                    placeholder="Precio"
                    value={precio}
                    onChange={e => setPrecio(e.target.value)}
                />
                <input
                    className={`idProveedor${modal !== "Insumos" ? " invisible" : ""}`}
                    type="number"
                    placeholder="ID Proveedor"
                    value={idProveedor}
                    onChange={e => setIdProveedor(e.target.value)}
                />
                <input
                    className={`direccion${modal !== "Clientes" ? " invisible" : ""}`}
                    type="text"
                    placeholder="Dirección"
                    value={direccion}
                    onChange={e => setDireccion(e.target.value)}
                />
                <input
                    className={`telefono${!['Clientes','Técnicos'].includes(modal) ? " invisible" : ""}`}
                    type="text"
                    placeholder="Teléfono"
                    value={telefono}
                    onChange={e => setTelefono(e.target.value)}
                />
                <input
                    className={`correo${modal !== "Clientes" ? " invisible" : ""}`}
                    type="email"
                    placeholder="Correo"
                    value={correo}
                    onChange={e => setCorreo(e.target.value)}
                />
                <input
                    className={`contacto${modal !== "Proveedores" ? " invisible" : ""}`}
                    type="text"
                    placeholder="Contacto"
                    value={contacto}
                    onChange={e => setContacto(e.target.value)}
                />
                <input
                    className={`modelo${modal !== "Máquinas" ? " invisible" : ""}`}
                    type="text"
                    placeholder="Modelo"
                    value={modelo}
                    onChange={e => setModelo(e.target.value)}
                />
                <input
                    className={`id_cliente${modal !== "Máquinas" ? " invisible" : ""}`}
                    type="number"
                    placeholder="ID Cliente"
                    value={id_cliente}
                    onChange={e => setIdCliente(e.target.value)}
                />
                <input
                    className={`ubicacion_cliente${modal !== "Máquinas" ? " invisible" : ""}`}
                    type="text"
                    placeholder="Ubicación Cliente"
                    value={ubicacion_cliente}
                    onChange={e => setUbicacionCliente(e.target.value)}
                />
                <input
                    className={`costo_alquiler_mensual${modal !== "Máquinas" ? " invisible" : ""}`}
                    type="number"
                    placeholder="Costo Alquiler Mensual"
                    value={costo_alquiler_mensual}
                    onChange={e => setCostoAlquilerMensual(e.target.value)}
                />
                <input
                    className={`id_maquina${!['Mantenimientos','Registro_Consumo'].includes(modal) ? " invisible" : ""}`}
                    type="number"
                    placeholder="ID Máquina"
                    value={id_maquina}
                    onChange={e => setIdMaquina(e.target.value)}
                />
                <input
                    className={`ci_tecnico${modal !== "Mantenimientos" ? " invisible" : ""}`}
                    type="text"
                    placeholder="CI Técnico"
                    value={ci_tecnico}
                    onChange={e => setCiTecnico(e.target.value)}
                />
                <input
                    className={`tipo${modal !== "Mantenimientos" ? " invisible" : ""}`}
                    type="text"
                    placeholder="Tipo"
                    value={tipo}
                    onChange={e => setTipo(e.target.value)}
                />
                <input
                    className={`fecha${!['Mantenimientos','Registro_Consumo'].includes(modal) ? " invisible" : ""}`}
                    type="date"
                    placeholder="Fecha"
                    value={fecha}
                    onChange={e => setFecha(e.target.value)}
                />
                <input
                    className={`observaciones${modal !== "Mantenimientos" ? " invisible" : ""}`}
                    type="text"
                    placeholder="Observaciones"
                    value={observaciones}
                    onChange={e => setObservaciones(e.target.value)}
                />
                <input
                    className={`nombre_publico${modal !== "Usuarios" ? " invisible" : ""}`}
                    type="text"
                    placeholder="Nombre Público"
                    value={nombre_publico}
                    onChange={e => setNombrePublico(e.target.value)}
                />
                <input
                    className={`contrasenia${modal !== "Usuarios" ? " invisible" : ""}`}
                    type="password"
                    placeholder="Contraseña"
                    value={contrasenia}
                    onChange={e => setContrasenia(e.target.value)}
                />
                <input
                    className={`id_insumo${modal !== "Registro_Consumo" ? " invisible" : ""}`}
                    type="number"
                    placeholder="ID Insumo"
                    value={id_insumo}
                    onChange={e => setIdInsumo(e.target.value)}
                />
                <input
                    className={`cantidad${modal !== "Registro_Consumo" ? " invisible" : ""}`}
                    type="number"
                    placeholder="Cantidad"
                    value={cantidad}
                    onChange={e => setCantidad(e.target.value)}
                />
                <input
                    className={`permisos${modal !== "Usuarios" ? " invisible" : ""}`}
                    type="text"
                    placeholder="Permisos (admin = 1 o user = 0)"
                    value={permisos}
                    onChange={e => setPermisos(e.target.value)}
                />
                <br />
                <button type="button" onClick={obtenerLista}>
                    Ver Lista de {modal}
                </button>
                <button type="button" onClick={Confirmar}>
                    Confirmar Modificacion
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
                                                            backgroundColor: '#007bff',
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
                                <button 
                                    className="cerrar"
                                    onClick={cerrarModal}
                                >
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

export default Modificacion;
