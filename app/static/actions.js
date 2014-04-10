
var ubicacion = new Array();
function onegai(){
    
    alert("funciona");
}

function showVid(){
    document.getElementById('images').style.display="none";
    document.getElementById('docs').style.display="none";
    document.getElementById('videos').style.display="block";
}

function showImg(){
    document.getElementById('videos').style.display="none";
    document.getElementById('docs').style.display="none";
    document.getElementById('images').style.display="block";
}

function showDoc(){
    document.getElementById('videos').style.display="none";
    document.getElementById('images').style.display="none";
    document.getElementById('docs').style.display="block";
}

function setImg(ubicacion){   
    document.getElementById('mainSet').innerHTML = "<img src="+ubicacion+" id='imgFile'>";
}

function setVid(ubicacion){
    /*document.getElementById('mainSet').innerHTML = '<video id="plaier" controls="controls">  <source src="'+ubicacion+'.mp4" type="video/mp4">  <source src="'+ubicacion+'.ogg" type="video/ogg">  <source src="'+ubicacion+'.webm" type="video/webm">  <object data="'+ubicacion+'.mp4" width="320" height="240">    <embed src="'+ubicacion+'.swf" width="320" height="240">  </object> </video>';*/
    document.getElementById('mainSet').innerHTML = '<video id="plaier" controls="controls">  <source src="'+ubicacion+'" type="video/mp4">  <source src="'+ubicacion+'" type="video/ogg">  <source src="'+ubicacion+'" type="video/webm">  <object data="'+ubicacion+'" width="320" height="240">    <embed src="'+ubicacion+'" width="320" height="240">  </object> </video>';
}

function setDoc(ubicacion){
    document.getElementById('mainSet').innerHTML = "<div id='ryder'><source src='"+ubicacion+"''></div>";
}

//----------------------------------------------------

function createEvnt(){
    var div='<div id="editEv"><form action="servletAltaEvento" method="post">  Id Evento: <input type="text" name="id" placeholder="Clave que solo tu sabras" required="required"/> <br><br> Nombre Evento: <input type="text" name="nom_evento" required="required"/><br><br>       <label>Direccion Evento</label><br>        Calle:<input type="text" name="calle" required="required"/><br>                       Colonia:<input type="text" name="colonia" required="required"/><br>                   Delegacion:<select name="delegacion"> <option>Seleccione una opcion</option> <option>Alvaro Obregon</option> <option>Azcapotzalco</option><option>Benito Juarez</option><option>Coyoacan</option><option>Cuajimalpa</option><option>Cuauhtemoc</option><option>Gustavo A. Madero</option><option>Iztacalco</option><option>Iztapalapa</option><option>Magdalena Contreras</option><option>Miguel Hidalgo</option><option>Milpa Alta</option><option>Tlahuac</option><option>Tlalpan</option><option>Venustiano Carranza</option><option>Xochimilco</option> </select><br>             <label>Fecha Evento</label><br>                        Fecha Evento<input type="text" name="fecha_evento" required="required" placeholder="DD-MM-AA"/><br>          Descripcion Evento:<br> <textarea placeholder="Ingrese una breve descripcion del evento" name="descripcion" required="required"></textarea><br>                      <input type="submit" value="Crear Evento" id="boton">                  </form></div>';
    document.getElementById('mainSet').innerHTML = div;
}
function delEvnt(){
    var div='<div id="editEv"> <form action="servletCancelatEvento" method="post"> Ingrese el id del evento que desea eliminar:<br><input type="text" name="ev_el" required="required"/><br> <input type="submit" value="eliminar"/> </form></div>';
    document.getElementById('mainSet').innerHTML = div;
    
}
function checkEvnt(){
    //var divChec='<%             List<eventos> list = null;            Conection myConnection=null; myConnection=new Conection(); myConnection.setDbname("street"); myConnection.setDriver("com.mysql.jdbc.Driver"); myConnection.setPassword("n0m3l0"); myConnection.setUrl("jdbc:mysql://localhost/street"); myConnection.setUser("root"); myConnection.open();                                 list=myConnection.selectAll();%>                        <form action="mostrareventos" method="POST">               <select name="evento">             <%                if(list!=null) {                    for(eventos usr:list) {  %>                <option><%=usr.getNombre_evento()%></option>            <%  }  %>              </select>               <input type="submit" value="Ver datos Evento"/>            </form>               <% myConnection.close(); }else{               %>               <option>No hay Eventos</option>            </select>            </form>            <%  }  %>';
    var divCheck="";
    document.getElementById('lowerLeft').innerHTML = divChec;
}

//----------------------------------------------------


