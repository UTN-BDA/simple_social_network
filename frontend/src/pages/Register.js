// import { useState } from 'react';
// import { useNavigate } from 'react-router-dom';

// function Register() {

//   const [nombre, setNombre] = useState("");
//   const [apellido, setApellido] = useState("");
//   const [nacimiento, setNacimiento] = useState("");
//   const [correo, setCorreo] = useState("");
//   const [contraseña, setContraseña] = useState("");

//   const [mostrar, setMostrar] = useState(false);
//   const [error, setError] = useState(null);

//   const navigate = useNavigate()

//   const toggleMostrarContraseña = () => {
//     setMostrar(prev => !prev);
//   };

//   const enviarDatos = () => {
//     fetch('http://127.0.0.1:5000/login/',{
//       method: 'POST',
//       headers: {
//       'Content-Type': 'application/json' 
//       },
//       body: JSON.stringify(
//         { correo: correo,
//           contraseña: contraseña}
//     ) 
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.data) {
//           navigate('/home');
//         } else {
//           // Muestra el error recibido del backend
//           setError(data.message || "Error desconocido")
//         }
//       })
//   }

//   return (
//     <div>
//       {error && <p style={{ color: 'red' }}>{error}</p>}
//       <h1>Estas en el register</h1>

//       <label>Nombre</label>
//       <input 
//         type="text" 
//         required="true" 
//         onChange={(e) => setNombre(e.target.value)}
//         value={nombre}>
//       </input>

//       <br />

//       <label>Apellido</label>
//       <input 
//         type="text" 
//         required="true"
//         onChange={(e) => setApellido(e.target.value)}
//         value={apellido}
//         ></input>

//       <br />

//       <label>Fecha de nacimiento</label>
//       <input 
//         type="date" 
//         required="true"
//         onChange={(e) => setNacimiento(e.target.value)}
//         value={nacimiento}
//       ></input>

//       <br />

//       <label>Correo</label>
//       <input 
//       type="email" 
//       required="true"
//       onChange={(e) => setCorreo(e.target.value)}
//       value={correo}
//       ></input>

//       <br />

//       <label>contraseña</label>
//       <input 
//       type={mostrar ? 'text' : 'password'}
//       required="true"
//       onChange={(e) => setContraseña(e.target.value)}
//       value={contraseña}
//       ></input>
//       <label> Mostrar contraseña </label>
//       <input
//         type='checkbox'
//         checked={mostrar}
//         onChange={toggleMostrarContraseña}
//       /> 

//       <br />

//       <button onClick={enviarDatos}>Crear Usuario</button>

//     </div>
//   );
// }

// export default Register;

import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Register() {
  const [nombre, setNombre] = useState("");
  const [apellido, setApellido] = useState("");
  const [nacimiento, setNacimiento] = useState("");
  const [correo, setCorreo] = useState("");
  const [contraseña, setContraseña] = useState("");

  const [mostrar, setMostrar] = useState(false);
  const [serverError, setServerError] = useState(null);
  const [errors, setErrors] = useState({});     // <-- errores de validación

  const navigate = useNavigate();

  const toggleMostrarContraseña = () => setMostrar((p) => !p);

  /* ----------  VALIDACIONES  ---------- */
  const validate = () => {
    const err = {};

    // Nombre y Apellido
    if (!nombre.trim()) err.nombre = "El nombre es obligatorio";
    else if (nombre.length < 2 || nombre.length > 30)
      err.nombre = "El nombre debe tener entre 2 y 30 caracteres";

    if (!apellido.trim()) err.apellido = "El apellido es obligatorio";
    else if (apellido.length < 2 || apellido.length > 30)
      err.apellido = "El apellido debe tener entre 2 y 30 caracteres";

    // Correo
    const mailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!correo) err.correo = "El correo es obligatorio";
    else if (!mailRegex.test(correo)) err.correo = "Correo electrónico inválido";

    // Fecha de nacimiento (ej. no permitir fechas futuras)
    if (!nacimiento) err.nacimiento = "La fecha de nacimiento es obligatoria";
    else if (new Date(nacimiento) > new Date())
      err.nacimiento = "La fecha no puede ser futura";

    // Contraseña
    if (!contraseña) err.contraseña = "La contraseña es obligatoria";
    else if (contraseña.length < 8)
      err.contraseña = "Mínimo 8 caracteres";
    // Extra: mayúscula, minúscula y número
    else if (!/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/.test(contraseña))
      err.contraseña = "Debe contener mayúscula, minúscula y número";

    return err;
  };

  /* ----------  ENVÍO AL BACKEND  ---------- */
  const enviarDatos = () => {
    fetch("http://127.0.0.1:5000/register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        nombre,
        apellido,
        nacimiento,
        correo,
        contraseña,
      }),
    })
      .then((r) => r.json())
      .then((data) => {
        if (data.message) {
          navigate("/home");
        } else {
          setServerError(data.message || "Error desconocido");
        }
      })
      .catch(() => setServerError("No se pudo conectar con el servidor"));
  };

  /* ----------  SUBMIT  ---------- */
  const handleSubmit = (e) => {
    e.preventDefault();
    const err = validate();
    setErrors(err);
    if (Object.keys(err).length === 0) {
      enviarDatos(); // solo si todo está OK
    }
  };

  return (
    <div>
      <h1>Registro</h1>

      {serverError && <p style={{ color: "red" }}>{serverError}</p>}

      <form onSubmit={handleSubmit} noValidate>
        {/* NOMBRE */}
        <label>
          Nombre
          <input
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            required
            minLength={2}
            maxLength={30}
            className={errors.nombre && "error"}
          />
        </label>
        {errors.nombre && <small className="errorMsg">{errors.nombre}</small>}

        <br />

        {/* APELLIDO */}
        <label>
          Apellido
          <input
            type="text"
            value={apellido}
            onChange={(e) => setApellido(e.target.value)}
            required
            minLength={2}
            maxLength={30}
            className={errors.apellido && "error"}
          />
        </label>
        {errors.apellido && (
          <small className="errorMsg">{errors.apellido}</small>
        )}
        
        <br />

        {/* NACIMIENTO */}
        <label>
          Fecha de nacimiento
          <input
            type="date"
            value={nacimiento}
            onChange={(e) => setNacimiento(e.target.value)}
            required
            className={errors.nacimiento && "error"}
          />
        </label>
        {errors.nacimiento && (
          <small className="errorMsg">{errors.nacimiento}</small>
        )}
        
        <br />

        {/* CORREO */}
        <label>
          Correo
          <input
            type="email"
            value={correo}
            onChange={(e) => setCorreo(e.target.value)}
            required
            className={errors.correo && "error"}
          />
        </label>
        {errors.correo && <small className="errorMsg">{errors.correo}</small>}
        
        <br />

        {/* CONTRASEÑA */}
        <label>
          Contraseña
          <input
            type={mostrar ? "text" : "password"}
            value={contraseña}
            onChange={(e) => setContraseña(e.target.value)}
            required
            className={errors.contraseña && "error"}
          />
        </label>
        {errors.contraseña && (
          <small className="errorMsg">{errors.contraseña}</small>
        )}

        <label style={{ marginLeft: "0.5rem" }}>
          <input
            type="checkbox"
            checked={mostrar}
            onChange={toggleMostrarContraseña}
          />{" "}
          Mostrar contraseña
        </label>
        
        <br />

        <button type="submit">Crear usuario</button>
      </form>
    </div>
  );
}

export default Register;
