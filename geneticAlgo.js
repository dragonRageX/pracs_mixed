let parentChromosomes = 6;
let parentChromosomesGenes = 8;

let populationArray = [];
let fitnessScores = [];

for(let i = 0; i < parentChromosomes; i++)
{
    populationArray[i] = [];
    let score = 0;
    for(let j = 0; j < parentChromosomesGenes; j++)
    {
        populationArray[i][j] = Math.floor(Math.random() * 2);
        score = score + populationArray[i][j];
    }
    fitnessScores[i] = score;
}

console.log(populationArray);
console.log(fitnessScores);

function bubbleSort(fitnessScores, populationArray)
{
    for(let i = 0; i < fitnessScores.length - 1; i++)
    {
        for(let j = 0; j < fitnessScores.length - i - 1; j++)
        {
            if(fitnessScores[j + 1] < fitnessScores[j])
            {
                let swap = fitnessScores[j + 1];
                fitnessScores[j + 1] = fitnessScores[j];
                fitnessScores[j] = swap;

                swap = populationArray[j + 1];
                populationArray[j + 1] = populationArray[j];
                populationArray[j] = swap;
            }
        }
    }
}
bubbleSort(fitnessScores, populationArray);

console.log("Sorted Population Array: " + JSON.stringify(populationArray));
console.log("Sorted Fitness Scores Array: " + JSON.stringify(fitnessScores));

let childrenArray = [];
let crossoverPoint = 5;   //position/index in a chromosome from where crossover occurs

for(let i = 0; i < parentChromosomes; i = i + 2)
{
    let value = [];
    for(let j = 0; j < parentChromosomesGenes; j++)
    {
        if(j < 5)
        {
            value.push(populationArray[i][j]);
        }
        else
        {
            value.push(populationArray[i + 1][j]);
        }
    }
    childrenArray.push(value);
}

console.log("Children Array: " + JSON.stringify(childrenArray));   //no.of children = (no.of parents / 2) as 2 parents are involved in the creation of a single child