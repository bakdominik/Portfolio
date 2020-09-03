let theme = localStorage.getItem('theme')

if(theme == null){
    setTheme('light')
} else {
    setTheme(theme)
}


let themeDots = document.getElementsByClassName('theme-dot')

for (var i=0; themeDots.length > i; i++){
    themeDots[i].addEventListener('click', function(){
        let mode=this.dataset.mode
        console.log(mode)
        setTheme(mode)
    })
}
function setTheme(mode) {
    if (mode != 'light'){
        document.getElementById('theme-style').href= static + mode + '.css'
    } else {
        document.getElementById('theme-style').href=''
    }

    localStorage.setItem('theme', mode)

}
