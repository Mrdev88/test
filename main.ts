input.onButtonPressed(Button.A, function () {
    basic.showString("Test")
})
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 2; index++) {
        basic.showArrow(ArrowNames.North)
        basic.pause(100)
        basic.showArrow(ArrowNames.NorthEast)
        basic.pause(100)
        basic.showArrow(ArrowNames.East)
        basic.pause(100)
        basic.showArrow(ArrowNames.SouthEast)
        basic.pause(100)
        basic.showArrow(ArrowNames.South)
        basic.pause(100)
        basic.showArrow(ArrowNames.SouthWest)
        basic.pause(100)
        basic.showArrow(ArrowNames.West)
        basic.pause(100)
        basic.showArrow(ArrowNames.NorthWest)
    }
})
input.onButtonPressed(Button.B, function () {
    myImage = images.createImage(`
        # # # # #
        # # . . #
        # . # # #
        # # # . #
        # # # # #
        `)
    myImage.showImage(0)
})
input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . # . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showArrow(ArrowNames.North)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
})
let myImage: Image = null
basic.showString("Hello!")
