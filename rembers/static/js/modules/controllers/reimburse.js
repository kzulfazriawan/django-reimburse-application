const API_REM = {
    "save": "/reimburse/api/save"
};


app.controller("Reimburse",
    function($scope, $window, Http){
        $scope.data = null;
        $scope.settings = {
            "value": {}
        };
        $scope.form = {
            "date": null,
            "document_attach": null,
            "category": "transport",
            "descriptioin": null
        };
        
        // ** LOADING SECTION SETTINGS **
        var init = function() {
            let endpoint = $window.location.host + API_SET.get_name + "?name=category";
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

        // ** SUBMIT UPDATE SETTINGS **
        var post_new = function(){
            let form = $scope.form;
            let endpoint = $window.location.host + API_REM.save;

            form.date = moment(form.date).format("YYYY-MM-DD");
            console.log(form);

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
    }
);