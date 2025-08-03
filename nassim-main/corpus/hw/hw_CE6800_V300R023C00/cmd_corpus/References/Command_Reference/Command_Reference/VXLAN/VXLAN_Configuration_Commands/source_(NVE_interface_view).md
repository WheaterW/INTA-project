source (NVE interface view)
===========================

source (NVE interface view)

Function
--------



The **source** command configures an IP address for a source VXLAN tunnel endpoint (VTEP).

The **undo source** command deletes the IP address of a source VTEP.



By default, no IP address is configured for any source VTEP.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**source** *ip-address*

**undo source** [ *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies an IP address for a source VTEP. | The value is in dotted decimal notation. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A VTEP is a VXLAN tunnel endpoint that encapsulates or decapsulates VXLAN packets. It is represented by a network virtualization edge (NVE).To configure an IP address for a source VTEP, run the **source** command. In VXLAN packets, the source IP address is the source VTEP's IP address, and the destination IP address is a remote VTEP's IP address. This pair of VTEP addresses corresponds to a VXLAN tunnel.

**Precautions**

A physical or loopback interface's IP address can be specified for a source VTEP. In this case, using the loopback interface address is recommended.Generally, you need to configure different VTEP addresses for the NVE interfaces of different devices; otherwise, traffic forwarding error may occur. However, in special scenarios where multiple devices are required to function as one NVE (such as an M-LAG dual-homing access scenario), you need to configure the same VTEP address for these devices' NVE interfaces.


Example
-------

# Configure the IP address 1.1.1.1 for a source VTEP.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] source 1.1.1.1

```