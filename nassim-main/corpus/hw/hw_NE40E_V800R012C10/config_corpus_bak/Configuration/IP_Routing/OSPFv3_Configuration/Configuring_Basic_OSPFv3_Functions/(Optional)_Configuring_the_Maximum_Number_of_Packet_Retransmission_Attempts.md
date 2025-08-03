(Optional) Configuring the Maximum Number of Packet Retransmission Attempts
===========================================================================

When no response to DD packets, Update packets, or Request packets is received, the retransmission mechanism is used and the maximum number of packet retransmission attempts is set to prevent dead loops caused by repeated transmissions.

#### Context

If no response is received when the maximum number of packet retransmission attempts is reached, the neighbor relationship will be interrupted.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**retransmission-limit**](cmdqueryname=retransmission-limit) [ *max-number* ]
   
   
   
   The maximum number of OSPFv3 packet retransmission attempts is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.