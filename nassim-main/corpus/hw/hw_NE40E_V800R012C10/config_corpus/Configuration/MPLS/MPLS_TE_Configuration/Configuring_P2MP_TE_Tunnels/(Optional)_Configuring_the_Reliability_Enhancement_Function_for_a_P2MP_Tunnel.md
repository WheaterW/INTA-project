(Optional) Configuring the Reliability Enhancement Function for a P2MP Tunnel
=============================================================================

Configure a function to improve service reliability as needed.

#### Context

To improve reliability of traffic transmitted along a P2MP tunnel, configure the following reliability enhancement functions as needed:

* Rapid MPLS P2MP switching
  
  With this function, if a device detects a fault in the active link, the device rapidly switches services to the standby link over which an MPLS P2MP tunnel is established, which improves service reliability.
* Multicast load balancing on a trunk interface
  
  Without this function, a device randomly selects a trunk member interface to forward multicast traffic. If this member interface fails, multicast traffic is interrupted. With this function, multicast traffic along a P2MP tunnel is balanced among all trunk member interfaces. This function helps improve service reliability and increase available bandwidth for multicast traffic.
* MPLS P2MP load balancing
  
  To enable P2MP load balancing globally, run the **mpls p2mp force-loadbalance enable** command. In a multicast scenario where load balancing is configured in the Eth-Trunk interface view,
  if a leaf node connected to the Eth-Trunk interface joins or quits the multicast model, packet loss occurs on the other leave nodes connected to the non-Eth-Trunk interfaces due to the model change. After the **mpls p2mp force-loadbalance enable** command is run, load balancing is forcibly enabled in the system view, therefore preventing packet loss.
* WTR time for traffic to be switched from the MPLS P2MP FRR path to the primary path.
  
  If the primary MPLS P2MP path fails, traffic on the forwarding plane is rapidly switched to the backup path. If the primary path recovers before MPLS P2MP convergence is complete on the downstream node, traffic is switched back to the primary path within the default WTR time. If only some entries are generated for the primary path within the period, some packets are dropped when traffic switches back to the primary path. To ensure that all entries are generated for the primary path during the switchback and prevent packet loss, you can flexibly set the WTR time for traffic to be switched from the MPLS P2MP FRR path to the primary path.

#### Procedure

* Configure rapid MPLS P2MP switching.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**mpls p2mp fast-switch enable**](cmdqueryname=mpls+p2mp+fast-switch+enable)
     
     Rapid MPLS P2MP switching is enabled.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure multicast load balancing on a trunk interface.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id* or [**interface ip-trunk**](cmdqueryname=interface+ip-trunk) *trunk-id*
     
     The Eth-Trunk interface view is displayed.
  3. Run [**multicast p2mp load-balance enable**](cmdqueryname=multicast+p2mp+load-balance+enable)
     
     Multicast traffic load balancing among trunk member interfaces is enabled on the trunk interface that functions as an outbound interface of a P2MP tunnel.
  4. Run [**multicast p2mp root load-balance enable**](cmdqueryname=multicast+p2mp+root+load-balance+enable)
     
     Multicast traffic load balancing among trunk member interfaces is enabled on the trunk interface that resides on the P2MP tunnel's root node or ABR (ASBR) in the segmented NG MVPN scenario.
  5. (Optional) Run [**multicast p2mp root load-balance spmsi disable**](cmdqueryname=multicast+p2mp+root+load-balance+spmsi+disable)
     
     Multicast traffic load balancing among trunk member interfaces is disabled on the root node of an S-PMSI tunnel.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure MPLS P2MP load balancing.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**mpls p2mp force-loadbalance enable**](cmdqueryname=mpls+p2mp+force-loadbalance+enable)
     
     MPLS P2MP load balancing is enabled globally.
  3. (Optional) Run [**multicast p2mp load-balance number**](cmdqueryname=multicast+p2mp+load-balance+number) *load-balance\_number*
     
     The number of trunk member interfaces that balance multicast traffic on a P2MP tunnel is set.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Set the WTR time for traffic to be switched from the MPLS P2MP FRR path to the primary path.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**mpls p2mp frr-wtr**](cmdqueryname=mpls+p2mp+frr-wtr) *time-value*
     
     The WTR time is set for traffic to be switched from the MPLS P2MP FRR path to the primary path.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.