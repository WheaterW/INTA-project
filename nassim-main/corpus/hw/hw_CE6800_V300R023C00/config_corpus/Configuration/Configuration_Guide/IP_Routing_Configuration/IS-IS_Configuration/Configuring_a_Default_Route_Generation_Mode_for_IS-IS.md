Configuring a Default Route Generation Mode for IS-IS
=====================================================

Configuring a Default Route Generation Mode for IS-IS

#### Prerequisites

Before configuring a default route generation mode for IS-IS, you have completed the following task:

* [Configure basic IS-IS functions](vrp_isis_ipv4_cfg_0011.html).

#### Context

If IS-IS is configured to advertise a default route on a border device that has external routes, the device advertises a default route 0.0.0.0/0 in the local area. After other devices receive the default route from the border device, they forward the traffic destined for other areas to the border device, which then forwards the traffic outside the local area. A static default route can also be configured on each device that needs to forward traffic destined for other areas to ensure the device forwards the traffic to the border device. However, this can lead to heavy configuration and management workloads when a large number of devices need to have static routes configured. In addition, default route advertisement using IS-IS is more flexible. If multiple border devices exist, you can configure a route-policy to allow only the border device that meets specified conditions to advertise a default route, which prevents routing black holes.

Default route generation can be controlled using either of the following methods:

* Configure default route advertisement on a device, enabling it to add a default route to an LSP and advertise it to its neighbors. Consequently, the neighbors can learn the default route.
* Allow Level-1 devices to generate a default route upon receipt of a Level-1 LSP with the ATT bit set to 1. According to IS-IS, if a Level-1-2 device can reach more areas through the Level-2 area than through the local Level-1 area, the device sets the ATT bit to 1 in the Level-1 LSP to be advertised to the local Level-1 area. Upon receipt of the Level-1 LSP, each Level-1 device generates a default route, with the Level-1-2 device as the next hop. Based on network requirements, you can configure whether the ATT bit is set and whether a Level-1 routing device generates a default route after it receives an LSP in which the ATT bit is set.![](public_sys-resources/note_3.0-en-us.png) 
  
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
  3. Configure default route advertisement.
     
     
     ```
     [default-route-advertise](cmdqueryname=default-route-advertise) [ always | match default | route-policy route-policy-name ] [ cost cost | tag tag | level-1 | level-1-2 | level-2 ] * [ avoid-learning ]
     ```
     
     The level of the device determines the level of the generated default route, which is advertised only to other devices of the same level as the local device. You can configure a route-policy so that the device generates a default route only when matching routes exist in the local routing table.
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
  3. Configure the device whether to set the ATT bit in the LSPs to be sent.
     
     
     ```
     [attached-bit advertise](cmdqueryname=attached-bit+advertise) { always | never }
     ```
     
     By default, a Level-1-2 routing device's Level-2 LSDB contains routing information that does not exist in the Level-1 LSDBs in the local Level-1 area, and the ATT bit in the Level-1 LSPs advertised by the Level-1-2 routing device is set to 1.
     
     If the **always** parameter is specified, the ATT bit is always set. After receiving the LSPs in which the ATT bit is set, the Level-1 routing device generates a default route.
     
     If the **never** parameter is specified, the ATT bit is never set. After receiving the LSPs carrying the ATT bit that is not set, each Level-1 routing device does not generate a default route, which reduces the size of its routing table.
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

* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] command to check IS-IS routing information.
* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) [ **verbose** [ **no-name** ] | { **level-1** | **level-2** } | { **local** | *lspid* | **is-name** *isname* } ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS LSDB information.