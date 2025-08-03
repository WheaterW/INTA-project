join-prune triggered-message-cache disable (IPv6 PIM view/VPN instance IPv6 PIM view)
=====================================================================================

join-prune triggered-message-cache disable (IPv6 PIM view/VPN instance IPv6 PIM view)

Function
--------



The **join-prune triggered-message-cache disable** command disables the Join/Prune message packaging function.

The **undo join-prune triggered-message-cache disable** command enables the Join/Prune message packaging function.



By default, this function is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**join-prune triggered-message-cache disable**

**undo join-prune triggered-message-cache disable**


Parameters
----------

None

Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The efficiency for sending PIM Join/Prune messages in a package is higher than that for separately sending a large number of PIM Join/Prune messages. By default, a device sends PIM Join/Prune messages in a package. Because the size of a PIM Join/Prune message package is large, devices that have poor performance cannot receive the PIM Join/Prune message package. If such devices exist, run the **join-prune triggered-message-cache disable** command to disable the Join/Prune message packaging function to prevent packet discarding.


Example
-------

# Disable the Join/Prune message packaging function.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] join-prune triggered-message-cache disable

```