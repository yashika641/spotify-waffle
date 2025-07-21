import React from "react";
import { LuPlus } from "react-icons/lu";
import { CiGlobe } from "react-icons/ci";

const Sidebar = () => {
  return (
    <div className="bg-[#111010] w-[30%] h-screen p-4 mt-17 rounded-sm fixed top-0 left-0">
      <div className="flex items-center justify-between text-white font-bold mb-10 ml-4">
        Your Library{" "}
        <span className="text-xl p-3 rounded-full hover:bg-[#2d2d2d] cursor-pointer transition">
          <LuPlus />
        </span>
      </div>
      <div className=" bg-[#1F1F1F] p-3 mb-5 rounded-xl">
        <p className="font-bold mb-1 ml-4">Create your first playlist</p>
        <p className="font-bold mb-5 ml-4">It's easy, we'll help you</p>
        <button className="bg-white ml-4 text-black rounded-full font-bold py-1 px-4 cursor-pointer mb-2">
          Create playlist
        </button>
      </div>
      <div className=" bg-[#1F1F1F] p-3 mb-5 rounded-xl">
        <p className="font-bold mb-1 ml-4">
          Let's find Some podcasts to follow
        </p>
        <p className="font-semibold mb-5 ml-4">
          We'll keep you updated on new episodes
        </p>
        <a href="https://open.spotify.com/genre/podcasts-web">
        <button className="bg-white ml-4 text-black rounded-full font-bold py-1 px-4 cursor-pointer mb-2">
          Browse podcasts
        </button>
        </a>
      </div>
      <div className="flex flex-wrap gap-2 mt-10 mr-5 w-90">
      <a href="https://www.spotify.com/in-en/legal/end-user-agreement/" className="text-[#B3B3B3] text-xs mb-3 ml-4 cursor-pointer">
        Legal</a>
        <a href="https://www.spotify.com/in-en/safetyandprivacy" className="text-[#B3B3B3] text-xs mb-3 ml-4 cursor-pointer">
        Safety&Privacy</a>
        <a href="https://www.spotify.com/in-en/legal/privacy-policy/" className="text-[#B3B3B3] text-xs mb-3 ml-4 cursor-pointer ">
        PrivacyPOlicy</a>
        <a href="https://www.spotify.com/in-en/legal/cookies-policy/" className="text-[#B3B3B3] text-xs mb-3 ml-4 cursor-pointer ">
        Cookies</a>
        <a href="https://www.spotify.com/in-en/legal/privacy-policy/#s3" className="text-[#B3B3B3] text-xs mb-3 ml-4 cursor-pointer ">
        AboutUs</a> 
        <a href="https://www.spotify.com/in-en/accessibility" className="text-[#B3B3B3] text-xs mb-3 ml-4 cursor-pointer">
       Accesibility</a>
      </div>
      <div className="flex items-center text-white font-bold mt-5 ml-4 gap-2 outline-[0.5px] py-1 w-25 rounded-full bg-transparent cursor-pointer hover:bg-[#2d2d2d]">
        <CiGlobe className="mt-1 text-xl ml-3"/> <button className="text-sm">English</button>
      </div>
    </div>
  );
};

export default Sidebar;
