Configuring an IPv6 Anycast Address for an Interface
====================================================

Configuring an IPv6 Anycast Address for an Interface

#### Context

Anycast addresses and unicast addresses are in the same address range, and an anycast address is used to identify a group of interfaces on different nodes.

* Similar to a multicast address, an anycast address is listened to by multiple nodes. Therefore, it is only used as a destination address.
* The packets destined for an anycast address are transmitted to an interface in the interface group identified by the anycast address and closest to the source node. (The distance between an interface and the source node is calculated based on the routing protocol). The packets destined for a multicast address are transmitted to a group of interfaces with the multicast address.

When the 6to4 tunnel is used for the communication between the 6to4 network and the native IPv6 network, the device supports the configuration of an anycast address with the prefix of **2002:c058:6301/48** on the tunnel interface of the 6to4 relay routing device.

Alternatively, you can configure a 6to4 address on the tunnel interface of the 6to4 relay routing device. When multiple 6to4 relay routing devices are configured on the network, the difference between the two methods is as follows:

* If a 6to4 address is used, you need to configure different addresses for the tunnel interfaces of all devices.
* If an anycast address is used, you need to configure the same address for the tunnel interfaces of all devices, reducing the number of addresses. If a 6to4 relay routing device fails, the 6to4 routing device can send packets to another 6to4 relay routing device based on the anycast address.

![](public_sys-resources/note_3.0-en-us.png) 

Before configuring an IPv6 anycast address, ensure that the system has been configured with a 6to4 tunnel. Moreover, this tunnel's source interface has been configured with an IPv4 anycast address on the network segment 192.168.99.0/24.




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
5. Configure an IPv6 anycast address for the interface.
   
   
   ```
   [ipv6 address](cmdqueryname=ipv6+address+anycast) { ipv6-address prefix-length | ipv6-address/prefix-length } anycast [ tag tag-value ]
   ```
   
   A maximum of 16 IPv6 anycast addresses can be configured for each interface.
   
   An anycast address is not necessarily a subnet-router anycast address. Instead, it can be a global unicast address that is configured using the [**ipv6 address anycast**](cmdqueryname=ipv6+address+anycast) command.
6. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```