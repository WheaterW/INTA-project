port priority
=============

port priority

Function
--------



The **port priority** command configures the priority for an interface.

The **undo port priority** command restores the default priority of an interface.



By default, the priority of an interface is 0.


Format
------

**port priority** *priority-value*

**undo port priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority-value* | Specifies the priority of an interface. | The value is an integer that ranges from 0 to 7. The default value is 0. A larger value indicates a higher priority. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the tag field of a VLAN frame, three bits are used to record the 802.1p priority of the frame. The 802.1p priority is used as a reference for QoS differentiated services.

* If an interface receives untagged packets, the interface priority needs to be added to the packets during internal forwarding.
* If the trust upstream none command is configured on an interface, the device performs mapping based on the interface priority configured using the **port priority** command.

**Precautions**

* When an Ethernet interface switches to Layer 3 mode, you cannot configure a priority for the Ethernet interface. This Ethernet interface uses priority 0.
* The **port priority** command is invalid if the current interface is a member interface of an Eth-Trunk.
* If you run the **port priority** command multiple times in the same interface view, only the latest configuration takes effect.


Example
-------

# Set the priority of 100GE1/0/1 to 1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port priority 1

```