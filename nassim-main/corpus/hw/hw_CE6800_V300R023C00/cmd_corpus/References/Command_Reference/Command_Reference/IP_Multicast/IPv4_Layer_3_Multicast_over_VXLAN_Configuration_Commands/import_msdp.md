import msdp
===========

import msdp

Function
--------



The **import msdp** command enables the function of transmitting (S, G) entry information in Multicast Source Discovery Protocol (MSDP) Source Active (SA) messages to the remote PE through BGP Source Active A-D routes.

The **undo import msdp** command restores the default configuration.



By default, (S, G) entry information in MSDP SA messages are not transmitted to the remote PE through BGP Source Active A-D routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**import msdp**

**undo import msdp**


Parameters
----------

None

Views
-----

VPN instance IPv4 address family MVPN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If PIM-SM MDT setup does not span MVPN tunnels, a rendezvous point (RP) can be deployed on a PE or CE. If a CE is configured as an RP, the CE needs to establish an MSDP peer relationship with its connected PE and send (S, G) entry information to the PE through MSDP SA messages. To advertise (S, G) entries to the remote PE through BGP Source Active A-D routes, run the **import msdp** command.

**Precautions**

If a PE is configured as a VPN instance's RP, you do not need to run the **import msdp** command.


Example
-------

# Enable the function of transmitting (S, G) entry information in MSDP SA messages to the remote PE through BGP Source Active A-D routes.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 2.2.2.2
[*HUAWEI] ip vpn-instance mcast1
[*HUAWEI-vpn-instance-mcast1] ipv4-family
[*HUAWEI-vpn-instance-mcast1-af-ipv4] route-distinguisher 1:1
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 2
[*HUAWEI-vpn-instance-mcast1-af-ipv4] mvpn
[*HUAWEI-vpn-instance-mcast1-af-ipv4-mvpn] import msdp

```