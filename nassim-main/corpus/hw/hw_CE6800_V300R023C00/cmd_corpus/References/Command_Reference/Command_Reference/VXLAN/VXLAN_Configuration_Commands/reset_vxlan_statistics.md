reset vxlan statistics
======================

reset vxlan statistics

Function
--------



The **reset vxlan statistics** command clears VXLAN packet statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset vxlan statistics source** *source-ip* **peer** *peer-ip* **vni** *vni-id*

**reset vxlan statistics vni** *vni-id*

**reset vxlan statistics source** *source-ip* **peer** *peer-ip*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *peer-ip* | Clears VXLAN packet statistics collected based on the IP address of the peer virtualized edge node. | The value is in dotted decimal notation. |
| **vni** | Clears VXLAN packets statistics collected based on a specified VNI ID. | The value is an integer ranging from 1 to 16777215. |
| *vni-id* | Specifies the value of VNI ID. | The value is an integer ranging from 1 to 16777215. |
| **source** *source-ip* | Clears VXLAN packets statistics collected based on the source IP address. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In cloud VPN scenarios, cloud GWs support VXLAN packet statistics collection. To clear VXLAN packet statistics, run the **reset vxlan statistics** command.

**Precautions**

After the **reset vxlan statistics** command is run, VXLAN packet statistics on a device are cleared and cannot be restored. Exercise caution when you run this command.


Example
-------

# Clear downstream VXLAN packet statistics collected based on the source IP address 10.1.1.1, remote VTEP IP address 10.2.2.2.
```
<HUAWEI> reset vxlan statistics source 10.1.1.1 peer 10.2.2.2

```

# Clear VXLAN packet statistics collected based on the VNI with the ID of 1.
```
<HUAWEI> reset vxlan statistics vni 1

```

# Clear VXLAN packet statistics collected based on the source IP address 1.1.1.1, VNI with the ID of 1, and the IP address of the peer virtualized edge node as 1.1.1.2.
```
<HUAWEI> reset vxlan statistics source 1.1.1.1 peer 1.1.1.2 vni 1

```