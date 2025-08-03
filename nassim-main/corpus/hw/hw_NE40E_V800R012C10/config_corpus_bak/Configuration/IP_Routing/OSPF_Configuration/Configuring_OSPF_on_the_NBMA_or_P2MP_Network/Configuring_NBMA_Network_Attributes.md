Configuring NBMA Network Attributes
===================================

To implement OSPF functions, configure NBMA network attributes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospf network-type**](cmdqueryname=ospf+network-type) **nbma**
   
   
   
   The network type of the OSPF interface is set to NBMA.
   
   
   
   The NBMA network must be fully meshed. Any two Routers on the NBMA network must be directly reachable. In most cases, however, this requirement cannot be met. To resolve this problem, change the network type to P2MP. For details, see [Configuring Network Types for OSPF Interfaces](dc_vrp_ospf_cfg_2029.html).
4. (Optional) Run [**ospf timer poll**](cmdqueryname=ospf+timer+poll) *interval*
   
   
   
   The interval at which Hello packets for polling are sent by an NBMA interface is set.
   
   On the NBMA network, after the neighbor relationship becomes invalid, the Router sends Hello packets at an interval defined in the polling mechanism.
5. (Optional) Run [**ospf dr-priority**](cmdqueryname=ospf+dr-priority) *priovalue*
   
   
   
   A priority is configured for the interface to compete for the DR.
   
   The priority of an interface determines whether the interface is qualified to be a DR. The interface with the highest priority is elected as the DR. If the priority of an interface on a device is 0, the device cannot be elected as a DR or BDR. On a broadcast or an NBMA network, you can set the priority of an interface to control the DR or BDR selection. When the DR and BDR are elected on a network segment, they send DD packets to all neighboring nodes and set up adjacencies with all neighboring nodes.
6. (Optional) Run [**ospf timer wait**](cmdqueryname=ospf+timer+wait) *interval*
   
   
   
   The wait time is configured for the interface.
   
   If no Backup Seen event is received within the *interval*, the DR election starts. Setting a proper value for the wait timer can slow down changes of the DR and BDR on the network, reducing network flapping. When setting the wait timer, note the following points:
   
   * The wait timer takes effect only on broadcast and NBMA interfaces.
   * The value of the wait timer cannot be greater than the value of the dead timer.
7. Configure a neighboring Router on the NBMA network.
   
   
   
   The interface with the network type of NBMA cannot broadcast Hello packets to discover neighboring Routers. Therefore, the IP address of a neighboring Router must be configured on the process and whether the neighboring Router can participate in DR election must be determined on the process.
   
   
   
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the interface view.
   2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
      
      
      
      The OSPF view is displayed.
   3. Run [**peer**](cmdqueryname=peer) *ip-address* [ **dr-priority** *priority* ]
      
      
      
      A neighbor is configured on the NBMA network.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.