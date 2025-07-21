import React from 'react'
import { FaSpotify } from "react-icons/fa";
import { Link } from 'react-router-dom'
import { useNavigate } from 'react-router-dom';

const Signup = () => {
  const navigate = useNavigate()
  return (
    <div className="min-h-screen bg-black text-white flex items-center justify-center px-4">
      <div className="max-w-xs w-full flex flex-col items-center mt-8">
        {/* Spotify Logo */}
        <div className="mb-5">
          <FaSpotify className="text-5xl text-white" />
          </div>

        {/* Heading */}
        <h1 className="text-5xl font-bold text-center mb-3">Sign up to</h1>
        <h2 className="text-5xl font-bold text-center mb-8">start listening</h2>

        {/* Email Input */}
        <div className="w-full">
          <label className="text-sm font-semibold mb-2 block">Email address</label>
          <input
            type="email"
            placeholder="name@domain.com"
            className="w-full p-3 rounded border border-gray-600 bg-black text-white focus:outline-none hover:border-white transition duration-200 focus:border-white"
          />
          <a href='#' className="text-green-500 text-sm mt-2 underline cursor-pointer">
            Use phone number instead.
          </a>
        </div>

        {/* Next Button */}
        <button onClick={() => navigate('/logged/home')} className="w-full bg-green-500 text-black font-bold py-3 rounded-full mt-6 cursor-pointer hover:bg-green-400 transition">
          Next
        </button>

        {/* Divider */}
        <div className="flex items-center my-6 w-full">
          <hr className="flex-grow border-white" />
          <span className="mx-4 text-white text-sm">or</span>
          <hr className="flex-grow border-white" />
        </div>

        {/* Sign up with Google */}
        <button className="w-full flex items-center justify-between px-10 gap-2 border border-gray-600 rounded-full py-3 mb-4 hover:border-white transition">
          <img src="/gogle_logo.png" alt="Google" className="w-7 h-7" />
          <span className='font-bold mr-10'>Sign up with Google</span>
        </button>

        {/* Sign up with Apple */}
        <button className="w-full flex items-center justify-between px-10 gap-2 border border-gray-600 rounded-full py-3 hover:border-white transition mb-10">
          <img src="/apple_logo.png" alt="Apple" className="w-7 h-7" />
          <span className='mr-10 font-bold'>Sign up with Apple</span>
        </button>

        {/*Divider */}
        <hr className="border-gray-800 mb-6 w-full" />

        {/* Login Link */}
        <p className="text-md text-[#B3B3B3] font-semibold">
          Already have an account?{" "}
          <Link to='/login' className="underline text-white hover:text-green-500">
            Log in here.
          </Link>
        </p>

        {/* Footer section */}
        <div className='flex flex-col items-center justify-center w-full text-xs text-[#B3B3B3] my-8 font-semibold'>
          <p>This site is protected by reCAPTCHA and the Google</p>
          <p><a href='https://policies.google.com/privacy' target='_blank' className='underline'>Privacy Policy</a> and <a href='https://policies.google.com/terms' target='_blank' className='underline'>Terms of Service</a> apply.</p>
        </div>
      </div>
    </div>
  )
}

export default Signup