import Sidebar from "../components/Sidebar";
import Publicaciones from "../components/Publicaciones";
import "./css/Profile.css";

function Profile() {

  const usuario = JSON.parse(localStorage.getItem("usuario"))

  return (
    <div className="profile-layout">
      <Sidebar />
      <main className="profile-container">
        <h1 className="profile-title">Perfil de {usuario.nombre}</h1>
        <div className="profile-info">
          <img
            src={usuario.imagen}
            alt="Foto de perfil"
            className="profile-image"
          />
        <div className="profile-details">
            <p><strong>Correo:</strong> {usuario.correo}</p>
        </div>
        </div>
        <div className="profile-posts">
          <Publicaciones titulo="Tus publicaciones" usuario_id={usuario.id} />
        </div>
      </main>
    </div>
  );
}

export default Profile;