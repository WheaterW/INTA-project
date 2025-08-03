Configuring a BSR Boundary (IPv6)
=================================

Before configuring IPv6 PIM-SM inter-domain multicast, configure BootStrap router (BSR) boundaries to divide a multicast network into different PIM-SM domains. Each BSR serves only the local PIM-SM domain, and Routers outside the BSR boundary of a PIM-SM domain do not take part in BSR messages forwarding in the PIM-SM domain.

#### Usage Scenario

After a BSR boundary is configured on the interface of an edge Router in an IPv6 PIM-SM domain, Bootstrap messages cannot pass through this interface. The interfaces configured with BSR boundaries divide a network into different PIM-SM domains.

BSR boundaries can also be used to isolate PIM-SM domains from the Internet.


#### Pre-configuration Tasks

Before configuring a BSR boundary, complete the following tasks:

* Configure an IPv6 unicast routing protocol to ensure that IPv6 unicast routes are reachable.
* Enable IPv6 multicast routing on all Routers and enable IPv6 PIM-SM on each interface on the Routers.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim ipv6 bsr-boundary**](cmdqueryname=pim+ipv6+bsr-boundary)
   
   
   
   A BSR boundary is configured. Bootstrap messages cannot pass through the BSR boundary.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display pim ipv6 bsr-info**](cmdqueryname=display+pim+ipv6+bsr-info) command to check information about the BSR in an IPv6 PIM-SM domain.


#### Follow-up Procedure

[Configure a BSR RP](dc_vrp_multicast_cfg_2010.html) in each IPv6 PIM-SM domain.