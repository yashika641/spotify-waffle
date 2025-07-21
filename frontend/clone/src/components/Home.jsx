import React from "react";
import Navbar from "./Navbar.jsx";
import Sidebar from "./Sidebar.jsx";
import Main from "./Main.jsx";
import Footer from "./Footer.jsx";


const Home = () => {
  return (
    <div>
      <div className="bg-black text-white h-screen px-3 py-2 h-100vh">
        <Navbar />
        <div className="flex h-screen">
          <Sidebar />
          <Main />
        </div>
       <Footer />
      </div>
    </div>
  );
};

export default Home;
