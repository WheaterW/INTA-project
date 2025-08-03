Configuring BGP SoO
===================

Configuring BGP SoO

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001533101177__fig199541322121811), DeviceA, DeviceB, Server, and Leaf reside in different ASs. DeviceA and DeviceB are connected to Server and establish EBGP peer relationships with Leaf and Server to transmit public network unicast routes. To reduce redundant routes, configure the SoO function on DeviceA and DeviceB. When DeviceA advertises a route to Leaf, it adds the SoO attribute to the route. After receiving the route forwarded by Leaf, DeviceB checks the SoO attribute carried in the route. If the SoO attribute is the same as that configured on DeviceB, DeviceB does not accept this route, reducing memory usage and route selection costs.

**Figure 1** BGP SoO application on a public network  
![](figure/en-us_image_0000001543493569.png)

#### Prerequisites

Before configuring BGP SoO, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the BGP-IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Configure an SoO value for a BGP peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+soo-reverse) { peerIpv4Addr | groupName } [soo-reverse](cmdqueryname=peer+soo-reverse) sooString
   ```
   
   If BGP SoO has been enabled for a peer group, a BGP peer has been added to the peer group, and you do not want the peer to inherit BGP SoO capability from the peer group, you can run the [**peer**](cmdqueryname=peer+soo-reverse) [**soo-reverse**](cmdqueryname=peer+soo-reverse) **disable** command.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the **[**peer soo-reverse**](cmdqueryname=peer+soo-reverse)** command is run, the device checks whether the routes received from the specified peer carry the SoO value that is the same as the locally configured one. If the routes carry this SoO value, the device discards the routes. In addition, the routes cannot be saved using the [**keep-all-routes**](cmdqueryname=keep-all-routes) command.
   
   If the [**peer soo-reverse**](cmdqueryname=peer+soo-reverse) command is run for a BGP peer that does not support route-refresh, the peer relationship is torn down.
5. Enable the device to advertise extended community attributes to the specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv4-address | group-name } [advertise-ext-community](cmdqueryname=advertise-ext-community)
   ```
   
   By default, a device does not advertise extended community attributes to any peer or peer group.
   
   After the [**peer advertise-ext-community**](cmdqueryname=peer+advertise-ext-community) command is run, BGP advertises the routes with extended community attributes to the specified peer. If the peer only needs to accept the routes but not the extended community attributes, you can run the [**peer discard-ext-community**](cmdqueryname=peer+discard-ext-community) command on the peer to discard the extended community attributes in the received routing information.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, perform the following operations to verify it:

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *ipv4-address* [ *mask* | *mask-length* ] ] command to check the BGP routing table.