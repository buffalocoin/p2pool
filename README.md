Requirements:
-------------------------
Generic:
* Bitcoin >=0.8.5
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

Running P2Pool:
-------------------------
Run P2Pool with the "--net buffalocoin" option.
Run your miner program, connecting to 127.0.0.1 on port 8985.
Forward port 29985 to the host running P2Pool.

Buffalocoin's use of ports 25085 and 25086. To avoid problems, add these lines to buffalocoin.conf
and restart litecoind:

    rpcport=25086
    port=25085

Donations towards further development:
-------------------------
    BJG379oBv9cn94cdz85E9K5ejRhrHcvKgs
    
Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool

