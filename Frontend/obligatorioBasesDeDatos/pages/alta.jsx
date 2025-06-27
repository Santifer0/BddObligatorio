import React, { useState } from "react";
import './css/gestion.css';
import fondoLogin from '../src/assets/fondo-login.jpg';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

const Alta = () => {
    const [modal, setModal] = useState(null);
    const navigate = useNavigate();
    const location = useLocation();
    const userName = location.state?.userName || "Usuario Anónimo";
    const Permiso = location.state?.Permiso || false;
    const accion = location.state?.modal || "Modal";

    return (
        
    );
};
