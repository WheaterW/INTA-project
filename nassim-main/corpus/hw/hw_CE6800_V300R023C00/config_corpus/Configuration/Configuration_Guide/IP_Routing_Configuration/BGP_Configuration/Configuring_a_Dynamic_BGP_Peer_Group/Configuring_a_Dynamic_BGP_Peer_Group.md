Configuring a Dynamic BGP Peer Group
====================================

Configuring a Dynamic BGP Peer Group

#### Prerequisites

Before configuring a dynamic BGP peer group, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Context

On a BGP network, multiple peers may change frequently, causing the establishment of peer relationships to change accordingly. If you configure peers in static mode, you must frequently add or delete peer configurations on the local device, increasing the maintenance workload. To address this problem, configure the dynamic BGP peer function to enable a BGP device to listen for BGP connection requests from a specified network segment, dynamically establish BGP peer relationships, and add these peers to the same dynamic peer group. As a result, manually adding or deleting BGP peer configurations in response to each dynamic peer change is no longer required.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. (Optional) Set the maximum number of dynamic BGP peer sessions that can be established.
   
   
   ```
   [bgp dynamic-session-limit](cmdqueryname=bgp+dynamic-session-limit) max-num
   ```
   
   By default, the maximum number of dynamic BGP peer sessions that can be established is 100.
4. Create a dynamic BGP peer group. In the command, **confederation-external** supports only single-instance dynamic peer groups.
   
   
   ```
   [group](cmdqueryname=group+listen+internal+external+confederation-external) group-name listen [ internal | external | confederation-external ]
   ```
5. (Optional) Configure the peer AS number for which the dynamic EBGP peer group listens.
   
   
   ```
   [peer](cmdqueryname=peer+listen-as) group-name listen-as { asn } &<1-6>
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You do not need to perform the configurations related to dynamic EBGP peer groups for dynamic IBGP peer groups.
6. (Optional) Configure the peer AS segment for which the dynamic EBGP peer group listens.
   
   
   ```
   [peer](cmdqueryname=peer+listen-as-segment+begin-as+end-as) group-name listen-as-segment begin-as begin-asn end-as end-asn
   ```
7. Configure a network segment for which the dynamic peer group listens.
   
   
   ```
   [peer](cmdqueryname=peer+listen-net) group-name listen-net ipv4-address [ mask-length | mask ]
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp group**](cmdqueryname=display+bgp+group) [ *group-name*] command to check information about a specified BGP peer group.
* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) command to check information about dynamic peers.