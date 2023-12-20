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

let stack = ["A"];

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

function pushNeighbours(poppedElement)
{
    if(neighboursArray[poppedElement] != null)
    {
        stack.push(...(neighboursArray[poppedElement]));
    }
}

while(stack.length !== 0)
{
    let poppedElement = stack.pop();
    if(poppedElement === goalNode)   //check the popped element, whether it is the goal node or not
    {
        found = 1;
        break;
    }
    else
    {
        pushNeighbours(poppedElement);
    }
}

if(found == 1)
{
    console.log("Goal Node found!");
    let path = retracePath("A", goalNode, neighboursArray);   //we can also make the retracePath() by keeping a track of the visited and unvisited nodes
    console.log(path);
}
else
{
    console.log("Goal Node not found!");
}