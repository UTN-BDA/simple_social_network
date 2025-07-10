import { useState } from 'react';

function Login() {

  var [contraseña, setContraseña] = useState("");
  var [correo, setCorreo] = useState("");

  // const handleLogin = () => {
  //   fetch('http://localhost:5000/inicio')
  //   .then(respuesta => respuesta.json())
  //   .then(data => console.log(data.message))
  // };

  const enviarDatos = () => {
    fetch('http://localhost:5000/inicio',{
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
    .then(data => console.log(data))
  }

  return (
    <>
      <h1>Inicio de sesión</h1>

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
        type="password"
        onChange={(e) => setContraseña(e.target.value)}
        value={contraseña}
      />
      <br />

      <button onClick={enviarDatos}>Ingresar</button>

    </>
  );
}

export default Login;