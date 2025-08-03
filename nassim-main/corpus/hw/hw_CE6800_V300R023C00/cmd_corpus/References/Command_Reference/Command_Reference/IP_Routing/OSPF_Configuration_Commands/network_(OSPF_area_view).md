network (OSPF area view)
========================

network (OSPF area view)

Function
--------



The **network** command specifies the interface that runs OSPF and the area to which the interface belongs.

The **undo network** command disables OSPF from an interface.



By default, the interface does not belong to any area.


Format
------

**network** *address* *wildcard-mask*

**network** *address* *wildcard-mask* **description** *text*

**undo network** *address* *wildcard-mask*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *address* | Specifies the address of a network segment where an interface resides. | The value is in dotted decimal notation. |
| *wildcard-mask* | Specifies the wildcard mask of an IP address, which is similar to the reversed form of an IP address mask. "1" represents that the corresponding bit in the IP address is ignored, and "0" represents that this bit must be reserved. | The value is in dotted decimal notation. |
| **description** *text* | Specifies the description of an OSPF network segment. | The value is a string of 1 to 80 case-sensitive characters, spaces supported. |



Views
-----

OSPF area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Using the address and wildcard-mask parameters, you can configure one or more interfaces in an area.OSPF can run on an interface only when the following conditions are met:

* The mask length of the IP address of the interface is greater than or equal to the mask length specified in the network (OSPF) command.
* The primary IP address of the interface must be in the range of the network segment specified in the network (OSPF) command. Otherwise, even if the secondary IP address of the interface is in the range of the network segment specified in the network (OSPF) command, the interface does not run OSPF.
* The IP address of the interface is a fixed address specified using the **ip address** command.

If wildcard-mask is set to all 0s in the **network** command and the IP address of the interface is the same as that configured in the **network address** command, the interface also runs OSPF.

**Precautions**

* For the same network address wildcard-mask, the last description specified by description takes effect.
* For the loopback interface, by default, OSPF advertises its IP address through 32-bit host routes, which is irrelevant to the mask length of the IP address on the interface.
* To advertise the network segment route of a loopback interface, run the ospf network-type command to configure the network type as broadcast or NBMA.
* If a large number of interfaces that do not need to run OSPF services borrow the IP address of a loopback interface, running the **ospf enable** command rather than the **network** command on the loopback interface is recommended. If the **network** command is run on the loopback interface, the configurations of some commands, such as the command used to configure, delete, or modify the loopback interface's IP address or the undo **network** command, may fail to be delivered, and device performance is affected after a master/slave main control board switchover is performed.


Example
-------

# Specify the primary IP address of the interface that runs OSPF to be in the network segment of 192.168.1.0/24, and the ID of the OSPF area where the interface resides to 2. In addition, specify the description for the network segment.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] area 2
[*HUAWEI-ospf-100-area-0.0.0.2] network 192.168.1.0 0.0.0.255 description this network is connected to Beijing

```