const API_REM = {
    "api": "/reimburse/api",
};


app.controller("Reimburse",
    function($scope, $window, $routeParams, Http){
        $scope.data = null;
        $scope.settings = {
            "value": {}
        };
        $scope.form = {
            "date": null,
            "document_attach": null,
            "category": "transport",
            "amount": 0,
            "descriptioin": null
        };
        
        // ** LOADING SECTION SETTINGS **
        var init = function() {
            let endpoint = $window.location.host + API_SET.first + "?name=category";
            Http.sendGet(endpoint).then(function(response)
            {
                let data = response.data;

                $scope.settings = data;
                $scope.settings.value = _.transform($scope.settings.value.split(","), function(result, n){
                    n = n.trim();
                    result[n] =  n.charAt(0).toUpperCase() + n.slice(1).replace(/_+/g, " ");
                }, {});
                console.log($scope.settings);
            });
        }

        var detail = function(id) {
            let endpoint = $window.location.host + API_REM.api + '/' + id;
            console.log(endpoint);
            Http.sendGet(endpoint).then(function(response){
                let data = response.data;
                $scope.data = data;
            });
        }

        // ** SUBMIT UPDATE SETTINGS **
        var post_new = function(){
            let form = $scope.form;
            let endpoint = $window.location.host + API_REM.api;

            form.date = moment(form.date).format("YYYY-MM-DD");

            Http.upload("post", endpoint, {"data": form}).then(function(response){
                console.log(response);
            });
        }

        $scope.post_save = function(){
            post_new();
        }

        $scope.init = function(){
            init();
        }

        $scope.detail = function(){
            detail($routeParams.id);
        }
    }
);