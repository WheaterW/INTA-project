dhcp snooping user-bind max-number(system view)
===============================================

dhcp snooping user-bind max-number(system view)

Function
--------



The **dhcp snooping user-bind max-number** command sets the maximum number of DHCP snooping binding entries that can be learned on an interface.

The **undo dhcp snooping user-bind max-number** command restores the default maximum number of DHCP snooping binding entries that can be learned on an interface.



By default, an interface can learn a maximum of 9216 DHCP snooping binding entries.


Format
------

**dhcp snooping user-bind max-number** *max-number* [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> ]

**undo dhcp snooping user-bind max-number** [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-number* | Specifies the maximum number of DHCP snooping binding entries that can be learned on an interface. | The value is an integer ranging from 1 to 9216. The default value is 9216. |
| **vlan** *vlan-id1* | Specifies the ID of the first VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vlan-id2* | Specifies the ID of the last VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The command sets the maximum number of DHCP snooping binding entries to be learned on an interface. If the number of DHCP snooping binding entries reaches the maximum value, subsequent users cannot access.When the number of entries in the DHCP snooping binding table on an interface reaches the maximum value set by the command, the DHCP snooping-enabled device fails to add entries to the binding table and sends a DHCP Release message to the DHCP server after receiving a DHCP ACK message.For the system view configuration, the sum of the maximum numbers of DHCP snooping binding entries that can be learned by all interfaces is the configured maximum number. For the VLAN view configuration, the maximum number of DHCP snooping binding entries that can be learned by any interface in the VLAN is the configured maximum number. If the configuration is performed in the system, VLAN, and interface views, the maximum number of DHCP snooping binding entries that can be learned by the interface is the smallest value among the three views.

**Prerequisites**

Before running this command, ensure that DHCP snooping has been enabled on the device using the dhcp snooping enable command and a VLAN has been configured if the vlan parameter needs to be delivered.


Example
-------

# Set the maximum number of DHCP users globally to 100.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] dhcp snooping user-bind max-number 100

```