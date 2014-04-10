/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

// Constructor
function listaDinamica( frm, name, data ) {
  this.frm = frm;
  this.name = name;
  this.data = data;
  this.size = 1;
  this.multiple = "";
  this.doc = document;
  this.onchange = "";
  this.objeto = null;
}


// Push
function pushLista( valor ) {
  if ( valor == null ) return null;
  if( this.search( valor ) < 0 )
    this.data[this.data.length] = valor;
}
listaDinamica.prototype.push = pushLista;


// Pop
function popLista( valor ) {
  if ( valor == null ) valor = this.value();
  var i = this.search( valor );
  if ( i == -1 ) return null;
  if( i > -1 ) {
    for( var j = i+1; j < this.data.length; j++ )
      this.data[j-1] = this.data[j];
    this.data.length--;
    return valor;
  }
  return null;
}
listaDinamica.prototype.pop = popLista;


// Length
function lengthLista() {
  return this.data.length;
}
listaDinamica.prototype.length = lengthLista;


// Search
function searchLista( valor ) {
  for( var i = 0; i < this.data.length; i++ )
    if( this.data[i] == valor )
      return i;
  return -1;
}
listaDinamica.prototype.search = searchLista;


// Sort
function sortLista() {
  if( this.data.length == 0 ) return;
  for( var i = 0; i < this.data.length; i++ ) {
    var min = i;
    for( var j=i+1; j < this.data.length; j++ )
      if( this.data < this.data )
        min = j;
    this.swap( i, min );
  }
}
listaDinamica.prototype.sort = sortLista;


// Swap
function swapLista( i, j ) {
  if( i == j ) return;
  var aux = this.data[i];
  this.data[i] = this.data[j];
  this.data[j] = aux;
}
listaDinamica.prototype.swap = swapLista;


// toString
function toStringLista( sep ) {
  if( sep == null ) sep = "_";
  if( this.data.length <= 0 )
    return "";
  var res = this.data[0];
  for( var i=1; i < this.data.length; i++ )
    res += sep+this.data[i];
  return res;
}
listaDinamica.prototype.toString = toStringLista;


// Write
function writeLista() {
  var buffer = '';
  buffer += '<!--INICIO LISTA DINAMICA "'+this.name+'"-->';
  var onchange = this.onchange ? 'onchange="'+this.onchange+'"' : '';
  buffer += '<select name="'+this.name+'" '+this.multiple+' size="'+this.size+'" '+onchange+'>';
  buffer += '<option>--------------------------------------------------</option>';
  for( var i = 0; i < this.data.length; i++ )
    buffer += '<option>'+this.data[i]+'</option>';
  buffer += '</select>';
  buffer += '<!--FIN LISTA DINAMICA "'+this.name+'"-->';
  this.doc.writeln( buffer );
  this.objeto = this.frm.elements[this.name];
  this.objeto.options[0] = null;
}
listaDinamica.prototype.write = writeLista;


// Refresh
function refreshLista() {
  while( this.objeto.options.length > 0 )
    this.objeto.options[0] = null;
  for( var i = 0; i < this.data.length; i++ )
    this.objeto.options[i] = new Option( this.data[i], this.data[i] );
}
listaDinamica.prototype.refresh = refreshLista;


// Clean
function cleanLista() {
  while( this.data.length > 0 ) {
    this.objeto.options[0] = null;
    this.data.length--;
  }
}
listaDinamica.prototype.clean = cleanLista;


// Index
function indexLista() {
  return this.objeto.options.selectedIndex;
}
listaDinamica.prototype.index = indexLista;


// Value
function valueLista() {
  if( this.index() > -1 )
    return this.data[this.index()];
  return null;
}
listaDinamica.prototype.value = valueLista;
