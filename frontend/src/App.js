import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from './pages/Login';
import Home from './pages/Home';
import Profile from './pages/Profile';
import Register from './pages/Register';
import Search from './pages/Search'

function App() {
  
  return (
     <BrowserRouter>
      <div className="app">
        
        <main className="content">
          <Routes>
           <Route path="/" element={<Login />} />
           <Route path="/register" element={<Register/>} />
           <Route path="/home" element={<Home />} />
           <Route path="/profile" element={<Profile />} />
           <Route path="/search" element={<Search />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
