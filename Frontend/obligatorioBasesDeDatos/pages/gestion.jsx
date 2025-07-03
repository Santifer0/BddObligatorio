import React, { useState } from "react";
import './css/gestion.css';
import fondoLogin from '../src/assets/fondo-login.jpg';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

const Gestion = () => {
    const [modal, setModal] = useState(null);
    const navigate = useNavigate();
    const location = useLocation();
    const userName = location.state?.userName || "Usuario Anónimo";
    const Permiso = location.state?.Permiso || false;
    const userPassword = location.state?.userPassword || "";

    const handleOpenModal = (nombre) => setModal(nombre);
    const handleCloseModal = () => setModal(null);
    const handleModal = (accion) => {
        switch (accion) {
            case "Alta":
                console.log(`Acción: Alta para ${modal}`);
                break;
            case "Baja":
                console.log(`Acción: Baja para ${modal}`);
                break;
            case "Modificacion":
                console.log(`Acción: Modificación para ${modal}`);
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
                <h2>Gestión</h2>
                <div>
                    {Permiso &&
                        <button onClick={() => handleOpenModal("Proveedores")}>
                            Proveedores
                        </button>
                    }
                    {Permiso &&
                        <button onClick={() => handleOpenModal("Máquinas")}>
                            Máquinas
                        </button>
                    }
                    {Permiso &&
                        <button onClick={() => handleOpenModal("Técnicos")}>
                            Técnicos
                        </button>
                    }
                    {Permiso &&
                        <button onClick={() => handleOpenModal("Usuarios")}>
                            Usuarios
                        </button>
                    }
<<<<<<< HEAD
=======
                    <button onClick={() => handleOpenModal("Empresas")}>
                        Empresas
                    </button>
                    <button onClick={() => handleOpenModal("Locales")}>
                        Locales
                    </button>
>>>>>>> origin/main
                    <button onClick={() => handleOpenModal("Insumos")}>
                        Insumos
                    </button>
                    <button onClick={() => handleOpenModal("Clientes")}>
                        Clientes
                    </button>
                    <button onClick={() => handleOpenModal("Mantenimientos")}>
                        Mantenimientos
                    </button>
<<<<<<< HEAD
                    <button className="back" onClick={() => navigate("/Home", { state: { userName, Permiso, userPassword } })}>
                        back
                    </button>
=======
<<<<<<< HEAD
<<<<<<< HEAD
                    <button className="back" onClick={() => navigate("/Home", { state: { userName, Permiso, userPassword } })}>
                        back
                    </button>
=======
>>>>>>> origin/main
=======
                    <button className="back" onClick={() => navigate("/Home", { state: { userName, Permiso, userPassword } })}>
                        back
                    </button>
>>>>>>> 27b333fd7684ad9edb2c1c713af5bcf51a3ed8dd
>>>>>>> 31646ca485c4072fea4890830ebd812730f4b549
                </div>
            </div>
            {modal && (
                <div className="modal-content">
<<<<<<< HEAD
=======

>>>>>>> origin/main
                    <h3>{modal}</h3>
                    <button onClick={() => navigate("/Alta", { state: { userName, Permiso, userPassword, modal } })}>Alta</button>
                    <button onClick={() => navigate("/Modificacion", { state: { userName, Permiso, userPassword, modal } })}>Modificacion</button>
                    <button onClick={() => navigate("/Baja", { state: { userName, Permiso, userPassword, modal } })}>Baja</button>
                    <button className="cerrar" onClick={handleCloseModal}>Cerrar</button>
<<<<<<< HEAD
=======

>>>>>>> origin/main
                </div>
            )}
        </div>
    );
};

export default Gestion;