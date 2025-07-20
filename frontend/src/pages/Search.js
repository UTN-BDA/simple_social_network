import Sidebar from "../components/Sidebar";
import Buscar from "../components/Buscar";

function Search() {

  return (
    <div>
      <Sidebar />
      <h1>Busqueda de usuario</h1>
      <Buscar />
    </div>
  );
}

export default Search;