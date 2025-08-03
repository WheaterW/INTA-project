(Optional) Enabling the Keepalive Function
==========================================

(Optional) Enabling the Keepalive Function

#### Context

Before you configure a tunnel policy and set the VPN tunnel type to GRE, you must enable the keepalive function. After this function is enabled, the local end will not use a GRE tunnel with an unreachable remote end, preventing data loss. This is because:

* Before the keepalive function is enabled, the local tunnel interface may be up even if the remote end is unreachable.
* After the keepalive function is enabled on the local end, the local tunnel interface is set to down when the remote end is unreachable. In this case, the local device does not select the unreachable GRE tunnel.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a tunnel interface.
   
   
   ```
   [interface tunnel](cmdqueryname=interface+tunnel) interface-number
   ```
3. Enable the keepalive function of GRE.
   
   
   ```
   [keepalive](cmdqueryname=keepalive) [ period period [ retry-times retry-times ] ]
   ```
   
   As the keepalive function is unidirectional, enable it on both ends of the GRE tunnel.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```