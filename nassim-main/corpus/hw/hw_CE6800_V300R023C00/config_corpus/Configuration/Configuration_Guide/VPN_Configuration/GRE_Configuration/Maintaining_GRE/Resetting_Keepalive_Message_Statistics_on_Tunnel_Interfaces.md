Resetting Keepalive Message Statistics on Tunnel Interfaces
===========================================================

Resetting Keepalive Message Statistics on Tunnel Interfaces

#### Context

You can reset the traffic statistics of a tunnel interface by resetting statistics about the keepalive messages and keepalive response messages sent and received by the tunnel interface.


#### Procedure

* Reset the statistics of a specified tunnel interface in the user view.
  
  
  ```
  [reset interface counters](cmdqueryname=reset+interface+counters) tunnel [ interface-number ]
  ```
* Reset keepalive message statistics on a specified tunnel interface.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [interface tunnel](cmdqueryname=interface+tunnel) interface-number
  [reset keepalive packets count](cmdqueryname=reset+keepalive+packets+count)
  ```