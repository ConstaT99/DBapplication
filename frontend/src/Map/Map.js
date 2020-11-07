import React, { Component } from 'react';
import { InfoWindow, Map, Marker, GoogleApiWrapper } from 'google-maps-react';

class GoogleMap extends Component {
    constructor(props) {
        super(props);
        this.state = { showingInfoWindow: false, activeMarkers: null, selectedPlace: null, messages: [] };
        this.onMarkerClick = this.onMarkerClick.bind(this);
    }

    componentDidMount() {
        this.props.updateMarkers();
    }

    onMarkerClick(props, marker, e) {
        fetch(`http://localhost:5000/api/location/messages?location=${encodeURIComponent(props.name)}`, {
            method: "GET"
        })
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        selectedPlace: props.name, showingInfoWindow: true, activeMarker: marker, messages: result.map((document) => {
                            return document.content;
                        })
                    });
                },
                (error) => {
                    alert("failed");
                });
    }

    render() {
        let markers = this.props.markers.map((document, idx) => {
            return (
                <Marker
                    name={document.incident_county}
                    position={{ lat: document.incident_latitude, lng: document.incident_longitude }}
                    key={idx}
                    onClick={this.onMarkerClick}
                />
            );
        });

        let messages = this.state.messages.map((message) => {
            return (
                <h4>
                    {message}
                </h4>
            );
        });

        return (
            // Important! Always set the container height explicitly
            <div style={{ height: '100vh', width: '100%', zIndex: 0 }}>
                <Map google={this.props.google}
                    style={{ width: '100%', height: '100%', position: 'relative' }}
                    className={'map'}
                    zoom={6}>
                    {markers}
                    <InfoWindow
                        marker={this.state.activeMarker}
                        visible={this.state.showingInfoWindow}>
                        <div>
                            <h1>{this.state.selectedPlace}</h1>
                            {messages}
                        </div>
                    </InfoWindow>
                </Map>
            </div >
        );
    }
}

export default GoogleApiWrapper({
    apiKey: ('AIzaSyCmZnRtw0xIanHy7w7IteNzYoY1wyuQW4s')
})(GoogleMap)

