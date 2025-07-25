import { useState } from "react";
import axios from "axios";
import Publicacion from "../components/Publicacion";
import "../pages/css/Publicaciones.css";

function Publicaciones(props) {
    const [publicaciones, setPublicaciones] = useState([]);
  
    function recargar(){
        axios.get("http://127.0.0.1:5000/usuario/publicaciones/" + props.usuario_id)
        .then(res => {
            setPublicaciones(res.data.data);
        })
        .catch(err => {
            console.error(err); 
        });
    }

  return (
    <div className="publicaciones-container">
      <div className="publicaciones-header">
          <h2>{props.titulo}</h2>
          <button onClick={recargar} className="recargar-btn">Recargar</button>
      </div>

          {publicaciones.length > 0 ? (
            publicaciones.map((pub) => (
              <Publicacion key={pub._id} publicacion={pub} />
            ))
          ) : (
            <p>No hay publicaciones.</p>
          )}
    </div>
  );
}

export default Publicaciones;
