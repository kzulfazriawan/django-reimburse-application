const API_REM = {
    "save": "/reimburse/api/save"
};


app.controller('Reimburse',
    function($scope, $window, Http){
        $scope.data = null;
        $scope.form = {};
        
        // ** SUBMIT UPDATE SETTINGS **
        var post_new = function(){
            let form = $scope.form;
            let endpoint = $window.location.host + API_REM.save;

            form.date = moment(form.date).format("YYYY-MM-DD");
            console.log(form);

            Http.upload('post', endpoint, {"data": form}).then(function(response){
                console.log(response);
            });
        }

        $scope.post_save = function(){
            post_new();
        }
    }
);