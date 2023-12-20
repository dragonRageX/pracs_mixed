const fs = require("fs");

fs.readFile("./data.json", "utf-8", (err, data) => {
    if(err)
    {
        console.log("Error reading file: " + err);
        return;
    }
    else
    {
        const jsonData = JSON.parse(data);
        console.log(jsonData);
        jsonData.map((object) => {
            console.log(object.name);
        });
    }
});