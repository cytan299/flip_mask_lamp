# Python script for controlling the flip mask and lamp

This directory contains the source code of _flipit.py_ that is used
for controlling the flip mask and lamp.

## Required Python version and packages

The required Python version is 3.

This [python library](https://github.com/FRC4564/Maestro/) is used by
the _flipit.py_ programme to talk to the
[Pololu Maestro](https://www.pololu.com/product/1350).

For convenience, the _maestro.py_ library is distributed with
_flipit.py_.

## Installation

Just copy the entire _flipit_ directory to a user directory.

## Executing flipit.py

```
python flipit.py
```
By default the serial port _flipit.py_ defaults to is
* _COM3_ on Win10.
* _/dev/cu.usbmodem00183281_ on Mac OS X Sierra.

Other serial ports can be specified as an argument.
```
python flipit.py [SERIAL_PORT]
```
Help is always available
```
python flipit.py -h
```

## Copyright

The software that is written by the author is copyright 2017 C.Y. Tan
and released under GPLv3.
