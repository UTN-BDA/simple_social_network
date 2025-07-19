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
            <NavLink to="/home">Home</NavLink>
          </li>
          <li>
            <NavLink to="/profile">Profile</NavLink>
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
