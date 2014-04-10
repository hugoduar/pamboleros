/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

                function Validacion(){
			
			var er_nombre = /^([a-z]|[A-Z]|�|�|�|�|�|�|�|\s|\.|-)+$/
			
			
			
			if(!er_nombre.test(document.forms["formulario"]["nombre"].value)) {   
				alert('Contenido del campo NOMBRE no v�lido.')  
				return false  
			}else{
				if(!er_nombre.test(document.forms["formulario"]["direccion"].value)){
					alert('Contenido del campo LUGAR DE PROCEDENCIA no valido.')
					return false
				}else{
					if(document.forms["formulario"]["equipo"].value == 0){
						alert('Selecciona una liga')
						return false
					}else{
						return true
					}
				}
			}
			
			
		}


                        
                        
			
			


