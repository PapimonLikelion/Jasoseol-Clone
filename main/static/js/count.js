const targetForm = document.querySelector('.jss_content_js')
let wordcount = document.querySelector('.wordcount')
targetForm.addEventListener('keyup', () => {
    wordcount.innerHTML = targetForm.value.length
})