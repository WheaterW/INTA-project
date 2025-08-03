Configuring BGP-LS (IPv6)
=========================

BGP-LS (IPv6) provides a simple and efficient method of collecting topology information.

#### Usage Scenario

Without BGP-LS, the Router uses an IGP (OSPF, OSPFv3, or IS-IS) to collect network topology information and report the topology information of each area to the controller separately. This method has the following disadvantages:

* The controller must have high computing capabilities and support the IGP and its algorithm.
* The controller cannot gain the complete inter-IGP area topology information and therefore is unable to calculate optimal E2E paths.
* Different IGPs report topology information separately to the controller, which complicates the controller's analysis and processing.

With the BGP-LS feature, the topology information discovered by the IGP is summarized by BGP and then sent to the upper-layer controller. With the powerful route selection capability of BGP, BGP-LS has the following advantages:

* Reduces computing capability requirements and spares the necessity of IGPs on the controller.
* Facilitates route selection and calculation on the controller by using BGP to summarize process or AS topology information and report the complete information to the controller.
* Requires only one routing protocol (BGP) to report topology information to the controller.

BGP-LS needs to be deployed on the devices connected to the controller.


#### Pre-configuration Tasks

Before configuring BGP-LS, complete the following task:

* [Configure basic IPv6 IS-IS functions](dc_vrp_isis_cfg_1023.html) or [basic OSPF functions](dc_vrp_ospf_cfg_0003.html) or [basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2000.html).

#### Procedure

1. Enable IGP topology advertisement based on network configurations.
   * Enable IS-IS topology advertisement.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
        
        An IS-IS process is configured.
     3. Run [**cost-style**](cmdqueryname=cost-style+narrow+wide+wide-compatible+compatible) { **narrow** | **wide** | **wide-compatible** | { **compatible** | **narrow-compatible** } [ **relax-spf-limit** ] }
        
        A cost style is set for the routes to be accepted and sent by the IS-IS device.
     4. Run [**traffic-eng**](cmdqueryname=traffic-eng+level-1+level-2+level-1-2) [ **level-1** | **level-2** | **level-1-2** ]
        
        TE is enabled at a specified level for the IS-IS process.
     5. Run [**ipv6 traffic-eng**](cmdqueryname=ipv6+traffic-eng+level-1+level-2+level-1-2) [ **level-1** | **level-2** | **level-1-2** ]
        
        IPv6 TE is enabled at the specified level for the IS-IS process.
     6. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6+locator+auto-sid-disable) **locator** *locator-name* [ **auto-sid-disable** ]
        
        IS-IS SRv6 is enabled.
     7. Run [**ipv6 bgp-ls enable**](cmdqueryname=ipv6+bgp-ls+enable+level-1+level-2+level-1-2) [ **level-1** | **level-2** | **level-1-2** ] [ **exclude-prefix** ]
        
        IS-IS topology advertisement is enabled.
     8. (Optional) Run [**bgp-ls identifier**](cmdqueryname=bgp-ls+identifier) *identifier-value*
        
        A BGP-LS identifier is configured for IS-IS.
     9. (Optional) Run [**bgp-ls report-exclude**](cmdqueryname=bgp-ls+report-exclude+metric-delay-average) { **metric-delay-average** | **metric-delay-variation** | **link-msd** } \*
        
        Filtering of IS-IS topology information to be advertised is configured.
     10. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.
   * Enable OSPF topology advertisement.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**ospf**](cmdqueryname=ospf+router-id+vpn-instance) [ *process-id* | **router-id** *router-id* | **vpn-instance** *vpn-instance-name* ] \*
        
        An OSPF process is configured.
     3. Run [**bgp-ls enable**](cmdqueryname=bgp-ls+enable)
        
        OSPF topology advertisement is enabled.
     4. (Optional) Run [**bgp-ls identifier**](cmdqueryname=bgp-ls+identifier) *identifier-value*
        
        A BGP-LS identifier is configured for OSPF.
     5. (Optional) Run [**bgp-ls report-exclude**](cmdqueryname=bgp-ls+report-exclude+metric-delay-average) { **metric-delay-average** | **metric-delay-variation** } \*
        
        Filtering of the OSPF topology information to be advertised is configured.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Enable OSPFv3 topology advertisement.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**ospfv3**](cmdqueryname=ospfv3+vpn-instance) [ *process-id* ] [ **vpn-instance** *vpn-instance-name* ]
        
        An OSPFv3 process is created.
     3. Run [**bgp-ls enable**](cmdqueryname=bgp-ls+enable)
        
        OSPFv3 topology advertisement is enabled.
     4. (Optional) Run [**bgp-ls identifier**](cmdqueryname=bgp-ls+identifier) *identifier-value*
        
        A BGP-LS identifier is configured for OSPFv3.
     5. (Optional) Run [**bgp-ls report-exclude**](cmdqueryname=bgp-ls+report-exclude+metric-delay+metric-delay-average) { **metric-delay** | **metric-delay-average** | **metric-delay-variation** } \*
        
        Filtering of the OSPFv3 topology information to be advertised is configured.
        
        After BGP-LS is configured, the device collects OSPFv3 topology information and reports it to the controller. The collected information includes the maximum, minimum, and average delays and delay variation. If you want the device not to report some of the information, you can configure the topology advertisement filtering function.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
2. Enable BGP-LS.
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      BGP is enabled, and the BGP view is displayed.
   3. Run [**peer**](cmdqueryname=peer+as-number) *ipv6-address* **as-number** { *as-number-plain* | *as-number-dot* }
      
      The IP address and AS number of a BGP peer are specified.
   4. Run [**link-state-family unicast**](cmdqueryname=link-state-family+unicast)
      
      BGP-LS is enabled, and the BGP-LS address family view is displayed.
   5. Run [**peer**](cmdqueryname=peer+enable) *ipv6-address* **enable**
      
      BGP-LS route exchange with the specified peer is enabled.
   6. (Optional) Run [**domain identifier**](cmdqueryname=domain+identifier) *domain-id*
      
      A BGP-LS domain ID is configured.
      
      A BGP-LS domain ID identifies a device with BGP-LS enabled. If no BGP-LS domain ID is configured, a BGP router ID is used as the BGP-LS domain ID by default. The same BGP-LS domain ID can be configured for multiple devices so that the controller calculates routes based on the combined topology information reported by the devices.
   7. (Optional) Run [**domain as**](cmdqueryname=domain+as) *domain-asNum*
      
      A BGP-LS domain AS number is configured.
      
      Two devices with different BGP AS numbers must have the same BGP-LS domain AS number configured using the [**domain as**](cmdqueryname=domain+as) command so that the controller can combine the topology information about the two ASs for route calculation.
   8. (Optional) Run [**peer**](cmdqueryname=peer+reflect-client) *ipv6-address* **reflect-client**
      
      An RR is configured, and a client is specified.
      
      The Router on which the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run functions as the RR, and the specified peer functions as a client.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the clients of an RR are fully meshed, you can run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable route reflection among these clients through the RR to reduce bandwidth consumption.
      
      If a cluster has multiple RRs configured, you can run the [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) *cluster-id* command to configure the same cluster ID for all the RRs. This command is applicable only to RRs.
   9. (Optional) Run [**peer**](cmdqueryname=peer+route-limit+alert-only+idle-forever+idle-timeout) *ipv6-address* **route-limit** *limit* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *minutes* ]
      
      The maximum number of BGP-LS routes that can be accepted from the specified peer is set.
      
      Generally, a BGP-LS routing table contains a large number of routes. If a large number of routes are received from peers, excessive system resources are consumed. To prevent this problem, run this command to set the maximum number of routes that a BGP device is allowed to accept from a peer. If **idle-forever** is configured, the peer relationship will be interrupted and will not be automatically re-established after the number of received routes exceeds the threshold. Therefore, configuring **idle-forever** is not recommended.
   10. (Optional) Run [**peer**](cmdqueryname=peer+route-policy+import+export) *ipv6-address* **route-policy** *route-policy-name* { **import** | **export** }
       
       A route-policy is specified for the BGP-LS routes to be received from or advertised to a peer.
       
       After a route-policy is created, you can run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to use the route-policy to filter the BGP-LS routes to be received from or advertised to a specified peer. The command configuration ensures that only desired routes are accepted or advertised, which helps manage routes and reduces the BGP-LS routing table size and system resource consumption.
   11. (Optional) Run [**peer**](cmdqueryname=peer+route-update-interval) *ipv6-address* **route-update-interval** *interval*
       
       An interval at which the device sends Update messages carrying the same route prefix to a specified peer is set.
       
       When BGP-LS routes change, the Router sends Update messages to notify its peers. If a route changes frequently, to prevent the Router from sending Update messages for every change, run this command to set an interval at which the Router sends Update messages carrying the same route prefix to a specified peer.
   12. (Optional) Run [**peer**](cmdqueryname=peer+allow-as-loop) *ipv6-address* **allow-as-loop** *num*
       
       The maximum number of AS number repetitions in the AS\_Path attribute is set for a peer or peer group.
   13. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the following commands to verify the configuration.

* Run the [**display bgp link-state unicast peer**](cmdqueryname=display+bgp+link-state+unicast+peer) command to check information about BGP-LS peers and their status.
* Run the [**display bgp link-state unicast routing-table**](cmdqueryname=display+bgp+link-state+unicast+routing-table) command to check BGP-LS route information.
* Run the [**display bgp link-state unicast routing-table statistics**](cmdqueryname=display+bgp+link-state+unicast+routing-table+statistics) command to check BGP-LS route statistics.