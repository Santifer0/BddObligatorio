import React from 'react';
import { Routes, Route, useNavigate } from 'react-router-dom';
import Login from '../pages/login';
import Home from '../pages/home'; 
import Gestion from '../pages/gestion';
import Registro from '../pages/registro';      
import Alta from '../pages/Alta';
import Modificacion from '../pages/modificacion';
import Baja from '../pages/baja';


function App() {  

  return (
    <div>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="*" element={<Login/>} />
        <Route path="/Home" element={<Home/>} />
        <Route path="/Gestion" element={<Gestion/>} />
        <Route path="/Registro" element={<Registro/>} />
        <Route path="/Alta" element={<Alta/>} />
        <Route path="/Modificacion" element={<Modificacion/>} />
        <Route path="/Baja" element={<Baja/>} />
      </Routes>
    </div>
  );
}

export default App;