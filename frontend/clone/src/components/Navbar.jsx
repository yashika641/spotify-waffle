import React from "react";
import { FaSpotify, FaSearch } from "react-icons/fa";
import { GoHomeFill } from "react-icons/go";
import { IoBrowsersOutline } from "react-icons/io5";
import { IoDownloadOutline } from "react-icons/io5";
import { useNavigate } from 'react-router-dom'


const Navbar = () => {

const navigate = useNavigate();


  return (
    <div className="flex justify-between items-center bg-black text-white fixed -top-1 left-0 right-0 z-50 px-4 py-1 h-20">
      <div className="flex items-center">
        <div className="gap-7 flex items-center">
          <FaSpotify className="text-4xl cursor-pointer" />
          <GoHomeFill className="cursor-pointer text-white bg-[#1F1F1F] hover:bg-[#2d2d2d] rounded-full p-3 h-13 w-13" />
        </div>
        <div className=" rounded-full flex justify-between items-center gap-2 p-2 px-5 h-12 w-120">
          <div className="flex items-center bg-[#1F1F1F] hover:bg-[#2d2d2d] rounded-full px-5 gap-3">
            <FaSearch className="text-2xl font-light " />
            <input
              className=" bg-transparent border-0 outline-0 w-90 p-3 "
              type="text"
              placeholder="What do you want to play?"
            ></input>
            <IoBrowsersOutline className="text-2xl" />
          </div>
        </div>
      </div>
      <div className="flex items-center gap-10">
        <div className="flex items-center gap-4">
          <a
            href="https://www.spotify.com/in-en/premium/"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] font-bold cursor-pointer"
          >
            Premium
          </a>
          <a
            href="https://support.spotify.com/in-en/"
            target="_blank"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] font-bold cursor-pointer"
          >
            Support
          </a>
          <a
            href="https://www.spotify.com/in-en/download/windows/"
            target="_blank"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] font-bold cursor-pointer"
          >
            Download
          </a>
        </div>
        <div className="font-light text-4xl">I</div>
        <div className="flex items-cnter gap-10 ">
          <a
            href="https://download.scdn.co/SpotifySetup.exe"
            download={"https://download.scdn.co/SpotifySetup.exe"}
          >
            <div className="flex items-center gap-2 ">
              <IoDownloadOutline />
              <p className="text-[#fffcfca4] hover:text-[#fffcfcf0] font-bold cursor-pointer ">
                Install App
              </p>
            </div>
          </a>
        <button onClick={() => navigate('/signup')} className="text-[#fffcfca4] hover:text-[#fffcfcf0] font-bold cursor-pointer">
            Sign Up
          </button>
        
        </div>
       <button onClick={() => navigate('/login')} className="bg-white text-black px-7 py-3 rounded-full font-bold cursor-pointer hover:bg-[#fffcfcf0]">
          Log In
        </button>
        
      </div>
    </div>
  );
};

export default Navbar;
