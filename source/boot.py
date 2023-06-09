import board
import digitalio
import storage

DRIVE_NAME = "KEYZ"

# Disable USB drive if GPIO14 is not connected to ground.
# There's a physical lock connected to it.
lock = digitalio.DigitalInOut(board.GP14)
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


