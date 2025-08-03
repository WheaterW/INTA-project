Configuring PIM over L2TP
=========================

PIM over L2TP allows users to access multicast services over an L2TP tunnel.

#### Usage Scenario

When a multicast service provider needs to provide multicast services for users through a third-party network, L2TP can be used to carry multicast services. To control the multicast traffic carried by L2TP, you can configure PIM over L2TP. This helps implement multicast user authentication and accounting.


#### Pre-configuration Tasks

Before configuring PIM over L2TP, complete the following tasks:

* Configure a unicast routing protocol to ensure that IP routes between nodes are reachable.
* Set up an L2TP tunnel between the LAC and the LNS.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-template**](cmdqueryname=interface+virtual-template) *vt-number*
   
   
   
   The VT interface template view is displayed.
3. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
4. Run [**pim snooping enable**](cmdqueryname=pim+snooping+enable) (virtual interface template view)
   
   
   
   PIM over L2TP is enabled on the VT interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.