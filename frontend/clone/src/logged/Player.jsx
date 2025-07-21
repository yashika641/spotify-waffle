import React from 'react'
import {assets, songsData} from '../assets/assets'


const Player = () => {
  return (
    <div className='flex items-center justify-between text-white w-[100%] h-20 p-4 fixed bottom-0 bg-black '>
        <div className='flex items-center space-x-4 ml-5'>
            <img src={songsData[0].image} alt={songsData[0].name}  className='h-15 w-15 rounded-sm'/>
            <div className='flex flex-col w-50'>
                <p>{songsData[0].name}</p>
                <p className='truncate'>{songsData[0].desc}</p>
            </div>
        </div>
        <div className='flex flex-col items-center justify-center gap-3'>
            <div className='flex items-center justify-center space-x-4'>
                <img src={assets.shuffle_icon} alt="shuffle" className='h-4 w-4 cursor-pointer' />
                <img src={assets.prev_icon} alt="previous" className='h-4 w-4 cursor-pointer' />
                <img src={assets.play_icon} alt="play" className='h-4 w-4 cursor-pointer' />
                <img src={assets.next_icon} alt="next" className='h-4 w-4 cursor-pointer' />
                <img src={assets.loop_icon} alt="repeat" className='h-4 w-4 cursor-pointer' />
            </div>
            <div className='w-150 flex gap-4 items-center justify-center text-sm'>
                <p>00:00</p>
                <hr className='w-full bg-white h-1 rounded-md cursor-pointer' />
                <p>03:45</p>
            </div>
        </div>
        <div className='flex items-center justify-center space-x-2 mr-5'>
            <img src={assets.plays_icon} alt="playlists" className='h-4 w-4 cursor-pointer' />
            <img src={assets.mic_icon} alt="mic" className='h-4 w-4 cursor-pointer' />
            <img src={assets.queue_icon} alt="queue" className='h-4 w-4 cursor-pointer' />
            <img src={assets.speaker_icon} alt="speaker" className='h-4 w-4 cursor-pointer' />
            <img src={assets.volume_icon} alt="volume" className='h-4 w-4 cursor-pointer' />
            <hr className='w-20 cursor-pointer h-1 bg-white rounded-md' />
            <img src={assets.mini_player_icon} alt="mini-player" className='h-4 w-4 cursor-pointer' />
            <img src={assets.zoom_icon} alt="zoom" className='h-4 w-4 cursor-pointer' />
        </div>
    </div>
  )
}

export default Player