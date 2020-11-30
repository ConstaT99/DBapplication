import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { InfoWindow, Map, Marker, GoogleApiWrapper } from 'google-maps-react';
import Comments from '../Comments.js'

class GoogleMap extends Component {
    constructor(props) {
        super(props);
        this.state = { showingInfoWindow: false, activeMarkers: null, incidentId: null, selectedPlace: null };
        this.onMarkerClick = this.onMarkerClick.bind(this);
        this.onInfoWindowClose = this.onInfoWindowClose.bind(this);
        this.onInfoWindowOpen = this.onInfoWindowOpen.bind(this);
    }

    componentDidMount() {
        this.props.updateMarkers();
    }

    onInfoWindowClose(props, e) {
        this.props.updateIncidentId(null);
        this.props.updateAnimation(null);
    }

    onInfoWindowOpen(props, e) {
        const newDiv = (<div><h1>{this.state.selectedPlace}</h1><Comments incidentId={this.state.incidentId} userId={this.props.userId} /></div>);
        ReactDOM.render(React.Children.only(newDiv), document.getElementById("iwc"));
    }

    onMarkerClick(props, marker, e) {
        this.props.updateIncidentId(props.incidentId);
        this.props.updateAnimation(props.index);
        this.setState({ selectedPlace: props.name, incidentId: props.incidentId, showingInfoWindow: true, activeMarker: marker });
    }

    render() {
        let markers = this.props.markers.map((document, idx) => {
            return (
                <Marker
                    name={document.incidentCounty}
                    incidentId={document.incidentId}
                    position={{ lat: document.incidentLatitude, lng: document.incidentLongitude }}
                    index={idx}
                    key={idx}
                    onClick={this.onMarkerClick}
                    animation={(this.props.animations[idx]) ? (this.props.google.maps.Animation.BOUNCE) : (null)}
                />
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
                        visible={this.state.showingInfoWindow}
                        onOpen={e => {
                            this.onInfoWindowOpen(this.props, e);
                        }}
                        onClose={e => {
                            this.onInfoWindowClose(this.props, e);
                        }}>
                        <div id="iwc" />
                    </InfoWindow>
                </Map>
            </div >
        );
    }
}

export default GoogleApiWrapper({
    apiKey: ('AIzaSyCmZnRtw0xIanHy7w7IteNzYoY1wyuQW4s')
})(GoogleMap)

