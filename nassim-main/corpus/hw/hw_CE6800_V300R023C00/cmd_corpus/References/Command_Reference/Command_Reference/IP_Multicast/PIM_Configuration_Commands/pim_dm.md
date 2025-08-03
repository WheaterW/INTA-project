pim dm
======

pim dm

Function
--------



The **pim dm** command enables Protocol Independent Multicast-Dense Mode (PIM-DM) on an interface.

The **undo pim dm** command restores the default setting.



By default, PIM-DM is disabled on an interface.


Format
------

**pim dm**

**undo pim dm**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A multicast network requires multicast protocols, and PIM is the most widely used intra-domain multicast protocol. PIM-DM is one of the implementations of PIM. PIM-DM resolves the problem of P2MP transmission on a small-scale network with many users.On a PIM-DM network, the **pim dm** command must be run to enable PIM-DM. Only a device with PIM-DM enabled can set up PIM neighbor relationships with neighboring devices and process protocol packets received from them.

**Prerequisites**

Multicast routing has been enabled using the **multicast routing-enable** command.

**Precautions**

The PIM modes of all interfaces in the same instance must be the same. When a device is deployed in a PIM-DM domain, you are advised to enable PIM-DM on all non-boundary interfaces.To switch between the PIM-DM and PIM-SM modes, you must disable the multicast function and then re-enable the multicast function.PIM-DM is mutually exclusive with the following features:

* PIM-DM cannot be deployed on the public network of Rosen MVPN
* Bind the interface to a VPN instance
* PIM-SM: The **pim dm** and **pim sm** commands cannot be configured in the same instance on a device.
* Load balancing
* DR switchover delay
* PIM Silent
* Neighbor filtering
* Multicast source filtering
* Layer 2 and Layer 3 mixed running
* SSM-Policy
* Multicast replication of BUM packets on NVE interfacesRunning the **undo pim dm** command will clear PIM neighbor information and protocol status on the interface. If multicast services are running on the interface, the multicast services will be affected.


Example
-------

# Enable PIM-DM on VLANIF 1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim dm

```