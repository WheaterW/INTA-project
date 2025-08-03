ospf timer dead
===============

ospf timer dead

Function
--------



The **ospf timer dead** command sets a dead interval for the OSPF neighbor in the instance to which an interface belongs.

The **undo ospf timer dead** command restores the default value.



By default, the dead interval of OSPF neighbors is 40 seconds on a P2P or broadcast interface, and is 120 seconds on an NBMA or P2MP interface.


Format
------

**ospf timer dead** *interval*

**undo ospf timer dead**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a dead interval for OSPF neighbors. | The value is an integer ranging from 1 to 235926000. Setting a dead interval that is longer than 10s for OSPF neighbors is recommended. If the dead interval is less than 10s, the session may be terminated. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If no Hello packet is received from a neighbor within a dead interval, the neighbor is considered invalid. The dead interval on OSPF interfaces must be greater than the transmission interval of Hello messages. In addition, the dead intervals of devices on the same network segment must be the same.By default, the dead interval of OSPF neighbors is four times the transmission interval of Hello messages.

**Precautions**

The command cannot be run on a null interface.If the dead interval of an OSPF neighbor is shorter than 10s, the session may be closed. Therefore, if dead interval is shorter than 10s, the actual dead interval of an OSPF neighbor is not shorter than 10s. If the conservative mode is configured using the **ospf timer hello** command, the configured dead timer takes effect even when its value is less than 10s.


Example
-------

# Set the dead interval on the interface to 60 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf timer dead 60

```