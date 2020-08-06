(function (){
  'use strict';
  angular.module("myFirstApp",[])
  .controller("MyFirstController",function ($scope){
    $scope.name="Vipul";
    $scope.sayHello=function(){
      return "Hello"
	};
	

  });
})();
