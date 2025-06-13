import React, { useContext } from "react";
import '../components/login.css';
import { Link } from "react-router-dom";
import { UserContext } from "../../context/UserContext"; // Importá el contexto

const Login = () => {
  const { userName, setUserName } = useContext(UserContext);

  return (
    <div className="login-wrapper">
      <div className="login-container">
        <h1>Login</h1>
        <input
          placeholder="Ingrese su usuario"
          value={userName}
          onChange={e => setUserName(e.target.value)}
        />
        <Link to="./home">
          <button className="login-button">Ingresar</button>
        </Link>
      </div>
    </div>
  );
};

export default Login;