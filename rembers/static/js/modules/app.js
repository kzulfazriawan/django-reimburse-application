// ____main module angularjs____
var app = angular.module('App', ['ngFileUpload']);

app.filter('range', function() {
    return function(iterate, max) {
        max = parseInt(max);
        
        for (var i = 0; i < max; i++) {
            iterate.push(i);
        }

        return iterate;
    };
});

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[$');
    $interpolateProvider.endSymbol('$]');
});