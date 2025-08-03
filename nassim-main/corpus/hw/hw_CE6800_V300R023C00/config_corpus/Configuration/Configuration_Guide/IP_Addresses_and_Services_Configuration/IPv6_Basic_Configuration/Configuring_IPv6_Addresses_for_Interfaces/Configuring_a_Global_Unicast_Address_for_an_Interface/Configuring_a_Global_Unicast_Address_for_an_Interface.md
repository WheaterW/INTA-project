Configuring a Global Unicast Address for an Interface
=====================================================

Configuring a Global Unicast Address for an Interface

#### Context

Global unicast addresses, equivalent to public IPv4 addresses, are used for data forwarding on a public network and are necessary for the communication between users.

EUI-64 addresses function the same as global unicast addresses. The difference is that only the network bits need to be specified for an EUI-64 address, and the host bits are derived from the interface MAC address; for a global unicast address, all 128 bits must be specified. The prefix length of the network bits in an EUI-64 address must not be longer than 64 bits.

EUI-64 addresses, global unicast addresses, or both can be configured on an interface to enable communication. Those configured on the same interface, however, must belong to different network segments.


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
5. Configure a global unicast address for the interface.
   
   
   ```
   [ipv6 address](cmdqueryname=ipv6+address+eui-64) { ipv6-address prefix-length | ipv6-address/prefix-length } [ eui-64 ] [ tag tag-value ]
   ```
   
   A maximum of 16 global unicast addresses can be configured for each interface.
   
   A global unicast address cannot be the same as its network prefix, because this type of address is a subnet-router anycast address reserved for a device. However, this rule does not apply to an IPv6 address with a 127-bit network prefix.
6. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```