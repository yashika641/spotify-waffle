import React from 'react'
import Sidebar from './Sidebar2'
import Main from './main2'
import Player from './Player'


const Home2 = () => {
  return (
    <>
    <div className='flex'>
        <Sidebar />
        <Main />
    </div>
    
    <Player />
    
    </>
  )
}

export default Home2