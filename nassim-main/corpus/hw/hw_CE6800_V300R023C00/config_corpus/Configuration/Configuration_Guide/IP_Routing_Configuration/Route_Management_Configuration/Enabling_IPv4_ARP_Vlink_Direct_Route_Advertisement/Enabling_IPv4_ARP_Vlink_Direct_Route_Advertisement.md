Enabling IPv4 ARP Vlink Direct Route Advertisement
==================================================

Enabling IPv4 ARP Vlink Direct Route Advertisement

#### Prerequisites

Before configuring IPv4 ARP Vlink direct route advertisement, you have completed the following task:

* Set data link layer protocol parameters and IPv4 addresses for interfaces to ensure that the data link layer protocol status on each interface is up.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable IPv4 ARP Vlink direct route advertisement.
   
   
   ```
   [arp direct-route enable](cmdqueryname=arp+direct-route+enable)
   ```
   
   After the device is enabled to advertise IPv4 ARP Vlink direct routes, IPv4 ARP Vlink direct routes can be advertised only after they are imported to the routing table of a dynamic routing protocol. Perform one of the following operations based on a routing protocol running on a device:
   
   * Enable RIP to import and advertise IPv4 ARP Vlink direct routes.
     ```
     [import-route](cmdqueryname=import-route) direct [ cost cost | route-policy route-policy-name ] *
     ```
   * Enable OSPF to import and advertise IPv4 ARP Vlink direct routes.
     ```
     [import-route](cmdqueryname=import-route) direct [ cost cost | route-policy route-policy-name | tag tag | type type ] *
     ```
   * Enable IS-IS to import and advertise IPv4 ARP Vlink direct routes.
     ```
     [import-route](cmdqueryname=import-route) direct [ cost-type { external | internal } | cost cost | tag tag | route-policy route-policy-name | [ level-1 | level-2 | level-1-2 ] ] *
     ```
   * Enable BGP to import and advertise IPv4 ARP Vlink direct routes.
     ```
     [import-route](cmdqueryname=import-route) direct [ med med | route-policy route-policy-name ] *
     ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
   ```
4. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Set a preference value for ARP Vlink direct routes.
   
   
   ```
   [arp direct-route preference](cmdqueryname=arp+direct-route+preference) preference-value
   ```
   
   By default, the preference value of ARP Vlink direct routes on VLANIF interfaces is 255, and the preference value of ARP Vlink direct routes on VBDIF interfaces is 0. ARP Vlink direct routes can be advertised by different routing protocols. If there are multiple ARP Vlink direct routes advertised by different routing protocols, you can run this command to change the preference values of these routes for route selection.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support VBDIF interfaces.
6. Set a tag value for ARP Vlink direct routes.
   
   
   ```
   [arp direct-route tag](cmdqueryname=arp+direct-route+tag) tag-value
   ```
   
   
   By default, the tag value of ARP Vlink direct routes to be advertised is 0. To change the tag value of ARP Vlink direct routes, run the [**arp direct-route tag**](cmdqueryname=arp+direct-route+tag) command. As shown in [Figure 1](#EN-US_TASK_0000001130622772__en-us_task_0172365357_en-us_cliref_0172379007_fig_arp_direct-route_tag01), GW1 and GW2 function as gateways and have the same IP address. GW1 and GW2 learn ARP entries carrying Switch information and generate ARP Vlink direct routes. GW1 and GW2 advertise the generated ARP Vlink direct routes and direct network segment routes destined for 10.1.1.6/24. The ARP Vlink direct routes and direct network segment routes cannot be advertised separately because they have the same tag value. If the link between GW1 and Switch fails, a related ARP Vlink direct route is withdrawn, but the network segment route advertised by GW1 is not withdrawn. As a result, DeviceA cannot detect the link fault and traffic cannot be quickly switched to the link between GW2 and Switch, causing a traffic forwarding failure. To resolve this problem, run the [**arp direct-route tag**](cmdqueryname=arp+direct-route+tag) command to change the tag value of ARP Vlink direct routes and create a route-policy to match the tag value. In this way, GW1 advertises only the ARP Vlink direct routes but not the direct network segment routes. If the link between GW1 and Switch fails, GW1 cannot learn ARP entries. After the ARP Vlink direct routes are withdrawn, DeviceA detects the fault on the link between GW1 and Switch and rapidly switches traffic to the link between GW2 and Switch.**Figure 1** Network diagram of setting a tag value for ARP Vlink direct routes  
   ![](figure/en-us_image_0000001130782570.png)
7. Set a delay in advertising ARP Vlink direct routes.
   
   
   ```
   [arp direct-route delay](cmdqueryname=arp+direct-route+delay) delay-time
   ```
   
   
   
   To prevent traffic loss when ARP Vlink direct route update is slower than route diversion, you can set a delay in advertising ARP Vlink direct routes.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```