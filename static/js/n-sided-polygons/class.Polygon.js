/*************************************
 *                                   * 
 *   @author: Nino P. Cocchiarella   *
 *	 Copyright (C) 2014              * 
 *   http://nino.cc                  *
 *                                   *
 *************************************/

// class Polygon {

function Polygon(n, r, c, rotation, axis, lineWidth, pointUpwards) {
    
    // accepts 'n' sides, radius 'r', center 'c'
    this.n = n;
    this.radius = r;
    this.center = c;
    this.rotation = rotation ? rotation : 0;

    // optional arguments
    this.axis = false;
    this.showAxis = axis ? axis : false;
    this.lineWidth = lineWidth ? lineWidth : 2;

    // define angle between lines from the
    // polygon's center, to each vertex
    this.theta = (Math.PI*2) / this.n;

    this.vertices = [];
    this.getVertices();

};

// define vertices around center (0,0)
Polygon.prototype.getVertices = function() {
    for (var i=0; i<this.n; i++) {
    	
        // define current angle
        var theta = this.theta * i;

        if (this.rotation) {
        	theta += this.rotation;
        }

        this.vertices.push([ 
            (this.radius * Math.cos(theta)), 
            (this.radius * Math.sin(theta))
        ]);
    }
    this.axis = [ 
    	[(this.radius * -0.7), 0], [(this.radius * 0.7), 0],
    	[0, (this.radius * -1.5)], [0, (this.radius * 1.5)]
    ];
};

Polygon.prototype.translate = function() {
    for (var i=0; i<this.vertices.length; i++) {
        this.vertices[i][0] += this.center[0];
        this.vertices[i][1] += this.center[1];
    }
    this.axis[0][0] += this.center[0];
    this.axis[0][1] += this.center[1];
    this.axis[1][0] += this.center[0];
    this.axis[1][1] += this.center[1];
    this.axis[2][0] += this.center[0];
    this.axis[2][1] += this.center[1];
    this.axis[3][0] += this.center[0];
    this.axis[3][1] += this.center[1];
};

// translate vertices to given center and draw polygon
Polygon.prototype.draw = function() {
    
    this.translate(); 
    
    for (var i=0; i<this.vertices.length; i++) {
        var next = this.vertices[(i+1) % this.n];
        gl.beginPath();
        gl.lineWidth = this.lineWidth;
        gl.moveTo(this.vertices[i][0], this.vertices[i][1]);
        gl.lineTo(next[0], next[1]); 
        gl.stroke();
    }

    if (this.showAxis) {

    	gl.lineWidth = this.lineWidth / 2;

    	gl.beginPath();
    	gl.moveTo(this.axis[0][0], this.axis[0][1]);
    	gl.lineTo(this.axis[1][0], this.axis[1][1]);
    	gl.stroke();

    	gl.beginPath();
    	gl.moveTo(this.axis[2][0], this.axis[2][1]);
    	gl.lineTo(this.axis[3][0], this.axis[3][1]);
    	gl.stroke();
    }

};

// } end class Polygon