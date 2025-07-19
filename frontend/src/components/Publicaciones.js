import { useEffect, useState } from "react";
import axios from "axios";
import Publicacion from "../components/Publicacion";

function Publicaciones(props) {
    const [publicaciones, setPublicaciones] = useState([]);
    const usuario = JSON.parse(localStorage.getItem("usuario"))
  
    function recargar(){
        axios.get("http://127.0.0.1:5000/usuario/publicaciones/" + usuario.id)
        .then(res => {
            console.log(res.data.data)
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
        {publicaciones.map((pub) => (
  <Publicacion key={pub._id} publicacion={pub} />
))}
    </div>
  );
}

export default Publicaciones;
