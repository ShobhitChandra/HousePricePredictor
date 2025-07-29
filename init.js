const express = require("express");
const app = express();
const path = require("path");
const ejsMate = require("ejs-mate");

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.engine("ejs", ejsMate);
app.use(express.static(path.join(__dirname, "public")));

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Home page with default message
app.get("/", (req, res) => {
    res.render("home/main", { prediction: null });
});

const { spawn } = require('child_process');

app.post("/predict", (req, res) => {
    const { username, area, bedrooms, floors, age } = req.body;
    console.log("Received inputs:", area, bedrooms, floors, age);

    // Spawn Python process with absolute path
    const pythonProcess = spawn('/Library/Frameworks/Python.framework/Versions/3.13/bin/python3', [
        path.join(__dirname, 'multifeaturelinearreg.py'),
        area,
        bedrooms,
        floors,
        age
    ]);

    let output = '';

    // Capture Python stdout
    pythonProcess.stdout.on('data', (data) => {
        output += data.toString();
    });

    // Capture Python stderr
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python error: ${data}`);
    });

    // When Python process finishes
    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
        if (code === 0) {
            console.log("Predicted Price:", output.trim());
            res.render("home/home", { prediction: output.trim(), 
                username,
                area,
                bedrooms,
                floors,
                age
            });
        } else {
            res.status(500).send("Prediction failed");
        }
    });
});

app.get("/main", (req, res) => {
    res.render("home/main");  
});


app.listen(8080, () => {
    console.log("App is listening on port 8080.");
});
