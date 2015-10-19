============
Serial Ports
============


Python
------

PySerial - https://github.com/pyserial

Open port at "9600,8,N,1", no timeout::

    >>> import serial
    >>> ser = serial.Serial('/dev/ttyUSB0')  # open serial port
    >>> print(ser.name)         # check which port was really used
    >>> ser.write(b"hello")     # write a string
    >>> ser.close()             # close port

Open named port at "19200,8,N,1", 1s timeout::

    >>> with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
    ...     x = ser.read()          # read one byte
    ...     s = ser.read(10)        # read up to ten bytes (timeout)
    ...     line = ser.readline()   # read a '\n' terminated line

Open port at "38400,8,E,1", non blocking HW handshaking::

    >>> ser = serial.Serial('COM3', 38400, timeout=0,
    ...                     parity=serial.PARITY_EVEN, rtscts=1)
    >>> s = ser.read(100)       # read up to one hundred bytes
    ...                         # or as much is in the buffer




Terminals
---------

  - MaxiCom
  - minicom
  - putty
  - gtkterm
  - moserial
  - cutecom


Tools
-----

  - udev
  - setserial
  - stty


* Attaching USB-Serial device with custom PID to ttyUSB0 on embedded
  http://unix.stackexchange.com/questions/67936/attaching-usb-serial-device-with-custom-pid-to-ttyusb0-on-embedded

* Последовательный порт
  http://ru.wikipedia.org/wiki/Последовательный_порт

* Как изменить параметры последовательного порта в Linux
  http://www.opennet.ru/tips/info/757.shtml

* Как настроить консоль на последовательном порту в Ubuntu
  http://vladimir-stupin.blogspot.co.il/2009/09/ubuntu.html

* Последовательный порт и модем
  http://rus-linux.net/MyLDP/HOWTO-ru/Modem-HOWTO-ru/Modem-HOWTO-4.html

Для управлением зоопарка устройств требуется написание udev правил (udev rules).

- http://wiki.archlinux.org/index.php/Udev_(Русский)
- http://tux-the-penguin.blogspot.co.il/2010/02/udev.html
- http://www.mcc-us.com/usinglinuxvcp.htm
- http://buzzdavidson.com/?p=45


Silicon Labs:

- http://www.silabs.com/Pages/default.aspx
- http://www.silabs.com/Support%20Documents/TechnicalDocs/AN571.pdf
- http://cp210x-program.sourceforge.net/
- http://unix.stackexchange.com/questions/75558/ubuntu-make-fails-with-no-such-file-or-directory-lib-modules-3-4-0-build


Links:

- http://cisco.opennet.ru/docs/RUS/serial_guide/index.html
- http://www.cmrr.umn.edu/~strupp/serial.html
- http://buzzdavidson.com/?p=45



Drivers:

  * Silicon Labs: cp210x
  * FDTI        : fdti_sio


Command line
~~~~~~~~~~~~
::

    (root)%> udevadm info -a -n /dev/ttyUSB0
    (root)%> udevadm monitor --env
    (root)%> udevadm info -a -p $(udevadm info -q path -n /dev/ttyUSB0)


Determine device
~~~~~~~~~~~~~~~~
::

    $ lsusb
    Bus 002 Device 003: ID 0cf3:e004 Atheros Communications, Inc.
    Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 003: ID 0c45:644f Microdia
    Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 002: ID 10c4:ec04 Cygnal Integrated Products, Inc.
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    
    #
    # Bus 003 Device 002: ID 10c4:ec04 Cygnal Integrated Products, Inc.
    #
    # ID = "10c4:ec04"
    #
    # Silicon Labs CP210x UART Bridge: ID = 10c4:ea60
    
    $ echo "10c4 ec04" > /sys/bus/usb-serial/drivers/cp210x/new_id


UDEV 
~~~~~

Example of rules::

    # cp210x
    SUBSYSTEMS=="usb", KERNEL=="ttyUSB[0-9]*", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", SYMLINK+="sensors/CP210x_%s{serial}", MODE="0666"
    
    # ftdi_sio
    SUBSYSTEMS=="usb", KERNEL=="ttyUSB[0-9]*", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", SYMLINK+="sensors/ftdi_%s{serial}"  MODE="0666"
    
    # PowerSupply1
    SUBSYSTEMS=="usb", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ec00",  RUN+="/sbin/modprobe cp210x"
    SUBSYSTEMS=="drivers", ENV{DEVPATH}=="/bus/usb-serial/drivers/cp210x", ATTR{new_id}="10c4 ec00"
    SUBSYSTEMS=="usb", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ec00",  SYMLINK+="crow/pps1", GROUP="users", MODE="0666"

