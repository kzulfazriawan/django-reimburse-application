const API_AUTH = {
    "post": "/accounts/api/login"
}

app.controller('Auth',
    function($scope, $window, $timeout, Http){
        $scope.alert  = null;
        $scope.form   = {};
        $scope.action = {
            "submit": true
        };

        var post_login = function(){
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
        };

        $scope.post_submit = function(){
            post_login();
        }
    }
);