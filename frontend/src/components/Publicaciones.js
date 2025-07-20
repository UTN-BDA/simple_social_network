import { useState } from "react";
import axios from "axios";
import Publicacion from "../components/Publicacion";

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
    <div>
        <h4>{props.titulo}</h4>
        <button onClick={recargar}>Recargar</button>
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
