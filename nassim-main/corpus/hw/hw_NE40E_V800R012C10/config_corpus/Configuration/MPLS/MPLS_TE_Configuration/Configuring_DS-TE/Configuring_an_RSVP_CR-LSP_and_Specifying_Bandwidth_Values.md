Configuring an RSVP CR-LSP and Specifying Bandwidth Values
==========================================================

When configuring an RSVP CR-LSP and specifying its bandwidth values, ensure that the sum of CT bandwidth values does not exceed the sum of BC bandwidth values.

#### Procedure

* Configure IGP TE.
  
  
  
  For detailed configurations, see [Configuring IGP TE (IS-IS)](dc_vrp_te-p2p_cfg_0005.html).
* Configure CSPF.
  
  
  
  For configuration details, see [Configuration CSPF](dc_vrp_te-p2p_cfg_0009.html).
* Configure bandwidth values for an MPLS TE tunnel.
  
  
  
  Perform the following steps on the ingress of a tunnel:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The MPLS TE tunnel interface view is displayed.
  3. Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) { **ct0** *bw-value* | **ct1** *bw-value* | **ct2** *bw-value* | **ct3** *bw-value* | **ct4** *bw-value* | **ct5** *bw-value* | **ct6** *bw-value* | **ct7** *bw-value* }
     
     
     
     Bandwidth is configured for the tunnel interface.
     
     
     
     Configure only one CT for each tunnel.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  For the same node, the sum of CTi bandwidth values must not exceed the BCi bandwidth values (0 <= i <= 7). CTi can use bandwidth resources only of BCi.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the bandwidth required by the MPLS TE tunnel is higher than 28,630 kbit/s, the available bandwidth assigned to the tunnel may not be precise, but the tunnel can be set up successfully.
* (Optional) Configure an explicit path.
  
  
  
  To limit the path over which an MPLS TE tunnel is established, perform the following steps on the ingress of the tunnel:
  
  
  
  1. Create an explicit path. For detailed configuration, see [(Optional) Configuring an MPLS TE Explicit Path](dc_vrp_te-p2p_cfg_0007.html).
  2. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  3. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The MPLS TE tunnel interface view is displayed.
  4. Run [**mpls te path explicit-path**](cmdqueryname=mpls+te+path+explicit-path) *path-name*
     
     
     
     An explicit path is configured for the tunnel.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.