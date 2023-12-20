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

let maxLevel = 3;

function pushNeighbours(poppedElement, j)
{
    if(neighboursArray[poppedElement] != null)
    {
        stack.push(...(neighboursArray[poppedElement]));
        j = j + neighboursArray[poppedElement].length;
    }
}

for(let i = 0; i < maxLevel; i++)
{
    let j = 0;
    while(stack.length !== 0)
    {
        let poppedElement = stack.pop();
        if(poppedElement === goalNode)
        {
            found = 1;
            break;
        }
        else if(j <= i && j < neighboursArray[poppedElement].length)
        {
            pushNeighbours(poppedElement, j);
        }
    }
    stack = ["A"];   //reset stack to contain only 'A' - the start node
}

if(found == 1)
{
    console.log("Goal Node found!");
}
else
{
    console.log("Goal Node not found!");
}