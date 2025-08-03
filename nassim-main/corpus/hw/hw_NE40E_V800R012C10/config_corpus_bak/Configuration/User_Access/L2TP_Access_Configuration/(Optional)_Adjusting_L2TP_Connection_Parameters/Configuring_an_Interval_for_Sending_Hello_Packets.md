Configuring an Interval for Sending Hello Packets
=================================================

A LAC and an LNS exchange Hello packets to detect tunnel connectivity.

#### Context

To check the connectivity of a tunnel established between a LAC and an LNS, the LAC and the LNS exchange hello packets periodically.

If the LAC or LNS fails to receive hello response packets from each other in a specified period, the packets are retransmitted. If the maximum number of retransmission times exceeds a specified number (see [Configuring Control Packet Retransmission](dc_ne_l2tp_cfg_013499.html)), the L2TP tunnel is regarded disconnected, and all sessions on the tunnel are deleted.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
   
   
   
   The L2TP group view is displayed.
3. Run [**tunnel timer hello**](cmdqueryname=tunnel+timer+hello) *interval-time*
   
   
   
   An interval for sending Hello packets is configured.
4. (Optional) Run [**tunnel hello peer-check**](cmdqueryname=tunnel+hello+peer-check)
   
   
   
   The NE40E is configured to send a Hello packet only after receiving a Hello packet from the peer end.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.