import './Sidebar.css';
import React, { Component } from 'react';
import User from './User.js'
import Admin from './Admin.js'
import Searchbar from './Searchbar.js'

class Sidebar extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className='sidebar'>
                <User userId={this.props.userId} password={this.props.password} updateUserInfo={this.props.updateUserInfo} />
                <Searchbar updateMarkers={this.props.updateMarkers} />
                <Admin />
            </div>
        );
    }
}

export default Sidebar;