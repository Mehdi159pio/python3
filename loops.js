//boucle for classique

for (let i= 0; i < 10;i++){
    console.log("i = "+ i)};

// boucle à rebours
for (let i =10; i >0;i--){
     console.log("i=" + i )};

// boucle foreach ALTgr 7
let users = ['foo','bar','baz'];
// le mot clé "of permet de récupérer l'élémént"
for (let user of users){
    console.log(user)};
// le mot clé "in" permet de récupérer l'index de l'élément
for (let i in users){
     let user = users[1] 
    console.log(`i = ${1},user =$ {user}`)}; 
// méthode forEach (asynchrone)
    users.forEach(
       function(user, i ,list){
         console.log(`i=${i},user =${user}`)});

// syntaxe aletrnative
users.forEach(
     (user, i ,list){
      console.log(`i=${i},user =${user}`)};
          