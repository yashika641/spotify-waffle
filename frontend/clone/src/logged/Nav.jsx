import React from "react";
import { FaArrowCircleLeft, FaArrowCircleRight } from "react-icons/fa";
import { useNavigate } from "react-router-dom";

const Nav = () => {
  const Navigate = useNavigate();
  return (
    <div className="w-265 -ml-2 h-27 text-white mt-4 rounded-md">
      <div className="flex items-center justify-between p-4">
        <div className="flex items-center space-x-4">
          <FaArrowCircleLeft size={28} onClick={()=>Navigate(-1)} className="cursor-pointer"/>
          <FaArrowCircleRight size={28} onClick={()=>Navigate(1)} className="cursor-pointer" />
        </div>
        <div>
          <button className="bg-white text-black px-4 py-2 cursor-pointer rounded-full text-sm font-bold">Explore Premium</button>
          <button className="bg-black text-white px-4 py-2 cursor-pointer rounded-full text-sm font-bold ml-2">Install App</button>
          <button className="w-7 h-7 rounded-full bg-purple-600 items-center justify-center text-black text-md font-bold ml-2 cursor-pointer">P</button>
        </div>
      </div>
      <div className="flex px-4 gap-2 mt-2">
        <button className="bg-white px-4 py-1 text-black rounded-full cursor-pointer">All</button>
        <button className="bg-black px-4 py-1 rounded-full cursor-pointer hover:bg-white hover:text-black">Music</button>
        <button className="bg-black px-4 py-1 rounded-full cursor-pointer hover:bg-white hover:text-black">Podcasts</button>
      </div>
    </div>
  );
};

export default Nav;
