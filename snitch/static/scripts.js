let shop = document.getElementById("dropdownHoverButton")
let shopMenu = document.getElementById("dropdownHover")
let ishidden = true

shop.addEventListener("click", ()=>{
    if (ishidden){
        shopMenu.classList.remove("hidden")
        ishidden = false
    } else {
        shopMenu.classList.add("hidden")
        ishidden=true
    }
})

const msg = document.getElementById("msg");

const hideMsg = () => {
//    msg.classList.add("hidden");
      msg.remove();
};

window.onload(setInterval(hideMsg, 5000))