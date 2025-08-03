Configuring a BGP Peer to Track the Physical Status of a Specified Physical Interface
=====================================================================================

Configuring a BGP Peer to Track the Physical Status of a Specified Physical Interface

#### Prerequisites

Before configuring a BGP peer to track the physical status of a specified physical interface, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Context

A device sets up BGP peer relationships with certain servers in a VLAN through a VLANIF interface. If the physical status of the interface connected to a server goes down, the BGP peer cannot quickly detect the status change, and the BGP peer relationship is disconnected only after a set period (180s by default). During this time, traffic is lost. To prevent this problem, enable the BGP peer to track the physical status of a specified physical interface. After the function is enabled, the establishment of a BGP peer relationship depends on the physical status of the specified physical interface. If the physical status of the specified physical interface is up, the BGP peer relationship can be established. If the physical status is down, the BGP peer relationship is disconnected.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. (Optional) Enter the VPN instance view or BGP-VPN instance IPv4 address family view.
   1. (Optional) Enter the BGP-VPN instance view.
      
      
      ```
      vpn-instance vpn-instance-name
      ```
   2. (Optional) Enter the BGP-VPN instance IPv4 address family view.
      
      
      ```
      [ipv4-family](cmdqueryname=ipv4-family+vpn-instance) vpn-instance vpn-instance-name
      ```
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      Ensure that a VPN instance has been created before you enter the VPN instance view or BGP-VPN instance IPv4 address family view.
4. Configure a BGP peer to track the physical status of a specified physical interface.
   
   
   ```
   [peer](cmdqueryname=peer+rely-state+interface) ipv4-address rely-state interface interface-type interface-number
   ```
   
   By default, a BGP peer is disabled from tracking the physical status of a specified physical interface.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) **verbose** command to check whether the BGP peer is configured to track the physical status of a specified physical interface.

If **Rely-state interface has been enabled** is displayed in the command output, the configuration is successful.