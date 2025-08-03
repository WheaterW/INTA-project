display ip-subnet-vlan vlan
===========================

display ip-subnet-vlan vlan

Function
--------



The **display ip-subnet-vlan vlan** command displays IP subnet configurations of VLANs.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ip-subnet-vlan vlan** { *vlan-id1* [ **to** *vlan-id2* ] | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Specifies the start VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **to** *vlan-id2* | Specifies the end VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **all** | Displays IP subnet configurations of all VLANs. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After dividing a LAN into VLANs based on IP subnets, run the display ip-subnet-vlan vlan command to check IP subnet configurations of VLANs.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IP subnet configurations of all VLANs.
```
<HUAWEI> display ip-subnet-vlan vlan all
IP-subnet-VLAN count: 1                 total count: 1
 ----------------------------------------------------------------
 VLAN    Index   IPAddress           SubnetMask          Priority
 ----------------------------------------------------------------
   10    1       1.1.1.1             255.255.255.0       1
 ----------------------------------------------------------------

```

**Table 1** Description of the **display ip-subnet-vlan vlan** command output
| Item | Description |
| --- | --- |
| IP-subnet-VLAN count | Configure the number of VLANs on the subnet. |
| total count | Total number of VLANs. |
| VLAN | IP subnet-based VLAN ID. |
| Index | IP subnet index. |
| IPAddress | IP subnet address. |
| SubnetMask | IP subnet mask. |
| Priority | 802.1p priority of the VLAN corresponding to the IP address. |