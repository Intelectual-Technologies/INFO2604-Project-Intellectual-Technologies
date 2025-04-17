
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


    function favorite(name){
      const icon = document.getElementById('name');

      let html = '';

      html = `
        <a ><ion-icon  name="star"></ion-icon></a>
      `;

      console.log(icon.innerHTML)
      
      icon.innerHTML = html;

    }

    function unfavorite(){
      const icon = document.getElementById('icons');

      icon.classList.remove('active');
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