import React from "react";
import { Link } from "react-router-dom";

const Footer = () => {
  
  return (
   

    <Link to="/signup">
      <div className="fixed bottom-0 left-0 w-full h-[9%] mt-4 bg-gradient-to-r from-[#af2896] to-[#509bf5] cursor-pointer flex items-center justify-between p-4 rounded-lg">
        <div className="">
          <p className="font-bold">Preview of Spotify</p>
          <p className="font-semibold">
            Sign up to get unlimited songs and podcasts with occasional ads.No
            credit card needed
          </p>
        </div>
        <div>
          <button  className="bg-white text-black font-bold py-2 text-lg px-4 rounded-full cursor-pointer ">
            sign up free
          </button>
        </div>
      </div>
    </Link >
  );
};

export default Footer;
