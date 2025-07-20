import { useState } from "react";
import axios from "axios";
import Publicacion from "../components/Publicacion";

function UltimasPublicaciones() {
    const [publicaciones, setPublicaciones] = useState([]);
    const usuario = JSON.parse(localStorage.getItem("usuario"))
  
    function recargar(){
        axios.get("http://127.0.0.1:5000/publicaciones/" + usuario.id)
        .then(res => {
            console.log(res.data)
            setPublicaciones(res.data.data);
        })
        .catch(err => {
            console.error(err); 
        });
    }

  return (
    <div className="ultimas-publicaciones">
        <h4>Últimas publicaciones</h4>
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

export default UltimasPublicaciones;
