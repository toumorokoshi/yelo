var yeloApp = angular.module('yeloApp', []);

yeloApp.controller('IndexCtrl', function($scope, $http) {
    $scope.title = 'yelo';

    $scope.loadElos = function () {
        $http.get('/api/elos').success(function(data) {
            $scope.players = data.results;
        });
    };

    $scope.loadMatches = function () {
        $http.get('/api/matches').success(function(data) {
            $scope.matches = data.results;
        });
    };

    $scope.formatDate = function (dt) {
        return dt.getMonth() + '/' + dt.getDate() + '/' + dt.getFullYear() +
            getHours() + ':' + getMinutes();
    };

    $scope.submitMatch = function () {
        $http.post('/record_match', {
            'winner': $scope.recordMatchWinner,
            'loser': $scope.recordMatchLoser
        }).success(function (data) {
            $scope.recordMatchWinner = null;
            $scope.recordMatchLoser = null;
            $scope.loadElos();
            $scope.loadMatches();
            $('#record-match').toggleClass('collapsed');
        }).error(function (data) {
            $scope.recordMatchError = data.detail;
        });
    };

    $scope.loadElos();
    $scope.loadMatches();
});
