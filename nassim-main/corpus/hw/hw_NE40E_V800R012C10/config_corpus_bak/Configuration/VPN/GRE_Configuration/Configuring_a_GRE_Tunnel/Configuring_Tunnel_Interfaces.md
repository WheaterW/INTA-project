Configuring Tunnel Interfaces
=============================

After creating a tunnel interface, you need to specify GRE as the encapsulation type and configure a source address or source interface and a destination address for the tunnel interface. To enable the tunnel to support dynamic routing protocols, you aso need to configure an IP address for the tunnel interface.

#### Context

A GRE tunnel is established between tunnel interfaces on the two ends of the tunnel. Therefore, you need to configure tunnel interfaces on devices at the two ends of the tunnel. For a GRE tunnel interface, you need to specify the protocol type as GRE and configure a source address or source interface and a destination address for the tunnel interface. You also need to specify an IP address if a dynamic routing protocol is used.

Note that you must not specify the involved tunnel interface as the source interface for a GRE tunnel. Instead, specify another interface that can be either a common interface or the tunnel interface of another tunnel on the same device.

The MTU value is valid only when a local device sends locally originated packets over a GRE tunnel and is invalid when a local device forwards received packets over a GRE tunnel.

A tunnel interface, which is a logical interface, goes down in any of the following situations:

* The destination address configured for the tunnel interface is unreachable or is set to the IP address of the tunnel interface.
* The source interface configured for the tunnel interface is down.
* The IP address configured on the tunnel interface is invalid.
* The keepalive function is configured on the tunnel interface and detects that the tunnel remote end is unreachable.

If the tunnel interface is deleted, all configurations on the tunnel interface are also deleted.

Perform the following steps on the endpoint Routers of a tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **tunnel** *interface-number*
   
   
   
   A tunnel interface is created, and its view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   A tunnel description is configured.
4. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **gre**
   
   
   
   GRE is configured as the tunneling protocol.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Changing, deleting, or initially configuring the tunnel mode of a tunnel interface will delete all tunnel-related configurations on the interface, such as the MTU. Exercise caution when performing this operation.
5. Run [**source**](cmdqueryname=source) { *ip-address* | *ifName* | *ifType ifNum* }
   
   
   
   A source address or source interface of the tunnel is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**binding tunnel gre**](cmdqueryname=binding+tunnel+gre) command must be run to bind the source interface or the interface where the source address resides to GRE. After the binding is configured, a GRE tunnel can use such an interface to forward GRE-encapsulated packets.
6. Run [**destination**](cmdqueryname=destination) [ **vpn-instance** *vpn-instance-name* ] *ip-address* The destination address of the tunnel interface is set.
7. (Optional) Run [**mtu**](cmdqueryname=mtu) *mtu*
   
   
   
   The MTU of the tunnel interface is set.
8. (Optional) Run [**tunnel pathmtu enable**](cmdqueryname=tunnel+pathmtu+enable)
   
   
   
   Path MTU learning is enabled.
   
   
   
   If two BGP nodes on which the [**peer path-mtu auto-discovery**](cmdqueryname=peer+path-mtu+auto-discovery) command is run communicate over a GRE tunnel, you can run the [**tunnel pathmtu enable**](cmdqueryname=tunnel+pathmtu+enable) command on tunnel interfaces of both nodes to prevent repetitive fragmentation for TCP packets carrying BGP messages when such packets are transmitted along the GRE tunnel, improving BGP message transmission efficiency.
9. (Optional) Run [**tcp adjust-mss**](cmdqueryname=tcp+adjust-mss) *mss-value* **inbound**
   
   
   
   An MSS is set for inbound TCP SYN/SYN+ACK packets of the GRE tunnel.
   
   
   
   You can set the MSS to be less than the sum of the configured interface MTU and GRE header length, so that the packets accepted by the tunnel interface will not be fragmented when being transmitted over the GRE tunnel.
10. Configure an IP address for the tunnel interface. Perform either of the following operations:
    
    
    * To configure an IPv4 address for the tunnel interface, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command.
    * To configure the tunnel interface to borrow an IPv4 address, run the [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered) **interface** *interface-type* *interface-number* command.
    
    To enable the tunnel to support dynamic routing protocols, you aso need to configure an IP address for the tunnel interface. The IP addresses of the tunnel interfaces on both ends of the GRE tunnel can be either public or private addresses and must be on the same network segment.
11. (Optional) Run [**target reassemble board**](cmdqueryname=target+reassemble+board) *slot-id* [ **backup** *slave-slot-id* ]
    
    
    
    A tunnel interface is mapped to a tunnel service board so that GRE fragments can be assembled on the tunnel service board.
    
    
    
    If GRE packets are fragmented during transmission over a tunnel (for example, when packets are forwarded over multiple transit links in load-balancing mode), configure a packet reassembly board on the egress of the tunnel so that all fragmented packets are reassembled on the same board.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The **target reassemble board** command takes effect for distributed
    GRE tunnels only.
12. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the tunnel interface view.
13. (Optional) Run [**global-gre forward-mode**](cmdqueryname=global-gre+forward-mode) { **through** | **loopback** }
    
    
    
    A forwarding mode is specified, which takes effect for all distributed GRE tunnels.
    
    
    
    Configure an appropriate forwarding mode based on service requirements.
    
    * **through**: enables the software loopback mode. This mode supports high forwarding performance, but does not support HQoS functions for outgoing packets.
    * **loopback**: enables the hardware loopback mode. This mode provides only half of the forwarding performance compared with the software loopback mode, but supports HQoS functions for outgoing packets.
    
    This command takes effect only for distributed GRE tunnels.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.