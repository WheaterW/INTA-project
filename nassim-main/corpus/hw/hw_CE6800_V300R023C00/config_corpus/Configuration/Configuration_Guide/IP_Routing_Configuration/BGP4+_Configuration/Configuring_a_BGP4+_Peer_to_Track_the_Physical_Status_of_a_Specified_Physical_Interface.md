Configuring a BGP4+ Peer to Track the Physical Status of a Specified Physical Interface
=======================================================================================

Configuring a BGP4+ Peer to Track the Physical Status of a Specified Physical Interface

#### Prerequisites

Before configuring a BGP4+ peer to track the physical status of a specified physical interface, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

A device sets up BGP4+ peer relationships with some servers in a VLAN through a VLANIF interface. If the physical status of the interface connected to a server goes down, the BGP4+ peer cannot detect the status change in time, and the BGP4+ peer relationship is disconnected after a specified period of time (180s by default). To prevent traffic loss during this period, enable the BGP4+ peer to track the physical status of a specified physical interface. The establishment of a BGP4+ peer relationship depends on the physical status of the specified physical interface. If the physical status of the specified physical interface is up, the BGP4+ peer relationship can be established; however, if the physical status is down, the BGP4+ peer relationship is disconnected.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. (Optional) Enter the VPN instance view or BGP-VPN instance IPv6 address family view.
   1. (Optional) Enter the BGP-VPN instance view.
      
      
      ```
      vpn-instance vpn-instance-name
      ```
   2. (Optional) Enter the BGP-VPN instance IPv6 address family view.
      
      
      ```
      [ipv6-family](cmdqueryname=ipv6-family+vpn-instance) vpn-instance vpn-instance-name
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      Ensure that a VPN instance has been created before you enter the VPN instance view or BGP-VPN instance IPv6 address family view.
4. Configure a BGP4+ peer to track the physical status of a specified physical interface.
   
   
   ```
   [peer](cmdqueryname=peer+rely-state+interface) ipv6-address rely-state interface interface-type interface-number
   ```
   
   By default, a BGP4+ peer is disabled from detecting the physical status of a specified physical interface.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display bgp**](cmdqueryname=display+bgp) **ipv6** **peer** **verbose** command to check whether the BGP4+ peer is configured to track the physical status of a specified physical interface.

If **Rely-state interface has been enabled** is displayed in the command output, the configuration succeeds.