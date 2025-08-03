Configuring the BGP Add-Path Function
=====================================

Configuring the BGP Add-Path Function

#### Prerequisites

Before configuring the BGP Add-Path function, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Context

Generally, BGP Add-Path is configured on an RR, and the Add-Path route receiver needs to be configured to accept such routes.

![](public_sys-resources/note_3.0-en-us.png) 

The BGP Add-Path function cannot be configured in a BGP confederation.



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
  5. Specify the IP address of a peer and the number of the AS where the peer resides.
     
     
     ```
     [peer](cmdqueryname=peer+as-number) { ipv4-address | ipv6-address | group-name } [as-number](cmdqueryname=as-number) as-number
     ```
  6. Enter the IPv4 unicast address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
     ```
     
     By default, the configuration is performed in the IPv4 unicast address family view.
  7. Enable the BGP Add-Path function and set the number of preferred routes that can be selected.
     
     
     ```
     [bestroute add-path](cmdqueryname=bestroute+add-path+path-number) path-number path-number
     ```
  8. Enable the device to send Add-Path routes to a specified peer.
     
     
     ```
     [peer](cmdqueryname=peer+capability-advertise+add-path+send) { ipv4-address | ipv6-address | group-name } capability-advertise add-path send
     ```
     
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     To run the [**peer**](cmdqueryname=peer+capability-advertise+add-path+%7B+receive+%7C+send+%7D) *ipv6-address* **capability-advertise** **add-path** **{ receive | send }** or [**peer**](cmdqueryname=peer+advertise+add-path+path-number) *ipv6-address* **advertise add-path path-number** *number* [ **route-policy** *route-policy-name* ] command, you need to enable the IPv6 peer in the IPv4 unicast address family view.
  9. Set the maximum number of preferred routes that the device can send to the peer.
     
     
     ```
     [peer](cmdqueryname=peer+advertise+add-path+path-number) { peerIpv4Addr | peerIpv6Addr | groupName } advertise add-path path-number number [ route-policy route-policy-name ]
     ```
     
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     To configure **route-policy** *route-policy-name*, you need to enter the route-policy view.
  10. Commit the configuration.
      
      
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
  3. Enable the device to accept Add-Path routes received from a specified peer.
     
     
     ```
     [peer](cmdqueryname=peer+capability-advertise+add-path+receive) { ipv4-address | ipv6-address | group-name } capability-advertise add-path receive
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the following command on the device that advertises the Add-Path routes to check configurations:

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) **verbose** command to check the BGP Add-Path status.