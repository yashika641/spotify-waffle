import React from 'react'
import { Navigate, useNavigate } from 'react-router-dom'

const Playlist = ({image,name,desc}) => {

    const Navigate = useNavigate();
  return (
  
        
    <div className='max-w-[180px] cursor-pointer hover:bg-[#FFFFFF11] p-3 px-2'>
        <img src={image} alt="Image" className='rounded-sm'/>
        <p className='mt-2 font-bold text-md'>{name}</p>
        <p className='text-gray-400 text-sm mb-5 truncate line-clamp-2'>{desc}</p>
    </div>
   
  )
}

export default Playlist