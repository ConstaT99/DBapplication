import './main.css';
import React, { Component } from 'react';
import Popup from 'reactjs-popup';

class Upload extends Component {
    constructor(props) {
        super(props);
        this.state = { file: null, content: "" };
        this.handleOnChange = this.handleOnChange.bind(this);
        this.handleOnUpload = this.handleOnUpload.bind(this);
    }

    handleOnChange(e) {
        e.preventDefault();
        if (e.target.name === 'file')
            this.setState({ [e.target.name]: e.target.files[0] });
        else
            this.setState({ [e.target.name]: e.target.value });
    }

    handleOnUpload(e) {
        e.preventDefault();
        if (this.props.incidentId === null) {
            alert("Please click on one marker to choose a certain incident!");
            return;
        }

        const data = new FormData();
        data.append('fireImage', this.state.file);
        data.append('userId', this.props.userId);
        data.append('incidentId', this.props.incidentId);

        fetch(`http://localhost:5000/api/image`, {
            method: "POST",
            body: data
        })
            .then(res => res.json())
            .then(result => {
                const data = new FormData();
                data.append('userId', this.props.userId);
                data.append('imageId', result);
                data.append('content', this.state.content);
                return fetch(`http://localhost:5000/api/comment`, {
                    method: "POST",
                    body: data
                });
            })
            .then(res => res.json())
            .catch(
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
                                        <input type="file" id="file" name="file" onChange={this.handleOnChange} />
                                    </div>
                                    <div className="userInputDiv">
                                        <label htmlFor="content">Content:</label>
                                        <input type="text" id="content" name="content" onChange={this.handleOnChange} />
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