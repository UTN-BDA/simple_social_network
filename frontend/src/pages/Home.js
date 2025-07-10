import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  return (
    <div>
      <h1>Pantalla Principal</h1>
      <button onClick={() => navigate('/profile')}>Ir al perfil</button>
    </div>
  );
}

export default Home;
