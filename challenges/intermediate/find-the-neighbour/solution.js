// https://jsfiddle.net/dianaberna/bmgypt78/

const regexCube = /-\||[A-Za-z]{1,6}/gm;

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

function check(nameList,query,queryName,position,i,j,z){
	if(query.indexOf(position) !== -1){
  	var index = nameList.indexOf(queryName);
    if(index == i || index == j || index == z){
    	return -1;
    }else{
    	var move;
    	switch(position){
      	case "left": move = -1; break; 
        case "right": move = 1; break;
        case "upstairs": move = 3; break;
        case "downstairs": move = 3; break;
      }
      return index+move;
    }
  }
}

function find_neighbour(cube, query) {
	var nameList = [];
  var queryName = query.split(":")[0];
  while((array = regexCube.exec(cube)) !== null){
    nameList.push(array[0])
  }

  var move = ["left", "right", "upstair", "downstair"];
  move.forEach(m =>{
    if(query.indexOf(m) !== -1){
      switch(m){
        case "left": e = check(nameList,query,queryName,"left",0,3,6); break;
        case "right": e = check(nameList,query,queryName,"right",2,5,8); break;
        case "upstairs": e = check(nameList,query,queryName,"right",0,1,2); break;
        case "downstairs": e = check(nameList,query,queryName,"right",6,7,8); break;
      }
    }
  });
	
  if(e==-1){
    console.log("nobody");
  }else{
    console.log(nameList[e]);
  }

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
