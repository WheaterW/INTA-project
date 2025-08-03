Configuring VPWS Load Balancing
===============================

Per-flow or per-packet load balancing can be implemented in LDP or SVC VPWS scenarios.

#### Usage Scenario

In LDP or SVC VPWS scenarios in which PW services are carried over multiple tunnels, VPWS load balancing can be implemented to fully utilize network bandwidths and improve transmission efficiency. Two VPWS load balancing modes are available:

* Per-flow load balancing: Packets from the same source and with the same destination are forwarded over the same tunnel.
* Per-packet load balancing: Packets are forwarded in sequence over alternate tunnels used for load balancing.
#### Pre-configuration Tasks

Before configuring VPWS load balancing, complete the following tasks:

* Configure LDP or SVC VPWS on interfaces.
* [Apply a tunnel policy to a VPN](dc_vrp_tnlm_cfg_0038.html).

Perform the following steps on a PE:



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The AC interface view is displayed.
3. Run [**mpls l2vpn load-balance packet**](cmdqueryname=mpls+l2vpn+load-balance+packet)
   
   
   
   Per-packet load balancing is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configurations are complete, check the configurations.

* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **interface** *interface-type* *interface-number* ] command on a PE to check the LDP VPWS load balancing mode and tunnels used for load balancing.
* Run the [**display mpls static-l2vc**](cmdqueryname=display+mpls+static-l2vc) [ **interface** *interface-type* *interface-number* ] command on a PE to check the SVC VPWS load balancing mode and tunnels used for load balancing.