Configuring the BGP4+ Add-Path Function
=======================================

Configuring the BGP4+ Add-Path Function

#### Prerequisites

Before configuring the BGP4+ Add-Path function, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

Generally, BGP4+ Add-Path is configured on an RR, and the Add-Path route receiver needs to be configured to accept such routes.

![](public_sys-resources/note_3.0-en-us.png) 

BGP Add-Path is not supported in BGP4+ confederation scenarios.



#### Procedure

* Perform the following steps on a device that needs to send Add-Path routes:
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. (Optional) Create a route-policy and enter the route-policy view.
     
     
     ```
     [route-policy](cmdqueryname=route-policy+node) route-policy-name matchMode node node
     ```
  3. (Optional) Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  4. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  5. Specify the IP address and AS number of a peer.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address |ipv6-address | group-name } [as-number](cmdqueryname=as-number) as-number
     ```
  6. Enter the IPv6 unicast address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
     ```
  7. Enable the IPv6 peer.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | ipv6-address | group-name } [enable](cmdqueryname=enable)
     ```
  8. Enable BGP4+ Add-Path and set the number of preferred routes that the device can select.
     
     
     ```
     [bestroute add-path](cmdqueryname=bestroute+add-path+path-number) path-number path-number
     ```
  9. Enable the device to send Add-Path routes to a specified peer.
     
     
     ```
     [peer](cmdqueryname=peer+capability-advertise+add-path+send) { ipv4-address | ipv6-address | group-name } capability-advertise add-path send
     ```
  10. Set the maximum number of preferred routes that the device can send to the peer.
      
      
      ```
      [peer](cmdqueryname=peer+advertise+add-path+path-number) { peerIpv4Addr | peerIpv6Addr | groupName } advertise add-path path-number path-number [ route-policy route-policy-name ]
      ```
      
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      To configure **route-policy** *route-policy-name*, you need to enter the route-policy view.
  11. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
* Perform the following steps on a device that needs to accept Add-Path routes:
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the IPv6 unicast address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
     ```
  4. Enable the device to accept Add-Path routes from a specified peer.
     
     
     ```
     [peer](cmdqueryname=peer+capability-advertise+add-path+receive) { ipv4-address | ipv6-address | group-name } capability-advertise add-path receive
     ```
  5. Commit the configuration.
     
     
     ```
     commit
     ```

#### Verifying the Configuration

After completing the configurations, check the configurations on the device that advertises Add-Path routes.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) **verbose** command to check the BGP4+ Add-Path status.