Configuring IS-IS-based Topology Reporting
==========================================

Before creating an SR-MPLS TE tunnel, enable IS-IS to report network topology information.

#### Context

Before an SR-MPLS TE tunnel is established, a forwarder must allocate labels, collect network topology information, and report that information to a controller so that the controller can use the information to compute a path and generate the corresponding label stack. SR-MPLS TE labels can be allocated by the controller or the extended IS-IS protocol on forwarders. Network topology information (including IS-IS-allocated labels) is collected by IS-IS and reported to the controller through BGP-LS.

IS-IS collects network topology information including the link cost, latency, and packet loss rate and advertises the information to BGP-LS, which then reports the information to a controller. The controller can compute an SR-MPLS TE tunnel based on link cost, latency, packet loss rate, and other factors to meet various service requirements.

Before the configuration, pay attention to the following points:

* If the controller computes an SR-MPLS TE tunnel based on the link cost, no additional configuration is required.
* If the controller computes an SR-MPLS TE tunnel based on the link latency, perform the operations described in [Configuring IS-IS Delay Information Advertisement (IPv4)](dc_vrp_isis_cfg_1053.html).
* If the controller computes an SR-MPLS TE tunnel based on the link-specific packet loss rate, perform the operations described in [Configuring an IS-IS Process to Advertise IPv4 Packet Loss Rates](dc_vrp_isis_cfg_1064.html).

#### Procedure

1. Configure IS-IS to advertise network topology information to BGP-LS.
   
   
   
   Perform the following steps on one or more nodes of the SR-MPLS TE tunnel:
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A forwarder can report network-wide topology information to the controller after they establish a BGP-LS peer relationship. The following steps can be configured on one or multiple nodes, depending on the network scale.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   3. Run [**bgp-ls enable**](cmdqueryname=bgp-ls+enable) [ **level-1** | **level-2** | **level-1-2** ]
      
      
      
      IS-IS is enabled to advertise network topology information to BGP-LS.
      
      
      
      To configure IS-IS to advertise the topology information of Level-1 areas and filter out the route prefixes leaked from Level-2 areas to Level-1 areas, run the [**bgp-ls enable**](cmdqueryname=bgp-ls+enable) **level-1** **level-2-leaking-route-ignore** command.
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