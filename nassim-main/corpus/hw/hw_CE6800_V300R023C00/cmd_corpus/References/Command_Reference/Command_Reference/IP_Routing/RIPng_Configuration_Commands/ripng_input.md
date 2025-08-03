ripng input
===========

ripng input

Function
--------



The **ripng input** command enables the specified interface to receive RIPng packets.

The **undo ripng input** command disables the specified interface from receiving RIPng packets.



By default, interfaces can receive RIPng packets.


Format
------

**ripng input**

**undo ripng input**


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

When a device running RIPng is connected to a network running other routing protocols, you can run the **undo ripng input** command on the interface that connects the device to the network to prevent the interface from receiving RIPng packets from the network.


Example
-------

# Disable 100GE 1/0/1 interface to receive RIPng packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] undo ripng input

```