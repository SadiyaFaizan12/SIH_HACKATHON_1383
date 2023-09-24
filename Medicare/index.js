const express=require("express")
const bodyParser=require("body-parser")
const mongoose=require("mongoose")

const app=express()

app.use(bodyParser.urlencoded({extended:true}));

mongoose.connect('mongodb+srv://aryamanabhi:DarKnight594@clusters.5t8gaqw.mongodb.net/MediCare',{useNewUrlParser:true},{useUnifiedTopology:true});

const notes={
    username: String,
    password: String,
    phone_no: String
}
const Note=mongoose.model("Login",notes);

var db=mongoose.connection;
db.on('error',()=>console.log("Error"));
db.once('open',()=>console.log("Connected"))

app.get("/",function(req,res){
    res.sendFile(__dirname+ "/index.html");
})

app.post("/Login",function(req,res){
    let Notes= new Note({
        username: req.body.username,
        password: req.body.password,
        phno: req.body.phno
    })
    Notes.save();
    res.redirect("/");
})

app.listen(5000,function(){
    console.log("Listening on PORT 5000");
})