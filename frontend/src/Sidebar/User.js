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
        const data = new FormData();
        if (this.props.option === signInOption) {
            data.append('userId', this.state.userId);
            data.append('password', this.state.password);
            fetch(`https://api.projectnull76.web.illinois.edu/api/user/login`, {
                method: "POST",
                body: data
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
        else {
            data.append('userId', this.state.userId);
            data.append('password', this.state.password);
            data.append('email', this.state.email);
            data.append('phoneNumber', this.state.phoneNumber);
            data.append('nickName', this.state.nickName);
            data.append('physicalLocation', this.state.physicalLocation);

            fetch(`https://api.projectnull76.web.illinois.edu/api/user`, {
                method: "POST",
                body: data
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
        this.state = { userId: "", password: "", email: "", phoneNumber: "", nickName: "", physicalLocation: "", showComments: false, comments: [] };
        this.handleOnChange = this.handleOnChange.bind(this);
        this.handleOnUpdate = this.handleOnUpdate.bind(this);
        this.handleOnDelete = this.handleOnDelete.bind(this);
        this.handleOnComments = this.handleOnComments.bind(this);
        this.handleOnOpenComment = this.handleOnOpenComment.bind(this);
        this.handleOnEditComment = this.handleOnEditComment.bind(this);
        this.updateComments = this.updateComments.bind(this);
    }

    componentDidMount() {
        fetch(`https://api.projectnull76.web.illinois.edu/api/user/${encodeURIComponent(this.props.userId)}`)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        userId: result.userId, password: result.password, phoneNumber: result.phoneNumber, email: result.email, nickName: result.nickName, physicalLocation: result.physicalLocation, comments: result.comments.map((commentId) => { return { commentId: commentId, content: "", focus: false }; })
                    });
                    this.updateComments();
                },
                (error) => {

                });
    }

    updateComments() {
        for (let idx in this.state.comments.length)
            fetch(`https://api.projectnull76.web.illinois.edu/api/comment/${encodeURIComponent(this.state.comments[idx].commentId)}`)
                .then(res => res.json())
                .then(
                    (result) => {
                        const newComments = this.state.comments.slice();
                        newComments[idx].content = result.content;
                        this.setState({ comments: newComments });
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
        const data = new FormData();
        data.append('userId', this.state.userId);
        data.append('password', this.state.password);
        data.append('email', this.state.email);
        data.append('phoneNumber', this.state.phoneNumber);
        data.append('nickName', this.state.nickName);
        data.append('physicalLocation', this.state.physicalLocation);

        fetch(`https://api.projectnull76.web.illinois.edu/api/user/${encodeURIComponent(this.state.userId)}`, {
            method: "PUT",
            body: data
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
        fetch(`https://api.projectnull76.web.illinois.edu/api/user/${encodeURIComponent(this.state.userId)}`, {
            method: "DELETE"
        })
            .then(res => res.json())
            .then(
                (result) => {
                    this.props.updateWhenLogout();
                })
            .catch(
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
        const data = new FormData();
        data.append('userId', this.state.userId);
        data.append('content', e.target.value);

        fetch(`https://api.projectnull76.web.illinois.edu/api/comment/${encodeURIComponent(this.state.comments[e.target.attributes['index'].value].commentId)}`, {
            method: "PUT",
            body: data
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
                return (<li onDoubleClick={this.handleOnOpenComment} key={idx} index={idx}>{object.content}</li>);
            else
                return (<input style={{ width: "100%" }} onBlur={this.handleOnEditComment} key={idx} index={idx} defaultValue={object.content}></input>);
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
                    {/* <button onClick={this.handleOnComments}>ShowComments </button> */}
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
        if (this.props.userId === null) {
            return (
                <div className='sidebarItem'>
                    <Popup trigger={<img style={{ width: '8vw' }} alt='user' src={user} />} modal nested>
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
                    <Popup trigger={<img style={{ width: '8vw' }} alt='user' src={user} />} modal nested>
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
