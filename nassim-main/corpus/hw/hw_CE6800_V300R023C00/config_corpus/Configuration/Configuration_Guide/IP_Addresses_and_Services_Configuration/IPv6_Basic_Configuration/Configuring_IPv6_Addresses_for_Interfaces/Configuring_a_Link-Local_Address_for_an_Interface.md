Configuring a Link-Local Address for an Interface
=================================================

Configuring a Link-Local Address for an Interface

#### Context

IPv6 addresses must be configured for routing device interfaces so that the routing devices can communicate with IPv6 devices.

Link-local addresses are used in neighbor discovery (ND) and in the communication between nodes on the local link during stateless address autoconfiguration. The packets with link-local addresses as source or destination addresses are forwarded only on the local link.

Link-local addresses can be automatically generated or manually configured.

* After IPv6 is enabled on an interface, the system automatically generates a link-local address for the interface.
* The link-local address that is manually configured must be valid (usually with the FE80::/10 prefix).

Link-local addresses are usually used for protocol communication between link-local nodes, meaning that these addresses are not directly related to the communication between users. Therefore, automatic generation of link-local addresses is recommended.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
5. Perform either of the following operations as required:
   
   
   * Configure the device to automatically generate a link-local address for the interface.
     
     ```
     [ipv6 address auto link-local](cmdqueryname=ipv6+address+auto+link-local)
     ```
   * Manually configure a link-local address for the interface.
     
     ```
     [ipv6 address](cmdqueryname=ipv6+address+link-local) ipv6-address link-local [ tag tag-value ]
     ```
     
     or
     
     ```
     [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length } [ tag tag-value ]
     ```
   
   You can configure multiple IPv6 addresses but only one link-local address for an interface.
   
   Manually configured link-local addresses have a higher priority than automatically generated ones. Specifically, manually configured addresses can overwrite automatically generated ones, but automatically generated addresses cannot overwrite manually configured ones. If manually configured addresses are deleted, the automatically generated ones that were previously overwritten take effect again.
6. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```