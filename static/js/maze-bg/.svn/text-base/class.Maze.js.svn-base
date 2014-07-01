/*************************************
 *                                   * 
 *   @author: Nino P. Cocchiarella   *
 *   Copyright (C) 2014              *                                                             
 *   http://nino.cc                  *
 *                                   *
 *************************************/

/*
Maze Generator pseudo-code

1. Make the initial cell the current cell and mark it as visited
2. While there are unvisited cells
    1. If the current cell has any neighbors which have not been visited
        1. Choose randomly one of the unvisited neighbors
        2. Push the chosen cell to the stack
        3. Remove the wall between the current cell and the chosen cell
        4. Make the chosen cell the current cell and mark it as visited
    2. Otherwise
        1. Pop a cell from the stack
        2. Make it the current cell
*/

// class Maze {

function Maze(dimension, x, y, cellSize) {

    this.x = x;
    this.y = y; 
    this.map = [];
    this.visited = [];
    this.stack = [];
    this.cellSize = cellSize;
    this.currentPosition = [0, 0];
    this.ballRadius = this.cellSize * 0.4;
    this.linesDrawn = [];
    this.frameInterval;
    this.building = true;
    this.margin = 2;
    this.gridColor = '#eeeeee';
    this.gridLineWidth = 1;
    this.wallColor = '#aaaaaa';
    this.wallLineWidth = 1;
    this.markerColor = "rgba(246, 250, 168, ";
    this.tailLength = 50;
    this.startCell = false;
    this.currentCell = false;
    this.nextCell = false;
    this.lastMarkerRect = false;

    this.setUpGrid();

    for (var i=0; i<y; i++) {
        this.map.push( [] );
        this.visited.push( [] );
        for (var j=0; j<x; j++) {
            this.map[i].push( [1,1,1,1] );
            this.visited[i].push( false );
        }
    }

    var self = this;
    this.renderStep = function() {
        self.renderFrame();
    };
}

Maze.prototype.unvisitedCellsExist = function() {
    for (var i=0; i<this.y; i++) {
        for (var j=0; j<this.x; j++) {
            if (this.visited[i][j]) return true;
        }
    }
    return false;
};

Maze.prototype.chooseNeighbor = function(cx,cy) {
    var neighbors = [];
    var directions = [];
    if (cx > 0 && !this.visited[cy][cx-1]) 
        { neighbors.push( [cx-1, cy] ); directions.push('W'); }
    if (cx < this.x-1 && !this.visited[cy][cx+1]) 
        { neighbors.push( [cx+1, cy] ); directions.push('E'); }
    if (cy < this.y-1 && !this.visited[cy+1][cx]) 
        { neighbors.push( [cx, cy+1] ); directions.push('S'); }
    if (cy > 0 && !this.visited[cy-1][cx]) 
        { neighbors.push( [cx, cy-1] ); directions.push('N'); }
    if (neighbors.length) {
        r = Math.floor(Math.random()*neighbors.length);
        return [ neighbors[r], directions[r] ];
    } else return false;
};

Maze.prototype.removeWall = function(x, y, direction) {
   
    var x1 = x * this.cellSize + this.margin;
    var y1 = y * this.cellSize + this.margin;
    var d = this.cellSize - (this.gridLineWidth*2);
    var l = this.gridLineWidth * (-1); 

    ctx.beginPath();

    switch (direction) {
        case 'N':
            this.map[y][x][0] = 0;
            this.map[y-1][x][2] = 0;
            ctx.clearRect(x1-l, y1-l, d, l*2)
        break;
        case 'E':
            this.map[y][x][1] = 0; 
            this.map[y][x+1][3] = 0;
            ctx.clearRect(x1+this.cellSize-l, y1-l, l*2, d)
        break;
        case 'S':
            this.map[y][x][2] = 0; 
            this.map[y+1][x][0] = 0;
            ctx.clearRect(x1-l, y1+this.cellSize-l, d, l*2)
        break;
        case 'W':
            this.map[y][x][3] = 0;
            this.map[y][x-1][1] = 0;
            ctx.clearRect(x1-l, y1-l, l*2, d)
        break;
    }

    this.renderCell(x,y);

}

Maze.prototype.renderCell = function(x,y) {

    ctx.strokeStyle = this.wallColor;
    ctx.lineWidth = this.wallLineWidth;

    ctx.beginPath();
    cell = this.map[y][x];
    cx = this.cellSize * x + this.margin;
    cy = this.cellSize * y + this.margin;
    var mt;
    var lt;

    if (cell[0]) {
        mt = [cx, cy];
        lt = [cx+this.cellSize, cy];
        if (!this.lineIsDrawn(mt, lt)) {
            this.linesDrawn.push([mt, lt]);
            ctx.moveTo(mt[0], mt[1]);
            ctx.lineTo(lt[0], lt[1]);
            ctx.stroke();
        }
    } 
    if (cell[1]) {
        mt = [cx+this.cellSize, cy];
        lt = [cx+this.cellSize, cy+this.cellSize];
        if (!this.lineIsDrawn(mt, lt)) {
            this.linesDrawn.push([mt, lt]);
            ctx.moveTo(mt[0], mt[1]);
            ctx.lineTo(lt[0], lt[1]);
            ctx.stroke();
        }
    } 
    if (cell[2]) {
        mt = [cx+this.cellSize, cy+this.cellSize];
        lt = [cx, cy+this.cellSize];
        if (!this.lineIsDrawn(mt, lt)) {
            this.linesDrawn.push([mt, lt]);
            ctx.moveTo(mt[0], mt[1]);
            ctx.lineTo(lt[0], lt[1]);
            ctx.stroke();
        }
    }
    if (cell[3]) {
        mt = [cx, cy+this.cellSize];
        lt = [cx, cy];
        if (!this.lineIsDrawn(mt, lt)) {
            this.linesDrawn.push([mt, lt]);
            ctx.moveTo(mt[0], mt[1]);
            ctx.lineTo(lt[0], lt[1]);
            ctx.stroke();
        }
    }
}

Maze.prototype.drawCurrentCellMarker = function(alpha) {
    
    var rect = [
        (this.currentCell[0]*this.cellSize+this.margin+this.gridLineWidth),
        (this.currentCell[1]*this.cellSize+this.margin+this.gridLineWidth),
        this.cellSize - this.gridLineWidth*2,
        this.cellSize - this.gridLineWidth*2
        ];

    if (this.lastMarkerRect) {
        for (var i=0; i<this.lastMarkerRect.length; i++) {
            ctx.clearRect(
                this.lastMarkerRect[i][0],
                this.lastMarkerRect[i][1],
                this.lastMarkerRect[i][2],
                this.lastMarkerRect[i][3]
                );
        }
        
    } else this.lastMarkerRect = [];
    
    this.lastMarkerRect.push([
        rect[0],
        rect[1],
        rect[2],
        rect[3]
        ]);
    
    for (var i=0; i<this.tailLength; i++) {
        if (this.stack[this.stack.length-i-1]) {

            var rect = [
                (this.stack[this.stack.length-i-1][0]*this.cellSize+this.margin+this.gridLineWidth),
                (this.stack[this.stack.length-i-1][1]*this.cellSize+this.margin+this.gridLineWidth),
                this.cellSize - this.gridLineWidth*2,
                this.cellSize - this.gridLineWidth*2
                ];

            ctx.beginPath();
            ctx.fillStyle = this.markerColor + (1 - (1/this.tailLength) * i).toString() + ')';
            ctx.fillRect(
                rect[0],
                rect[1],
                rect[2],
                rect[3]
                );
        }
    }
    
};

Maze.prototype.renderFrame = function() {
    
    /*
    now render as we go
    old generateMap() and render() 
    now together in one method
    */

    if (!this.startCell) {
        this.startCell = [];
        this.currentCell = [];
        this.nextCell = [];
        this.startCell.push(Math.floor(Math.random()*this.x));
        this.startCell.push(Math.floor(Math.random()*this.y)); 
        this.currentCell = [this.startCell[0], this.startCell[1]];
        this.visited[this.startCell[1]][this.startCell[0]] = true;
    }

    this.drawCurrentCellMarker();

    var next;
    var nextDirection;

    // if there are still unvisited cells
    if (this.unvisitedCellsExist()) {
        if (this.chooseNeighbor(this.currentCell[0],this.currentCell[1])) {
            
            next = this.chooseNeighbor(this.currentCell[0],this.currentCell[1]);
            
            this.nextCell[0] = next[0][0];
            this.nextCell[1] = next[0][1];
            
            nextDirection = next[1];
            this.stack.push( [this.nextCell[0], this.nextCell[1]] );
            this.removeWall(this.currentCell[0], this.currentCell[1], nextDirection);
            
            this.visited[this.nextCell[1]][this.nextCell[0]] = true;

            this.currentCell[0] = this.nextCell[0];
            this.currentCell[1] = this.nextCell[1];
        
        } else if (this.stack.length) {

            next = this.stack.pop();
            this.currentCell[0] = next[0];
            this.currentCell[1] = next[1];
      
        } else {
        
            this.building = false;  
            clearInterval(this.frameInterval);
      
        }

    } else {

        this.building = false;
        clearInterval(this.frameInterval);

    }

};

Maze.prototype.lineIsDrawn = function(mt, lt) {
    for (var i=0; i<this.linesDrawn.length; i++) {
        if (this.linesDrawn[i][0][0] == mt[0] &&
            this.linesDrawn[i][0][1] == mt[1] &&
            this.linesDrawn[i][1][0] == lt[0] &&
            this.linesDrawn[i][1][1] == lt[1]) {

            return true;
        }
    }
    return false;
};

Maze.prototype.setUpGrid = function() {
    ctx.lineWidth = this.gridLineWidth;
    ctx.strokeStyle = this.gridColor;
    for (var i=0; i<=this.y; i++) {
        ctx.moveTo(this.margin, (this.cellSize*i)+this.margin);
        ctx.lineTo((this.cellSize*this.x)+this.margin, (this.cellSize*i)+this.margin);
        ctx.stroke();
    }
    for (i=0; i<=this.x; i++) {
        ctx.moveTo((this.cellSize*i)+this.margin, this.margin);
        ctx.lineTo((this.cellSize*i)+this.margin, (this.cellSize*this.y)+this.margin);
        ctx.stroke();
    }

    /*var dg = 100;
    var h = (this.y * this.cellSize);
    for (i=0; i<dg; i++) {
        ctx.beginPath();
        ctx.fillStyle = "rgba(255, 255, 255, " + (1-(i/dg)).toString() + ")";
        ctx.fillRect(0, (h/2)+((h/2)/dg)*i, this.x*this.cellSize, (h/2)/dg);
    }*/
}


// } end class Maze