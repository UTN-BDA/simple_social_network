import { useState } from "react";
import axios from "axios";

function Publicar() {
  const [texto, setTexto] = useState("");
  const [imagenes, setImagenes] = useState([]);
  const [error, setError] = useState("");
  const [subiendo, setSubiendo] = useState(false);

  const usuario = JSON.parse(localStorage.getItem("usuario"))

  const handleImagenesChange = (e) => {
    const files = Array.from(e.target.files);
    if (files.length > 4) {
      setError("Puedes subir un máximo de 4 imágenes.");
      return;
    }
    setImagenes(files);
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!texto && imagenes.length === 0) {
      setError("Debes ingresar texto o al menos una imagen.");
      return;
    }

    const formData = new FormData();
    formData.append("id_usuario", usuario.id)
    formData.append("texto", texto);
    imagenes.forEach((img) => formData.append("imagenes", img));

    try {
      setSubiendo(true);
      const res = await axios.post("http://127.0.0.1:5000/publicaciones/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      console.log("Publicación exitosa:", res.data);
      // Limpiar el formulario
      setTexto("");
      setImagenes([]);
      setError("");
    } catch (err) {
      console.error("Error al publicar:", err);
      setError("Hubo un error al subir la publicación.");
    } finally {
      setSubiendo(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="publicar-form">
      <h3>Crear publicación</h3>
      <textarea
        value={texto}
        onChange={(e) => setTexto(e.target.value)}
        placeholder="¿Qué estás pensando?"
        rows="4"
      />
      <input
        type="file"
        multiple
        accept="image/*"
        onChange={handleImagenesChange}
        disabled={imagenes.length >= 4}
      />
        {imagenes.length > 0 && (
          <div style={{ marginTop: "10px" }}>
            <strong>{imagenes.length} imagen{imagenes.length > 1 ? "es" : ""} seleccionada{imagenes.length > 1 ? "s" : ""}</strong>
          </div>
        )}
      {error && <p className="error">{error}</p>}
      <button type="submit" disabled={subiendo}>
        {subiendo ? "Publicando..." : "Publicar"}
      </button>
    </form>
  );
}

export default Publicar;
