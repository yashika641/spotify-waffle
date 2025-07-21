import React from "react";
import Nav from "./Nav";
import SongCard from "./SongCard";

const main2 = () => {
  return (
    <div className="w-[70%] h-screen mt-4 rounded-sm bg-[#121212] text-white flex flex-col overflow-y-auto scroll-smooth fixed right-2 top-0 bottom-0">
      <div className="ml-5">
        <Nav />
        <SongCard />
      </div>
    </div>
  );
};

export default main2;
