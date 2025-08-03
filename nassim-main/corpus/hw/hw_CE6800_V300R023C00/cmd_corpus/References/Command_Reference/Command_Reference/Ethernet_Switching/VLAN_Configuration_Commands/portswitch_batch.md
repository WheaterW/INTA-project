portswitch batch
================

portswitch batch

Function
--------



The **portswitch batch** command changes the mode of Ethernet interfaces from Layer 3 to Layer 2 in batches.

The **undo portswitch batch** command changes the mode of Ethernet interfaces from Layer 2 to Layer 3 in batches.



By default, an Ethernet interface works in Layer 2 mode.


Format
------

**portswitch batch** *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10>

**portswitch batch** *interface-name*

**undo portswitch batch** *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10>

**undo portswitch batch** *interface-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies an interface type. | - |
| *interface-number1* | Specifies the start interface. | - |
| *interface-number2* | Specifies the end interface. | - |
| *interface-name* | Specifies an interface name. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, Ethernet interfaces of Layer 3 devices such as the Router operate in Layer 3 mode. If these interfaces need to be added to a VLAN or other Layer 2 configurations need to be performed on these interfaces, the mode of these interfaces needs to be switched to Layer 2.If the mode of multiple interfaces needs to be changed in batches, either from Layer 3 to Layer 2, or from Layer 2 to Layer 3, run the portswitch batch or the undo **portswitch batch** command.



**Precautions**

When you run this command on an interface, the mode switching configuration takes effect when only attribute configurations (such as shutdown and description configurations) or configurations that are supported on Layer 2 or Layer 3 interfaces exist on the interface. Configurations that are not supported by the interface mode after the switch should not exist.When an interface range is specified, ensure that the following conditions are met:

* The types of the interfaces are the same.
* The interfaces in the range must exist.
* If the **portswitch batch** command is run more than once, all configurations take effect.Eth-Trunk member interfaces do not support changes of the working mode between Layer 2 and Layer 3.In addition, only Layer 2 Eth-Trunk interfaces can be bound to or unbound from a VLAN. If an Eth-Trunk interface is changed from the Layer 3 to Layer 2 mode, all Layer 3 functions and identifiers of the Eth-Trunk interface are disabled, and the system MAC address is used.


Example
-------

# Change the mode of 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3 to Layer 2.
```
<HUAWEI> system-view
[~HUAWEI] portswitch batch 100GE 1/0/1 1/0/2 1/0/3

```