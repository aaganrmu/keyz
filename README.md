
# keyz
Keyboard software for Pi Pico.

## Features:
- Password generator (don't trust it though)
- Configurable
- Layers

## Installation:
1. Install Circuitpython
3. Edit `config` file in source to match your setup
4. Create `pad` file in source folder with a long number on Pi Pico
2. Copy/paste contents of source folder to Pi Pico (or use install.sh)

## Normal keys

Use keys as defined in keycode.py

## Layers

Two options that can be combined:
Keys defined as `SET_LAYER_#` will set your layer to # until a different layer is set.
Keys defined as `SHIFT_LAYER_#` will increase your layer by # while held. You can combine multiple shifts with a set.

Create layers for all options using `layer_#`
Default layer is 0
Keep `SHIFT_LAYER_#` definitions constant between layers or there will be glitches.

## Password generator

Type password using `PASSWORD_#` keys (only numbers), then press `PASSWORD_ENTER` to generate a password.

It is probably not secure so don't use it for important passwords.