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

	// draw first polygon
	this.polygons.push( new Polygon(this.n, this.radius, [0,0], 0) );
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
	

	var d;
	if (this.n % 2) {
		d = this.iterations % 2 ? 1 : -1;
	} else d = 1;
	
	var theta = ((2*Math.PI) / this.n) + Math.PI;
	var theta2 = (2*Math.PI) / this.n
	

	for (var i=0; i<this.n; i++) {
		dx = Math.sqrt(this.n-2) * this.radius * Math.sin(theta2*i);
		dy = Math.sqrt(this.n-2) * this.radius * Math.cos(theta2*i);

		if (!this.polygonExists([x+dx,y+dy])) {
			this.polygons.push(
				new Polygon(this.n, this.radius, [x+dx, y+dy], d*theta)
				);
			this.polygonCenters.push([x+dx, y+dy]);
			this.iterate(x+dx,y+dy,(n+1));
		}
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