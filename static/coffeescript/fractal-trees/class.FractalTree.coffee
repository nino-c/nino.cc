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

RECURSION_LIMIT = 10

moveTo = ([x,y]) -> gl.moveTo(x, y)
lineTo = ([x,y]) -> gl.lineTo(x, y)

class FractalTree
    constructor: (@height) ->
        @trunk = new Branch @height, [@height*2, @height*2], pi/2, 0
        @frameInterval = setInterval (=> @trunk.grow()), 20

class Branch
    constructor: (@length, @start, @angle, @generation, @parent) ->
        return if @generation >= RECURSION_LIMIT
        @angleVariation = pi/3
        @ratio = 2/(1+root(5))
        @maxChildren = 10
        @parent ?= null
        @unit = 2
        @children = []
        @location = @start.slice()
        @childLocations = (Math.random()*@length*@ratio/2+(@length*@ratio) \
            for n in [0...@maxChildren])

    grow: ->
        gl.beginPath()
        moveTo @location
        @location[0] += @unit * cos(@angle)
        @location[1] -= @unit * sin(@angle)
        lineTo @location
        gl.stroke()

        child.grow() for child in @children

        if @getLength() >= @childLocations[@children.length]
            @birthChild()


    getLength: ->
        return root( (@location[0]-@start[0])**2 + (@location[1]-@start[1])**2 )

    birthChild: ->
        angle = @angle + (Math.random()*@angleVariation*2) - @angleVariation
        child = new Branch @length * @ratio, @location, angle, @generation+1, this
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
    gl.strokeStyle = '#333333'
    gl.lineWidth = 1

    map = new FractalTree 200