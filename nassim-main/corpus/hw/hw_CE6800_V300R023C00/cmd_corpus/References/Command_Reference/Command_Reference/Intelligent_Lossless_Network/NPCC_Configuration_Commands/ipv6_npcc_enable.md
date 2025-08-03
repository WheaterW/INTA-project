ipv6 npcc enable
================

ipv6 npcc enable

Function
--------



The **ipv6 npcc enable** command enables IPv6 NPCC in the interface view.

The **undo ipv6 npcc enable** command disables IPv6 NPCC in the interface view.



By default, IPv6 NPCC is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**ipv6 npcc enable**

**undo ipv6 npcc enable**


Parameters
----------

None

Views
-----

100GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the lossless queue for IPv6 NPCC is specified globally, you need to enable IPv6 NPCC in the interface view to implement NPCC for IPv6 traffic.

**Precautions**

* IPv6 NPCC and dynamic load balancing are mutually exclusive.
* IPv6 NPCC and iQCN are mutually exclusive.
* VXLAN is not supported.
* After IPv6 NPCC is enabled on an interface, RoCEv2 packets in queues that are not enabled with IPv6 NPCC are also counted in the RoCEv2 flow table maintained by IPv6 NPCC.

Example
-------

# Enable IPv6 NPCC on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ipv6 npcc enable

```