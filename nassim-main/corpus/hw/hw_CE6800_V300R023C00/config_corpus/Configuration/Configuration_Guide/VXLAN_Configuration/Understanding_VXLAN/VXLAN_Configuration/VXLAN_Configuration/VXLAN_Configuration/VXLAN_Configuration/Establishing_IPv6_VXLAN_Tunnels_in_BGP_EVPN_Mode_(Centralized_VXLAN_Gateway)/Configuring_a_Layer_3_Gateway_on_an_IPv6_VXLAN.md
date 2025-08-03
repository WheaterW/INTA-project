Configuring a Layer 3 Gateway on an IPv6 VXLAN
==============================================

Configuring a Layer 3 Gateway on an IPv6 VXLAN

#### Context

On an IPv6 VXLAN, a BD can be mapped to a VNI (identifying a tenant) in 1:1 mode to transmit VXLAN data packets. You can create a VBDIF interface (logical Layer 3 interface) for each BD to implement communication between IPv6 VXLAN segments, between IPv6 VXLAN segments and non-VXLAN segments, and between Layer 2 and Layer 3 networks. After you configure an IP address for a VBDIF interface, the interface functions as the gateway for tenants in the BD to forward packets at Layer 3 based on the IP address.

VBDIF interfaces are configured on Layer 3 gateways for inter-segment communication, and are not required for intra-segment communication.

![](../public_sys-resources/note_3.0-en-us.png) 

The DHCP relay function can be configured on a VBDIF interface so that hosts can request IP addresses from an external DHCP server.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a VBDIF interface and enter its view.
   
   
   ```
   [interface vbdif](cmdqueryname=interface+vbdif) bd-id
   ```
   
   *bd-id* specified in this command must be the same as *bd-id* specified in Step 2 in the service access point configuration.
3. Configure an IPv6 address for the VBDIF interface to implement Layer 3 communication.
   * On an IPv4 overlay network, run the following command to configure an IPv4 address:
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
     ```
   * On an IPv6 overlay network, run the following command to configure an IPv6 address:
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length } [ eui-64 ]
     ```
4. (Optional) Configure a MAC address for the VBDIF interface.
   
   
   ```
   [mac-address](cmdqueryname=mac-address) mac-address
   ```
   
   By default, the MAC address of a VBDIF interface is the system MAC address.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```