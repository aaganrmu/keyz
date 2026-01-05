import board
import digitalio
import storage

DRIVE_NAME = "KEYZ"
LOCK_IO = board.GP12

# Disable USB drive if chosen GPIO is not connected to ground.
# Can be used with a physical lock, a mode switch, or even a single key.
lock = digitalio.DigitalInOut(LOCK_IO)
lock.direction = digitalio.Direction.INPUT
lock.pull = digitalio.Pull.UP

if lock.value:
    print(f'Boot: disabling drive')
    storage.disable_usb_drive()
else:
    print(f'Boot: renaming drive to {DRIVE_NAME}')
    storage.remount("/", readonly=False)
    mount = storage.getmount("/")
    mount.label = DRIVE_NAME
    storage.remount("/", readonly=True)
    print(f'Boot: enabling drive')
    storage.enable_usb_drive()
