portswitch
==========

portswitch

Function
--------



The **portswitch** command changes the mode of an Ethernet interface from Layer 3 to Layer 2.

The **undo portswitch** command changes the mode of an Ethernet interface from Layer 2 to Layer 3.



By default, an Ethernet interface works in Layer 2 mode.


Format
------

**portswitch**

**undo portswitch**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, Ethernet interfaces of Layer 3 devices such as the Router operate in Layer 3 mode. If these interfaces need to be added to a VLAN or other Layer 2 configurations need to be performed on these interfaces, the mode of these interfaces needs to be switched to Layer 2.



**Precautions**



When you run this command on an interface, the mode switching configuration takes effect when only attribute configurations (such as shutdown and description configurations) or configurations that are supported on Layer 2 or Layer 3 interfaces exist on the interface. Configurations that are not supported by the interface mode after the switch should not exist.In addition, only Layer 2 Eth-Trunk interfaces can be bound to or unbound from a VLAN. If an Eth-Trunk interface is changed from the Layer 3 to Layer 2 mode, all Layer 3 functions and identifiers of the Eth-Trunk interface are disabled, and the system MAC address is used.Eth-Trunk member interfaces do not support changes of the working mode between Layer 2 and Layer 3.If an interface has sub-interfaces, interface mode switching affects forwarding of all the sub-interfaces.



The CE6885-LL in low latency mode does not support the undo portswtich command. That is, no Layer 3 service can be configured on an Eth-Trunk interface of the device.




Example
-------

# Switch the mode of Eth-Trunk 1 to Layer 2.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] portswitch

```

# Switch the mode of 100GE1/0/1 to Layer 2.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch

```