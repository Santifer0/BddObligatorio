import React, { useState, useEffect } from "react";
import './css/registro_insumos.css';
import fondoLogin from '../src/assets/fondo-login.jpg';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

const RegistroConsumo = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const userName = location.state?.userName || "Usuario Anónimo";
    const Permiso = location.state?.Permiso || false;
    const userPassword = location.state?.userPassword || "";

    const [maquinas, setMaquinas] = useState([]);
    const [insumos, setInsumos] = useState([]);
    const [id_maquina, setIdMaquina] = useState("");
    const [id_insumo, setIdInsumo] = useState("");
    const [cantidad, setCantidad] = useState("");
    const [fecha, setFecha] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            try {
                const maquinasRes = await fetch("http://localhost:5000/api/maquinas", { credentials: "include" });
                const insumosRes = await fetch("http://localhost:5000/api/insumos", { credentials: "include" });
                const maquinasData = await maquinasRes.json();
                const insumosData = await insumosRes.json();
                setMaquinas(maquinasData.maquinas || maquinasData);
                setInsumos(insumosData.insumos || insumosData);
            } catch (err) {
                setError("Error al cargar datos");
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    const handleConfirmar = async () => {
        if (!id_maquina || !id_insumo || !cantidad || !fecha) {
            alert("Completa todos los campos");
            return;
        }
        setLoading(true);
        setError("");
        try {
            const res = await fetch("http://localhost:5000/api/registro/consumo", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                credentials: "include",
                body: JSON.stringify({ id_maquina, id_insumo, cantidad, fecha })
            });
            const result = await res.json();
            if (res.ok) {
                alert("Consumo registrado exitosamente");
                setIdMaquina("");
                setIdInsumo("");
                setCantidad("");
                setFecha("");
            } else {
                alert("Error al conectar con el servidor");
            }
        } catch (err) {
            setError("Error de conexión con el servidor");
        } finally {
            setLoading(false);
        }
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
                <h2>Registrar Consumo de Insumo</h2>
                {error && <div style={{ color: 'red' }}>{error}</div>}
                <h3>Máquina:</h3>
                <select value={id_maquina} onChange={e => setIdMaquina(e.target.value)}>
                    <option value="">Selecciona una máquina</option>
                    {maquinas.map(maquina => (
                        <option key={maquina.id} value={maquina.id}>{maquina.modelo} (ID: {maquina.id})</option>
                    ))}
                </select>
                <h3>Insumo:</h3>
                <select value={id_insumo} onChange={e => setIdInsumo(e.target.value)}>
                    <option value="">Selecciona un insumo</option>
                    {insumos.map(insumo => (
                        <option key={insumo.id} value={insumo.id}>{insumo.nombre}</option>
                    ))}
                </select>
                <h3>Cantidad:</h3>
                <input type="number" value={cantidad} onChange={e => setCantidad(e.target.value)} min="1" />
                <h3>Fecha:</h3>
                <input type="date" value={fecha} onChange={e => setFecha(e.target.value)} />
                <br />
                <button onClick={handleConfirmar}>
                    Confirmar Consumo
                </button>
                <button onClick={() => navigate("/Registro", { state: { userName, Permiso, userPassword } })}>
                    Volver a Registro
                </button>
            </div>
        </div>
    );
};

export default RegistroConsumo;
