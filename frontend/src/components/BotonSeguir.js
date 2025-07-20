import axios from "axios";
import '../pages/css/Search.css'; 

function BotonSeguir(params) {
    const handleSeguir = async () => {
     
        const formData = new FormData();

        // Contenido que se enviará
        formData.append("id_seguidor", JSON.parse(localStorage.getItem("usuario")).id); 
        formData.append("id_seguido", params.id_usuario); 

        try {
        const res = await axios.post("http://127.0.0.1:5000/usuario/seguir", formData, {
            headers: { "Content-Type": "multipart/form-data" },
        });

        if (res.status === 200 || res.data.message) {
           console.log(res.data)
        }
        } catch (err) {
        console.error("Error al subir información:", err);
        }
    };
        

  return (
    <button onClick={handleSeguir} className="boton-seguir">Seguir</button>
  );
};

export default BotonSeguir;
