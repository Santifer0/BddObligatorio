import React from 'react';
<<<<<<< HEAD
import { Routes, Route, useNavigate } from 'react-router-dom';
import Login from './pages/login';
import Home from './pages/home';       
=======
import { Routes, Route } from 'react-router-dom';
import Login from '../pages/login';
import Home from '../pages/home'; 
import Gestion from '../pages/gestion';
import Registro from '../pages/registro';      
import Alta from '../pages/Alta';
import Modificacion from '../pages/modificacion';
import Baja from '../pages/baja';
import RegistroConsumo from '../pages/registro_insumos';
>>>>>>> 27b333fd7684ad9edb2c1c713af5bcf51a3ed8dd


function App() {  
  return (
    <div>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="*" element={<Login/>} />
        <Route path="/Home" element={<Home/>} />
<<<<<<< HEAD
=======
        <Route path="/Gestion" element={<Gestion/>} />
        <Route path="/Registro" element={<Registro/>} />
        <Route path="/Alta" element={<Alta/>} />
        <Route path="/Modificacion" element={<Modificacion/>} />
        <Route path="/Baja" element={<Baja/>} />
        <Route path="/RegistroConsumo" element={<RegistroConsumo/>} />
>>>>>>> 27b333fd7684ad9edb2c1c713af5bcf51a3ed8dd
      </Routes>
    </div>
  );
}

export default App;