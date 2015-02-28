var yeloApp = angular.module('yeloApp', []);

yeloApp.controller('IndexCtrl', function($scope, $http) {
    $scope.title = 'yelo';

    $scope.loadElos = function () {
        $http.get('/api/elos?ordering=-elo').success(function(data) {
            $scope.players = data.results;
        });
    };

    $scope.submitMatch = function () {
        $http.post('/record_match', {
            'winner': $scope.recordMatchWinner,
            'loser': $scope.recordMatchLoser
        }).success(function (data) {
            $scope.loadElos();
            $scope.recordMatchWinner = null;
            $scope.recordMatchLoser = null;
            $('#record-match').toggleClass('collapsed');
        }).error(function (data) {
            $scope.recordMatchError = data.detail;
        });
    };

    $scope.loadElos();
});
