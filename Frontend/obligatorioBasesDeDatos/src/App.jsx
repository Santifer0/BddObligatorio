import React from 'react';
import { Routes, Route, useNavigate } from 'react-router-dom';
import Login from '../pages/login';
import Home from '../pages/home'; 
import Gestion from '../pages/gestion';
import Registro from '../pages/registro';      


function App() {  

  return (
    <div>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="*" element={<Login/>} />
        <Route path="/Home" element={<Home/>} />
        <Route path="/Gestion" element={<Gestion/>} />
        <Route path="/Registro" element={<Registro/>} />
      </Routes>
    </div>
  );
}

export default App;