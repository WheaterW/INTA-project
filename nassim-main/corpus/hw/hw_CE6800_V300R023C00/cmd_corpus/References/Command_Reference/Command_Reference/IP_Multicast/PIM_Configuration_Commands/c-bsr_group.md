c-bsr group
===========

c-bsr group

Function
--------



The **c-bsr group** command configures a candidate-bootstrap router (C-BSR) for the BSR administrative domain that serves a specified multicast group.

The **undo c-bsr group** command restores the default configuration.



By default, no C-BSR is configured for a BSR administrative domain.


Format
------

**c-bsr group** *group-address* { *mask-length* | *mask* } [ **hash-length** *hash-length* | **priority** *priority* ] \*

**undo c-bsr group** *group-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Specifies a multicast group address. | The value ranges from 239.0.0.0 to 239.255.255.255, in dotted decimal notation. |
| *mask-length* | Specifies the mask length of a multicast address. | The value is an integer ranging from 8 to 32. |
| *mask* | Specifies the mask of a multicast group address. | The value is an integer ranging from 8 to 32. |
| **hash-length** *hash-length* | Specifies the hash mask length for a C-BSR in the BSR administrative domain that serves a specified multicast group. | The value is an integer ranging from 0 to 32. The default value is 30. |
| **priority** *priority* | Specifies the priority for a C-BSR in the BSR administrative domain that serves a specified multicast group. A larger value indicates a higher C-BSR priority. | The value is an integer ranging from 0 to 255. The default value is 0. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, a PIM-SM domain has only one BSR and the entire PIM-SM domain is managed by the BSR. A PIM-SM domain can be divided into multiple BSR administrative domains and a global domain to facilitate network management. This can reduce the workload of a single BSR and provide dedicated services for users in a specific domain by using private group addresses.Each BSR administrative domain maintains a BSR that serves the multicast groups on the network segment 239.0.0.0/8. The multicast packets for the groups on this network segment cannot go across the border of the BSR administrative domain. The multicast groups that do not belong to any BSR administrative domain belong to the global domain. The global domain maintains a BSR that serves all the remaining multicast groups, that is, multicast groups beyond 239.0.0.0/8.A BSR administrative domain is similar to a VPN in unicast and multicast address 239.0.0.0/8 is equivalent to unicast address 10.0.0.0/8. Other multicast group addresses are common on the public network and cannot conflict with each other. After a PIM-SM domain is divided into different BSR administrative domains, each BSR administrative domain is equivalent to a VPN, and the multicast address in a BSR administrative domain must be 239.0.0.0/8. The same multicast group address can be used in different BSR administration domains.

**Prerequisites**

The BSR administrative domain function has been enabled using the **c-bsr admin-scope** command.

**Configuration Impact**

If the c-bsr group command is run more than once, the latest configuration overrides the previous one.After the undo pim command or the undo multicast routing-enable command is run in the system view, C-BSRs of a BSR administrative domain are automatically disabled.

**Precautions**

Each BSR administrative domain serves a multicast group address range. Multicast packets whose group addresses are within a specified range can be transmitted only within the corresponding BSR administrative domain


Example
-------

# In the public network instance, configure a C-BSR in the BSR administrative domain that serves the multicast group 239.0.0.0/8, and set the priority of the C-BSR to 10.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] c-bsr group 239.0.0.0 255.0.0.0 priority 10

```