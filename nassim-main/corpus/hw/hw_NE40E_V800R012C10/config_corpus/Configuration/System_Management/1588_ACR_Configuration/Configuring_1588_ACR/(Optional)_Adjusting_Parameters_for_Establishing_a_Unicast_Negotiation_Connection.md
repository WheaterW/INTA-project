(Optional) Adjusting Parameters for Establishing a Unicast Negotiation Connection
=================================================================================

Adjustable parameters include the maximum number of consecutive Announce packets that the client fails to receive (If the number of unreceived Announce packets exceeds the threshold, the client determines that the connection to the server fails), duration of the Sync, Delay\_Resp, and Announce packets (After the duration of a Sync packet, a Delay\_Resp packet, or an Announce packet expires, the client re-establishes the connection with the server), DSCP value (the DSCP value ensures that 1588v2 packets reach the destination even if a congestion occurs on the network), and the interval at which the server sends Sync, Delay\_Resp, and Announce packets.

#### Context

Adjustable parameters on a client are as follows:

* Maximum number of consecutive Delay\_Resp packets that the client fails to receive
* Duration field values in Sync, Delay\_Resp and Announce packets
* DSCP value for 1588 ACR packets
* Interval at which Sync, Delay\_Resp and Announce packets are sent

Adjustable parameters on a clock server are as follows:

* DSCP value for 1588 ACR packets

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ptp-adaptive dscp**](cmdqueryname=ptp-adaptive+dscp) *dscp-value*
   
   
   
   The DSCP value in 1588 ACR packets is set.
   
   
   
   Setting a large DSCP value ensures that 1588v2 packets reach the destination even if a congestion occurs on a network.
3. Run [**ptp-adaptive**](cmdqueryname=ptp-adaptive) { **announce-duration** | **sync-duration** | **delay-resp-duration** } *duration-value*
   
   
   
   The duration field value is set for each type of 1588 ACR packet.
4. Run [**ptp-adaptive request sync-interval**](cmdqueryname=ptp-adaptive+request+sync-interval) *interval-value*
   
   
   
   The interval at which an ACR clock server sends Sync packets is set.
5. Run [**ptp-adaptive request announce-interval**](cmdqueryname=ptp-adaptive+request+announce-interval) *announce-interval-value*
   
   
   
   The interval at which an ACR clock server sends Announce packets is set.
6. Run [**ptp-adaptive request delay-resp-interval**](cmdqueryname=ptp-adaptive+request+delay-resp-interval) *interval-value*
   
   
   
   The interval at which an ACR clock server sends Delay\_Resp packets is set.
7. Run [**ptp-adaptive announce receipt-timeout**](cmdqueryname=ptp-adaptive+announce+receipt-timeout) *timeout-time*
   
   
   
   The allowable maximum number of consecutive Announce packets that the client fails to receive is set.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.