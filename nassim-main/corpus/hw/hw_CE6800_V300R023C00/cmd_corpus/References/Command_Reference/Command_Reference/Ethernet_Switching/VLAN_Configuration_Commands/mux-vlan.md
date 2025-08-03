mux-vlan
========

mux-vlan

Function
--------



The **mux-vlan** command configures a VLAN as the principal VLAN in a MUX VLAN.

The **undo mux-vlan** command deletes the principal VLAN in a MUX VLAN.



By default, a VLAN is a common VLAN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mux-vlan**

**undo mux-vlan**


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

On an enterprise intranet, both employees and customers of the enterprise need to access the enterprise server, and some employees need to communicate with each other. To meet this requirement, you can configure a VLAN for the enterprise server, another VLAN for employees with the communication requirement, and different VLANs for employees without the communication requirement. This consumes a lot of VLAN IDs, and increases maintenance work for the network administrator.To resolve the preceding problem, configure a MUX VLAN function on a switch. The MUX VLAN provides Layer 2 traffic isolation within a VLAN. The MUX VLAN provides the following types of VLANs:

* Principal VLAN: Interfaces in the principal VLAN can communicate with all interfaces in the MUX VLAN.
* Subordinate VLAN
* Separate VLAN: Interfaces in the same VLAN cannot communicate with each other, but can communicate with interfaces in the principal VLAN. Interfaces in different subordinate VLANs cannot communicate with each other.
* Group VLAN: Interfaces in the same VLAN can communicate with each other and with the interfaces in the principal VLAN. Interfaces in different subordinate VLANs cannot communicate with each other.Based on the MUX VLAN function, you can run mux-vlan command to add the enterprise server to the principal VLAN. After employees who need to communicate with each other are added to a group VLAN and employees who do not need to communicate with each other are added to a separate VLAN, all employees can access the enterprise server, but employees in the separate VLAN cannot communicate with each other. The MUX VLAN function meets enterprise requirements, resolves the problem of insufficient VLAN IDs, and facilitates network maintenance.

**Follow-up Procedure**

Configure subordinate VLANs, and enable the MUX VLAN function.

**Precautions**

A principal VLAN cannot be configured as a super-VLAN or sub-VLAN.A principal VLAN cannot be configured as a subordinate VLAN of other VLANs.The principal VLAN does not support Layer 2 proxy ARP.


Example
-------

# Configure VLAN 5 as the principal VLAN in the MUX VLAN.
```
<HUAWEI> system-view
[~HUAWEI] vlan 5
[*HUAWEI-vlan5] mux-vlan

```