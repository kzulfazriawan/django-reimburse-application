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
    })

    .when("/accounts/update-profile", {
        "templateUrl": "/accounts/update-profile",
        "controller" : "Accounts"
    })
});

app.controller('Global',
    function($scope, $window, $timeout, Http){
        var init_account = function(){
            let endpoint = $window.location.host + API_AUTH.post;
            Http.send("post", endpoint, {"data": $scope.form}).then(function success(response)
            {
                let data = response.data;
                $scope.alert = {
                    "status": "success", "message": data.message
                };
                $scope.alert.message += ", redirect in 3 seconds";
                $timeout(function(){
                    $window.location.href = '/';
                }, 3000);
            }, function error(response){
                if (response.data.message !== 'undefined'){
                    $scope.alert = {"status": "danger", "message": response.data.message};
                } else {
                    $scope.alert = {"status": "danger", "message": "Something went wrong"};
                }
            });
        }
    }
);
