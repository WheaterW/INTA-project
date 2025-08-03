m-lag peer-link reserved
========================

m-lag peer-link reserved

Function
--------



The **m-lag peer-link reserved** command configures the VLAN to contain only the peer-link interface.

The undo m-lag peer-link reserved command restores the default configuration and allows the VLAN to include other Layer 2 interfaces.



By default, a VLAN can contain other Layer 2 interfaces in addition to the peer-link interface.


Format
------

**m-lag peer-link reserved**

**undo m-lag peer-link reserved**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable traffic and protocol packets in a VLAN to be forwarded only through the peer-link (but not through other Layer 2 interfaces), run the **m-lag peer-link reserved** command. For example, in the multicast scenario where an M-LAG is connected to a Layer 3 network, if the upstream device or link of the M-LAG fails, multicast traffic and protocol packets are forwarded only through the peer-link of the VLAN.

**Precautions**

The **m-lag peer-link reserved** command configured in the VLAN view is mutually exclusive with adding a Layer 2 interface to the VLAN.The **m-lag peer-link reserved** command configured in the VLAN view is mutually exclusive with the **port vlan exclude** command.A maximum of 1024 VLANs can be configured with this command.


Example
-------

# Configure a VLAN to contain only the peer-link interface in the VLAN view.
```
<HUAWEI> system-view
[~HUAWEI] vlan 2
[*HUAWEI-vlan2] m-lag peer-link reserved

```