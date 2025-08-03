mld snooping router-learning disable
====================================

mld snooping router-learning disable

Function
--------



The **mld snooping router-learning disable** command disables router interfaces from dynamically learning forwarding entries.

The **undo mld snooping router-learning disable** command enables router interfaces to dynamically learn forwarding entries.



By default, router interfaces are enabled to dynamically learn forwarding entries.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping router-learning disable**

**undo mld snooping router-learning disable**


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

On a device enabled with MLD snooping, interfaces that receive MLD general Query messages with source IP addresses other than 0::0 or Protocol Independent Multicast (PIM) Hello packets are considered as dynamic router interfaces. The device records all router interfaces in a list. Using this mechanism, the device is incapable of controlling data forwarding to users. To resolve this issue, run the undo mld snooping router-learning disable command to disable router interfaces in a VLAN from dynamically learning forwarding entries.


Example
-------

# Enable interfaces in VLAN 10 to dynamically learn forwarding entries.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] undo mld snooping router-learning disable

```