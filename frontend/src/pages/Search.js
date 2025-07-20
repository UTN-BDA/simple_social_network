import Sidebar from "../components/Sidebar";
import Buscar from "../components/Buscar";
import './css/Search.css';

function Search() {

  return (
    <div className="search-container">
      <Sidebar />
      <div className="main-content">
      <h1>Busqueda de usuario</h1>
      <Buscar />
    </div>
    </div>
    
  );
}

export default Search;