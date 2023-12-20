let nodes = 7;

let graph = [
        //S, B, C, D, F, E, G
    /*S*/[0, 4, 3, 0, 0, 0, 0],   //graph value gives actual cost
    /*B*/[0, 0, 0, 0, 5, 12, 0],
    /*C*/[0, 0, 0, 7, 0, 10, 0],
    /*D*/[0, 0, 0, 0, 0, 2, 0],
    /*F*/[0, 0, 0, 0, 0, 0, 16],
    /*E*/[0, 0, 0, 0, 0, 0, 5],
    /*G*/[0, 0, 0, 0, 0, 0, 0]
];

let heuristicValueArray = [
    /*S*/ 14,
    /*B*/ 12,
    /*C*/ 11,
    /*D*/ 6,
    /*F*/ 11,
    /*E*/ 4,
    /*G*/ 0
];

let startNode = 0;
let goalNode = 6;
let currentNode = startNode;

let path = [];
let optimalNode;
let distanceFromStartNode = 0;

for(let i = 0; i < nodes; i++)
{
    let min = Infinity;
    for(let j = 0; j < nodes; j++)
    {
        if(graph[currentNode][j] != 0)
        {
            if(distanceFromStartNode + graph[currentNode][j] + heuristicValueArray[j] < min)   //distance from start node to previous node + previous node to current node + heuristic of current node
            {
                min = distanceFromStartNode + graph[currentNode][j] + heuristicValueArray[j];
                optimalNode = j;
            }
        }
    }
    distanceFromStartNode = distanceFromStartNode + graph[currentNode][optimalNode];   //distance from start node to previous node + distance from previous node to current optimal node
    path.push({ optimalNode: optimalNode, distanceFromStartNode: distanceFromStartNode });
    currentNode = optimalNode;
    if(currentNode == goalNode)   //break from the loop if the goal node is reached
    {
        break;
    }
}

//print final path
for (let i = 0; i < path.length; i++) {
    console.log(`Step ${i + 1}: Optimal Node - ${path[i].optimalNode}, Distance - ${path[i].distanceFromStartNode}`);
}