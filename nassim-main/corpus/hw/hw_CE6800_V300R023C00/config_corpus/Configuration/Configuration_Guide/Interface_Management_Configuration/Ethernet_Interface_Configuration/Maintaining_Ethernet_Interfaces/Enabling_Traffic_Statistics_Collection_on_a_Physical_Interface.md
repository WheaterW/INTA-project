Enabling Traffic Statistics Collection on a Physical Interface
==============================================================

Enabling Traffic Statistics Collection on a Physical Interface

#### Context

To check the network status or locate network faults, you can enable traffic statistics collection on interfaces. By default, traffic statistics collection is enabled on a Layer 2 physical interface.

To collect statistics about IPv4 or IPv6 packets on a Layer 2 physical interface, you can enable IPv4 or IPv6 traffic statistics collection. By default, IPv4 or IPv6 traffic statistics collection is disabled on interfaces.

![](public_sys-resources/note_3.0-en-us.png) 

* Enabling IPv4 or IPv6 traffic statistics collection on Layer 2 physical interfaces may affect the forwarding performance. For example, some interfaces may fail to forward packets at the line rate when all interfaces provide line-rate forwarding. Therefore, use this function only when necessary. You are advised to disable this function immediately after using it.
* IPv4 or IPv6 traffic statistics collection on Layer 2 physical interfaces needs to occupy ACL resources of the system. If traffic statistics collection is enabled on too many Layer 2 physical interfaces, other services may fail to obtain ACL resources.
* The system cannot collect statistics on unicast and multicast packets separately.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Enable traffic statistics collection on the interface
   
   
   ```
   [statistics](cmdqueryname=statistics) { ipv4 | ipv6 } enable [ inbound | outbound ]
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command in any view or the [**display this interface**](cmdqueryname=display+this+interface) command in the interface view to check traffic statistics on the interface.