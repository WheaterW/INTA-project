(Optional) Configuring the Maximum Number of Packet Retransmission Attempts
===========================================================================

(Optional) Configuring the Maximum Number of Packet Retransmission Attempts

#### Context

By enabling retransmission and setting the maximum number of packet retransmission attempts on a device, infinite loops caused by repeated transmissions when the device receives no response to DD, LSU, or LSR packets are prevented. If no response is received when the maximum number of packet retransmission attempts is reached, the neighbor relationship will be disconnected. By default, the retransmission mechanism is disabled.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Set the maximum number of OSPF packet retransmission attempts.
   
   
   ```
   [retransmission-limit](cmdqueryname=retransmission-limit) [ max-number ]
   ```
   
   *max-number* specifies the maximum number of packet retransmission attempts. The default value is 30.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```