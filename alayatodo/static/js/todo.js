// Adding the todo into the list through the verification of
// the description
function addTodo(page){
	// Description input value
	let desc = $("input[name='description']").val();
	// Alert message
	let msg = "";

	// If no description warning alert
	if(desc === ""){
		msg = "<strong>Warning!</strong> Please enter a description for your todo.";
		showAlert("alert-warning", msg);
	} else { // If description exists send the request to server
		let data = {description: desc, page: page};
		ajaxCall("/todo/", data, function(res){
			msg = "Your todo added successfully to the last page.";
			
			showAlert("alert-success", msg);

			let pagination = $('nav ul.pagination');
			pagination.html(res);
		});
	}
}


// Show the alert based on its type (css class) and including the
// message msg
function showAlert(alertType, msg){
	let alert = $(".alert");
	let parag = alert.find("p");
	alert.removeClass("alert-warning alert-success alert-danger");
	
	alert.addClass(alertType);
	parag.html(msg);
	alert.fadeIn();
	alert.fadeOut(5000);
}


// Toggle the value of the is_completed field if checked or not
function toggleCompleted(checkbox, todoId){
	// getting the td parent containing the checkbox
	let td = $(checkbox).closest('td');
	// getting all the td tags in a tr (the todo row)
	let tdList = td.siblings('td');
	// description a tag
	let desc = tdList.find('a.description');
	// POST data
	let data = {
		todoId: todoId
	};
	
	if(checkbox.checked){
		// set the value of is_completed field of the todo 
		data.is_completed = 1;
		// strick through the completed todo
		desc.wrap('<del>');
	} else {
		// set the value of is_completed field of the todo 
		data.is_completed = 0;
		// remove the strick through
		desc.unwrap('<del>');
	}
	
	ajaxCall(`/todo/${todoId}/update/`, data, function(res){
			console.log("toggleCompleted:", res);
		});
}

// Deleting the todo from the database and remove the
// todo row from the view
function deleteTodo(elem, todoId, page){
	let tr = $(elem).closest('tr');

	// calling the delete route
	ajaxCall(`/todo/${todoId}/delete`, {page: page}, function(res){
		msg = "Your todo has been deleted.";
		// displaying the alert
		showAlert("alert-danger", msg);
		// removing the row
		tr.remove();

		let pagination = $('nav ul.pagination');
		pagination.html(res);
	});
}

// Send jQuery POST ajax call
function ajaxCall(url, data, callback){
	$.post(url, data)
		.done(callback)
		.fail(function(err){
			console.log("err", err);
		});
}


