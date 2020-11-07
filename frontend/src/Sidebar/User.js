import './Sidebar.css'
import './main.css'
import user from './user.svg';
import React, { Component } from 'react';
import Popup from 'reactjs-popup';

var signInOption = "signIn"
var signUpOption = "signUp"
var profileOption = "profile"

class UserForm extends Component {
    constructor(props) {
        super(props);
        this.state = { userId: "", password: "", email: "", phoneNumber: "", nickName: "", physicalLocation: "" };
        this.handleOnSubmit = this.handleOnSubmit.bind(this);
        this.handleOnChange = this.handleOnChange.bind(this);
    }

    handleOnChange(e) {
        e.preventDefault();
        this.setState({ [e.target.name]: e.target.value });
    }

    handleOnSubmit(e) {
        e.preventDefault();
        if (this.props.option === signInOption) {
            fetch(`http://localhost:5000/api/user/login?userId=${encodeURIComponent(this.state.userId)}&password=${encodeURIComponent(this.state.password)}`)
                .then(res => res.json())
                .then(
                    (result) => {
                        this.props.updateWhenLogin(this.state.userId, this.state.password);
                        // this.props.close();
                    },
                    (error) => {
                        alert("failed");
                    });
        }
        else {
            fetch(`http://localhost:5000/api/user?userId=${encodeURIComponent(this.state.userId)}&password=${encodeURIComponent(this.state.password)}&email=${encodeURIComponent(this.state.email)}&phoneNumber=${encodeURIComponent(this.state.phoneNumber)}&nickName=${encodeURIComponent(this.state.nickName)}&physicalLocation=${encodeURIComponent(this.state.physicalLocation)}`, {
                method: "POST"
            })
                .then(res => res.json())
                .then(
                    (result) => {
                        this.props.updateWhenLogin(this.state.userId, this.state.password);
                        // this.props.close();
                    },
                    (error) => {
                        alert("failed");
                    });
        }
    };

    render() {
        if (this.props.option === signInOption) {
            return (
                <div>
                    <div className="userInputDiv">
                        <label htmlFor="userId">UserId:</label>
                        <input type="text" id="userId" name="userId" onChange={this.handleOnChange} />
                    </div>
                    <div className="userInputDiv">
                        <label htmlFor="password">Password:</label>
                        <input type="password" id="password" name="password" onChange={this.handleOnChange} />
                    </div>
                    <div className="userInputDiv">
                        <button onClick={this.handleOnSubmit}>SignIn </button>
                    </div>
                </div>
            );
        }
        else if (this.props.option === signUpOption)
            return (
                <div>
                    <div className="userInputDiv">
                        <label htmlFor="userId">UserId:</label>
                        <input type="text" id="userId" name="userId" onChange={this.handleOnChange} />
                    </div>
                    <div className="userInputDiv">
                        <label htmlFor="password">Password:</label>
                        <input type="password" id="password" name="password" onChange={this.handleOnChange} />
                    </div>
                    <div className="userInputDiv">
                        <label htmlFor="email">Email:</label>
                        <input type="email" id="email" name="email" onChange={this.handleOnChange} />
                    </div>
                    <div className="userInputDiv">
                        <label htmlFor="phoneNumber">Phone:</label>
                        <input type="tel" id="phoneNumber" name="phoneNumber" onChange={this.handleOnChange} />
                    </div>
                    <div className="userInputDiv">
                        <label htmlFor="nickName">Nickname:</label>
                        <input type="text" id="nickName" name="nickName" onChange={this.handleOnChange} />
                    </div>
                    <div className="userInputDiv">
                        <label htmlFor="physicalLocation">physicalLocation:</label>
                        <input type="text" id="physicalLocation" name="physicalLocation" onChange={this.handleOnChange} />
                    </div>
                    <div className="userInputDiv">
                        <button onClick={this.handleOnSubmit}>SignUp </button>
                    </div>
                </div>
            );
        else
            return (<div></div>)
    }
}

class UserProfile extends Component {
    constructor(props) {
        super(props);
        this.state = { userId: "", password: "", email: "", phoneNumber: "", nickName: "", alertLocation: "", physicalLocation: "", showComments: false, comments: [] };
        this.handleOnChange = this.handleOnChange.bind(this);
        this.handleOnUpdate = this.handleOnUpdate.bind(this);
        this.handleOnDelete = this.handleOnDelete.bind(this);
        this.handleOnComments = this.handleOnComments.bind(this);
        this.handleOnOpenComment = this.handleOnOpenComment.bind(this);
        this.handleOnEditComment = this.handleOnEditComment.bind(this);
        this.updateComments = this.updateComments.bind(this);
    }

    componentDidMount() {
        fetch(`http://localhost:5000/api/user?userId=${encodeURIComponent(this.props.userId)}&password=${encodeURIComponent(this.props.password)}`)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({ userId: result.userId, password: result.password, phoneNumber: result.phoneNumber, email: result.email, nickName: result.nickName, alertLocation: result.alertLocation, physicalLocation: result.physicalLocation })
                },
                (error) => {

                });
    }

    updateComments() {
        fetch(`http://localhost:5000/api/location/messages?userId=${encodeURIComponent(this.state.userId)}`)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({ comments: result.map((document) => { return { messageId: document.messageId, comment: document.content, focus: false }; }) });
                },
                (error) => {
                    alert("failed");
                });
    }

    handleOnChange(e) {
        e.preventDefault();
        this.setState({ [e.target.name]: e.target.value });
    }

    handleOnUpdate(e) {
        e.preventDefault();

        fetch(`http://localhost:5000/api/user?userId=${encodeURIComponent(this.state.userId)}&password=${encodeURIComponent(this.state.password)}&email=${encodeURIComponent(this.state.email)}&phoneNumber=${encodeURIComponent(this.state.phoneNumber)}&nickName=${encodeURIComponent(this.state.nickName)}&alertLocation=${encodeURIComponent(this.state.alertLocation)}&physicalLocation=${encodeURIComponent(this.state.physicalLocation)}`, {
            method: "PUT"
        })
            .then(res => res.json())
            .then(
                (result) => {
                },
                (error) => {
                    alert("failed");
                });
    };

    handleOnDelete(e) {
        e.preventDefault();
        fetch(`http://localhost:5000/api/user?userId=${encodeURIComponent(this.state.userId)}&password=${encodeURIComponent(this.state.password)}`, {
            method: "DELETE"
        })
            .then(res => res.json())
            .then(
                (result) => {
                    this.props.updateWhenLogout();
                },
                (error) => {
                    alert("failed");
                });
    };

    handleOnComments(e) {
        e.preventDefault();
        if (!this.state.showComments) {
            this.updateComments();
        }
        else
            this.setState({ comments: [] });

        this.setState({ showComments: !this.state.showComments });
    }

    handleOnOpenComment(e) {
        e.preventDefault();
        const newComments = this.state.comments.slice();
        newComments[e.target.attributes['index'].value].focus = true;
        this.setState({ comments: newComments });
    }

    handleOnEditComment(e) {
        e.preventDefault();
        const newComments = this.state.comments.slice();
        newComments[e.target.attributes['index'].value].focus = false;
        this.setState({ comments: newComments });
        fetch(`http://localhost:5000/api/location/messages?messageId=${encodeURIComponent(this.state.comments[e.target.attributes['index'].value].messageId)}&content=${encodeURIComponent(e.target.value)}`, {
            method: "PUT"
        })
            .then(res => res.json())
            .then(
                (result) => {
                    this.updateComments();
                },
                (error) => {
                    alert("failed");
                });

    }

    render() {
        let comments = this.state.comments.map((object, idx) => {
            if (!object.focus)
                return (<li onDoubleClick={this.handleOnOpenComment} key={idx} index={idx}>{object.comment}</li>);
            else
                return (<input style={{ width: "100%" }} onBlur={this.handleOnEditComment} key={idx} index={idx} defaultValue={object.comment}></input>);
        });

        return (
            <div>
                <div className="userInputDiv">
                    <label htmlFor="userId">UserId:</label>
                    <input type="text" id="userId" name="userId" value={this.state.userId} onChange={this.handleOnChange} />
                </div>
                <div className="userInputDiv">
                    <label htmlFor="password">Password:</label>
                    <input type="password" id="password" name="password" value={this.state.password} onChange={this.handleOnChange} />
                </div>
                <div className="userInputDiv">
                    <label htmlFor="email">Email:</label>
                    <input type="email" id="email" name="email" value={this.state.email} onChange={this.handleOnChange} />
                </div>
                <div className="userInputDiv">
                    <label htmlFor="phoneNumber">Phone:</label>
                    <input type="tel" id="phoneNumber" name="phoneNumber" value={this.state.phoneNumber} onChange={this.handleOnChange} />
                </div>
                <div className="userInputDiv">
                    <label htmlFor="nickName">Nickname:</label>
                    <input type="text" id="nickName" name="nickName" value={this.state.nickName} onChange={this.handleOnChange} />
                </div>
                <div className="userInputDiv">
                    <label htmlFor="physicalLocation">physicalLocation:</label>
                    <input type="text" id="physicalLocation" name="physicalLocation" value={this.state.physicalLocation} onChange={this.handleOnChange} />
                </div>
                <div className="userInputDiv">
                    <label htmlFor="alertLocation">AlertLocation:</label>
                    <input type="text" id="alertLocation" name="alertLocation" value={this.state.alertLocation} onChange={this.handleOnChange} />
                </div>
                <div>
                    <nav hidden={!this.state.showComments}>
                        <ul>
                            {comments}
                        </ul>
                    </nav>
                </div>
                <div className="userInputDiv">
                    <button onClick={this.handleOnUpdate}>Update </button>
                    <button onClick={this.handleOnDelete}>Delete </button>
                    <button onClick={this.props.updateWhenLogout}>Logout </button>
                    <button onClick={this.handleOnComments}>ShowComments </button>
                </div>
            </div>
        );
    }
}

class User extends Component {
    constructor(props) {
        super(props);
        this.state = { option: signInOption };
        this.updateWhenLogin = this.updateWhenLogin.bind(this);
        this.updateWhenLogout = this.updateWhenLogout.bind(this);
    }

    updateWhenLogin(uid, pw) {
        this.props.updateUserInfo(uid, pw);
        this.setState({ option: profileOption });
    }

    updateWhenLogout() {
        this.props.updateUserInfo(null, null);
        this.setState({ option: signInOption });
    }

    render() {
        if (this.props.userId == null) {
            return (
                <div className='sidebarItem'>
                    <Popup trigger={<img style={{ width: '8vw' }} src={user} />} modal nested>
                        {
                            close => (
                                <div className="modal">
                                    <button className="close" onClick={close}>
                                        &times;
                                    </button>
                                    <button className="header" onClick={() => this.setState({ option: signInOption })}> SignIn </button>
                                    <button className="header" onClick={() => this.setState({ option: signUpOption })}> SignUp </button>
                                    <UserForm option={this.state.option} updateWhenLogin={this.updateWhenLogin} close={close}></UserForm>
                                </div>
                            )
                        }
                    </Popup>
                </div>
            );
        }
        else {
            return (
                <div className='sidebarItem'>
                    <Popup trigger={<img style={{ width: '8vw' }} src={user} />} modal nested>
                        {
                            close => (
                                <div className="modal">
                                    <button className="close" onClick={close}>
                                        &times;
                                    </button>
                                    <UserProfile userId={this.props.userId} password={this.props.password} updateWhenLogout={this.updateWhenLogout}></UserProfile>
                                </div>
                            )
                        }
                    </Popup>
                </div>
            )
        }

    }
}

export default User;
