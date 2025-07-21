import React from "react";
import Playlist from "../cards/Playlist";
import { albumsData } from "../assets/assets.js";
import Songs from "../cards/Songs.jsx";
import { songsData } from "../assets/assets.js";

const SongCard = () => {
  return (
    <div>
      <h1 className=" my-3 ml-2 w-[190px] text-2xl font-bold cursor-pointer hover:underline">
        Featured Chart's
      </h1>
      <div className="flex overflow-auto mx-3 mt-5 space-x-3 scroll-smooth">
        {albumsData.map((item, index) => (
          <Playlist
            key={index}
            name={item.name}
            desc={item.desc}
            image={item.image}
            Number={item.id}
          />
        ))}
      </div>
      <div className="mb-30">
      <h1 className=" my-3 ml-2 w-[230px] text-2xl font-bold cursor-pointer hover:underline">
       Today's biggest hits
      </h1>
      <div className="flex overflow-auto mt-5 space-x-3 scroll-smooth">
        {songsData.map((item, index) => (
          <Songs
            key={index}
            name={item.name}
            desc={item.desc}
            image={item.image}
          />
        ))}
      </div>
      </div>
    </div>
  );
};

export default SongCard;
