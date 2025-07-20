import Sidebar from "../components/Sidebar";
import Publicaciones from "../components/Publicaciones";

function Profile() {

  const usuario = JSON.parse(localStorage.getItem("usuario"))

  return (
    <div>
      <Sidebar />
      <h1>Perfil de {usuario.nombre}</h1>
      <img src={usuario.imagen} alt="Foto de perfil" style={{ width: 200 }} />
      <p>Correo: {usuario.correo}</p>
      <Publicaciones titulo={"Tus publicaciones"} usuario_id={usuario.id}/>
    </div>
  );
}

export default Profile;