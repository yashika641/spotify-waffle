import React from "react";
import Home from "./components/Home.jsx";
import Login from "./pages/Login.jsx";
import Signup from "./pages/Signup.jsx";
import Home2 from "./logged/Home2.jsx";
import {Routes, Route} from 'react-router-dom';

const App = () => {
  return (
    <div>
       <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/logged/home" element={ <Home2 />} />
    </Routes>
    </div>
  );
};

export default App;
