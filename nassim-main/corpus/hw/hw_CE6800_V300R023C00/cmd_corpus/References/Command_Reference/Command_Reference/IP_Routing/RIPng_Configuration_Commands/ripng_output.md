ripng output
============

ripng output

Function
--------



The **ripng output** command enables an interface to send RIPng packets.

The **undo ripng output** command disables an interface from sending RIPng packets.



By default, an interface can send RIPng packets.


Format
------

**ripng output**

**undo ripng output**


Parameters
----------

None

Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a device running RIPng is connected to a network running other routing protocols, you can run the **undo ripng output** command on the interface that connects the device to the network to prevent the interface from sending RIPng packets to the network.


Example
-------

# Disable 100GE 1/0/1 interface to send RIPng packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] undo ripng output

```