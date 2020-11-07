import './Sidebar.css'
import './main.css'
import admin from './admin.svg';
import React, { Component } from 'react';
import Popup from 'reactjs-popup';

class Admin extends Component {
    constructor(props) {
        super(props);
        this.state = { results: [] }
        this.showUsersInFireByStatistics = this.showUsersInFireByStatistics.bind(this);
        this.showUsersInFireByAlert = this.showUsersInFireByAlert.bind(this);
    }

    showUsersInFireByStatistics(e) {
        e.preventDefault();
        fetch(`http://localhost:5000/api/userInFire`)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        results: result.map((document) => {
                            return document.userId;
                        })
                    });
                },
                (error) => {
                    alert("failed");
                });
    };

    showUsersInFireByAlert(e) {
        e.preventDefault();
        fetch(`http://localhost:5000/api/userInAlert`)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        results: result.map((document) => {
                            return document.userId;
                        })
                    });
                },
                (error) => {
                    alert("failed");
                });
    }

    render() {
        let results = this.state.results.map((result, idx) => {
            return (<li key={idx}>{result}</li>);
        });

        return (
            <div className='sidebarItem'>
                <Popup trigger={<img style={{ width: '8vw' }} src={admin} />} modal nested>
                    {
                        close => (
                            <div className="modal">
                                <button className="close" onClick={close}>
                                    &times;
                                </button>
                                <div>
                                    <nav>
                                        <ul>
                                            {results}
                                        </ul>
                                    </nav>
                                    <div className="userInputDiv">
                                        <button onClick={this.showUsersInFireByStatistics}>showUsersInFireByStatistics </button>
                                        <button onClick={this.showUsersInFireByAlert}>showUsersInFireByAlert </button>
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

export default Admin;