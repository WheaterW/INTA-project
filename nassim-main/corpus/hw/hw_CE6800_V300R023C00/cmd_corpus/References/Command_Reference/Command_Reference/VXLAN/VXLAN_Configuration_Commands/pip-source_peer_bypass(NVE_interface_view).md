pip-source peer bypass(NVE interface view)
==========================================

pip-source peer bypass(NVE interface view)

Function
--------



The **pip-source peer bypass** command configures a static bypass VXLAN IPv6 tunnel.

The **undo pip-source peer bypass** command deletes a static bypass VXLAN IPv6 tunnel.



By default, no static bypass VXLAN IPv6 tunnel is configured.

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
| *src-ip* | Specifies the peer IPv6 address of a bypass VXLAN tunnel. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *peer-ip* | Specifies the source IPv6 address of a bypass VXLAN tunnel. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a server is dual-homed to a VXLAN network through an M-LAG and a downlink of the M-LAG fails, service traffic needs to be transmitted through the peer-link between the M-LAG member devices. Therefore, in this scenario, you must run this command on the M-LAG member devices to establish a static bypass VXLAN IPv6 tunnel and divert the detoured service traffic to the peer-link.


Example
-------

# Configure the source and peer addresses of the static bypass VXLAN IPv6 tunnel.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] pip-source 2001:db8:1::1 peer 2001:db8:2::1 bypass

```