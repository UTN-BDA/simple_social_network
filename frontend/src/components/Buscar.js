import { useState } from "react";
import axios from "axios";
import BotonSeguir from "../components/BotonSeguir";
import Publicaciones from "../components/Publicaciones";
import '../pages/css/Search.css'; 


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
    <div className="buscar-box">
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
          <div className="usuario-encontrado">
            <div className="usuario-perfil">
              <img className="usuario-imagen" src={usuario.imagen} alt="Foto de perfil" />
              
              <div className="usuario-detalles">
                <h2>{usuario.nombre} {usuario.apellido}</h2>
                <p className="usuario-correo">{usuario.correo}</p>
                <BotonSeguir id_usuario={usuario.id} />
              </div>
            </div>

            <div className="usuario-publicaciones">
              <Publicaciones
                titulo={`Publicaciones de ${usuario.nombre}`}
                usuario_id={usuario.id}
              />
            </div>
          </div>
          
        )}

    </div>
  );
}

export default Buscar;
