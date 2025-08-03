Configuring an IPv6 MTU for an Interface
========================================

Configuring an IPv6 MTU for an Interface

#### Context

By default, devices can determine the dynamic PMTU, which is the smallest of all interface MTUs on the path from the source to the destination.

To protect a device against attacks initiated by sending jumbo packets, configure a static PMTU that defines the maximum length of a packet that can be sent from the source to the destination.

The static PMTU is usually less than or equal to the IPv6 MTU of an interface along the link. If the static PMTU is greater than the IPv6 MTU of an interface, the device fragments packets based on the IPv6 MTU.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of an interface on which IPv6 is to be enabled.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Enable IPv6 on the interface.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
5. Configure an MTU for the interface.
   
   
   ```
   [ipv6 mtu](cmdqueryname=ipv6+mtu) mtu
   ```
6. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```