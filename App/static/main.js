
// async function getUserData(){
//     const response = await fetch('/api/users');
//     return response.json();
// }

// function loadTable(users){
//     const table = document.querySelector('#result');
//     for(let user of users){
//         table.innerHTML += `<tr>
//             <td>${user.id}</td>
//             <td>${user.username}</td>
//         </tr>`;
//     }
// }

// async function main(){
//     const users = await getUserData();
//     loadTable(users);
// }

// main();

// NAV CODE
function openNav() {
    document.getElementById("mySidebar").style.width = "200px";
    document.getElementById("main").style.marginLeft = "200px";
    document.getElementById("button").style.scale = "0";
  }
  
  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.getElementById("button").style.scale = "1";
  }

//END NAV CODE


    function favorite(recipeId, recipeName) {
      fetch(`/add-user-recipe/${recipeId}`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          }
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
            const icon = document.getElementById(`${recipeName}`);

            let html = '';
    
            html = `
              <a onclick="unfavorite(${recipeId}, '${recipeName}')"><ion-icon  name="star"></ion-icon></a>
            `;
    
            icon.innerHTML = html;
          } else {
              console.error(data.message);
          }
      })
      .catch(error => console.error('Error:', error));
    }

    function unfavorite(recipeId, recipeName) {
      fetch(`/remove-user-recipe/${recipeId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
            const icon = document.getElementById(`${recipeName}`);

            let html = '';
    
            html = `
              <a onclick="favorite(${recipeId}, '${recipeName}')"><ion-icon  name="star-outline"></ion-icon></a>
            `;
                
            icon.innerHTML = html;
          } else {
              console.error(data.message);
          }
      })
      .catch(error => console.error('Error:', error));
    }


    // function searchCategories(){
    //   let searchKey = document.querySelector('#searchKey').value;

    //   let results = [];

    //   for(let rec of cats){
    //     let searchText = rec.strCategory.toUpperCase();
    //     searchKey = searchKey.toUpperCase();

    //     if ( searchText.search(searchKey) !== -1 ){
    //       results.push(rec);
    //     }
    //     renderCategories(results);
    //   }
    // }

    // function searchCategoriesOut(){
    //   let searchKey = document.querySelector('#searchKey').value;

    //   let results = [];

    //   for(let rec of cats){
    //     let searchText = rec.strCategory.toUpperCase();
    //     searchKey = searchKey.toUpperCase();

    //     if ( searchText.search(searchKey) !== -1 ){
    //       results.push(rec);
    //     }
    //     renderCategoriesOut(results);
    //   }
    // }

    // function searchCatRecipes(category){
    //   let searchKey = document.querySelector('#searchKey').value;
    //   let results = [];

    //   for(let rec of state){
    //     let searchText = rec.strMeal.toUpperCase();
    //     searchKey = searchKey.toUpperCase();
        
    //     if ( searchText.search(searchKey) !== -1 ){
    //       if(rec.strCategory === category){
    //         results.push(rec);
    //       }
    //     }
    //     renderAllRecipes(results);
    //   }
    // }

    // async function searchAllRecipes(){
    //   let searchKey = document.querySelector('#searchKey').value;

    //   let results = [];
      
    //   for(let rec of state){

    //     let searchText = rec.strMeal.toUpperCase();
    //     searchKey = searchKey.toUpperCase();

    //     if ( searchText.search(searchKey) !== -1 ){
    //       results.push(rec);
    //     }

    //     renderAllRecipes(results);
    //   }
    // }

    // function catBackBtn (){
    //   renderCategories(cats);
    // }



    // function AllRecipes(){
    //   renderAllRecipes(state);
    // }