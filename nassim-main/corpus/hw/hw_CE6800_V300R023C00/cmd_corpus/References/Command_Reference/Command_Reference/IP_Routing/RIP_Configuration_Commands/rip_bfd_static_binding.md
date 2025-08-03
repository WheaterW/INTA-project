rip bfd static binding
======================

rip bfd static binding

Function
--------



The **rip bfd static binding** command enables static BFD for a specified neighbor on a specified RIP interface.

The **undo rip bfd static binding** command disables static BFD for a specified neighbor on a specified RIP-enabled interface.



By default, static BFD is disabled for a specified neighbor on a RIP interface.


Format
------

**rip bfd static binding** *peer-address*

**undo rip bfd static binding** *peer-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the IP address of a neighbor. | The value is in dotted decimal notation. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a network deployed with high-speed data services, if a link fault occurs, it takes a long time for RIP to detect the link fault. As a result, a large amount of data is lost. Therefore, BFD needs to be deployed on the network to speed up RIP link detection.You can run the **rip bfd static binding** command to enable BFD on a specified link to rapidly detect link faults. In addition, there are a large number of devices that do not support BFD. Therefore, you can run this command to implement unaffiliated BFD detection independently of other devices.

**Prerequisites**

BFD has been enabled using the **bfd** command.

**Precautions**

If the rip bfd block, rip bfd enable, rip bfd static, and **rip bfd static binding** commands override each other, and the latest configuration overrides the previous one.This command will change the existing BFD configuration mode.


Example
-------

# Enable static BFD for a specified neighbor on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip bfd static binding 192.168.1.2

```