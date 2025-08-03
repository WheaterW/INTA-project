Preventing Routing Loops
========================

RIP is based on the DV algorithm. RIP devices advertise their routing tables to their neighbors, and therefore, routing loops may occur.

#### Usage Scenario

RIP prevents routing loops through the following mechanisms:

* Counting to infinity: RIP defines the cost 16 as infinity. If the cost of a route reaches 16 due to a routing loop, this route is considered unreachable.
* Split horizon: Split horizon prevents a RIP-enabled interface from sending back the routes it learns, which reduces bandwidth consumption and prevents routing loops.
* Poison reverse: Poison reverse allows a RIP-enabled interface to set the cost of the route that it learns from a neighbor to 16 (indicating that the route is unreachable) and then send the route back. After receiving this route, the neighbor deletes the useless route from its routing table, which prevents loops.
* Suppression timers: Suppression timers can prevent routing loops and reduce the possibility of resulting in incorrect routing information due to the receiving of incorrect routes.
* Disabling an interface from receiving and sending RIP packets: Similar to split horizon or poison reverse, this function filters out unreliable RIP routes. However, routing information on the network may be incorrect because neighbors cannot receive packets from the local Router.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Counting to infinity is a basic feature of RIP, and therefore, it does not need to be configured. Split horizon and poison reverse, however, need to be configured. When both split horizon and poison reverse are configured, only poison reverse takes effect.




#### Pre-configuration Tasks

Before configuring RIP to prevent routing loops on the network, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configuring Basic RIP Functions](dc_vrp_rip_cfg_0003.html)

#### Configuration Procedure

Perform one or more of the following configurations as required.


[Configuring Split Horizon](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0012.html)

You can configure split horizon to prevent routing loops.

[Configuring Poison Reverse](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0013.html)

You can configure poison reverse to prevent routing loops.

[Configuring Suppression Timers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0014.html)

Suppression timers can prevent routing loops and reduce the possibility of generating incorrect routing information due to the receiving of incorrect routes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0017.html)

After routing loop prevention is configured, you can view the current running status of RIP, information about interfaces, and RIP routing information.