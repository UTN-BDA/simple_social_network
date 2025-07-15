import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useUser } from "../context/UserContext"; 
import axios from 'axios';

function Login() {

  var [contraseña, setContraseña] = useState("");
  var [correo, setCorreo] = useState("");
  const [error, setError] = useState(null);
  const [mostrar, setMostrar] = useState(false);

  const navigate = useNavigate();

  const { setUsuario } = useUser(); 

/* ----------  ENVÍO AL BACKEND  ---------- */
  const enviarDatos = async () => {
     
    const formData = new FormData();

    formData.append("correo", correo); 
    formData.append("contraseña", contraseña); 

    try {
      const res = await axios.post("http://127.0.0.1:5000/login/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      if (res.status === 200 || res.data.message) {
        setUsuario(res.data.data);
        navigate("/home");   
    } 
    } catch (err) {
      console.error("Error al subir información:", err);
    }
  };


  const toggleMostrarContraseña = () => {
    setMostrar(prev => !prev);
  };

  return (
    <>
      {error && <p style={{ color: 'red' }}>{error}</p>}


      <h1>Inicio de sesión</h1>

      <label>¿No tienes cuenta? </label>
      <button onClick={()=>navigate("/register")}>Registrate</button>

      <br />

      <label>Correo electrónico: </label>
      <input
        type="email"
        required={true}
        placeholder="sunombre@gmail.com"
        onChange={(e) => setCorreo(e.target.value)}
        value={correo}
      />

      <br />

      <label>Contraseña: </label>
      <input
        required={true}
        type={mostrar ? 'text' : 'password'}
        onChange={(e) => setContraseña(e.target.value)}
        value={contraseña}
        id='miContraseña'
      /> 
      <label> Mostrar contraseña </label>
      <input
        type='checkbox'
        checked={mostrar}
        onChange={toggleMostrarContraseña}
      /> 

      <br />

      <button onClick={enviarDatos}>Ingresar</button>

    </>
  );
}

export default Login;