let neighboursArray = {
    A: ["B", "C", "D"],
    B: ["E", "F"],
    C: ["G", "H"],
    D: ["I"],
    E: null,
    F: null,
    G: null,
    H: null,
    I: null
};

let queue = ["A"];

let goalNode = "G";

let found = 0;

function retracePath(startNode, goalNode, neighboursArray)
{
    let targetValue = goalNode;   //initial target value
    let path = [goalNode];
    let currentKey = null;
    while(currentKey != startNode)   //since we only want to check upto the first property i.e. A
    {
        for(const key in neighboursArray)
        {
            if(neighboursArray.hasOwnProperty(key) && neighboursArray[key].includes(targetValue))
            {
                path.unshift(key);
                currentKey = key;
                targetValue = key;
                break;   //break out of the inner (for) loop
            }
        }
    }
    return path;
}

function pushNeighbours(currentNode)
{
    if(neighboursArray[currentNode] != null)
    {
        queue.push(...(neighboursArray[currentNode]));
    }
}

while(queue.length !== 0)
{
    if(queue[0] == goalNode)
    {
        found = 1;
        break;
    }
    else
    {
        pushNeighbours(queue[0]);
        queue.shift();   //remove first element
    }
}

if(found === 1)
{
    console.log("Goal Node found!");
    let path = retracePath("A", goalNode, neighboursArray);
    console.log(path);
}
else
{
    console.log("Goal Node not found!");
}