const $loadingScreen = document.querySelector('.loading-screen')

window.addEventListener('load', () => {
	$loadingScreen.classList.remove('is-loading')
})

window.addEventListener('pageshow', () => {
	$loadingScreen.classList.remove('is-loading')
})

window.addEventListener('beforeunload', () => {
	$loadingScreen.classList.add('is-loading')
})
