
var app = angular.module("app",["ngResource"]);
//Definir el controlador
app.controller("controlador",function($scope,datos_cuenta,datos_cliente,datos_transaccion){
	$scope.mensaje ="saludos";
	$scope.lista_cliente= datos_cliente.get();
	$scope.lista_cuenta= datos_cuenta.get();
	$scope.lista_transaccion= datos_transaccion.get();


	/*$scope.validar = function(a){
		var dato = $scope.cedula;
		var mensaje="hola";

		for(var i=0 ; i< $scope.lista_alumnos.length; i++){
			if ( angular.equals(dato, $scope.lista_alumnos[i].cedula)) {
				window.location.href="datos.html";
			}
			else{
				mensaje="No se valido la cedula";
			}
		}	
		return mensaje;
	}*/

});
 //Definir el factori que retorne datos del webservice
app.factory("datos_cliente",['$resource',function($resource){
 	return $resource('http://127.0.0.1:8000/api/cliente/',{},{get:{method:'GET',pararms:{}, isArray:true}});
 	}
 ])
 
 app.factory("datos_cuenta",['$resource',function($resource){
 	return $resource('http://127.0.0.1:8000/api/cuenta/',{},{get:{method:'GET',pararms:{}, isArray:true}});
 	}
 ])

 app.factory("datos_transaccion",['$resource',function($resource){
 	return $resource('http://127.0.0.1:8000/api/transaccion/',{},{get:{method:'GET',pararms:{}, isArray:true}});
 	}
 ])
 