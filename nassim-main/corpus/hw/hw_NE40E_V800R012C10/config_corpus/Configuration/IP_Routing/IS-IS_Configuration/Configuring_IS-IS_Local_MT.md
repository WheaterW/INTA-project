Configuring IS-IS Local MT
==========================

With IS-IS local multicast topology (MT), multicast traffic can be transmitted over a traffic engineering (TE) tunnel, and the Router through which the tunnel passes can generate multicast forwarding entries.

#### Usage Scenario

When both multicast and an MPLS TE tunnel are deployed on a network, multicast packets may be forwarded through the TE tunnel. As a result, the Routers spanned by the TE tunnel cannot detect the multicast packets and therefore cannot create multicast forwarding entries. To prevent this problem, configure local multicast topology (MT) and enable IGP Shortcut for the TE tunnel. In this case, an MIGP routing table can be established to guide multicast packet forwarding.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Local MT takes effect only in IS-IS processes of the public network instance.



#### Pre-configuration Tasks

Before configuring IS-IS local MT, complete the following tasks:

* Configure IP addresses for interfaces to ensure network connectivity between neighboring nodes.


[Enabling Local MT](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0113.html)

After local MT is enabled, routers through which a TE tunnel passes can generate multicast forwarding entries.

[(Optional) Controlling the Size of the MIGP Routing Table](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0114.html)

You can configure a filtering policy based on the multicast source address so that the router adds only the routes destined to the specified multicast source address to the independent Multicast IGP (MIGP) routing table, which controls the size of the MIGP routing table.

[Verifying the Configuration of IS-IS Local MT](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0115.html)

After configuring local MT, check the MIGP routing table, routing information, SPF tree, and IS-IS statistics.