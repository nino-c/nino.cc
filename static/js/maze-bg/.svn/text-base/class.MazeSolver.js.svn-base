/*

@author: Nino P. Cocchiarella

MazeSolver pseudo-code

1. start at the entrance
2. while not at the exit
    1. push the current cell to visited
    2. if exists one or more directions that have not been visited
        1. push the current cell to pathStack
        2. choose any direction from those not visited
        3. move in that direction
        4. draw path from previous cell to chosen cell
        5. make the chosen cell the current cell
    3. otherwise backtrack
        1. pop the pathStack
        2. remove line from currentCell to popped cell
        3. do not remove popped cell from visited
*/

// class MazeSolver {

function MazeSolver(maze) {
    this.Maze = maze;
    this.position = [0, 0];
    this.pathStack = [];
    this.visited = [];
    this.Maze.clearBall();

    var self = this;
    this.solveStep = function() {
        self.moveForward();
    };
}

MazeSolver.prototype.getValidDirections = function(x,y) {
    
    var directions = [];
    
    if (!this.Maze.map[y][x][0]) 
        directions.push([0,-1]);
    if (!this.Maze.map[y][x][1] && (x!=this.Maze.x-1 || y!=this.Maze.y-1)) 
        directions.push([1,0]);
    if (!this.Maze.map[y][x][2]) 
        directions.push([0,1]);
    if (!this.Maze.map[y][x][3] && (x||y)) 
        directions.push([-1,0]);

    var validDirections = [];
    for (var i=0; i<directions.length; i++) {
        var tx = x+directions[i][0];
        var ty = y+directions[i][1];
        if (!this.isVisited(tx,ty)) {
            validDirections.push(directions[i]);
        }
    }

    return validDirections;
};

MazeSolver.prototype.isVisited = function(x,y) {
    for (var i=0; i<this.visited.length; i++) {
        if (this.visited[i][0] == x && this.visited[i][1] == y) 
            return true;
    }
    return false;
};

MazeSolver.prototype.isDeadEnd = function(x,y) {
    if (!this.getValidDirections(x,y).length)
        return true;
    return false;
};

MazeSolver.prototype.movePath = function(cx,cy,nx,ny) {
    ctx.lineWidth = 4;
    ctx.strokeStyle = '#5555ff';
    ctx.beginPath();

    ctx.moveTo(cx*this.Maze.cellSize+this.Maze.cellSize/2, 
        cy*this.Maze.cellSize+this.Maze.cellSize/2);
    ctx.lineTo(nx*this.Maze.cellSize+this.Maze.cellSize/2, 
        ny*this.Maze.cellSize+this.Maze.cellSize/2);
    ctx.stroke();
};

MazeSolver.prototype.clearPath = function(x,y) {
    ctx.clearRect(x*this.Maze.cellSize+2, y*this.Maze.cellSize+2, 
        this.Maze.cellSize-4, this.Maze.cellSize-4);
};

MazeSolver.prototype.isFinished = function() {
    if (this.position[0] == this.Maze.x-1 && this.position[1] == this.Maze.y-1)
        return true;
    return false;
};

MazeSolver.prototype.moveForward = function() {
    
    var cx = this.position[0];
    var cy = this.position[1];
    
    this.visited.push([cx,cy]);
    
    if (this.isFinished()) {
        console.log("FINISH");
        clearInterval(this.interval);
        return;
    }

    if (!this.isDeadEnd(cx,cy)) {
        this.pathStack.push([cx,cy]);
        var directions = this.getValidDirections(cx,cy);
        var randomDirection = Math.floor(Math.random()*directions.length);
        
        var nx = cx + directions[randomDirection][0];
        var ny = cy + directions[randomDirection][1];

        this.movePath(cx,cy,nx,ny);
        this.position = [nx,ny];

    } else { 
        this.backtrack();
    }
};

MazeSolver.prototype.backtrack = function() {
    var lastCell = this.pathStack.pop();
    this.clearPath(this.position[0], this.position[1]);
    this.position = [lastCell[0], lastCell[1]];
};

// } end class MazeSolver