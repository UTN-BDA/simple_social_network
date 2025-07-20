import { NavLink } from "react-router-dom";

export default function Sidebar() {
  function cerrar_sesion (){
    localStorage.removeItem("usuario")
  }

  return (
    <aside className="sidebar">
      <nav>
        <ul>  
          <li>
            <NavLink to="/home">Inicio</NavLink>
          </li>
          <li>
            <NavLink to="/search">Buscar</NavLink>
          </li>
          <li>
            <NavLink to="/profile">Perfil</NavLink>
          </li>
          <li>
            <NavLink to="/" end onClick={cerrar_sesion}>
              Cerrar sesión
            </NavLink>
          </li>
        </ul>
      </nav>
    </aside>
  );
}
