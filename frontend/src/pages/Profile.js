import { useUser } from "../context/UserContext";

function Profile() {
  const { usuario } = useUser();

  return (
    <div>
      <h1>Perfil de {usuario.nombre}</h1>
      <img src={usuario.imagen} alt="Foto de perfil" style={{ width: 200 }} />
      <p>Correo: {usuario.correo}</p>
    </div>
  );
}

export default Profile;