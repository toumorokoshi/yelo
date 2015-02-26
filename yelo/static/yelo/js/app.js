var yeloApp = angular.module('yeloApp', []);

yeloApp.controller('IndexCtrl', function($scope, $http) {
    $http.get('/api/elos').success(function(data) {
        $scope.players = data.results;
    });
});
