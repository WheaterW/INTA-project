Configuring a Packet Forwarding Mode
====================================

Configuring a Packet Forwarding Mode

#### Context

The default mode for packet forwarding is store-and-forward. If a low packet latency is required, you can speed up packet forwarding by setting the mode to cut-through. In cut-through mode, CRC error packets are also forwarded but not discarded. If network congestion occurs on a device in cut-through mode, the device automatically changes the packet forwarding mode to store-and-forward, and reverts back to cut-through after network congestion is eliminated.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a packet forwarding mode.
   
   
   ```
   [assign forward mode](cmdqueryname=assign+forward+mode+cut-through+store-and-forward) { cut-through | store-and-forward }
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```