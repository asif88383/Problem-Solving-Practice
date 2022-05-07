class App{
    test(){
        console.log("Hello World");
        this.test2();
    }

    test2(){
        document.write("Hello World");
    }
} 

let app = new App();
app.test();