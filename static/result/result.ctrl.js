resultApp.controller("resultCtrl", ["$http", "ResultService", function($http, ResultService) {
	var self = this;
	self.ice = {'url': null,
			'username': null,
			'password': null};
	
	self.results = function() {
		return ResultService.results;
	};
	
	self.result = function() {
		return ResultService.result;
	};
	
	self.sbol = function() {
		return ResultService.sbol;
	};

	self.saveResults = function() {
		return ResultService.saveResults(self.ice);
	};
}]);