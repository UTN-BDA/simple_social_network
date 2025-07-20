import { useState } from "react";
import axios from "axios";
import BotonSeguir from "../components/BotonSeguir";
import Publicaciones from "../components/Publicaciones";

function Buscar() {
  const [correo, setCorreo] = useState("");
  const [usuario, setUsuario] = useState(null);

  const handleSubmit = (e) => {
    axios.get('http://127.0.0.1:5000/usuario/buscar', {
        params: { correo: correo }
    })
    .then(response => {
        setUsuario(response.data.data);
    })
    .catch(error => {
        console.error(error);
    });
    };


  return (
    <div>
      <h3>Buscar usuario</h3>
      <input
        type="email"
        required={true}
        placeholder="sunombre@gmail.com"
        onChange={(e) => setCorreo(e.target.value)}
        value={correo}
      />

      <button onClick={handleSubmit}>Buscar usuario</button>

      {usuario && (
        <div style={{ marginTop: "1rem", padding: "1rem", border: "1px solid #ccc" }}>
          <h4>Datos del usuario:</h4>
          <p><strong>ID:</strong> {usuario.id}</p>
          <p><strong>Nombre:</strong> {usuario.nombre}</p>
          <p><strong>Apellido:</strong> {usuario.apellido}</p>
          <p><strong>Correo:</strong> {usuario.correo}</p>
          <img src={usuario.imagen} alt="Foto de perfil" style={{ width: 200 }} />
          
          <BotonSeguir id_usuario={usuario.id}/>
          <Publicaciones titulo={"Publicaciones de " + usuario.nombre} usuario_id={usuario.id}/>
        </div>

      )}

    </div>
  );
}

export default Buscar;
