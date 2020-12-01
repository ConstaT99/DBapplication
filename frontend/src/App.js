import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import GoogleMap from './Map/Map.js';
import Sidebar from './Sidebar/Sidebar.js'
import Upload from './Image/Upload.js'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { markers: [], animations: [], userId: null, password: null, incidentId: null }
    this.updateMarkers = this.updateMarkers.bind(this);
    this.updateAnimation = this.updateAnimation.bind(this);
    this.updateUserInfo = this.updateUserInfo.bind(this);
    this.updateIncidentId = this.updateIncidentId.bind(this);
  }

  updateMarkers(startDate = "20200806", endDate = "20201106") {
    fetch(`https://api.projectnull76.web.illinois.edu/api/location?startDate=${encodeURIComponent(startDate)}&endDate=${encodeURIComponent(endDate)}`)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({ markers: result, animations: new Array(result.length).fill(false) });
        },
        (error) => {

        });
  }

  updateAnimation(index) {
    const newAnimations = this.state.animations.slice();
    let orig_animation = newAnimations[index];
    newAnimations.fill(false);

    if (index !== null)
      newAnimations[index] = !orig_animation;
    this.setState({ animations: newAnimations });
  }

  updateUserInfo(userId, password) {
    this.setState({ userId: userId, password: password });
  }

  updateIncidentId(incidentId) {
    this.setState({ incidentId: incidentId });
  }

  render() {
    return (
      <div>
        <Sidebar userId={this.state.userId} password={this.state.password} updateMarkers={this.updateMarkers} updateUserInfo={this.updateUserInfo}></Sidebar>
        <GoogleMap userId={this.state.userId} markers={this.state.markers} animations={this.state.animations} updateMarkers={this.updateMarkers} updateIncidentId={this.updateIncidentId} updateAnimation={this.updateAnimation}></GoogleMap>
        <Upload userId={this.state.userId} incidentId={this.state.incidentId}></Upload>
      </div >
    );
  }
}

export default App;
