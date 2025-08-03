Configuring the MACsec Replay Window Size
=========================================

Configuring the MACsec Replay Window Size

#### Context

To prevent against attacks based on repeatedly sent data packets, the receiver discards duplicate or out-of-order data packets. In some cases, however, because the priorities of data packets are different, the packets are reordered in the forwarding process. When the packets arrive at the receive end, they are in disorder. To ensure that these out-of-order data packets can be received normally, configure the replay protection window.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**macsec replay-window**](cmdqueryname=macsec+replay-window) *window-size*
   
   
   
   The MACsec replay window size is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.