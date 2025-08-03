pip-source peer bypass
======================

pip-source peer bypass

Function
--------



The **pip-source peer bypass** command configures a static bypass VXLAN tunnel.

The **undo pip-source peer bypass** command deletes a static bypass VXLAN tunnel.



By default, no bypass vxlan tunnel is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pip-source** *src-ip* **peer** *peer-ip* **bypass**

**undo pip-source** *src-ip* **peer** *peer-ip* **bypass**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *src-ip* | Specifies the source IP address of a bypass VXLAN tunnel. | The value is in dotted decimal notation. |
| *peer-ip* | Specifies the peer IP address of a bypass VXLAN tunnel. | The value is in dotted decimal notation. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a VXLAN scenario with M-LAG configured, if one user-side link fails, service traffic is transmitted through the peer-link between the M-LAG devices. In this scenario, the pip-source peer bypass command must berun on M-LAG devices to create a static bypass VXLAN tunnel to divert traffic to the peer-link.


Example
-------

# Configure a source address and a peer address for a static bypass VXLAN tunnel.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] pip-source 1.1.1.1 peer 2.2.2.2 bypass

```