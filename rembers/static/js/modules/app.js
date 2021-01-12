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
    .when("/reimburse", {
        "templateUrl": "/reimburse",
        "controller" : "Reimburse"
    })
    .when("/reimburse/create", {
        "templateUrl": "/reimburse/create",
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
    function($scope, $window, $timeout, $rootScope, $location, Http){
        $scope.init = function(){
            let endpoint = $window.location.host + API_ACC.api;
            Http.sendGet(endpoint).then(function success(response)
            {
                let data = response.data;
                $rootScope.account = data;

            }, function error(response){
                switch(response.status){
                    case 404:
                        $scope.alert = {"status": "danger", "message": "Profile is empty!, Please create it"};
                        $timeout(function(){
                            $location.path('/accounts/update-profile');
                        }, 3000);        
                        break;
                    default:
                        $scope.alert = {"status": "danger", "message": response.data.message};

                        $timeout(function(){
                            $window.location.href = '/accounts/login';
                        }, 3000);
                        break;
                }
            });
        }

    }
);
