Configuring a VXLAN BD Whitelist for MAC Address Flapping Detection
===================================================================

Configuring a VXLAN BD Whitelist for MAC Address Flapping Detection

#### Prerequisites

Before configuring a VXLAN BD whitelist for MAC address flapping detection, you have completed one of the following tasks:

* [Establishing VXLAN Tunnels in Static Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1039.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](dc_vrp_vxlan_cfg_1066.html)


#### Context

In some VXLAN scenarios, when a device connects to a load balancing server equipped with two network interface cards, two interfaces on the device may learn the MAC address of the server. This is normal and MAC address flapping detection is not needed, so you can configure a VXLAN BD whitelist for MAC address flapping detection.

By default, MAC address flapping detection is enabled globally. However, detection is not performed for a BD that has been added to a MAC address flapping detection whitelist. Even if MAC address flapping occurs in the BD, it does not generate an alarm or a record.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a VXLAN BD whitelist for MAC address flapping detection.
   
   
   ```
   [mac-address flapping detection exclude bridge-domain](cmdqueryname=mac-address+flapping+detection+exclude+bridge-domain) bd-id1 [ to bd-id2 ]
   ```
   
   By default, no VXLAN BD whitelist for MAC address flapping detection is configured.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display mac-address flapping**](cmdqueryname=display+mac-address+flapping) command to check the MAC address flapping detection configuration.