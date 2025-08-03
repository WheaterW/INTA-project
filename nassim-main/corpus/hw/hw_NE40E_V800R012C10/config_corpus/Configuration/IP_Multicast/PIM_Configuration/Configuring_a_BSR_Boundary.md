Configuring a BSR Boundary
==========================

Before configuring PIM inter-domain multicast, configure BootStrap router (BSR) boundaries to divide a multicast network into different PIM-SM domains. Each BSR serves only the local PIM-SM domain, and Routers outside the BSR boundary of a PIM-SM domain do not take part in BSR message forwarding in this PIM-SM domain.

#### Usage Scenario

After a BSR boundary is configured on the interface of an edge Router in a PIM-SM domain, Bootstrap messages cannot pass through this interface. The interfaces configured with BSR boundaries divide the network into different PIM-SM domains.

BSR boundaries can also be used to isolate PIM-SM domains from the Internet.


#### Pre-configuration Tasks

Before configuring a BSR boundary, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* Enable multicast routing on all Routers and enable PIM-SM on all interfaces.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim bsr-boundary**](cmdqueryname=pim+bsr-boundary) [ **incoming** ]
   
   
   
   A BSR boundary is configured. BSR messages cannot pass through the BSR boundary.
   
   If **incoming** is specified, the local PIM-SM domain can send BSR messages to all other PIM-SM domains but cannot receive BSR messages from other PIM-SM domains.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **bsr-info** command to check BSR information in a PIM-SM domain.


#### Follow-up Procedure

1. [Configure a BSR RP](dc_vrp_multicast_cfg_0010.html) for each PIM-SM domain.
2. Set up MSDP peer relationships between RPs in PIM-SM domains and [configure PIM-SM inter-domain multicast](dc_vrp_multicast_cfg_0045.html).