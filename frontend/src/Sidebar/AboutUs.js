import './Sidebar.css'
import './main.css'
import aboutus from './aboutus.svg';
import React, { Component } from 'react';
import Popup from 'reactjs-popup';

class AboutUs extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className='sidebarItem'>
                <Popup trigger={<img style={{ width: '8vw' }} alt="aboutus" src={aboutus} />} modal nested>
                    {
                        close => (
                            <div className="modal">
                                <button className="close" onClick={close}>
                                    &times;
                                </button>
                                <div>
                                    <h2> Team Name </h2>
                                    <p> Team NULL</p>
                                    <h2> Members </h2>
                                    <p> rtao6, yitianj2, binyaoj2, dianz3</p>
                                    <h2> Project TA</h2>
                                    <p> Haining Yang</p>
                                    <h2> Project Summary </h2>
                                    <p> This project is going to visualizing the real-time wildfire data. </p>
                                    <p> Our site will established an unique social system based on the wildfire information </p>
                                    <p> where user can share, comment and react to the fire incident </p>
                                    <p> and when user found a wildfire, they can upload the picture to related incident or location.</p>
                                </div>
                            </div>
                        )
                    }
                </Popup>
            </div>
        )
    }
}

export default AboutUs;