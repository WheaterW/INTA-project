Configuring BGP4+ SoO
=====================

Configuring BGP4+ SoO

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001535130025__fig20544202814319), DeviceA, DeviceB, Server, and Leaf reside in different ASs. DeviceA and DeviceB are connected to Server and establish EBGP peer relationships with Leaf and Server to transmit public network unicast routes. To reduce redundant routes, configure the SoO function on DeviceA and DeviceB. When DeviceA advertises a route to Leaf, it adds the SoO attribute to the route. After receiving the route forwarded by Leaf, DeviceB checks the SoO attribute carried in the route. If the SoO attribute is the same as that configured on DeviceB, DeviceB does not accept this route, reducing memory usage and route selection costs.

**Figure 1** BGP4+ SoO application in a public network IPv6 scenario  
![](figure/en-us_image_0000001484529844.png)

#### Prerequisites

Before configuring BGP4+ SoO, complete the following tasks:

* [Configure basic BGP4+ functions.](vrp_bgp6_cfg_0006.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the BGP-IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Configure an SoO value for a BGP4+ peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+soo-reverse) { peerIpv6Addr | groupName } [soo-reverse](cmdqueryname=peer+soo-reverse) sooString
   ```
   
   If BGP SoO has been enabled for a peer group, a BGP peer has been added to the peer group, and you do not want the peer to inherit BGP SoO capability from the peer group, you can run the [**peer**](cmdqueryname=peer+soo-reverse) [**soo-reverse**](cmdqueryname=peer+soo-reverse) **disable** command.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the **[**peer soo-reverse**](cmdqueryname=peer+soo-reverse)** command is run, the device checks whether the routes received from the specified peer carry the SoO value that is the same as the locally configured one. If the routes carry this SoO value, the device discards the routes. In addition, the routes cannot be saved using the [**keep-all-routes**](cmdqueryname=keep-all-routes) command.
   
   If the [**peer soo-reverse**](cmdqueryname=peer+soo-reverse) command is run for a BGP peer that does not support route-refresh, the peer relationship is torn down.
5. Enable the device to advertise extended community attributes to the specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv6-address | group-name } [advertise-ext-community](cmdqueryname=advertise-ext-community)
   ```
   
   By default, a device does not advertise extended community attributes to any peer or peer group.
   
   After the [**peer advertise-ext-community**](cmdqueryname=peer+advertise-ext-community) command is run, BGP4+ advertises the routes with extended community attributes to the specified peer. If the peer only needs to accept the routes but not the extended community attributes, you can run the [**peer discard-ext-community**](cmdqueryname=peer+discard-ext-community) command on the peer to discard the extended community attributes in the received routing information.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) command on the remote end to check the BGP4+ routing table.