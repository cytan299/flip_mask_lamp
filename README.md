# Remote controlled flip Bahtinov mask and lamp

by C.Y. Tan 2017

![Flip mask and lamp](https://github.com/cytan299/flip_mask_lamp/blob/master/pics/IMG_1873.jpg)

I made a flip mask and lamp for my FSQ106 so that when they are
mounted on the telescope, they will balance each other out when mounted on
the opposite side of the telescope.

![Flip mask and lamp mounted on an FSQ106 ](https://github.com/cytan299/flip_mask_lamp/blob/master/pics/IMG_1891.jpg)

## Design

The flip mask and lamp are designed as a master and slave pair. I have
chosen the flip mask controller to be the master and the flip lamp
controller to be the slave.

The mechanical design of the flip mask and lamp are mirror images of
each other. The principal parts used in the design are as follows:

* A servo controller made by Pololu called the [Maestro](https://www.pololu.com/product/1350).
* A servo that rotates greater than 270
degrees: the [Feetech FR5311M](http://www.feetechrc.com/product/continuous-rotation-servo/two-working-mode-digital-programmable-metal-gears-servo-fr5311m/).
* A sprocket and chain system for connecting the servo to the mask and lamp.
* Interlock switches to indicate where the mask or lamp is
  * A mechanical lever switch
  * A Hall switch
* A lamp made from an
[electroluminescent panel with dimmer and power inverter](https://knema.com/collections/electroluminescent-el-panels/products/electroluminescent-panel-split-electrode-type-blue-green-or-white-includes-power-supply-and-dimming-inverter).

## Movie

A movie of how the flip mask and lamp in action can be found on [youtube](https://youtu.be/KrSrh4rIldk).

## Support

This is unsupported hardware. Build at your own peril! :)

You can submit questions or bug reports using the
[issues](https://github.com/cytan299/flip_mask_lamp/issues) tab on
the right and then click on **NEW**.

Have fun!

## Directory structure

* **howto** Assembly instructions for the flip mask and lamp.
* **ponoko** The files that are used for laser cutting the acrylic parts of
the design. These files are can be sent directly to
[Ponoko](http://www.ponoko.com) for laser cutting.
* **bom** Bill of materials for 1 pair of flip mask and lamp.
* **eagle** Eagle schematic and board files.
* **python** Source code for the python control program.
* **pics** Photographs used in the README's and Wiki.

## Other information

More information can be found in he *README.md* files in each
directory and the [wiki](https://github.com/cytan299/flip_mask_lamp/wiki/Flip-Mask-and-Lamp) of this project on github.

## Copyright
All the software, documentation, and hardware that I have written is
copyright 2017 C.Y. Tan.

All software is released under GPLv3

All documentation is released under Creative Commons
Attribution-ShareAlike 3.0 Unported License or GNU Free
Documentation License, Version 1.3

All hardware is released under CERN Hardware Open License v1.2



