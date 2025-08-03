vxlan vni force-redirect interface
==================================

vxlan vni force-redirect interface

Function
--------



The **vxlan vni force-redirect interface** command configures the redirection outbound interface used to forward packets after forcible VXLAN decapsulation.

The **undo vxlan vni force-redirect interface** command restores the default configuration.



By default, the original outbound interface is used to forward packets after forcible VXLAN decapsulation.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan vni** *vni-id1* [ **to** *vni-id2* ] **force-redirect** **interface** { *interface-name* | *interface-type* *interface-num* }

**undo vxlan vni** *vni-id1* [ **to** *vni-id2* ] **force-redirect** **interface** { *interface-name* | *interface-type* *interface-num* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-id1* | Specifies the start VNI value. | The value is an integer that ranges from 1 to 16777215. |
| **to** *vni-id2* | Specifies the end VNI value. | The value is an integer that ranges from 1 to 16777215. |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-num* | Specifies the number of an interface. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a device needs to send VXLAN packets to the analyzer, you can run the **vxlan force-decapsulation enable** command to enable forcible VXLAN decapsulation on the inbound interface of VXLAN packets to reduce the load of the analyzer. To enable the analyzer to receive only specified original packets, run the **vxlan vni force-redirect interface** command to configure the redirection outbound interface for packets after forcible VXLAN decapsulation. This command binds a VNI to a redirection outbound interface. When forcibly decapsulating a VXLAN packet, the device obtains the VNI of the VXLAN packet. After decapsulating the VXLAN packet, the device forwards the original packet to the analyzer through the redirection outbound interface.


Example
-------

# Configure the redirection outbound interface used to forward packets after forcible VXLAN decapsulation.
```
<HUAWEI> system-view
[~HUAWEI] vxlan vni 2000 to 3000 force-redirect interface 100GE 1/0/1

```