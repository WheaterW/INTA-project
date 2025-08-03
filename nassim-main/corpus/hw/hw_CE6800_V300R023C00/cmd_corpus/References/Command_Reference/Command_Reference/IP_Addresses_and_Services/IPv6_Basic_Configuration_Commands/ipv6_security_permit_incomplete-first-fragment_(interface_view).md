ipv6 security permit incomplete-first-fragment (interface view)
===============================================================

ipv6 security permit incomplete-first-fragment (interface view)

Function
--------



The **ipv6 security permit incomplete-first-fragment** command enables the function not to check the packets with an incomplete first fragment header.

The **undo ipv6 security permit incomplete-first-fragment** command disables the function not to check the packets with an incomplete first fragment header.



By default, the function not to check the packets with an incomplete first fragment header is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 security permit incomplete-first-fragment**

**ipv6 security permit incomplete-first-fragment disable**

**undo ipv6 security permit incomplete-first-fragment**

**undo ipv6 security permit incomplete-first-fragment disable**


Parameters
----------

None

Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a router needs to process IPv6 packets with an incomplete first fragment header, the capability of receiving such packets must be reserved. To enable the function not to check the packets with an incomplete first fragment header, run the ipv6 security permit incomplete-first-fragment command.


Example
-------

# On an IPv6-capable interface, enable the function not to check the packets with an incomplete first fragment header.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk1
[*HUAWEI-Eth-Trunk1] undo portswitch
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 security permit incomplete-first-fragment

```