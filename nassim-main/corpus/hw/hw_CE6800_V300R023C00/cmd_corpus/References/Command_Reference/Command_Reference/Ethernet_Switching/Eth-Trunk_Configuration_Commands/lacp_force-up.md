lacp force-up
=============

lacp force-up

Function
--------



The **lacp force-up** command configures an interface to stay in the force-up state.

The **undo lacp force-up** command cancels the force-up state configured for an interface.

The **lacp force-up extension** command enables the force-up extension function on an interface.



By default, an interface does not have the force-up state configured.


Format
------

**lacp force-up** [ **extension** ]

**undo lacp force-up** [ **extension** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **extension** | Enable the extended function. | - |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In a scenario where a device directly connects to a server through an interface that has been added as a member of an Eth-Trunk interface in static LACP mode, if the server restarts or goes online and the Eth-Trunk member interface does not receive any LACPDU within the specified timeout period, the interface goes down. To enable the interface to continue to forward service traffic, run the **lacp force-up** command to forcibly set the interface state to force-up. To prevent the force-up function from causing packet loss when server and device interfaces are not correctly connected or the interface is falsely removed from the Eth-Trunk interface, run the **lacp force-up extension** command to enable the force-up extension function on the interface. After the extension function is enabled, the force-up function can take effect only once. However, if the interface state changes from down to up in the future, the function can take effect again.



**Precautions**



This command is used when a Huawei device interconnects to a server.After this command is run, the force-up state takes effect only when all the member interfaces of the Eth-Trunk interface in static LACP mode time out in receipt of LACPDUs.When all the Eth-Trunk member interfaces' force-up state takes effect, the minimum number of active member links configured using the **least active-linknumber link-number** command still takes effect, but the maximum number of active member links configured using the **max active-linknumber link-number** command stops taking effect.This command does not support Layer 3 forwarding. Only Eth-Trunk member interfaces in force-up state can forward Layer 2 traffic through hardware. Packets sent to the CPU cannot be forwarded through the Eth-Trunk.




Example
-------

# Set 100GE 1/0/1 to force-up.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static
[*HUAWEI-Eth-Trunk1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] lacp force-up

```