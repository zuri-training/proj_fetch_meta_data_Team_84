const form = document.getElementById('form');
const firstName = document.getElementById('firstName');
const lastName = document.getElementById('lastName');
const signUpEmail = document.getElementById('signUpEmail');
const signUpPassword = document.getElementById('signUpPassword');
const signUpPassword2 = document.getElementById('signUpPassword2');

form.addEventListener('submit', e => {
	e.preventDefault();
	
	checkInputs();
});

function checkInputs() {
	// trim to remove the whitespaces
	const firstNameValue = firstName.value.trim();
    const lastNameValue = lastName.value.trim();
	const emailValue = signUpEmail.value.trim();
	const passwordValue = signUpPassword.value.trim();
	const password2Value = signUpPassword2.value.trim();
	
	if(firstNameValue === '') {
		setErrorFor(firstName, 'First name cannot be blank');
	} else {
		setSuccessFor(firstName);
	}

    if(lastNameValue === '') {
		setErrorFor(lastName, 'Last name cannot be blank');
	} else {
		setSuccessFor(lastName);
	}
	
	if(emailValue === '') {
		setErrorFor(signUpEmail, 'Email cannot be blank');
	} else if (!isEmail(emailValue)) {
		setErrorFor(signUpEmail, 'Not a valid email');
	} else {
		setSuccessFor(signUpEmail);
	}
	
	if(passwordValue === '') {
		setErrorFor(signUpPassword, 'Password cannot be blank');
	} else {
		setSuccessFor(signUpPassword);
	}
	
	if(password2Value === '') {
		setErrorFor(signUpPassword2, 'Password cannot be blank');
	} else if(passwordValue !== password2Value) {
		setErrorFor(signUpPassword2, 'Passwords does not match');
	} else{
		setSuccessFor(signUpPassword2);
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}
	
function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}