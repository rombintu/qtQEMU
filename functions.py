import os

def createDisk(name, gb):
    os.system(f"qemu-img create -f qcow2 images/{name}.qcow {gb}G")

def deleteDisk(name):
    os.system(f"rm images/{name}")

def startVM(car, mem, kvmStatus):
    if kvmStatus == 2:
        os.system(f"qemu-system-x86_64 -hda {car} -m {mem} -enable-kvm")
    else:
        os.system(f"qemu-system-x86_64 -hda {car} -m {mem}")

def bootCar(disk, pathToISO, mem):
    os.system(f"qemu-system-x86_64 -hda {disk} -boot d -cdrom {pathToISO} -m {mem} -enable-kvm")