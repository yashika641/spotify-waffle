import React from "react";
import songs from "../data/songs.json";
import artist from "../data/artist.json";
import album from "../data/album.json";
import featured from "../data/featured.json";
import { FaPlay } from "react-icons/fa";
import {
  FaInstagram,
  FaTwitter,
  FaFacebook,
  FaRegCopyright,
} from "react-icons/fa";

const Main = () => {
  return (
    <div className="flex-1 bg-[#1e1b1b] min-h-screen w-full space-y-10 rounded-lg mt-17 ml-115 text-white scroll-smooth overflow-y-auto">
      {/* Trending Songs */}
      <div className="ml-10">
        <h2 className="w-44 text-2xl mt-8 font-bold mb-4 cursor-pointer hover:underline">
          Trending songs
        </h2>
        <div className="flex gap-1 overflow-x-auto scrollbar-hide pb-2 scroll-smooth w-full">
          {songs.map((song, index) => (
            <div
              key={index}
              className=" min-w-[205px] rounded-lg p-3 hover:bg-[#242121] cursor-pointer h-60 relative group"
            >
              <img
                src={song.image}
                alt={song.title}
                className=" w-45 h-45 rounded-xl mb-2 "
              />

              <p className="font-semibold text-sm mb-2 truncate line-clamp-2">
                {song.title}
              </p>
              <p className="text-xs text-zinc-400 truncate hover:underline">
                {song.artist}
              </p>
              <button className="absolute cursor-pointer bottom-20 right-5 opacity-0 group-hover:opacity-100 transition bg-green-500 text-white p-4 rounded-full">
                <FaPlay
                  className="text-lg flex items-center justify-center text-black"
                  size={20}
                />
              </button>
            </div>
          ))}
        </div>
      </div>

      <div className="ml-10">
        <h2 className="w-44 text-2xl mt-8 font-bold mb-4 cursor-pointer hover:underline">
          Popular artists
        </h2>
        <div className="flex gap-1 overflow-x-auto scrollbar-hide pb-2 scroll-smooth">
          {artist.map((song, index) => (
            <div
              key={index}
              className="min-w-[210px] rounded-lg p-3 hover:bg-[#242121] cursor-pointer h-60 relative group"
            >
              <img
                src={song.image}
                alt={song.artist}
                className="h-45 w-45 object-cover rounded-full mb-2"
              />
              <p className="font-semibold text-sm mb-2">{song.artist}</p>
              <p className="text-xs text-zinc-400 truncate">{song.type}</p>
              <button className="absolute cursor-pointer bottom-12 right-5 opacity-0 group-hover:opacity-100 transition bg-green-500 text-white p-4 rounded-full">
                <FaPlay
                  className="text-lg flex items-center justify-center text-black"
                  size={20}
                />
              </button>
            </div>
          ))}
        </div>
      </div>

      <div className="ml-10">
        <h2 className="w-80 text-2xl mt-8 font-bold mb-4 cursor-pointer hover:underline">
          Popular albums and singles
        </h2>
        <div className="flex gap-1 overflow-x-auto scrollbar-hide pb-2 scroll-smooth">
          {album.map((song, index) => (
            <div
              key={index}
              className="min-w-50 rounded-lg p-3 hover:bg-[#242121] cursor-pointer h-75 relative group"
            >
              <img
                src={song.image}
                alt={song.title}
                className="w-45 h-45 rounded-xl mb-5"
              />

              <p className="font-semibold text-sm line-clamp-2 mb-2">
                {song.title}
              </p>

              <p className="text-xs text-zinc-400 line-clamp-2">{song.artist}</p>

              <button className="absolute cursor-pointer bottom-30 right-5 opacity-0 group-hover:opacity-100 transition bg-green-500 text-white p-4 rounded-full">
                <FaPlay
                  className="text-lg flex items-center justify-center text-black"
                  size={20}
                />
              </button>
            </div>
          ))}
        </div>
      </div>

      <div className="ml-10 mb-10">
        <h2 className="w-47 text-2xl mt-8 font-bold mb-4 cursor-pointer hover:underline">
          Featured chart's
        </h2>
        <div className="flex gap-1 overflow-x-auto scrollbar-hide pb-2 scroll-smooth">
          {featured.map((song, index) => (
            <div
              key={index}
              className=" min-w-55 rounded-lg p-3 hover:bg-[#242121] cursor-pointer h-65 relative group"
            >
              <img
                src={song.image}
                alt={song.title}
                className=" w-50 h-48 rounded-lg mb-5 "
              />

              <p className=" font-semibold text-sm line-clamp-2 mb-2 text-zinc-400 ">
                {song.description}
              </p>
              <button className="absolute  cursor-pointer bottom-17 right-7 opacity-0 group-hover:opacity-100 transition bg-green-500 text-white p-4 rounded-full">
                <FaPlay
                  className="text-lg flex items-center justify-center text-black"
                  size={20}
                />
              </button>
            </div>
          ))}
        </div>
      </div>

      <hr className="border-t-2 border-gray-800 mx-10 mb-20" />
      <div className="flex justify-between items-start ml-10 mb-15">
        <div className="flex flex-col gap-2">
          <h2 className="font-bold">Company</h2>
          <a
            href="https://www.spotify.com/in-en/about-us/contact/"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            About
          </a>
          <a
            href="https://www.lifeatspotify.com/"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Jobs
          </a>
          <a
            href="https://newsroom.spotify.com/"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            For the Record
          </a>
        </div>

        <div className="flex flex-col gap-2">
          <h2 className="font-bold">Communities</h2>
          <a
            href="https://artists.spotify.com/home"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            For Artists
          </a>
          <a
            href="https://developer.spotify.com/"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Developers
          </a>
          <a
            href="https://ads.spotify.com/en-IN/"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Advertising
          </a>
          <a
            href="https://investors.spotify.com/home/default.aspx"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Investors
          </a>
          <a
            href="https://spotifyforvendors.com/"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Vendors
          </a>
        </div>

        <div className="flex flex-col gap-2">
          <h2 className="font-bold">Useful links</h2>
          <a
            href="https://support.spotify.com/in-en/"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Support
          </a>
          <a
            href="https://www.spotify.com/in-en/free/"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Free Mobile App
          </a>
          <a
            href="https://open.spotify.com/popular-in/in"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Popular by Country
          </a>
        </div>

        <div className="flex flex-col gap-2 mr-10">
          <h2 className="font-bold">Spotify Plans</h2>
          <a
            href="https://www.spotify.com/in-en/premium/#ref=spotifycom_footer_premium_individual"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Premium Individual
          </a>
          <a
            href="https://www.spotify.com/in-en/duo/#ref=spotifycom_footer_premium_duo"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Premium Duo
          </a>
          <a
            href="https://www.spotify.com/in-en/family/#ref=spotifycom_footer_premium_family"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Premium Family
          </a>
          <a
            href="https://www.spotify.com/in-en/student/#ref=spotifycom_footer_premium_student"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Premium Student
          </a>
          <a
            href="https://www.spotify.com/in-en/free/#ref=spotifycom_footer_free"
            className="text-[#fffcfca4] hover:text-[#fffcfcf0] hover:underline cursor-pointer"
          >
            Spotify Free
          </a>
        </div>

        <div className="flex items-center gap-6 mr-10 text-white">
          <a href="https://www.instagram.com/spotify/" target="_blank">
            {" "}
            <FaInstagram className="text-2xl mb-2" />
          </a>
          <a href="https://x.com/spotify" target="_blank">
            {" "}
            <FaTwitter className="text-2xl mb-2" />
          </a>
          <a href="https://www.facebook.com/Spotify" target="_blank">
            {" "}
            <FaFacebook className="text-2xl mb-2" />
          </a>
        </div>
      </div>

      <hr className="border-t-2 border-gray-800 mx-10 mb-10" />
      <div className="mb-30 flex flex-row ml-10 text-[#fffcfca4] text-sm">
        <FaRegCopyright className="mt-1.5 mr-1 size-3" />
        <p> 2025 spotify AB</p>
      </div>
    </div>
  );
};

export default Main;
