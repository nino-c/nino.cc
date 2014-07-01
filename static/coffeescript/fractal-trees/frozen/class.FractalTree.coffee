#####################################
#                                   #
#   @author: Nino P. Cocchiarella   #
#	Copyright (C) 2014              #
#   http://nino.cc                  #
#                                   #
#####################################

pi = Math.PI
abs = Math.abs
sin = Math.sin
cos = Math.cos
root = Math.sqrt
count = 0

RECURSION_LIMIT = 4

move = ([x,y]) -> gl.moveTo(x, y)
line = ([x,y]) -> gl.lineTo(x, y)

class FractalTree
    constructor: (@height) ->
        @trunk = new Branch @height, [200,300], pi/2, 0, null, this
        @frameInterval = setInterval (=> @trunk.grow()), 20

class Branch
    constructor: (@length, @start, @angle, @generation, @parent, @tree) ->
        @parentTree = @tree
        @angleVariation = pi/2.4
        @ratio = 2/(1+root(5))
        @maxChildren = 7
        @parent ?= null
        @unit = 2
        @children = []
        @location = @start.slice()
        @growing = true
        @color = 'rgba(98, 78, 44, ' + (1 - @generation*0.2).toString() + ')'
        console.log @color
        @thickness = 1.5#RECURSION_LIMIT - @generation
        @childLocations = ( Math.random()*@length*@ratio/2+(@length*@ratio/2) \
            for n in [0...@maxChildren] )

    grow: ->
        @draw() if @growing
        @growing = false if @getLength() >= @length
        if @getLength() >= @childLocations[@children.length]
            @birthChild() unless @generation >= RECURSION_LIMIT

        child.grow() for child in @children
            
    draw: ->
        gl.strokeStyle = @color
        gl.lineWidth = @thickness
        gl.beginPath()
        move @location
        @location[0] += @unit * cos(@angle)
        @location[1] -= @unit * sin(@angle)
        line @location
        gl.stroke()

    getLength: ->
        return root( (@location[0]-@start[0])**2 + (@location[1]-@start[1])**2 )

    birthChild: ->
        angle = @angle + (Math.random()*@angleVariation*2) - @angleVariation
        child = new Branch @length * @ratio, @location, angle, @generation+1, this, @tree
        @children.push child


#################################################

canvas = null
gl = null

$(document).ready ->
    canvas = document.createElement('canvas')
    canvas.width = $(window).width()
    canvas.height = $(window).height()
    document.body.appendChild(canvas)

    gl = canvas.getContext("2d")

    map = new FractalTree 120