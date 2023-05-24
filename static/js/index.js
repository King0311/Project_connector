function bottom(){
    window.scrollTo({
        top:10000,
        behavior:"smooth"
    });
}
function about(){
    window.scrollTo({
        top:400,
        behavior:"smooth"
    });
}
function upper(){
    window.scrollTo({
        top:-1000000,
        behavior:"smooth"
    });
}

window.addEventListener("scroll",()=>{
    const p = window.scrollY;
    console.log(p)
    if (p>=250){
        document.body.classList.add("dikho2");
    }
});