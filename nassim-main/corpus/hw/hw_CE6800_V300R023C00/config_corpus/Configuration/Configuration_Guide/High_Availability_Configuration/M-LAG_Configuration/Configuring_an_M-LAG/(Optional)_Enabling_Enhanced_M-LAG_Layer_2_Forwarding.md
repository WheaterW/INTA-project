(Optional) Enabling Enhanced M-LAG Layer 2 Forwarding
=====================================================

(Optional) Enabling Enhanced M-LAG Layer 2 Forwarding

#### Context

To speed up convergence when an M-LAG member interface fails in an overlay scenario, you can enable enhanced M-LAG Layer 2 forwarding. Backup FRR resources are requested for all MAC address entries whose outbound interfaces are M-LAG member interfaces. The outbound interfaces can be changed to peer-link interfaces to establish active and standby paths for traffic forwarding. Once an M-LAG member interface fault is detected, traffic is quickly switched to a peer-link interface, improving the switching performance in fault scenarios.

![](../public_sys-resources/note_3.0-en-us.png) 

Enhanced M-LAG Layer 2 forwarding is supported only by the CE6863H, CE6863H-K, CE6881H, and CE6881H-K.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable enhanced M-LAG Layer 2 forwarding.
   
   
   ```
   [m-lag forward layer-2 overlay enhanced enable](cmdqueryname=m-lag+forward+layer-2+overlay+enhanced+enable)  
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```