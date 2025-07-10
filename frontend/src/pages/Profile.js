import { useNavigate } from "react-router-dom";

function Profile() {

  const navigate = useNavigate()

  

  return (
    <div>
      <h1>Perfil del Usuario</h1>
      <button onClick={() => navigate('/')}>Inicio de sesion</button>
      <button onClick={() => navigate('/home')}>Menu principal</button>
    </div>
  );
}

export default Profile;
