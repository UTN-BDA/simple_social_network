import Publicar from "../components/Publicar"
import Sidebar from "../components/Sidebar";
import UltimasPublicaciones from "../components/UltimasPublicaciones";
import "./css/Home.css";

function Home() {
  return (
    <div className="home-container">
      <Sidebar />
      <main className="main-content">
        <h1>Pantalla Principal</h1>
        <Publicar />
        <UltimasPublicaciones />
      </main>    
    </div>
  );
}

export default Home;
