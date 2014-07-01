/*************************************
 *                                   * 
 *   @author: Nino P. Cocchiarella   *
 *	 Copyright (C) 2014              *                                                             
 *   http://nino.cc                  *
 *                                   *
 *************************************/

// class InterlacedPolygons {

function InterlacedPolygons(n, r, iterations, translation) {

	this.n = n;
	this.radius = r;
	this.iterations = iterations;
	this.translation = translation;
	this.polygons = [];

	// draw first polygon
	this.polygons.push( new Polygon(this.n, this.radius, [0,0], 0) );

	// iteration
	
	var theta = ((2*Math.PI) / this.n) + Math.PI;
	var theta2 = (2*Math.PI) / this.n

	for (var i=0; i<this.n; i++) {
		var x = Math.sqrt(this.n-2) * this.radius * Math.sin(theta2*i);
		var y = Math.sqrt(this.n-2) * this.radius * Math.cos(theta2*i);
		console.log([x,y])
		this.polygons.push(
			new Polygon(this.n, this.radius, [x, y], theta)
			);
	}


}

InterlacedPolygons.prototype.draw = function() {
	for (var i=0; i<this.polygons.length; i++) {
		this.polygons[i].center[0] += this.translation[0];
		this.polygons[i].center[1] += this.translation[1];
		this.polygons[i].draw();
	}
};

// } end class InterlacedPolygons