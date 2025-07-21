import React from 'react';
import { GoHomeFill } from 'react-icons/go';
import { FaSearch } from 'react-icons/fa';
import { IoLibrary } from 'react-icons/io5';
import { IoAdd } from 'react-icons/io5';

const Sidebar = () => {
  return (
    <div className="w-[30%] bg-black text-white flex flex-col justify-between p-4 fixed h-screen ">
      <div>
        {/* Top icons: Home, Search */}
        <div className="space-y-4 pl-10 py-5 bg-[#121212] rounded-md">
          <div className="flex items-center space-x-3 text-white  cursor-pointer">
            <GoHomeFill size={22} />
            <span className="text-md font-bold text-white">Home</span>
          </div>
          <div className="flex items-center space-x-3 text-white cursor-pointer">
            <FaSearch size={18} />
            <span className="text-md font-bold text-white">Search</span>
          </div>
        </div>

        {/* Library section */}
        <div className="mt-2 bg-[#121212] p-3 rounded-md h-screen">
          <div className="flex items-center justify-between text-white text-sm font-semibold ml-5 mb-5 mt-3">
            <div className="flex items-center space-x-3">
              <IoLibrary size={25} />
              <span className='font-bold'>Your Library</span>
            </div>
            <IoAdd size={25} className="cursor-pointer hover:text-white" />
          </div>

          {/* Create playlist and Browse podcasts */}
          <div className="mt-4 space-y-4 text-sm bg-[#1F1F1F] p-3 mb-3 rounded-md">
            <div className="p-3 rounded-md">
              <p className="mb-2 text-white font-semibold">Create your first playlist</p>
              <p className="mb-3 text-gray-400">it's easy we'll help you</p>
              <button className="bg-white text-black px-4 py-1 rounded-full text-sm font-bold">
                Create playlist
              </button>
            </div>
          </div>
          <div className='mt-4 space-y-4 text-sm bg-[#1F1F1F] p-3 mb-5 rounded-md'>
            <div className=" p-3 rounded-md">
              <p className="mb-2 text-white font-semibold">Let's find some podcasts to follow</p>
              <p className="mb-3 text-gray-400">We’ll keep you updated on new episodes</p>
              <button className="bg-white text-black px-4 py-1 rounded-full text-sm font-bold">
                Browse podcasts
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom spacing if needed */}
      <div className="text-gray-400 text-xs">
        {/* Add additional links or settings here if needed */}
      </div>
    </div>
  );
};

export default Sidebar;
