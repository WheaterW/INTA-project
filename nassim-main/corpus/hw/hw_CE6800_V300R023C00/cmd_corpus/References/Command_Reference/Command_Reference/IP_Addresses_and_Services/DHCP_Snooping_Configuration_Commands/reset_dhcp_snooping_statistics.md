reset dhcp snooping statistics
==============================

reset dhcp snooping statistics

Function
--------



The **reset dhcp snooping statistics** command clears DHCP snooping statistics.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**reset dhcp snooping statistics** { **global** | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **bridge-domain** *bd-id* }

For CE6820H, CE6820H-K, CE6820S, CE6885-LL (low latency mode):

**reset dhcp snooping statistics** { **global** | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **global** | Clears global DHCP snooping statistics. | - |
| **interface** *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| *interface-name* | interface-name specifies the name of an interface. | The value is a string of 1 to 128 case-sensitive characters. It cannot contain spaces. |
| **vlan** *vlan-id* | Clears DHCP snooping statistics in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **bridge-domain** *bd-id* | Clears DHCP snooping statistics in a specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer that ranges from 1 to 16777215. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If packet statistics are generated after DHCP snooping is enabled, you can run the reset dhcp snooping statistics command to clear the statistics.

**Precautions**

If both interface and vlan are specified, the specified interface must have been added to the specified VLAN. The reset dhcp snooping statistics command is used to clear DHCP snooping statistics in the VLAN to which the specified interface is added.


Example
-------

# Clear DHCP snooping statistics on 100GE1/0/1.
```
<HUAWEI> reset dhcp snooping statistics interface 100GE1/0/1

```