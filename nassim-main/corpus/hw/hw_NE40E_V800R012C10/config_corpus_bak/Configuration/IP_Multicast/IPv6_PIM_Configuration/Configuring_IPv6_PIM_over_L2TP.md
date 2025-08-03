Configuring IPv6 PIM over L2TP
==============================

IPv6 PIM over L2TP allows users to access multicast services over an L2TP tunnel.

#### Usage Scenario

When a multicast service provider needs to provide multicast services for users through a third-party network, L2TP can be used to carry multicast services. To control the multicast traffic carried by L2TP, you can configure IPv6 PIM over L2TP. This helps implement multicast user authentication and accounting.


#### Prerequisites

Before configuring IPv6 PIM over L2TP, complete the following tasks:

* Configure a unicast routing protocol to ensure that devices are reachable.
* Set up an L2TP tunnel between the LAC and the LNS.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-template**](cmdqueryname=interface+virtual-template) *vt-number*
   
   
   
   The VT interface view is displayed.
3. Run [**pim ipv6 sm**](cmdqueryname=pim+ipv6+sm)
   
   
   
   IPv6 PIM-SM is enabled.
4. Run [**pim ipv6 snooping enable**](cmdqueryname=pim+ipv6+snooping+enable) (virtual template interface view)
   
   
   
   IPv6 PIM over L2TP is enabled on the VT interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.