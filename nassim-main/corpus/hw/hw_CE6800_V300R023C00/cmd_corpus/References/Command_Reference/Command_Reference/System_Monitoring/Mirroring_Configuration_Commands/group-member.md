group-member
============

group-member

Function
--------



The **group-member** command adds a specified interface to an observing port group.

The **undo group-member** command deletes a specified interface from an observing port group.



By default, no interface is added to an observing port group.


Format
------

**group-member** { { *interface-type* *interface-number1* | *interface-name1* } [ **to** { *interface-type* *interface-number2* | *interface-name2* } ] } &<1-8>

**undo group-member** { *interface-type* *interface-number1* | *interface-name1* } [ **to** { *interface-type* *interface-number2* | *interface-name2* } ] &<1-8>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of ports to be added to an observing port group. | - |
| *interface-number1* | Specifies the number of ports to be added to an observing port group. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *interface-name1* | Specifies the name of a port to be added to an observing port group. | - |
| *interface-number2* | Specifies the number of ports to be added to an observing port group. | - |
| *interface-name2* | Specifies the name of a port to be added to an observing port group. | - |



Views
-----

observe-port-group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If users want to mirror packets to multiple observing ports, add these ports to an observing port group. The mirrored packets are then copied to all the member ports of the observing port group.

**Prerequisites**

An observing port group has been created using the **observe-port group** command.

**Precautions**

* Mirroring port, observing port, and Eth-Trunk member port cannot be added to an observing port group.
* A member port added to an observing port group cannot be configured as an observing port.
* A maximum of 64 member ports can be added to an observing port group.

Example
-------

# Add 100GE1/0/1 to 100GE1/0/4 to observing port group 1.
```
<HUAWEI> system-view
[~HUAWEI] observe-port group 1
[*HUAWEI-observe-port-group-1] group-member 100GE 1/0/1 to 100GE 1/0/4

```