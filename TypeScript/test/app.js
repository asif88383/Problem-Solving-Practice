var App = /** @class */ (function () {
    function App() {
    }
    App.prototype.test = function () {
        console.log("Hello World");
        this.test2();
    };
    App.prototype.test2 = function () {
        document.write("Hello World");
    };
    return App;
}());
var app = new App();
app.test();
