/*************************************
 *                                   * 
 *   @author: Nino P. Cocchiarella   *
 *	 Copyright (C) 2014              *                                                             
 *   http://nino.cc                  *
 *                                   *
 *************************************/

var RECURSION_LIMIT = 10;

// class InterlacedPolygons {

function InterlacedPolygons(n, r, x, y, translation) {
	this.n = n;
	this.radius = r;
	this.x = x;
	this.y = y;
	this.translation = translation;
	this.polygons = [];
	this.polygonIndeces = [];
	this.angles = [];
	this.seedX = Math.floor(this.x/2);
	this.seedY = Math.floor(this.y/2);

	this.bounds = [[0,0], [this.x * 2 * this.radius, this.y * 2 * this.radius]];

	this.dtheta = (2*Math.PI) / this.n;
	for (var i=1; i<=this.n; i++) {
		this.angles.push(this.dtheta * i);
	}

	// set all indeces to false
	/*switch (this.n) {
		case 3:
			for (var i=0; i<this.y; i++) {
				this.polygonIndeces.push([]);
				for (var j=0; j<this.x; j++) {
					this.polygonIndeces[i].push([false, false]);
				}
			}
		break;
	}*/

	// draw first polygon
	this.polygons.push( 
		new Polygon(this.n, this.radius, 
			[this.seedX*this.radius, this.seedY.this.radius], this.angles[0]) 
		);
	this.polygonIndeces.push([this.seedX, this.seedY]);

	// start iterations
	this.iterate(this.seedX, this.seedY, 0);

}

InterlacedPolygons.prototype.polygonExists = function(x,y,c) {
	for (var i=0; i<this.polygonIndeces.length; i++) {
		if (this.po)
	}
};

InterlacedPolygons.prototype.iterate = function(x,y,n) {
	
	// check recursion limit
	if (n >= RECURSION_LIMIT) return;

	// check bounds
	if (x <= this.bounds[0][0]) return;
	if (x >= this.bounds[1][0]) return;
	if (y <= this.bounds[0][1]) return;
	if (y >= this.bounds[1][1]) return;
	
	for (var i=0; i<this.n; i++) {
		
		// get rotation of current polygon
		var theta = this.angles[i];

		// if iteration is even, flip angle around pi
		if (n%2==0) { theta += (Math.PI); }

		var side = this.radius * 2 * Math.sin(Math.PI/this.n);
		var apothem = Math.sqrt(  Math.pow(this.radius, 2) - Math.pow((side/2), 2)  );
		var d = 2 * apothem;
		var dr = this.n > 3 ? 2 : 1;
		var dx = d * Math.cos(theta+this.dtheta/dr);
		var dy = d * Math.sin(theta+ this.dtheta/dr);
		
		var center = [x+dx, y+dy];

		this.polygons.push(
			new Polygon(this.n, this.radius, center, theta)
			);

		this.iterate(center[0], center[1], (n+1));

	}
};

InterlacedPolygons.prototype.draw = function() {
	for (var i=0; i<this.polygons.length; i++) {
		this.polygons[i].center[0] += this.translation[0];
		this.polygons[i].center[1] += this.translation[1];
		this.polygons[i].draw();
	}
};

// } end class InterlacedPolygons

