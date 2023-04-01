//Get search form and page links
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

if(searchForm){
  for(let i =0; i < pageLinks.length; i++) {
    pageLinks[i].addEventListener('click', function (e) {
      e.preventDefault()
      
      //get the data attribute
      let page = this.dataset.page
      
      //add hidden search input to form
      searchForm.innerHTML += `<input value=${page} name="page" hidden />`
      
      //subimt form
      searchForm.submit()
    })
  }
}