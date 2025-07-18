import React, { useState } from "react";
import './css/alta.css';
import fondoLogin from '../src/assets/fondo-login.jpg';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

const Alta = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const userName = location.state?.userName || "Usuario Anónimo";
    const Permiso = location.state?.Permiso || false;
    const userPassword = location.state?.userPassword || "";
    const modal = location.state?.modal || "Item";

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

    const Confirmar = async () => {
        // Simplificar: no verificar sesión antes de cada request
        // La sesión ya fue establecida en el login
        let endpoint = "";
        let body = {};

        if (modal === "Insumos") {
            endpoint = "http://localhost:5000/api/insumos/alta";
            body = { nombre, precio, idProveedor };
        } else if (modal === "Clientes") {
            endpoint = "http://localhost:5000/api/clientes/alta";
            body = { nombre, direccion, telefono, correo };
        
        } else if (modal === "Proveedores") {
            endpoint = "http://localhost:5000/api/proveedores/alta";
            body = { nombre, contacto };
        } else if (modal === "Técnicos") {
            endpoint = "http://localhost:5000/api/tecnicos/alta";
            body = { ci, nombre, apellido, telefono };
        } else if (modal === "Usuarios") {
            endpoint = "http://localhost:5000/api/usuarios/alta";
            body = { nombre_publico, nombre, contrasenia, permisos: parseInt(permisos) };
        } else if (modal === "Máquinas") {
            endpoint = "http://localhost:5000/api/maquinas/alta";
            body = { modelo, idCliente: id_cliente, ubicacionCliente: ubicacion_cliente, costo_alquiler: costo_alquiler_mensual };
        } else if (modal === "Mantenimientos") {
            endpoint = "http://localhost:5000/api/mantenimientos/alta";
            body = { id_maquina, ci_tecnico, tipo, fecha, observaciones };
        } else if (modal === "Registro_Consumo") {
            endpoint = "http://localhost:5000/api/registro_consumo/alta";
            body = { id_maquina, id_insumo, fecha, cantidad };
        }

        try {
            const response = await fetch(endpoint, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: "include", // Usar la sesión establecida en login
                body: JSON.stringify(body),
            });

            const result = await response.json();

            if (response.ok) {
                alert(`Alta de ${modal} realizada exitosamente!`);
                setNombre("");
                setContacto("");
                setPrecio("");
                setIdProveedor("");
                setDireccion("");
                setTelefono("");
                setCorreo("");
                setModelo("");
                setIdCliente("");
                setUbicacionCliente("");
                setCostoAlquilerMensual("");
                setCi("");
                setApellido("");
                setIdMaquina("");
                setCiTecnico("");
                setTipo("");
                setFecha("");
                setObservaciones("");
                setNombrePublico("");
                setContrasenia("");
                setIdInsumo("");
                setCantidad("");
                setPermisos("");
                navigate("/Gestion", { state: { userName, Permiso, userPassword } });
            } else {
                alert(`Error: ${result.message}`);
            }
        } catch (error) {
            console.error("Error en la solicitud:", error);
            alert("Hubo un problema al realizar la alta.");
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
                <h2>Alta de {modal}</h2>
                <input
                    className={`ci${modal !== "Técnicos" ? " invisible" : ""}`}
                    type="text"
                    placeholder="CI"
                    value={ci}
                    onChange={e => setCi(e.target.value)}
                />
                <input
                    className={`nombre${!["Insumos","Clientes","Empresas","Locales","Proveedores","Técnicos","Usuarios"].includes(modal) ? " invisible" : ""}`}
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
                    className={`direccion${!["Clientes","Locales"].includes(modal) ? " invisible" : ""}`}
                    type="text"
                    placeholder="Dirección"
                    value={direccion}
                    onChange={e => setDireccion(e.target.value)}
                />
                <input
                    className={`telefono${!["Clientes","Empresas","Locales","Técnicos"].includes(modal) ? " invisible" : ""}`}
                    type="text"
                    placeholder="Teléfono"
                    value={telefono}
                    onChange={e => setTelefono(e.target.value)}
                />
                <input
                    className={`correo${!["Clientes","Empresas","Locales"].includes(modal) ? " invisible" : ""}`}
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
                    className={`apellido${modal !== "Técnicos" ? " invisible" : ""}`}
                    type="text"
                    placeholder="Apellido"
                    value={apellido}
                    onChange={e => setApellido(e.target.value)}
                />
                <input
                    className={`id_maquina${!["Mantenimientos","Registro_Consumo"].includes(modal) ? " invisible" : ""}`}
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
                    className={`fecha${!["Mantenimientos","Registro_Consumo"].includes(modal) ? " invisible" : ""}`}
                    type={modal === "Mantenimientos" ? "datetime-local" : "date"}
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
                <button type="button" onClick={Confirmar}>
                    Confirmar Alta
                </button>
                <button type="button" onClick={volverAGestion}>
                    Volver a Gestión
                </button>
            </div>
        </div>
    );
};

export default Alta;