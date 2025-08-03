(Optional) Enabling the Keepalive Function
==========================================

The keepalive function of a GRE tunnel prevents a service module from selecting a GRE tunnel that is unreachable to the peer end, preventing data loss.

#### Context

The keepalive function can be configured on one end of a GRE tunnel to test the GRE tunnel status. If the remote end is found unreachable, the tunnel is disconnected on time to avoid data black hole.

**Figure 1** Networking of a GRE tunnel that supports the keepalive function  
![](images/fig_dc_vrp_gre_cfg_200901.png)  


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number* command to enter the tunnel interface view.
3. Run the [**keepalive**](cmdqueryname=keepalive) [ **period** *period* [ **retry-times** *retry-times* ] ] command to enable the keepalive function for the GRE tunnel.
   
   
   
   The keepalive function of a GRE tunnel is unidirectional. To apply the keepalive function in both directions, enable the keepalive function on both ends of the GRE tunnel. Whether the peer end supports the keepalive function does not affect the keepalive function of the local end. However, you are advised to enable the keepalive function on both ends of the tunnel.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before you configure a tunnel policy and set the VPN tunnel type to GRE, you must enable the keepalive function. After this function is enabled, the local end will not use a GRE tunnel with an unreachable remote end, preventing data loss. This is because:
   
   * Before the keepalive function is enabled, the local tunnel interface may be up even if the remote end is unreachable.
   * After the keepalive function is enabled on the local end, if the local end does not receive any keepalive response packet from the peer end within the timeout period, the local tunnel interface is set to down. In this case, the local VPN does not select the unreachable GRE tunnel, preventing data loss.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.