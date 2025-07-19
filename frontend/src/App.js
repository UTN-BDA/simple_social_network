import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from './pages/Login';
import Home from './pages/Home';
import Profile from './pages/Profile';
import Register from './pages/Register';

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
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
