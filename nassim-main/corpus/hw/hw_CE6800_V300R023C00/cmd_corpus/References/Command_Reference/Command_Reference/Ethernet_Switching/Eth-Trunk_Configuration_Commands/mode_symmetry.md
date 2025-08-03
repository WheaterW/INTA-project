mode symmetry
=============

mode symmetry

Function
--------



The **mode symmetry** command enables Eth-Trunk-based and ECMP-based forwarding of packets with the same source and destination addresses.

The **undo mode symmetry** command disables Eth-Trunk-based and ECMP-based forwarding of packets with the same source and destination addresses.



By default, an Eth-Trunk interface is disabled from forwarding packets with the same source and destination addresses.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mode symmetry**

**undo mode symmetry**


Parameters
----------

None

Views
-----

Load balancing profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Bidirectional data packets with the same source and destination addresses of the same network connection must be forwarded by the same outbound interface. During network traffic analysis, a device is required to analyze bidirectional traffic between communicating parties. During this process, the packets of such communicating parties must be forwarded to the same device for analysis, which requires the device to forward packets with the source and destination addresses through the same outbound interface.An Eth-Trunk interface can be enabled to forward packets with the same source and destination addresses. When traffic is copied to the analysis server in traffic diversion mode, the packets that meet the conditions are sent out through a fixed member interface of the Eth-Trunk interface based on the reverse of the source and destination IP addresses or source and destination MAC addresses of the packets. The traffic is forwarded to the connected analysis server so that the same server can analyze bidirectional traffic.

**Precautions**

* The configuration takes effect on all Eth-Trunk interfaces on the device.


Example
-------

# Configure the function of forwarding packets with the same source and destination addresses.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile default
[~HUAWEI-load-balance-profile-default] mode symmetry

```