const pwdInput = document.getElementById('password')
const btnToggleVisibility = document.querySelector('.btn-toggle-visibility')

btnToggleVisibility.addEventListener('click', function(e){
    console.log(btnToggleVisibility.getAttribute('checked'))
    const iconBtnToggleVisibility = btnToggleVisibility.querySelector('i')
    console.log(iconBtnToggleVisibility)

    if (btnToggleVisibility.getAttribute('checked') == null)
    {
        btnToggleVisibility.setAttribute('checked', 'checked')
        pwdInput.type = 'text'
        iconBtnToggleVisibility.classList.remove("bi-eye");
        iconBtnToggleVisibility.classList.add("bi-eye-slash");
    }
    else
    {
        btnToggleVisibility.removeAttribute('checked')
        pwdInput.type = 'password'
        iconBtnToggleVisibility.classList.remove("bi-eye-slash");
        iconBtnToggleVisibility.classList.add("bi-eye");
    }
})