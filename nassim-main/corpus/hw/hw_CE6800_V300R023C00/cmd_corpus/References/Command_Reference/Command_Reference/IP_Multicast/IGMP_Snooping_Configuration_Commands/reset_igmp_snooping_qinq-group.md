reset igmp snooping qinq-group
==============================

reset igmp snooping qinq-group

Function
--------



The **reset igmp snooping qinq-group** command deletes multicast entries on dot1q termination sub-interfaces.




Format
------

**reset igmp snooping qinq-group** { **all** | **interface** { *interface-type* *interface-number* | *interface-name* } [ **pe-vid** *pe-vid* [ *group-address* [ **mask** { *group-mask* | *mask-length* } ] [ *source-address* [ **mask** { *source-mask* | *source-mask-length* } ] ] ] ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Deletes multicast entries on all QinQ or dot1q termination sub-interfaces. | - |
| **interface** | Deletes multicast entries on a specified QinQ or dot1q termination sub-interface. | - |
| *interface-type* *interface-number* | Specifies the type and number of an interface. | - |
| **pe-vid** *pe-vid* | Specifies the ID of the VLAN to which a PE belongs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *group-address* | Specifies a multicast group address. | This value is in dotted decimal notation. |
| **mask** | Indicates a mask. | - |
| *group-mask* | Specifies the mask of a multicast group address. | This value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of a multicast group address. | The value is an integer ranging from 0 to 32. |
| *source-address* | Specifies a multicast source address. | This value is in dotted decimal notation. |
| *source-mask* | Specifies the mask of a multicast source address. | This value is in dotted decimal notation. |
| *source-mask-length* | Specifies the mask length of a multicast source address. | The value is an integer ranging from 0 to 32. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If multicast entries on all or a specified dot1q termination sub-interface are unnecessary, run the reset igmp snooping qinq-group command to delete the multicast entries.


Example
-------

# Delete multicast entries on all dot1q termination sub-interfaces.
```
<HUAWEI> reset igmp snooping qinq-group all

```

# Delete multicast entries on a specified dot1q termination sub-interface.
```
<HUAWEI> reset igmp snooping qinq-group interface 100GE1/0/1.1

```