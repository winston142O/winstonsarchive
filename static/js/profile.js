window.onload = function() {
    // Get and store elements
    var userData = document.getElementById('user-data');
    var editUserForm = document.getElementById('edit-user-form');
    
    // Hide initially
    editUserForm.classList.add('hide-div');

    // Apply fade-in animations
    userData.classList.add('fade-in', 'visible');
    editUserForm.classList.add('fade-in');
};

document.addEventListener('DOMContentLoaded', function() {
    // Get and store elements
    var editProfileBtn = document.getElementById('edit-profile');
    var editUserForm = document.getElementById('edit-user-form');
    var userData = document.getElementById('user-data');
    var cancel_edit = document.getElementById('cancel-edit');

    // Add click event listener
    editProfileBtn.addEventListener('click', function() {
        editUserForm.classList.remove('hide-div');
        setTimeout(function() {
            editUserForm.classList.add('visible');
            userData.classList.remove('visible');
        }, 200);        
    });

    // Add click event listener
    cancel_edit.addEventListener('click', function() {
        editUserForm.classList.remove('visible');
        userData.classList.add('visible');
        setTimeout(function() {
            editUserForm.classList.add('hide-div');
        }, 400);        
    });
});
