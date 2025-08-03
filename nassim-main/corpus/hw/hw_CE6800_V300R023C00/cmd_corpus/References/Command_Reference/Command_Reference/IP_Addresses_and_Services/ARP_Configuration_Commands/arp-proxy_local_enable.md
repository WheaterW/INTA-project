arp-proxy local enable
======================

arp-proxy local enable

Function
--------



The **arp-proxy local enable** command enables local proxy ARP so that isolated hosts in a bridge domain (BD) can communicate with each other.

The **undo arp-proxy local enable** command disables local proxy ARP.



By default, local proxy ARP is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp-proxy local enable**

**undo arp-proxy local enable**


Parameters
----------

None

Views
-----

VBDIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the EVC model, after receiving packets, the member interfaces of a BD broadcast these packets in the BD. To reduce broadcast traffic, network administrators usually run the isolate enable command in a BD where users do not need to communicate with each other. After this command is run, users on different access interfaces in the BD are isolated and cannot communicate with each other at Layer 2. However, as services become more diverse and keep increasing, users have growing needs for intra-BD communication. To allow isolated users in a BD to communicate, configure local proxy ARP on the VBDIF interface of the BD.

**Precautions**



Currently, local proxy ARP cannot be configured in the following situations:

The arp l2-proxy enable command has been run in the BD view of the VBDIF interface to be configured with local proxy ARP.




Example
-------

# Enable local proxy ARP on a VBDIF interface.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] quit
[*HUAWEI] interface vbdif 10
[*HUAWEI-Vbdif10] arp-proxy local enable

```