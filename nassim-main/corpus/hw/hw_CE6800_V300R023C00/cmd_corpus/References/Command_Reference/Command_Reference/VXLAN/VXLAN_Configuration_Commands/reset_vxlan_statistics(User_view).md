reset vxlan statistics(User view)
=================================

reset vxlan statistics(User view)

Function
--------



The **reset vxlan statistics** command clears IPv6 VXLAN packet statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset vxlan statistics source** *source-ipv6* **peer** *peer-ipv6* **vni** *vni-val*

**reset vxlan statistics source** *source-ipv6* **peer** *peer-ipv6*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *peer-ipv6* | Clears IPv6 VXLAN packet statistics collected based on the IPv6 address of the peer virtualized edge node. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vni** *vni-val* | Clears IPv6 VXLAN packet statistics with a specified VNI ID. | The value is an integer ranging from 1 to 16777215. |
| **source** *source-ipv6* | Clears IPv6 VXLAN packets statistics collected based on the IPv6 source address. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In cloud VPN scenarios, cloud GWs support IPv6 VXLAN packet statistics collection. To clear IPv6 VXLAN packet statistics, run the **reset vxlan statistics** command.


Example
-------

# Clear IPv6 VXLAN packet statistics collected based on the source IPv6 address 2001:DB8:1::1, VNI with the ID of 1, and the IPv6 address of the peer virtualized edge node as 2001:DB8:2::2.
```
<HUAWEI> reset vxlan statistics source 2001:DB8:1::1 peer 2001:DB8:2::2 vni 1

```