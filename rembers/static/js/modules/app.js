// ____main module angularjs____
var app = angular.module('App', ['ngRoute', 'ngFileUpload']);

app.filter('range', function() {
    return function(iterate, max) {
        max = parseInt(max);
        
        for (var i = 0; i < max; i++) {
            iterate.push(i);
        }

        return iterate;
    };
});

app.config(function($interpolateProvider, $routeProvider) {
    $interpolateProvider.startSymbol('[$');
    $interpolateProvider.endSymbol('$]');

    $routeProvider.when("/settings", {
        "templateUrl": "/settings",
        "controller" : "Settings"
    })
    // reimburse route url
    .when("/reimburse/all", {
        "templateUrl": "/reimburse/all",
        "controller" : "Reimburse"
    })
    .when("/reimburse/post", {
        "templateUrl": "/reimburse/post",
        "controller" : "Reimburse"
    })
    .when("/reimburse/detail/:id", {
        "templateUrl": "/reimburse/detail",
        "controller" : "Reimburse"
    });
});