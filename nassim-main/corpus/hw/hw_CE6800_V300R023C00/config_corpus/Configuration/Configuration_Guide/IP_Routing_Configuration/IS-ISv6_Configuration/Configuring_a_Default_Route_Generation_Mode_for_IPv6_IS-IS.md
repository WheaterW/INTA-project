Configuring a Default Route Generation Mode for IPv6 IS-IS
==========================================================

Configuring a Default Route Generation Mode for IPv6 IS-IS

#### Prerequisites

Before configuring a default route generation mode for IPv6 IS-IS, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

The destination address and mask of an IPv6 default route are ::/0. If the destination address of a packet does not match any entry in the routing table of a device, the device sends the packet along the default route. If neither the default route nor a match entry exists in the routing table, the device discards the packet and informs the source end that the destination address or network is unreachable.

Default route generation can be controlled using either of the following methods:

* Configure default route advertisement on a device, enabling it to add a default route to an LSP and advertise it to its neighbors. Consequently, the neighbors can learn the default route.
* Allow Level-1 devices to generate a default route upon receipt of a Level-1 LSP with the ATT bit set to 1. According to IS-IS, if a Level-1-2 device can reach more areas through the Level-2 area than through the local Level-1 area, the device sets the ATT bit to 1 in the Level-1 LSP to be advertised to the local Level-1 area. Upon receipt of the Level-1 LSP, each Level-1 device generates a default route, with the Level-1-2 device as the next hop. You can also configure a Level-1-2 device whether to set the ATT bit to 1 in the preceding situation and configure a Level-1 device whether to generate a default route upon receipt of a Level-1 LSP with the ATT bit set to 1.![](public_sys-resources/note_3.0-en-us.png) 
  
  The second method applies only to Level-1 devices.

#### Procedure

* Configure default route advertisement.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure default route advertisement for IPv6 IS-IS.
     
     
     ```
     [ipv6 default-route-advertise](cmdqueryname=ipv6+default-route-advertise) [ always | match default | route-policy route-policy-name ] [ [ cost cost ] | [ tag tag ] | [ level-1 | level-1-2 | level-2 ] ] * [ avoid-learning ]
     ```
     
     The level of the device determines the level of the generated default route, which is advertised only to other devices of the same level as the local device. You can configure a route-policy so that the IPv6 IS-IS device generates a default route only when matching routes exist in the local routing table.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the Level-1-2 device whether to set the ATT bit to 1 in the Level-1 LSPs to be sent.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. Configure the Level-1-2 device whether to set the ATT bit to 1 in the Level-1 LSPs to be sent.
     
     
     ```
     [attached-bit advertise](cmdqueryname=attached-bit+advertise) { always | never }
     ```
     
     By default, a Level-1-2 routing device's Level-2 LSDB contains routing information that does not exist in the Level-1 LSDBs in the local Level-1 area, and the ATT bit in the Level-1 LSPs advertised by the Level-1-2 routing device is set to 1.
     
     If the **always** parameter is specified, the Level-1-2 device sets the ATT bit to 1 in the Level-1 LSPs to be sent. By default, each Level-1 device generates a default route after receiving the LSPs.
     
     If the **never** parameter is specified, the Level-1-2 device keeps the ATT bit as 0 in the Level-1 LSPs to be sent, preventing the receivers of these Level-1 LSPs from generating a default route and in turn reducing the routing table size.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Disable a Level-1 device from generating a default route based on the ATT bit that is set to 1 in received Level-1 LSPs.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IS-IS view.
     
     
     ```
     [isis](cmdqueryname=isis) [ process-id ]
     ```
  3. The Level-1 device is disabled from generating a default route even though it receives Level-1 LSPs carrying the ATT bit that is set to 1.
     
     
     ```
     [attached-bit avoid-learning](cmdqueryname=attached-bit+avoid-learning)
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display isis**](cmdqueryname=display+isis) *process-id* **route** **ipv6** [ *ipv6-address* [ *ipv6-mask-length* ] | { **level-1** | **level-2** } | **verbose** ] \* command to check IPv6 IS-IS routing information.
* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ **verbose** [ **no-name** ] | { **level-1** | **level-2** } | { **local** | *lspid* | **is-name** *isname* } ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.