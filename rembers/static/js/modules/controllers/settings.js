const API_SET = {
    "get" : "/settings/api/",
    "save": "/settings/api/save",
    "get_name": "/settings/api/name/"
};


app.controller('Settings',
    function($scope, $window, Http){
        $scope.data = null;
        $scope.form = {};
        
        // ** LOADING SECTION SETTINGS **
        var init = function() {
            let endpoint = $window.location.host + API_SET.get;
            Http.sendGet(endpoint).then(function(response)
            {
                let data = response.data;
                $scope.data = _.transform(data, function(result, n){
                    n.label_name = n.name.charAt(0).toUpperCase() + n.name.slice(1);
                    n.label_name = n.label_name.replace(/_+/g, " ");

                    n.description = n.description.charAt(0).toUpperCase() + n.description.slice(1);

                    if (result[n.category] !== 'undefined' && Array.isArray(result[n.category])){
                        result[n.category].push(n);
                    } else {
                        result[n.category] = [n];
                    }
                }, {});

                $scope.form = _.transform(data, function(result, n){
                    result[n.name] = n.value;
                }, {});
            });
        }

        // ** SUBMIT UPDATE SETTINGS **
        var submit = function(){
            let endpoint = $window.location.host + API_SET.save;

            Http.send('post', endpoint, {"data": $scope.form}).then(function(response){
                console.log(response);
            });
        }

        $scope.init = function(){
            init();
        };

        $scope.save = function(){
            submit();
        }
    }
);