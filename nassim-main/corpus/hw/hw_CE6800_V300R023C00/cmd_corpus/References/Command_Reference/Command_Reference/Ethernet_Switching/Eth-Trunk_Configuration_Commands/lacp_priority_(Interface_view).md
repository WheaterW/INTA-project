lacp priority (Interface view)
==============================

lacp priority (Interface view)

Function
--------



The **lacp priority** command sets the LACP priority for an interface.

The **undo lacp priority** command restores the default LACP priority of an interface.



The default LACP priority is 32768.


Format
------

**lacp priority** *priority*

**undo lacp priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **priority** *priority* | Specifies the LACP priority of an interface. | The value is an integer ranging from 0 to 65535. The smaller the priority value, the higher the priority. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

LACP interface priorities are set to prioritize interfaces of the same device. Interfaces with higher priorities are selected as active interfaces.Two devices are connected through three interfaces on each side. After the three interfaces are bundled into an Eth-Trunk interface, the **mode lacp-static** command is used to configure the Eth-Trunk interface to work in static LACP mode. Two Eth-Trunk member interfaces are active. If you want to use an inactive interface to replace one of the active interfaces, you can take either of the following actions:

* Run the lacp priority command in the interface view to set the LACP interface priority of an inactive interface to 10 or another value as long as the LACP priority of the inactive interface is lower than that of an active interface.
* Run the lacp priority command in the interface view to set the LACP interface priority of an active interface to 180 or another value as long as the LACP priority of the active interface is higher than that of any inactive interface.

**Prerequisites**



The **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in static LACP mode.



**Precautions**



When LACP interfaces have the same priority, the Eth-Trunk selects active interfaces based on the member interface numbers in LACP. The smaller the member interface number, the higher the priority.




Example
-------

# Set the LACP priority of the member interface 100GE 1/0/1 to 1.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 10
[*HUAWEI-Eth-Trunk10] mode lacp-static
[*HUAWEI-Eth-Trunk10] trunkport 100GE 1/0/1
[*HUAWEI-Eth-Trunk10] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] lacp priority 1

```