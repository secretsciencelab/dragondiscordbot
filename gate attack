var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var geometry = new THREE.BoxGeometry( 0.5,0.5,0.5);
var material = new THREE.MeshBasicMaterial( { color: 00000190 } );
var cube = new THREE.Mesh( geometry, material );
scene.add( cube );

camera.position.z = 5;

var dir = new THREE.Vector3( 1, 2, 0 );

//normalize the direction vector (convert to vector of length 1)
dir.normalize();

var origin = new THREE.Vector3( 0, 0, 0 );
var length = 1.25;
var hex = 00000190;

var arrowHelper = new THREE.ArrowHelper( dir, origin, length, hex );
scene.add( arrowHelper );

var dir = new THREE.Vector3( -1, 2, 0 );

//normalize the direction vector (convert to vector of length 1)
dir.normalize();

var origin = new THREE.Vector3( 0, 0, 0 );
var length = 1.25;
var hex = 00000190;

var arrowHelper = new THREE.ArrowHelper( dir, origin, length, hex );
scene.add( arrowHelper );
var dir = new THREE.Vector3( 1, -2, 0 );

//normalize the direction vector (convert to vector of length 1)
dir.normalize();

var origin = new THREE.Vector3( 0, 0, 0 );
var length = 1.25;
var hex = 00000190;

var arrowHelper = new THREE.ArrowHelper( dir, origin, length, hex );
scene.add( arrowHelper );
var dir = new THREE.Vector3( -1, -2, 0)

//normalize the direction vector (convert to vector of length 1)
dir.normalize();

var origin = new THREE.Vector3( 0, 0, 0 );
var length = 1.25;
var hex = 0000190

var arrowHelper = new THREE.ArrowHelper( dir, origin, length, hex );
scene.add( arrowHelper );

var dir = new THREE.Vector3( 10, 2, 7 );

var animate = function () {
    requestAnimationFrame( animate );

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    renderer.render( scene, camera );
};

animate(THREE.LoopRepeat);
THE GATE MODULE
THREE.JS
