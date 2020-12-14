import './Sidebar.css'
import './main.css'
import admin from './admin.svg';
import React, { Component } from 'react';
import Popup from 'reactjs-popup';

class Admin extends Component {
    constructor(props) {
        super(props);
        this.state = { results: [] }
        this.showUsersInFire = this.showUsersInFire.bind(this);
        this.showPopularIncidents = this.showPopularIncidents.bind(this);
    }

    showUsersInFire(e) {
        e.preventDefault();
        fetch(`http://localhost:5000/api/admin/userInFire`)
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

    showPopularIncidents(e) {
        e.preventDefault();
        fetch(`http://localhost:5000/api/admin/popularIncidents`)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        results: result.map((document) => {
                            return document.incidentName + ": " + document.count + " comments";
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
                <Popup trigger={<img style={{ width: '8vw' }} alt="admin" src={admin} />} modal nested>
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
                                        <button onClick={this.showUsersInFire}>showUsersInFire </button>
                                        <button onClick={this.showPopularIncidents}>showPopularIncidents </button>
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