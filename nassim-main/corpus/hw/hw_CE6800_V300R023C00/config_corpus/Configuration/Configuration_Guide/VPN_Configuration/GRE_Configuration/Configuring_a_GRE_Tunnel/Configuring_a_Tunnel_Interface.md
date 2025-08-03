Configuring a Tunnel Interface
==============================

Configuring a Tunnel Interface

#### Prerequisites

Before configuring a tunnel interface, you have completed the following task:

* Configure a routing protocol to ensure IP connectivity between devices.

#### Context

A tunnel interface must be configured on each end of a GRE tunnel to be established. You need to set the tunnel encapsulation type of the tunnel interfaces to GRE and specify a source address (or source interface) and a destination address for the interfaces. If the tunnel interfaces need to be advertised using dynamic routing protocols, you also need to configure IP addresses for the tunnel interfaces.

When configuring a source interface for a tunnel, do not specify the tunnel interface of this tunnel as the source interface. Instead, specify the tunnel interface of another tunnel.

The MTU value is valid only when a local device sends locally originated packets over a GRE tunnel and is invalid when a local device forwards received packets over a GRE tunnel.

A tunnel interface is a logical interface and goes down in the following situations:

* The destination address configured for the tunnel interface is unreachable or is the IP address of the tunnel interface.
* The source interface configured for the tunnel interface is down.
* The IP address configured for the tunnel interface is invalid.
* The keepalive function is configured on the tunnel interface and detects that the tunnel remote end is unreachable.

Perform the following steps on the devices at both ends of a GRE tunnel.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a tunnel interface and enter the tunnel interface view.
   
   
   ```
   [interface](cmdqueryname=interface) tunnel interface-number
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The tunnel interface on a centralized GRE tunnel must be named using the slot ID, subcard ID, and interface number. The tunnel interface's slot ID must be the same as the slot ID of the tunnel where the source interface resides. If the slot IDs are different, the GRE tunnel cannot be established.
3. (Optional) Configure a description for the tunnel interface.
   
   
   ```
   [description](cmdqueryname=description) text
   ```
4. Set the tunnel encapsulation type to GRE.
   
   
   ```
   [tunnel-protocol](cmdqueryname=tunnel-protocol) gre
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Configuring, changing, or deleting the tunnel mode of a tunnel interface will delete all tunnel-related configurations on the interface, such as the MTU. Exercise caution when performing this operation.
5. Configure a source address or source interface for the tunnel interface.
   
   
   ```
   [source](cmdqueryname=source) { source-ip-address | interface-type interface-number }
   ```
6. Configure a destination address for the tunnel interface.
   
   
   ```
   [destination](cmdqueryname=destination) ip-address
   ```
7. (Optional) Set the MTU for the tunnel interface.
   
   
   ```
   [mtu](cmdqueryname=mtu) mtu
   ```
8. (Optional) Enable path MTU auto-discovery on the tunnel interface.
   
   
   ```
   [tunnel pathmtu enable](cmdqueryname=tunnel+pathmtu+enable)
   ```
   
   
   
   By default, path MTU auto-discovery is disabled.
9. (Optional) Enable the MTU check function for the GRE tunnel.
   
   
   ```
   [mtu check enable](cmdqueryname=mtu+check+enable)
   ```
   
   By default, the MTU check function is disabled for a GRE tunnel.
   
   After the MTU check function is enabled for a GRE tunnel using this command, when packets need to be transmitted through the GRE tunnel, the device first checks whether the packet lengths exceed the MTU of the tunnel. If so, the device sends an ICMP Packet Too Big message to the sender (specified by the source IP address of the packets) to notify the sender that the packet lengths exceed the MTU and provide a TCP packet fragment size reference for the sender.
10. (Optional) Configure the DiffServ mode for the tunnel interface.
    
    
    ```
    [tunnel pipe dscp](cmdqueryname=tunnel+pipe+dscp) dscpvalue
    ```
    
    By default, the DiffServ mode of a tunnel interface is uniform.
11. Configure an IP address for the tunnel interface. By default, no IP address is configured for a tunnel interface. If a dynamic routing protocol is used on the tunnel interface, configure an IP address for the tunnel interface. The IP addresses of tunnel interfaces on both ends of a tunnel must be on the same network segment. Perform one of the following operations:
    
    
    * Configure an IPv4 address for the tunnel interface.
      ```
      [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
      ```
    * Configure the tunnel interface to borrow an IPv4 address.
      ```
      [ip address unnumbered](cmdqueryname=ip+address+unnumbered) interface interface-type interface-number
      ```
    * Configure an IPv6 address for the tunnel interface.
      ```
      [ipv6 enable](cmdqueryname=ipv6+enable)
      [ipv6 address](cmdqueryname=ipv6+address) ipv6-address prefix-length
      ```
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```