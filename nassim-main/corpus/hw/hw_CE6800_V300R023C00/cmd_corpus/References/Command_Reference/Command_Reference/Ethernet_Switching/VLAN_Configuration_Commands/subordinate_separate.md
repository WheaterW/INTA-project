subordinate separate
====================

subordinate separate

Function
--------



The **subordinate separate** command configures a separate VLAN for a principal VLAN.

The **undo subordinate separate** command deletes a separate VLAN from a principal VLAN.



By default, a VLAN created by the system is a common VLAN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**subordinate separate** *vlan-id*

**undo subordinate separate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies a VLAN ID. | The value is an integer ranging from 1 to 4094. |



Views
-----

VLAN view


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
* Group VLAN: Interfaces in the same VLAN can communicate with each other and with the interfaces in the principal VLAN. Interfaces in different subordinate VLANs cannot communicate with each other.Based on the MUX VLAN function, you can run mux-vlan command to add the enterprise server to the principal VLAN. After employees who need to communicate with each other are added to a group VLAN and employees who do not need to communicate with each other are added to a separate VLAN, all employees can access the enterprise server, but employees in the separate VLAN cannot communicate with each other. The MUX VLAN function meets enterprise requirements, resolves the problem of insufficient VLAN IDs, and facilitates network maintenance.To isolate enterprise employees but enable them to access the enterprise server, run the **subordinate separate** command and add interfaces connecting to enterprise customers' PCs to the separate VLAN.

**Prerequisites**

A principal VLAN has been created, and the principle VLAN view is displayed.The VLAN to be configured as a separate VLAN has been created.The VLAN to be configured as a separate VLAN is not configured as a super VLAN.If there are interfaces in a separate VLAN, before deleting this VLAN using the undo subordinate group command, delete the interfaces from this VLAN.

**Configuration Impact**

Only one separate VLAN can be configured for a principal VLAN. Before configuring another VLAN as a separate VLAN, run the undo **subordinate separate** command to delete the existing separate VLAN.A separate VLAN cannot be configured as a super-VLAN.

**Follow-up Procedure**

Add an interface to the separate VLAN, and enable the MUX VLAN function on this interface.

**Precautions**

The subordinate VLAN must be different from the principal VLAN.The separate VLAN and group VLAN must be different VLANs.A separate VLAN does not support Layer 2 proxy ARP.


Example
-------

# Configure VLAN 7 as the separate VLAN of VLAN 5.
```
<HUAWEI> system-view
[~HUAWEI] vlan 5
[*HUAWEI-vlan5] mux-vlan
[*HUAWEI-vlan5] subordinate separate 7

```