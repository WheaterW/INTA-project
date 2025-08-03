Enabling Fast EBGP Peer Reset
=============================

Enabling Fast EBGP Peer Reset

#### Prerequisites

Before enabling fast EBGP peer reset, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Context

With fast EBGP peer reset enabled by default, BGP immediately responds to a fault on an interface and deletes the direct EBGP sessions on the interface without waiting for the Hold timer to expire, which speeds up BGP network convergence.

![](public_sys-resources/note_3.0-en-us.png) 

Fast EBGP peer reset enables BGP to quickly respond to interface faults, but not to interface recovery. Once the interface recovers, BGP uses its state machine to restore relevant sessions.

If the status of an interface used to establish an EBGP connection changes frequently, the EBGP session will be deleted and reestablished repeatedly, causing network flapping. To address this issue, disable fast EBGP peer reset so that BGP will not delete a direct EBGP session on the interface until the Hold timer expires. Therefore, disabling rapid EBGP peer reset suppresses BGP network flapping, speeds up BGP network convergence, and reduces network bandwidth consumption.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enable fast EBGP peer reset.
   
   
   ```
   [ebgp-interface-sensitive](cmdqueryname=ebgp-interface-sensitive)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) [ **verbose** ] command to check information about all BGP peers.
* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) *ipv4-address* { **log-info** | **verbose** } command to check information about a specified BGP peer.