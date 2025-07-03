import React from 'react';
<<<<<<< HEAD
=======
<<<<<<< HEAD
import { Routes, Route, useNavigate } from 'react-router-dom';
import Login from './pages/login';
import Home from './pages/home';       
=======
>>>>>>> 31646ca485c4072fea4890830ebd812730f4b549
import { Routes, Route } from 'react-router-dom';
import Login from '../pages/login';
import Home from '../pages/home'; 
import Gestion from '../pages/gestion';
import Registro from '../pages/registro';      
import Alta from '../pages/Alta';
import Modificacion from '../pages/modificacion';
import Baja from '../pages/baja';
import RegistroConsumo from '../pages/registro_insumos';
<<<<<<< HEAD
=======
>>>>>>> 27b333fd7684ad9edb2c1c713af5bcf51a3ed8dd
>>>>>>> 31646ca485c4072fea4890830ebd812730f4b549


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
<<<<<<< HEAD
=======
>>>>>>> 27b333fd7684ad9edb2c1c713af5bcf51a3ed8dd
>>>>>>> 31646ca485c4072fea4890830ebd812730f4b549
      </Routes>
    </div>
  );
}

export default App;