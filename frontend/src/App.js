import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import GoogleMap from './Map/Map.js';
import Sidebar from './Sidebar/Sidebar.js'
import Upload from './Image/Upload.js'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { markers: [], userId: null, password: null }
    this.updateMarkers = this.updateMarkers.bind(this);
    this.updateUserInfo = this.updateUserInfo.bind(this);
  }

  updateMarkers(startDate = "20200806", endDate = "20201106") {
    fetch(`http://localhost:5000/api/location?startDate=${encodeURIComponent(startDate)}&endDate=${encodeURIComponent(endDate)}`)
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result);
          this.setState({ markers: result })
        },
        (error) => {

        });
  }

  updateUserInfo(uid, pw) {
    this.setState({ userId: uid, password: pw });
  }

  render() {
    return (
      <div>
        <Sidebar userId={this.state.userId} password={this.state.password} updateMarkers={this.updateMarkers} updateUserInfo={this.updateUserInfo}></Sidebar>
        <GoogleMap markers={this.state.markers} updateMarkers={this.updateMarkers}></GoogleMap>
        <Upload userId={this.state.userId}></Upload>
      </div >
    );
  }
}

export default App;
