dhcp snooping trusted tunnel(Bridge domain view)
================================================

dhcp snooping trusted tunnel(Bridge domain view)

Function
--------



The **dhcp snooping trusted tunnel** command configures a tunnel in a BD as a trusted tunnel.

The **undo dhcp snooping trusted tunnel** command configures a tunnel in a BD as an untrusted tunnel.



By default, an interface is untrusted.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcp snooping trusted tunnel**

**undo dhcp snooping trusted tunnel**


Parameters
----------

None

Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable DHCP clients to obtain IP addresses from authorized DHCP servers, the DHCP snooping security mechanism allows you to configure trusted and untrusted interfaces. The trusted interface forwards DHCP messages, and untrusted interfaces discard DHCP ACK and DHCP Offer messages returned from DHCP servers. The interface directly or indirectly connected to the DHCP server trusted by the administrator needs to be configured as the trusted interface, and other interfaces are configured as untrusted interfaces. This ensures that DHCP clients can obtain IP addresses only from authorized DHCP servers and prevents bogus DHCP servers from assigning IP addresses to DHCP clients. DHCPv6 packets are processed in the same way as in this scenario.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.


Example
-------

# Configure the tunnel bound to bd1 as a trusted tunnel.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] bridge-domain 1
[*HUAWEI-bd1] dhcp snooping trusted tunnel

```