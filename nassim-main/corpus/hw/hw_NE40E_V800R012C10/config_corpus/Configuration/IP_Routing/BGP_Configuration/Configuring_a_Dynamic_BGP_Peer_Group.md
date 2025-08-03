Configuring a Dynamic BGP Peer Group
====================================

Configuring dynamic BGP peer groups reduces network maintenance workload.

#### Usage Scenario

On a BGP network, multiple peers may frequently change, causing the establishment of peer relationships to change accordingly. If you configure peers in static mode, you need to frequently add or delete peer configurations on the local device, which increases the maintenance workload. To address this problem, configure the dynamic BGP peer function to enable BGP to listen for BGP connection requests from a specified network segment, dynamically establish BGP peer relationships, and add these peers to the same dynamic peer group. This spares you from adding or deleting BGP peer configurations in response to each change in BGP peers.


#### Pre-configuration Tasks

Before configuring a dynamic BGP peer group, complete the following task:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. (Optional) Run [**bgp dynamic-session-limit**](cmdqueryname=bgp+dynamic-session-limit) *max-num*
   
   
   
   The maximum number of dynamic BGP peer sessions that can be established is set.
4. Run [**group**](cmdqueryname=group+listen+internal+external+confederation-external) *group-name* **listen** [ **internal** | **external** | **confederation-external** ]
   
   
   
   A dynamic BGP peer group is created.
5. Run either of the following commands to configure the peer AS number or AS range from which the dynamic EBGP peer group listens for connection requests.
   
   
   * To specify the peer AS number from which the dynamic EBGP peer group listens for connection requests, run the [**peer**](cmdqueryname=peer+listen-as) *group-name* **listen-as** { *asn* } &<1-6> command.
   * To specify the peer AS range from which the dynamic EBGP peer group listens for connection requests, run the [**peer**](cmdqueryname=peer+listen-as-segment+begin-as+end-as) *group-name* **listen-as-segment** **begin-as** *begin-asn* **end-as** *end-asn* command.
6. Run [**peer**](cmdqueryname=peer+listen-net) *group-name* **listen-net** *ipv4-address* { **mask-length** | **mask** }
   
   
   
   A network segment from which the dynamic BGP peer group listens for BGP connection requests is specified.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display bgp group**](cmdqueryname=display+bgp+group) [ *group-name* ] command to check information about a specified BGP peer group.
* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) command to check information about dynamic peers.