import React from "react";
import { FaSpotify } from "react-icons/fa";
import { Link } from 'react-router-dom'
import { useNavigate } from "react-router-dom";

const Login = () => {

  const navigate = useNavigate();

  return (
    
    <div className="flex flex-col items-center justify-center h-full bg-gradient-to-t from-neutral-900 to-neutral-900 text-white fixed top-0 left-0 right-0 bottom-0 overflow-y-auto scroll-auto scroll-m-2">
      <div className="flex flex-col items-center justify-center w-180 h-full mt-50 p-6 rounded-lg shadow-lg bg-black mb-10">
        <form >
          <div className="flex flex-col items-center justify-center mb-10">
            <div className="flex flex-col items-center mt-10 justify-center">
              <FaSpotify className="text-4xl" />
              <h2 className="text-3xl font-bold mb-10">Log in to Spotify</h2>
            </div>
            <div className="flex flex-col items-center justify-center w-full">
              <button className="cursor-pointer flex items-center justify-center w-full px-10 py-2 mb-3 text-white bg-transparent rounded-full border border-[#818181] hover:border-white transition-colors duration-300">
                <img
                  src="/gogle_logo.png"
                  alt="Google"
                  className="w-6 h-6 mr-11"
                />
                <span className="text-lg font-bold ">
                  {" "}
                  Continue with Google
                </span>
              </button>

              <button className="cursor-pointer flex items-center justify-center w-full px-10 py-2 mb-3 text-white bg-transparent rounded-full border border-[#818181] hover:border-white transition-colors duration-300">
                <img
                  src="/facebook_logo.png"
                  alt="Facebook"
                  className="w-6 h-6 mr-7"
                />
                <span className="text-lg font-bold ">
                  {" "}
                  Continue with Facebook
                </span>
              </button>
              <button className="cursor-pointer flex items-center justify-center w-full px-10 py-2 mb-3 text-white bg-transparent rounded-full border  border-[#818181] hover:border-white transition-colors duration-300">
                <img
                  src="/apple_logo.png"
                  alt="Apple"
                  className="w-6 h-6 mr-15"
                />
                <span className="text-lg font-bold"> Continue with Apple</span>
              </button>
              <button className="cursor-pointer flex items-center justify-center w-full px-10 py-2 mb-3 text-white bg-transparent rounded-full border border-[#818181] hover:border-white transition-colors duration-300 text-lg font-bold">
                Continue with phone number
              </button>
            </div>
          </div>
          <hr className="border-[#818181] mb-10"/>
          <div className="flex flex-col items-start justify-center mb-5">
            <label className="text-sm font-bold mb-2">Email or Username</label>
            <input
              type="text"
              className="w-full px-4 py-3 bg-transparent border border-[#818181] rounded-lg text-white focus:outline-none focus:border-white hover:border-white transition-colors duration-300 mb-5"
              placeholder="Email or username" required></input>
              <button onClick={()=> navigate('/logged/home')} className="cursor-pointer flex items-center justify-center w-full px-10 py-3 mb-10 text-black bg-green-500 rounded-full border border-[#818181] hover:bg-green-400 transition-colors duration-300 text-lg font-bold">Continue</button>
              <div className="flex items-center justify-center w-full mb-15">
              <p className="text-[#B3B3B3]">Don't have an account?</p>
              <Link to="/signup" className="ml-2 text-white underline hover:text-green-500 ">Sign up for Spotify</Link>
              </div>
          </div>
        </form>
      </div>
      <div className="flex items-center justify-center w-full h-20 p-10 text-sm bg-black text-[#B3B3B3]">
      <p>This site is protected by reCAPTCHA and the Google 
        <a href="https://policies.google.com/privacy" target="_blank" className="underline ">Privacy Policy</a> and <a href="https://policies.google.com/terms" target="_blank" className="underline">Terms of Service</a> apply.</p>
    </div>
    </div>
    
   
  );
};

export default Login;
