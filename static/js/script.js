var b=document.getElementById("btn_registrar");

function goRegistro(){
    location.href="../../templates/registroUsuario.html";
}

function buttonUp(){
    var adminEmplo = document.getElementById('adminEmplo')
    console.log(adminEmplo);
}

function goEmpleado(){
    return render_template('crearEmpleado.html')

}

