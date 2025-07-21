import React from 'react'

const Songs = ({image,name,desc}) => {
  return (
    <div className='max-w-[180px] px-2 p-3 hover:bg-[#FFFFFF11] cursor-pointer'>
        <img src={image} alt='Image' className='rounded-sm'/>
        <p className='font-bold text-md mt-2'>{name}</p>
        <p className='text-gray-400 text-sm mb-5 truncate line-clamp-2'>{desc}</p>
    </div>
  )
}

export default Songs