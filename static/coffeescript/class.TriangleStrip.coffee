#####################################
#                                   #
#   @author: Nino P. Cocchiarella   #
#	 Copyright (C) 2014               #
#   http://nino.cc                  #
#                                   #
#####################################

root 	= Math.sqrt
pi 		= Math.PI
abs 	= Math.abs

class TriangleStrip
    constructor: (@length, @side, @dir, @translation, @top) ->
        @triangles = []
        @getTriangles()

    getTriangles: ->
        h = (root(3)/2) * @side
        for i in [0..@length]
            x = @side/2 * i

            if @dir
                y1 = 0
                y2 = h
            else
                y1 = h
                y2 = 0

            unless i%2
                @triangles.push([
                    [x, y1], [x+(@side/2), y2], [x+@side, y1]
                ])
            else
                @triangles.push([
                    [x, y2], [x+(@side/2), y1], [x+@side, y2]
                ])

    translate: ->
        for i in [0..@length]
            for j in [0...3]
                @triangles[i][j][0] += @translation[0]
                @triangles[i][j][1] += @translation[1]

    draw: ->
        @translate()
        for i in [0...@triangles.length]
            tri = @triangles[i]

            # left-most side
            # only on the left-most iteration
            if i==0
                gl.beginPath()
                gl.moveTo(tri[0][0], tri[0][1])
                gl.lineTo(tri[1][0], tri[1][1])
                gl.stroke()

            # right-most side
            # always draw
            gl.beginPath()
            gl.moveTo(tri[1][0], tri[1][1])
            gl.lineTo(tri[2][0], tri[2][1])
            gl.stroke()


            # horizontal side
            # if bottom, draw, if top, don't draw unless necessary
            draw = true
            draw = false if tri[1][1] > tri[0][1] and not @top
            draw = true if tri[1][1] > tri[0][1] and i%2==0 and i==0

            if draw
                gl.beginPath()
                gl.moveTo(tri[2][0], tri[2][1])
                gl.lineTo(tri[0][0], tri[0][1])
                gl.stroke()


class TriangleGrid
    constructor: (@width, @length, @size, @translation) ->
        @cells = []
        @map = []

        for i in [0...@length]
            trans = [@translation[0], @translation[1] + (@size * (root(3)/2) * i)]
            if i==0 then top = true else top = false

            dir = if i % 2 then true else false
            strip = new TriangleStrip(@width, @size, dir, trans, top)
            @cells.push(strip.triangles)

            @map[i] = []
            for j in [0...strip.length]
                @map[i].push false

            strip.draw()

    triangleUp: (x, y) ->
        return true if y % 2 and x % 2
        return false

    erase: ([from, to]) ->
        x = if from[0] < to[0] then from[0] else to[0]
        y = if from[1] < to[1] then from[1] else to[1]
        if from[1] == to[1]
            w = abs(from[0] - to[0]) - 2
            h = 2
            gl.clearRect(x+1, y-1, w, h)
        else
            w = abs(from[0] - to[0]) - 2
            h = abs(from[1] - to[1]) - 2
            gl.clearRect(x+1, y+1, w, h)

    removeWall: (x, y, side) ->
        #console.log [x,y,side]
        if @getSide(x, y, side)
            @erase(@getSide(x, y, side))

    getSide: (x, y, side) ->
        switch side
            when 'T'
                return [@cells[y][x][2], @cells[y][x][0]] unless @triangleUp(x, y)
            when 'B'
                return [@cells[y][x][2], @cells[y][x][0]] if @triangleUp(x, y)
            when 'L'
                return [@cells[y][x][0], @cells[y][x][1]]
            when 'R'
                return [@cells[y][x][1], @cells[y][x][2]]
            else
                return null





"Maze Generator pseudo-code

1. Make a random initial cell the current cell and mark it as visited
2. While there are unvisited cells
    1. If the current cell has any neighbors which have not been visited
        1. Choose randomly one of the unvisited neighbors
        2. Push the chosen cell to the stack
        3. Remove the wall between the current cell and the chosen cell
        4. Make the chosen cell the current cell and mark it as visited
    2. Otherwise
        1. Pop a cell from the stack
        2. Make it the current cell"

class TriangleMaze
    constructor: (@width, @length, @size) ->
        @stack = []
        @grid = new TriangleGrid @width, @length, @size, [50,50]
        @visited = @grid.map
        @startCell = null
        @currentCell = null
        @nextCell = null

        @frameInterval = setInterval (=> @renderStep()), 20

    unvisitedCellsExist: ->
        for i in [0...@width]
            for j in [0...@length]
                unless @visited[i][j]
                    return true
        return false

    chooseNeighbor: ->
        neighbors = []
        # left
        if @currentCell[0] > 0
            neighbors.push [[@currentCell[0]-1, @currentCell[1]], 'L']
        # right
        if @currentCell[0] < @width - 1
            neighbors.push [[@currentCell[0]+1, @currentCell[1]], 'R']
        # above
        if @currentCell[1] > 0
            unless @grid.triangleUp @currentCell[0], @currentCell[1]
                neighbors.push [[@currentCell[0], @currentCell[1]-1], 'T']
        # beneath
        if @currentCell[1] < @length - 1
            if @grid.triangleUp @currentCell[0], @currentCell[1]
                neighbors.push [[@currentCell[0], @currentCell[1]+1], 'B']

        unvisitedNeighbors = []
        for n in neighbors
            unless @visited[n[0][1]][n[0][0]]
                unvisitedNeighbors.push n

        if unvisitedNeighbors.length
            return unvisitedNeighbors[Math.floor(Math.random()*unvisitedNeighbors.length)]

            return null


    renderStep: ->
        unless @startCell?
            @currentCell = null
            @startCell = [Math.floor(Math.random() * @width), Math.floor(Math.random() * @length)]
            @currentCell = @startCell
            @visited[@startCell[1]][@startCell[0]] = true

        #@drawCurrentCellMarker()

        # if there are still unvisited cells
        if @unvisitedCellsExist()

            next = @chooseNeighbor()

            if (next)
                @nextCell = next[0]
                nextDirection = next[1]
                @stack.push [@nextCell[0], @nextCell[1]]
                @grid.removeWall @currentCell[0], @currentCell[1], nextDirection
                @visited[@nextCell[1]][@nextCell[0]] = true
                @currentCell = @nextCell

            else if @stack.length
                @currentCell = @stack.pop()
            else
                clearInterval @frameInterval

        else
            clearInterval @frameInterval




canvas = null
gl = null

$(document).ready ->
    canvas = document.createElement('canvas')
    canvas.width = $(window).width()
    canvas.height = $(window).height()
    document.body.appendChild(canvas)

    gl = canvas.getContext("2d")
    gl.strokeStyle = '#333333'
    gl.lineWidth = 1

    map = new TriangleMaze 70, 20, 30
