var Main = React.createClass({
	getInitialState: function() {
		return {title: "Skeleton Code"}
	},
	render: function() {
		return (
			<div>
				<div className="container">
					<h1 className="title">{this.state.title}</h1>
				</div>
				<TestUserCreate/>
			</div>

		)
	}
});

var TestUserCreate = React.createClass({
	getInitialState: function() {
		return {'username': '', 'device_ID': ''}
	},
	updateUserName: function(e) {
		e.preventDefault()
		this.setState({'username': e.target.value})
	},
	updateDeviceID: function(e) {
		e.preventDefault()
		this.setState({'device_ID': e.target.value})
	},
	submit: function(e) {
		e.preventDefault()
		var form = new FormData()
		console.log(this.state)
		form.append("user", JSON.stringify(this.state))
		$.ajax({
		    type: 'POST',
		    url: '/test/insertdb/user',
		   	contentType: false,
		   	processData: false,
		    data: form,
			success: function(resp) {
				console.log(resp)
		    	this.setState({"id": JSON.parse(resp)})
		    }.bind(this)
  		});
	},
	render: function() {
		return (
			<div className="test-user-create-container">
				<h3 className="test-title">Test User Creation</h3>
				<form className="form" onSubmit={this.submit}>
					<input className="person-input-field" type="text" placeholder="username" value={this.state.username} onChange={this.updateUserName}/>
					<input className="person-input-field" type="text" placeholder="device_ID" value={this.state.device_ID} onChange={this.updateDeviceID}/>
					<input type="submit" value="Submit" />
				</form> 
				<h4>{this.state.id}</h4>
			</div>
		)
	}
})

ReactDOM.render(<Main />, document.getElementById('content'));