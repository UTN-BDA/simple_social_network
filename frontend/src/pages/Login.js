import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {

  var [contraseña, setContraseña] = useState("");
  var [correo, setCorreo] = useState("");
  const [error, setError] = useState(null);
  const [mostrar, setMostrar] = useState(false);

  const navigate = useNavigate();

  // const handleLogin = () => {
  //   fetch('http://localhost:5000/inicio')
  //   .then(respuesta => respuesta.json())
  //   .then(data => console.log(data.message))
  // };

  const enviarDatos = () => {
    fetch('http://127.0.0.1:5000/login/',{
      method: 'POST',
      headers: {
      'Content-Type': 'application/json' 
      },
      body: JSON.stringify(
        { correo: correo,
          contraseña: contraseña}
    ) 
    })
    .then(response => response.json())
    .then(data => {
        if (data.data) {
          navigate('/home');
        } else {
          // Muestra el error recibido del backend
          setError(data.message || "Error desconocido")
        }
      })
  }

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