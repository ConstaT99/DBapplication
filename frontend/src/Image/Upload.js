import './main.css';
import React, { Component } from 'react';
import Popup from 'reactjs-popup';

class Upload extends Component {
    constructor(props) {
        super(props);
        this.state = { location: "", message: "" };
        this.handleOnChange = this.handleOnChange.bind(this);
        this.handleOnUpload = this.handleOnUpload.bind(this);
    }

    handleOnChange(e) {
        e.preventDefault();
        this.setState({ [e.target.name]: e.target.value });
    }

    handleOnUpload(e) {
        e.preventDefault();
        fetch(`http://localhost:5000/api/location/messages?location=${encodeURIComponent(this.state.location)}&content=${encodeURIComponent(this.state.message)}&userId=${encodeURIComponent(this.props.userId)}`, {
            method: "POST"
        })
            .then(res => res.json())
            .then(
                (result) => {
                },
                (error) => {
                    alert("failed");
                });
    }

    render() {
        return (
            <div className='sidebarItem'>
                <Popup trigger={<button className='upload'>Upload</button>} modal nested>
                    {
                        close => (
                            <div className="modal">
                                <button className="close" onClick={close}>
                                    &times;
                                </button>
                                <div>
                                    <div className="userInputDiv">
                                        <label htmlFor="location">Location:</label>
                                        <input type="text" id="location" name="location" onChange={this.handleOnChange} />
                                    </div>
                                    <div className="userInputDiv">
                                        <label htmlFor="message">Message:</label>
                                        <input type="text" id="message" name="message" onChange={this.handleOnChange} />
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

        );
    }
}

export default Upload;