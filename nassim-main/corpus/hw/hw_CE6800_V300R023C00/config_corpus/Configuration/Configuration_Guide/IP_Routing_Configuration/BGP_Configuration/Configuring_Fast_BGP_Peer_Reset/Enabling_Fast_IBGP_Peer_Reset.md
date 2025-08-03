Enabling Fast IBGP Peer Reset
=============================

Enabling Fast IBGP Peer Reset

#### Prerequisites

Before enabling fast IBGP peer reset, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Context

If the [**ibgp-interface-sensitive**](cmdqueryname=ibgp-interface-sensitive) command is not run and the local interface directly connected to an IBGP peer fails, the system does not delete the IBGP peer relationship on the interface until the hold timer expires. As a result, routes cannot be rapidly switched. To address this problem, run the [**ibgp-interface-sensitive**](cmdqueryname=ibgp-interface-sensitive) command. After this command is run, if the local interface directly connected to an IBGP peer fails, the device immediately responds to the failure by deleting the IBGP peer relationship on the interface, implementing fast route switching.

![](public_sys-resources/note_3.0-en-us.png) 

If a local interface directly connected to an IBGP peer alternates between up and down, do not run the [**ibgp-interface-sensitive**](cmdqueryname=ibgp-interface-sensitive) command; otherwise, route flapping may occur.

This command enables the device to quickly respond to failures of a local interface directly connected to an IBGP peer, but not to recovery of the interface. Once the interface recovers, BGP uses its state machine to restore the relevant session.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Enable the device to immediately delete the IBGP peer relationship on the local interface directly connected to an IBGP peer when the interface fails.
   
   
   ```
   [ibgp-interface-sensitive](cmdqueryname=ibgp-interface-sensitive)
   ```
   
   By default, the device is not configured to immediately delete the IBGP peer relationship on the local interface directly connected to an IBGP peer when the interface fails.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) [ **verbose** ] command to check information about all BGP peers.
* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) *ipv4-address* { **log-info** | **verbose** } command to check information about a specified BGP peer.