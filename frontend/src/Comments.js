import './Comments.css';
import React, { Component } from 'react';

var defaultImageLimit = 3;
var defaultCommentsLimit = 5;
class Comments extends Component {
    constructor(props) {
        super(props);
        this.state = { messages: [], imageLimit: defaultImageLimit };
        this.fetchComments = this.fetchComments.bind(this);
        this.fetchLikes = this.fetchLikes.bind(this);
        this.fetchImages = this.fetchImages.bind(this);
        this.handleOnChange = this.handleOnChange.bind(this);
        this.handleOnReply = this.handleOnReply.bind(this);
        this.handleOnLike = this.handleOnLike.bind(this);
        this.handleOnShowMore = this.handleOnShowMore.bind(this);
        this.handleOnOpenMessage = this.handleOnOpenMessage.bind(this);
        this.handleOnEditMessage = this.handleOnEditMessage.bind(this);
        this.handleOnLoadMore = this.handleOnLoadMore.bind(this);
        this.contentRef = [];
    }

    componentDidMount() {
        if (this.props.userId === null) {
            alert("Please log in!");
            return;
        }

        this.fetchImages();
    }

    handleOnChange(e) {
        e.preventDefault();
        this.setState({ [e.target.name]: e.target.value });
    }

    fetchImages(limit) {
        if (limit === undefined)
            limit = this.state.imageLimit;

        if (this.props.incidentId !== null)
            fetch(`https://api.projectnull76.web.illinois.edu/api/image/popular/${encodeURIComponent(this.props.incidentId)}?limit=${encodeURIComponent(limit)}`, {
                method: "GET"
            })
                .then(res => res.json())
                .then(
                    (result) => {
                        this.setState({
                            messages: result.map((document) => {
                                return { image: { imageId: document.imageId, imageUrl: `https://api.projectnull76.web.illinois.edu/api/image/${encodeURIComponent(document.imageId)}`, liked: false, count: document.like }, comments: { commentIds: document.comments, contents: new Array(document.comments.length).fill(""), focuses: new Array(document.comments.length).fill(false), limit: Math.min(document.comments.length, defaultCommentsLimit) } };
                            })
                        });

                        result.forEach((document, msg_idx) => {
                            this.fetchLikes(msg_idx);
                            this.fetchComments(msg_idx);
                        });
                    })
                .catch(
                    (error) => {
                        alert("failed");
                    });
        // else
        //     fetch(`https://api.projectnull76.web.illinois.edu/api/user/${encodeURIComponent(this.props.userId)}`, {
        //         method: "GET"
        //     })
        //         .then(res => res.json())
        //         .then(
        //             (result) => {
        //                 this.setState({
        //                     messages: result.uploads.slice(0, this.state.imageLimit).map((document) => {
        //                         return { image: { imageId: document.imageId, imageUrl: `https://api.projectnull76.web.illinois.edu/api/image/${encodeURIComponent(document.imageId)}` }, comments: { commentIds: document.comments, contents: new Array(document.comments.length).fill(""), focuses: new Array(document.comments.length).fill(false), limit: Math.min(document.comments.length, defaultCommentsLimit) } };
        //                     })
        //                 });

        //                 result.forEach((document, msg_idx) => {
        //                     this.fetchComments(msg_idx);
        //                 });
        //             })
        //         .catch(
        //             (error) => {
        //                 alert("failed");
        //             });
    }

    fetchComments(imageIdx) {
        this.state.messages[imageIdx].comments.commentIds.slice(0, this.state.messages[imageIdx].comments.limit).forEach((commentId, comment_idx) => {
            fetch(`https://api.projectnull76.web.illinois.edu/api/comment/${encodeURIComponent(commentId)}`, {
                method: "GET"
            })
                .then(res => res.json())
                .then(result => {
                    console.log(result);
                    const newMessages = this.state.messages.slice();
                    newMessages[imageIdx].comments.contents[comment_idx] = result.userId + ": " + result.content;
                    this.setState({ messages: newMessages });
                });
        });
    }

    fetchLikes(imageIdx) {
        fetch(`https://api.projectnull76.web.illinois.edu/api/user/${encodeURIComponent(this.props.userId)}`)
            .then(res => res.json())
            .then(result => {
                const newMessages = this.state.messages.slice();
                newMessages[imageIdx].image.liked = result.likes.includes(newMessages[imageIdx].image.imageId);
                this.setState({ messages: newMessages });
            });
    }

    handleOnOpenMessage(e) {
        let imageIdx = e.target.attributes['imageIdx'].value;
        let commentIdx = e.target.attributes['index'].value;
        e.preventDefault();
        const newMessages = this.state.messages.slice();
        newMessages[imageIdx].comments.focuses[commentIdx] = true;
        this.setState({ messages: newMessages });
    }

    handleOnEditMessage(e) {
        let imageIdx = e.target.attributes['imageIdx'].value;
        let commentIdx = e.target.attributes['index'].value;
        e.preventDefault();
        const newMessages = this.state.messages.slice();
        newMessages[imageIdx].comments.focuses[commentIdx] = false;
        this.setState({ messages: newMessages });
        const data = new FormData();
        data.append('userId', this.props.userId);
        data.append('content', e.target.value.substring(e.target.value.indexOf(": ") + 2));

        fetch(`https://api.projectnull76.web.illinois.edu/api/comment/${encodeURIComponent(this.state.messages[imageIdx].comments.commentIds[commentIdx])}`, {
            method: "PUT",
            body: data
        })
            .then(res => res.json())
            .then(
                (result) => {
                    this.fetchImages();
                },
                (error) => {
                    alert("failed (perhaps you are not the user who wrote the comment)");
                });

    }

    handleOnReply(e) {
        e.preventDefault();

        if (this.props.userId === null) {
            alert("Please log in!");
            return;
        }

        let imageIdx = e.target.getAttribute('imageidx');
        let imageId = e.target.getAttribute('imageid');
        const data = new FormData();
        data.append('userId', this.props.userId);
        data.append('imageId', imageId);
        data.append('content', this.contentRef[imageIdx].value);
        this.contentRef[imageIdx].value = "";
        fetch(`https://api.projectnull76.web.illinois.edu/api/comment`, {
            method: "POST",
            body: data
        })
            .then(res => res.json())
            .then(result => this.fetchImages())
            .catch(
                (error) => {
                    alert("failed");
                });
    }

    handleOnLike(e) {
        e.preventDefault();

        if (this.props.userId === null) {
            alert("Please log in!");
            return;
        }

        let imageIdx = e.target.getAttribute('imageidx');
        let imageId = e.target.getAttribute('imageid');
        fetch(`https://api.projectnull76.web.illinois.edu/api/image/${imageId}/like/${encodeURIComponent(this.props.userId)}`, {
            method: "PUT"
        })
            .then(res => res.json())
            .then(result => {
                const newMessages = this.state.messages.slice();
                newMessages[imageIdx].image.count = result.like;
                this.setState({ messages: newMessages });
                this.fetchLikes(imageIdx);
            });
    }

    handleOnShowMore(e) {
        e.preventDefault();
        let msgIndex = e.target.attributes['msgindex'].value;
        const newMessages = this.state.messages.slice();
        newMessages[msgIndex].comments.limit = Math.min(newMessages[msgIndex].comments.contents.length, 2 * newMessages[msgIndex].comments.limit);
        this.setState({ messages: newMessages });
        this.fetchComments(msgIndex);
    }

    handleOnLoadMore(e) {
        e.preventDefault();
        let limit = this.state.imageLimit * 2;
        this.setState({ imageLimit: limit });
        this.fetchImages(limit);
    }

    render() {
        let messages = this.state.messages.filter(message => message.image.imageUrl !== null).map((message, imageIdx) => {
            return (
                <div key={imageIdx}>
                    <img style={{ width: '24vw' }} src={message.image.imageUrl} alt={message.image.imageId} />
                    {
                        message.comments.contents.slice(0, message.comments.limit).map((content, idx) => (
                            (!message.comments.focuses[idx]) ? (<li onDoubleClick={this.handleOnOpenMessage} key={idx} index={idx} imageidx={imageIdx}>{content}</li>) : (<input style={{ width: "100%" }} onBlur={this.handleOnEditMessage} key={idx} index={idx} imageidx={imageIdx} defaultValue={content}></input>)
                        ))}
                    <div className="commentBtnDiv">
                        {(message.image.liked) ? (<button imageid={message.image.imageId} imageidx={imageIdx} onClick={this.handleOnLike} className="clickedButton">Upvote({message.image.count})</button>) : (<button imageid={message.image.imageId} imageidx={imageIdx} onClick={this.handleOnLike}>Upvote({message.image.count})</button>)}
                        <button imageid={message.image.imageId} imageidx={imageIdx} onClick={this.handleOnReply} >Reply</button>
                        <input type="text" name="content" ref={(ref) => { this.contentRef[imageIdx] = ref; return true; }} />
                        {(message.comments.limit !== message.comments.contents.length) ? <button msgindex={imageIdx} onClick={this.handleOnShowMore} >ShowMore</button> : null}
                    </div>
                </div>
            );
        });

        return (
            <div>
                {messages}
                <div className="commentBtnDiv">
                    <button onClick={this.handleOnLoadMore}>LoadMore...</button>
                </div>
            </div>
        );
    }
}

export default Comments;