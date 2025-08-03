Configuring BGP-LS
==================

BGP-LS provides a simple and efficient method of collecting topology information.

#### Usage Scenario

Without BGP-LS, the Router uses an IGP (OSPF, OSPFv3, or IS-IS) to collect network topology information and report the topology information of each area to the controller separately. This method has the following disadvantages:

* The controller must have high computing capabilities and support the IGP and its algorithm.
* The controller cannot gain the complete inter-area topology information and therefore is unable to calculate optimal E2E paths.
* Different IGPs report topology information separately to the controller, which complicates the controller's analysis and processing.

With powerful route selection capabilities of BGP, BGP-LS has the following advantages:

* Reduces computing capability requirements and spares the necessity of IGPs on the controller.
* Facilitates route selection and calculation on the controller by using BGP to summarize process or AS topology information and report the complete information to the controller.
* Requires only one routing protocol (BGP) to report topology information to the controller.

BGP-LS needs to be deployed on the devices connected to the controller.


#### Pre-configuration Tasks

Before configuring BGP-LS, complete the following tasks:

* [Configure basic IPv4 IS-IS functions](dc_vrp_isis_cfg_1000.html) or [basic OSPF functions](dc_vrp_ospf_cfg_0003.html) or [basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2000.html).

#### Procedure

1. Enable IGP topology advertisement to BGP. You can determine to enable IS-IS topology advertisement to BGP or OSPF topology advertisement to BGP based on network configurations.
   * Enable IS-IS topology advertisement to BGP.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
        
        An IS-IS process is configured.
     3. Run [**bgp-ls enable**](cmdqueryname=bgp-ls+enable+level-1+level-2+level-1-2+level-1) [ **level-1** | **level-2** | **level-1-2** ] [ **exclude-prefix** ]
        
        IS-IS topology advertisement is enabled.
        
        To enable IS-IS to advertise topology information of Level-1 areas and filter the route prefixes leaked from Level-2 areas to Level-1 areas, run the [**bgp-ls enable**](cmdqueryname=bgp-ls+enable+level-1+level-2-leaking-route-ignore) **level-1** **level-2-leaking-route-ignore** command.
     4. (Optional) Run [**bgp-ls identifier**](cmdqueryname=bgp-ls+identifier) *identifier-value*
        
        A BGP-LS identifier is configured for IS-IS.
     5. (Optional) Run [**bgp-ls report-exclude**](cmdqueryname=bgp-ls+report-exclude+metric-delay-average) { **metric-delay-average** | **metric-delay-variation** | **link-msd** } \*
        
        Filtering of IS-IS topology information to be advertised is configured.
     6. Run [**commit**](cmdqueryname=commit)
        
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
   3. Run [**peer**](cmdqueryname=peer+as-number) { *group-name* | *ipv4-address* } **as-number** *as-number*
      
      The IP address and AS number of a BGP peer are specified.
   4. Run [**link-state-family unicast**](cmdqueryname=link-state-family+unicast)
      
      BGP-LS is enabled, and the BGP-LS address family view is displayed.
   5. Run [**peer**](cmdqueryname=peer+enable) { *group-name* | *ipv4-address* } **enable**
      
      BGP-LS route exchange with the specified peer or peer group is enabled.
   6. (Optional) Run [**domain identifier**](cmdqueryname=domain+identifier) *domain-id*
      
      A BGP-LS domain ID is configured.
      
      A BGP-LS domain ID identifies a device with BGP-LS enabled. If no BGP-LS domain ID is configured, a BGP router ID is used as the BGP-LS domain ID by default. The same BGP-LS domain ID can be configured for multiple devices so that the controller calculates routes based on the combined topology information reported by the devices.
   7. (Optional) Run [**domain as**](cmdqueryname=domain+as) *domain-asNum*
      
      A BGP-LS domain AS number is configured.
      
      Two devices with different BGP AS numbers must have the same BGP-LS domain AS number configured using the [**domain as**](cmdqueryname=domain+as) command so that the controller can obtain combined topology information about the two ASs for route calculation.
   8. (Optional) Run [**peer**](cmdqueryname=peer+reflect-client) { *group-name* | *ipv4-address* } **reflect-client**
      
      An RR is configured, and a client is specified.
      
      The Router on which the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run functions as the RR, and the specified peer or peer group functions as a client.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the clients of an RR are fully meshed, you can run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable route reflection among these clients through the RR to reduce bandwidth consumption.
      
      If a cluster has multiple RRs configured, you can run the [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) *cluster-id* command to configure the same cluster ID for all the RRs. This command is applicable only to RRs.
   9. (Optional) Run [**peer**](cmdqueryname=peer+route-limit+alert-only+idle-forever+idle-timeout) { *group-name* | *ipv4-address* } **route-limit** *limit* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *minutes* ]
      
      The maximum number of BGP-LS routes that the local device can accept from a specified peer is set.
      
      Generally, a BGP-LS routing table contains a large number of routes. If a large number of routes are received from peers, excessive system resources are consumed. To prevent this problem, run this command to set the maximum number of routes that a BGP device is allowed to accept from a peer. If **idle-forever** is configured, the peer relationship will be interrupted and will not be automatically re-established after the number of received routes exceeds the threshold. Therefore, configuring **idle-forever** is not recommended.
   10. (Optional) Run [**peer**](cmdqueryname=peer+route-policy+import+export) { *group-name* | *ipv4-address* } **route-policy** *route-policy-name* { **import** | **export** }
       
       A route-policy is specified for the BGP-LS routes to be received from or advertised to a specified BGP peer or peer group.
       
       After a route-policy is created, you can run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to use the route-policy to filter the BGP-LS routes to be received from or advertised to a specified BGP peer or peer group. The command configuration ensures that only desired routes are accepted or advertised, which helps manage routes and reduces the BGP-LS routing table size and system resource consumption.
   11. (Optional) Run [**peer**](cmdqueryname=peer+route-update-interval) { *group-name* | *ipv4-address* } **route-update-interval** *interval*
       
       An interval at which the device sends Update messages carrying the same route prefix to a specified peer or peer group is set.
       
       When BGP-LS routes change, the Router sends Update messages to notify its peers. If a route changes frequently, to prevent the Router from sending Update messages for every change, run this command to set an interval at which the Router sends Update messages carrying the same route prefix to a specified peer or peer group.
   12. (Optional) Run [**peer**](cmdqueryname=peer+allow-as-loop) { *group-name* | *ipv4-address* } **allow-as-loop** *num*
       
       The maximum number of AS number repetitions in the AS\_Path attribute allowed by a peer or peer group is configured.
   13. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp link-state unicast peer**](cmdqueryname=display+bgp+link-state+unicast+peer) command to check information about BGP-LS peers and their status.
* Run the [**display bgp link-state unicast routing-table**](cmdqueryname=display+bgp+link-state+unicast+routing-table) command to check BGP-LS route information.
* Run the [**display bgp link-state unicast routing-table statistics**](cmdqueryname=display+bgp+link-state+unicast+routing-table+statistics) command to check BGP-LS route statistics.