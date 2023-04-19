function copyEmail() {
    // Get the email address
    var email = document.getElementById("email").innerHTML.trim();
    
    // Copy the email address to the clipboard
    navigator.clipboard.writeText(email);
    
    // Show the confirmation message
    var copiedText = document.getElementById("copied-text");
    copiedText.style.display = "inline-block";
    setTimeout(function() {
        copiedText.style.display = "none";
    }, 2000);
}

function del_alert(){
    let div_dismissable= document.getElementById("disp_msg");
    setTimeout(()=>{
        div_dismissable.setAttribute("display","hidden");
    },3000);
}