qos phb marking dscp disable
============================

qos phb marking dscp disable

Function
--------



The **qos phb marking dscp disable** command disables the mapping of the inner priority to the outer DSCP priority of VXLAN packets.

The **undo qos phb marking dscp disable** command enables the mapping of the inner priority to the outer DSCP priority of VXLAN packets.



By default, the mapping of the inner priority to the outer DSCP priority of VXLAN packets is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qos phb marking dscp disable**

**undo qos phb marking dscp disable**


Parameters
----------

None

Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, when a packet enters a VXLAN tunnel, the 802.1p or DSCP priority of the original packet is mapped to the internal priority. When VXLAN encapsulation is performed, the outer DSCP priority is 0. When the mapping of PHBs to DSCP priorities is enabled for outgoing packets on an Ethernet interface, the internal priority is mapped to the outer DSCP priority. In this case, the outer DSCP priority of the encapsulated packet may be different from the DSCP priority of the original packet.If the outer DSCP priority of the VXLAN packet needs to be the same as the DSCP priority of the original packet after VXLAN encapsulation is performed, you can disable the mapping of the inner priority to the outer DSCP priority of VXLAN packets. In this way, the DSCP priority of the original packet is copied as the outer DSCP priority of the VXLAN packet during VXLAN encapsulation, ensuring that the two DSCP priorities are the same.


Example
-------

# Disable the mapping of the inner priority to the outer DSCP priority of VXLAN packets.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] qos phb marking dscp disable

```