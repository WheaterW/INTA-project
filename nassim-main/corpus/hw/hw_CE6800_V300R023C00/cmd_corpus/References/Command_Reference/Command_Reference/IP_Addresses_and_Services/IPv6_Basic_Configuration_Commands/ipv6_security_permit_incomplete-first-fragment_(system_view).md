ipv6 security permit incomplete-first-fragment (system view)
============================================================

ipv6 security permit incomplete-first-fragment (system view)

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

**undo ipv6 security permit incomplete-first-fragment**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a router needs to process IPv6 packets with an incomplete first fragment header, the capability of receiving such packets must be reserved. To enable the function not to check the packets with an incomplete first fragment header, run the ipv6 security permit incomplete-first-fragment command.


Example
-------

# Enable the function not to check the packets with an incomplete first fragment header.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 security permit incomplete-first-fragment

```