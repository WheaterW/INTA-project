gtp teid
========

gtp teid

Function
--------



The **gtp teid** command enables the TEID-based hash function for GTP packets.

The **undo gtp teid** command restores the default configuration.



By default, the TEID-based hash function is disabled for GTP packets.


Format
------

**gtp teid**

**undo gtp teid**


Parameters
----------

None

Views
-----

ECMP load balancing view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When GTP packets are forwarded based on the hash factors configured in the system, uneven load balancing may occur.To solve this problem, run the **gtp teid** command to enable the TEID-based hash function for GTP packets so that the packets can be forwarded evenly.

**Precautions**

* This command takes effect only after the Layer 4 port number is enabled. For common Layer 3 forwarding, enable l4-src-port or l4-dst-port in ip src-ip dst-ip l4-src-port l4-dst-port. For tunnel bypass forwarding, enable inner-l4-sport or inner-l4-dport in ip-tunnel inner-src-ip inner-dst-ip inner-l4-sport inner-l4-dport or vxlan inner-src-ip inner-dst-ip inner-l4-sport inner-l4-dport inner-protocol.
* If l4-src-port/inner-l4-sport is configured, the most significant 16 bits of the TEID are used for load balancing; if l4-dst-port/inner-l4-dport is configured, the least significant 16 bits of the TEID are used for load balancing; if l4-src-port/inner-l4-sport and l4-dst-port/inner-l4-dport are configured, the 32 bits of the TEID are used for load balancing.
* GTP packets are hashed based on TEIDs. The display load-balance forwarding-path unicast interface ecmp command cannot be used to query an outbound interface through simulated calculation.



GTP packets are hashed based on TEIDs. The display load-balance forwarding-path unicast interface ecmp command cannot be used to query an outbound interface through simulated calculation.




Example
-------

# Enable the TEID-based hash function for GTP packets.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] gtp teid

```