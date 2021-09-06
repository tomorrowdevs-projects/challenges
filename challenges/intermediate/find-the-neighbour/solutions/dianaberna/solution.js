// https://jsfiddle.net/dianaberna/bmgypt78/
const regexCube = /-\||[a-zA-Z]+/gm;

const cubeStr = `
   ______________________
  /_____________________/|
 /_____________________/ |
 |      |      |      |  |
 | Tom  |Jerry | John | /|
 |______|______|______|/ |
 |      |      |      |  |
 | Mike |Peter |Alice | /|
 |______|______|______|/ |
 |      |      |      |  |
 |  Bob | Bill | Wang | /
 |______|______|______|/
`;


function find_neighbour(cube, query) {
  var nameList = [];
  var queryName = query.split(":")[0];
  while((array = regexCube.exec(cube)) !== null){
    	nameList.push(array[0])
  }
  
  let arrayMovement = [
    {key: "left", move: -1, nope: [0,3,6]},
    {key: "right", move: 1, nope: [2,5,8]},
    {key: "upstairs", move: -3, nope: [0,1,2]},
    {key: "downstairs", move: 3, nope: [6,7,8]}
  ];
  
  arrayMovement.forEach( obj => {
  	if(query.indexOf(obj.key) !== -1){
        var index = nameList.indexOf(queryName);
        if(index < 7 && index > 1){
        	console.log(nameList[index+obj.move]); 
        }else{
          	console.log("nobody");
        }
    }
  })

}

// Test cases

find_neighbour(cubeStr, "Peter: My left neighbor is (?)") === "Mike"
find_neighbour(cubeStr, "Bob: My upstairs neighbor is (?)") === "Mike"
find_neighbour(cubeStr, "Tom: My right neighbor is (?)") === "Jerry"
find_neighbour(cubeStr, "Jerry: My downstairs neighbor is (?)") === "Peter"

// When there is no neighbour, return "nobody"

find_neighbour(cubeStr, "Wang: My right neighbor is (?)") === "nobody"
find_neighbour(cubeStr, "Wang: My downstairs neighbor is (?)") === "nobody"
find_neighbour(cubeStr, "Tom: My upstairs neighbor is (?)") === "nobody"
