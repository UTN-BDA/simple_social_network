import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function Login() {

  var [contraseña, setContraseña] = useState("");
  var [correo, setCorreo] = useState("");
  const [error, setError] = useState(null);
  const [mostrar, setMostrar] = useState(false);

  const navigate = useNavigate();

/* ----------  ENVÍO AL BACKEND  ---------- */
  const enviarDatos = async () => {
     
    const formData = new FormData();

    // Contenido que se enviará
    formData.append("correo", correo); 
    formData.append("contraseña", contraseña); 

    try {
      const res = await axios.post("http://127.0.0.1:5000/login/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      if (res.status === 200 || res.data.message) {
        const userData = res.data.data;

        // Convertir la imagen de URL a base64
        const imageUrl = userData.imagen;
        const imageResponse = await fetch(imageUrl);
        const blob = await imageResponse.blob();

        const base64Image = await new Promise((resolve, reject) => {
          const reader = new FileReader();
          reader.onloadend = () => resolve(reader.result); // base64 result
          reader.onerror = reject;
          reader.readAsDataURL(blob); // convierte a base64
        });

        // Reemplazar la URL con la imagen en base64
        userData.imagen = base64Image;

        // Guardar en localstorage
        localStorage.setItem("usuario", JSON.stringify(userData));

        // Redirigir
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