Configuring Layer 3 VXLAN Gateways
==================================

Configuring Layer 3 VXLAN Gateways

#### Context

Each tenant can be identified by a VNI. VNIs can be mapped to BDs in 1:1 mode, and a BD can function as a VXLAN network entity to transmit VXLAN data packets. You can create a VBDIF interface (logical Layer 3 interface) for each BD to implement communication between VXLAN segments, between VXLAN segments and non-VXLAN segments, and between Layer 2 and Layer 3 networks. After you configure an IP address for a VBDIF interface, the interface functions as the gateway for tenants in the BD to forward packets at Layer 3 based on the IP address.

In distributed VXLAN gateway scenarios, inter-subnet communication between hosts requires Layer 3 forwarding. To allow this, Layer 3 VXLAN gateways must be configured.


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
3. Bind the VBDIF interface to a VPN instance.
   
   
   ```
   [ip binding vpn-instance](cmdqueryname=ip+binding+vpn-instance) vpn-instance-name
   ```
4. Configure an IP address for the VBDIF interface to implement Layer 3 communication.
   * On an IPv4 overlay network, run the following command to configure an IPv4 address:
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
     ```
   * On an IPv6 overlay network, run the following command to configure an IPv6 address:
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length } [ eui-64 ]
     ```
5. (Optional) Configure a MAC address for the VBDIF interface.
   
   
   ```
   [mac-address](cmdqueryname=mac-address) mac-address
   ```
   
   By default, the MAC address of a VBDIF interface is the system MAC address.
6. (Optional) Enable ARP broadcast probe used when a VXLAN tunnel or Layer 2 sub-interface goes down.
   
   
   ```
   [arp broadcast-detect enable](cmdqueryname=arp+broadcast-detect+enable)
   ```
   
   By default, ARP broadcast probe is disabled when a VXLAN tunnel or Layer 2 sub-interface goes down.
   
   If the VXLAN tunnel or Layer 2 sub-interface on the local device is down, the ARP entries learned from the VXLAN tunnel or Layer 2 sub-interface are deleted. As a result, traffic cannot be forwarded. By default, the device triggers ARP Miss messages through traffic forwarding to relearn ARP entries. To enable the device to quickly learn ARP entries, enable ARP broadcast probe on the VBDIF interface.
7. Enable the distributed gateway function.
   
   
   ```
   [vxlan anycast-gateway enable](cmdqueryname=vxlan+anycast-gateway+enable)
   ```
   
   
   
   By default, the distributed gateway function is disabled.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   After the distributed gateway function is enabled on a Layer 3 gateway, the Layer 3 gateway discards network-side ARP or NS messages and learns only user-side ARP or NS messages.
8. Configure host route advertisement based on overlay network types and the types of routes to be advertised between gateways.
   
   
   
   **Table 1** Configuring host route advertisement
   | Overlay Network Type | Type of Route to Be Advertised Between Gateways | Command for Host Route Advertisement |
   | --- | --- | --- |
   | IPv4 | IRB route | [**arp collect host enable**](cmdqueryname=arp+collect+host+enable) |
   | IP prefix route | [**arp direct-route enable**](cmdqueryname=arp+direct-route+enable) [ **route-policy** *route-policy-name* ] |
   | IPv6 | IRB route | [**ipv6 nd collect host enable**](cmdqueryname=ipv6+nd+collect+host+enable) |
   | IP prefix route | [**ipv6 nd direct-route enable**](cmdqueryname=ipv6+nd+direct-route+enable) [ **route-policy** *route-policy-name* ] |
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```