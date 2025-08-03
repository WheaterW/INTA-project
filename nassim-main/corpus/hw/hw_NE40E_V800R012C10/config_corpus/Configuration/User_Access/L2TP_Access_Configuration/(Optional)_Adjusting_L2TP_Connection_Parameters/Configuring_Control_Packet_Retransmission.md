Configuring Control Packet Retransmission
=========================================

After control packet retransmission is enabled, if a device on one end of a tunnel does not receive any response packet from its peer for a specified number of times within a certain period, the device considers that the tunnel is torn down.

#### Context

A LAC and an LNS exchange control packets to set up a tunnel. If one end fails to receive any response from the peer in a specified period due to network congestion, this end retransmits the control packet to the peer. You can configure an interval at which control packets are retransmitted and the maximum number of allowed retransmission times.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
   
   
   
   The L2TP group view is displayed.
3. Run [**tunnel retransmit**](cmdqueryname=tunnel+retransmit) *retransmit-times*
   
   
   
   The maximum number of allowed retransmission times is configured.
4. Run [**tunnel timeout**](cmdqueryname=tunnel+timeout) *time-value*
   
   
   
   An interval at which control packets are retransmitted is configured.
   
   If a large number of L2TP tunnels are established, it is recommended that the retransmission interval be set to 5 seconds.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.