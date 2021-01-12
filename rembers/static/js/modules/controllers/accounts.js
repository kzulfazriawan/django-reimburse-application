const API_ACC = {
    "api": "/accounts/api/accounts"
};


app.controller("Accounts",
    function($scope, $window, Http){
        $scope.data = null;
        $scope.settings = {
            "value": {}
        };

        $scope.form = {
            "name": null,
            "phone_number": null,
            "bank_name": null,
            "bank_account": null,
            "descriptioin": null
        };
        
        // ** LOADING SECTION SETTINGS **
        var initSetting = function() {
            let endpoint = $window.location.host + API_SET.get_name + "?name=bank_available";
            Http.sendGet(endpoint).then(function(response)
            {
                let data = response.data;

                $scope.settings = data;
                $scope.settings.value = _.transform($scope.settings.value.split(","), function(result, n){
                    n = n.trim();
                    result[n] =  n.toUpperCase();
                }, {});
            });
        }

        var init = function(){
            let endpoint = $window.location.host + API_ACC.api;
            Http.sendGet(endpoint).then(function(response)
            {
                let data = response.data;
                $scope.form = data;
            });
        }

        // ** SUBMIT UPDATE SETTINGS **
        var post_update = function(){
            let form = $scope.form;
            let endpoint = $window.location.host + API_ACC.api;

            Http.upload("post", endpoint, {"data": form}).then(function(response){
                console.log(response);
            });
        }

        $scope.post_save = function(){
            post_update();
        }

        $scope.init = function(){
            initSetting();
            init();

        }
    }
);