import './Sidebar.css'
import './main.css'
import searchbar from './searchbar.svg';
import React, { Component } from 'react';
import Popup from 'reactjs-popup';

class Searchbar extends Component {
    constructor(props) {
        super(props);
        this.state = { startdate: "20200806", enddate: "20201106" };
        this.handleOnUpload = this.handleOnUpload.bind(this);
        this.handleOnChange = this.handleOnChange.bind(this);
    }

    handleOnUpload(e) {
        e.preventDefault();
        this.props.updateMarkers(this.state.startdate, this.state.enddate);
    };

    handleOnChange(e) {
        e.preventDefault();
        this.setState({ [e.target.name]: e.target.value });
    }

    render() {
        return (
            <div className='sidebarItem'>
                <Popup trigger={<img style={{ width: '8vw' }} alt="searchbar" src={searchbar} />} modal nested>
                    {
                        close => (
                            <div className="modal">
                                <button className="close" onClick={close}>
                                    &times;
                                </button>
                                <div>
                                    <div className="userInputDiv">
                                        <label htmlFor="startdate">StartDate:</label>
                                        <input type="text" id="startdate" name="startdate" value={this.state.startdate} onChange={this.handleOnChange} />
                                    </div>
                                    <div className="userInputDiv">
                                        <label htmlFor="enddate">EndDate:</label>
                                        <input type="text" id="enddate" name="enddate" value={this.state.enddate} onChange={this.handleOnChange} />
                                    </div>
                                    <div className="userInputDiv">
                                        <button onClick={this.handleOnUpload}>Upload </button>
                                    </div>
                                </div>
                            </div>
                        )
                    }
                </Popup>
            </div>
        )
    }
}

export default Searchbar;