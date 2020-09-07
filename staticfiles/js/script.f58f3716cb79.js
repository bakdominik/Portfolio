let theme = localStorage.getItem('theme')

if(theme == null){
    setTheme('style')
} else {
    setTheme(theme)
}


let themeDots = document.getElementsByClassName('theme-dot')

for (var i=0; themeDots.length > i; i++){
    themeDots[i].addEventListener('click', function(){
        let mode=this.dataset.mode
        setTheme(mode)
    })
}
function setTheme(mode) {
    document.getElementById('theme-style').href= static + mode + '.css'

    localStorage.setItem('theme', mode)

}

