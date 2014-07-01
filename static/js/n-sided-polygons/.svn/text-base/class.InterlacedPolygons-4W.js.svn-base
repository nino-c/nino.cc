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
	this.polygonCenters = [];
	this.angles = [];

	this.dtheta = (2*Math.PI) / this.n;
	for (var i=1; i<=this.n; i++) {
		this.angles.push(this.dtheta * i); console.log(this.n + ': ' + this.angles[i-1]*(180/Math.PI))
	}

	// draw first polygon
	this.polygons.push( new Polygon(this.n, this.radius, [0,0], this.angles[0]) );
	this.iterate(0,0,0);

}

InterlacedPolygons.prototype.polygonExists = function(x,y) {
	for (var i=0; i<this.polygonCenters.length; i++) {
		if (this.polygonCenters[i][0] == x && this.polygonCenters[i][1] == y) {
			console.log('eq');
			return true;
		}
	}
	return false;
}

InterlacedPolygons.prototype.iterate = function(x,y,n) {
	if (n==this.iterations) return;
	
	for (var i=0; i<this.n; i++) {
		
		// get rotation of current polygon
		var theta = this.angles[i];

		// if iteration is even, flip angle around pi
		if (n%2==0) { theta += (Math.PI); }

		var dx = Math.sqrt((this.n-2)*Math.pow(this.radius, 2)) *
			Math.cos(theta-(Math.PI/this.n)*(this.n-3));
		var dy = Math.sqrt((this.n-2)*Math.pow(this.radius, 2)) *
			Math.sin(theta-(Math.PI/this.n)*(this.n-3));
		
		var center = [x+dx, y+dy];

		this.polygons.push(
			new Polygon(this.n, this.radius, center, theta)
			);

		this.iterate(center[0], center[1], (n+1));

	}
};

InterlacedPolygons.prototype.draw = function() {
	var colors = ['#333333', '#ff0000', '#00ff00', '#0000ff', '#ffff00'];
	for (var i=0; i<this.polygons.length; i++) {
		//gl.strokeStyle = colors[i];
		this.polygons[i].center[0] += this.translation[0];
		this.polygons[i].center[1] += this.translation[1];
		this.polygons[i].draw();
	}
};

// } end class InterlacedPolygons