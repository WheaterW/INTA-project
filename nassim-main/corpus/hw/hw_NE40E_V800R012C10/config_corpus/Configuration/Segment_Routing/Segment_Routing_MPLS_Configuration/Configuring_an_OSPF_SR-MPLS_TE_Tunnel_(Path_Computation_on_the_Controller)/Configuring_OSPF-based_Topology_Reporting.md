Configuring OSPF-based Topology Reporting
=========================================

Before creating an SR-MPLS TE tunnel, enable OSPF to report network topology information.

#### Context

Before an SR-MPLS TE tunnel is established, a device must assign labels, collect network topology information, and report the information to the controller so that the controller uses the information to calculate a path and a label stack for the path. SR-MPLS TE labels can be assigned by the controller or the extended OSPF protocol on forwarders. Network topology information (including labels allocated by OSPF) is collected by OSPF and reported to the controller through BGP-LS.

OSPF collects network topology information including the link cost, latency, and packet loss rate and advertises the information to BGP-LS, which then reports the information to a controller. The controller can compute an SR-MPLS TE tunnel based on link cost, latency, and other factors to meet various service requirements.

Before the configuration, pay attention to the following points:

* If the controller computes an SR-MPLS TE tunnel based on the link cost, no additional configuration is required.
* If the controller computes an SR-MPLS TE tunnel based on the link latency, run the [**metric-delay advertisement enable**](cmdqueryname=metric-delay+advertisement+enable) command in the OSPF view to configure the latency advertisement function.

#### Procedure

1. Configure OSPF to advertise network topology information to BGP-LS.
   
   
   
   Perform the following steps on one or more nodes of an SR-MPLS TE tunnel:
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A forwarder can report network-wide topology information to the controller after they establish a BGP-LS peer relationship. The following steps can be configured on one or multiple nodes, depending on the network scale.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
      
      
      
      The OSPF view is displayed.
   3. Run [**bgp-ls enable**](cmdqueryname=bgp-ls+enable)
      
      
      
      OSPF is enabled to advertise network topology information to BGP-LS.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure a BGP-LS peer relationship between the forwarder and controller so that the forwarder can report topology information to the controller through BGP-LS.
   1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      BGP is enabled, and the BGP view is displayed.
   2. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number-plain*
      
      
      
      A BGP peer is created.
   3. Run [**link-state-family unicast**](cmdqueryname=link-state-family+unicast)
      
      
      
      BGP-LS is enabled, and the BGP-LS address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+enable) { *group-name* | *ipv4âaddress* } **enable**
      
      
      
      The device is enabled to exchange BGP-LS routing information with a specified peer or peer group.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.