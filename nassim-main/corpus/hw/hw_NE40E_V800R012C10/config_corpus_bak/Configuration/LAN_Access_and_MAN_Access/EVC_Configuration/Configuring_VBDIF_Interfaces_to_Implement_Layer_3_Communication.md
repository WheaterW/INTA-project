Configuring VBDIF Interfaces to Implement Layer 3 Communication
===============================================================

VBDIF interfaces are Layer 3 logical interfaces. After creating VBDIF interfaces, you can configure Layer 3 features.

#### Usage Scenario

When a device needs to communicate with a Layer 3 network through EVC, you can create a BD-based logical interface (namely, the VBDIF interface), because EVC defines Layer 2 interfaces, which do not support IP addresses. VBDIF interfaces are network layer interfaces and can be assigned IP addresses. Through these IP addresses, Layer 3 communication can be implemented through EVC.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Both Layer 2 traffic and Layer 3 traffic are transmitted over the VBDIF interface. Running the [**shutdown**](cmdqueryname=shutdown) command in the VBDIF interface view prohibits only Layer 3 traffic. After running the [**display interface vbdif**](cmdqueryname=display+interface+vbdif) command, you can view that traffic statistics still increase on this VBDIF interface.

To prohibit all traffic on the VBDIF interface, run the [**shutdown**](cmdqueryname=shutdown) command in the BD view.

#### Pre-configuration Tasks

Before configuring VBDIF interfaces to implement Layer 3 communication, complete the following task:

* [Establish an EVC model](dc_vrp_evc_cfg_0003.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Configure the [**rewrite pop**](cmdqueryname=rewrite+pop) { **single** | **double** } command as an action to have all VLAN tags removed from packets.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface vbdif**](cmdqueryname=interface+vbdif) *bd-id*
   
   
   
   A VBDIF interface is created, and its view is displayed.
   
   
   
   The VBDIF interface number must be the ID of a BD that has been created.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If an interface is bound to a BD, a VBDIF interface can be created for the BD only when the interface has EVC Layer 2 sub-interfaces encapsulated with untag, dot1q, or QinQ.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is assigned to the VBDIF interface for communication at the network layer.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If IP addresses assigned to VBDIF interfaces belong to different network segments, a routing protocol must be configured to provide reachable routes. Otherwise, VBDIF interfaces cannot communicate with each other at the network layer. For configurations of routing protocols, see *NE40E Configuration Guide - IP Routing*.
4. (Optional) Run [**mtu**](cmdqueryname=mtu) *mtu*
   
   
   
   The maximum transmission unit (MTU) is configured for the VBDIF interface.
   
   
   
   Generally, the IP layer controls the maximum length of frames that are sent each time. Any time the IP layer receives an IP packet to be sent, it checks which local interface the packet needs to be sent to and queries the MTU of the interface. Then, the IP layer compares the MTU with the length of the packets to be sent. If the packet length is greater than the MTU, the IP layer fragments the packet to ensure that the length of each fragment is smaller or equal to the MTU.
   
   If forcible unfragmentation is configured, certain packets are lost during data transmission at the IP layer. To ensure jumbo packets are not dropped during transmission, you need to configure forcible fragmentation. In this case, you can run the [**mtu**](cmdqueryname=mtu) command to set the size of a fragment.
   
   After using the [**mtu**](cmdqueryname=mtu) command to change the MTU of a VBDIF interface, you need to change the MTU of the peer VBDIF interface to ensure that the MTUs of both interfaces are the same. Otherwise, services may be interrupted.
5. (Optional) Run [**bandwidth**](cmdqueryname=bandwidth) *bandwidth*
   
   
   
   The bandwidth is configured for the VBDIF interface.
   
   The bandwidth command mainly ensures that the network management station (NMS) can acquire the bandwidth of the VBDIF interface.
6. (Optional) Run [**forward-mode loopback**](cmdqueryname=forward-mode+loopback)
   
   
   
   The packet forwarding mode on a VBDIF interface is set to loopback.
   
   After the [**forward-mode loopback**](cmdqueryname=forward-mode+loopback) command is run to set the packet forwarding mode to loopback, downstream MTU fragmentation is supported on a VBDIF interface, and only one copy of traffic forwarded by the VBDIF interface is collected in multicast traffic statistics.
7. (Optional) Run [**damping time**](cmdqueryname=damping+time) *delay-time*
   
   
   
   The BD damping function is enabled, and the delay after which the BD Down event is reported to the BDIF interface is set.
   
   
   
   If all the interfaces added to a BD go Down, the BD will report a BD Down event to the corresponding BDIF interface, causing the BDIF interface status to change. The master/slave switchover will cause the BDIF interface to alternate frequently between Up and Down. As a result, network flapping occurs. To avoid this situation, enable the BD damping function on the BDIF interface. If the last Up interface in the BD becomes Down, the device enabled with the BD damping function will report the BD status to the BDIF interface after the set delay expires. If an interface in the BD becomes Up before the set delay expires, the BDIF interface status remains Up.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring a VBDIF interface, run the [**display interface vbdif**](cmdqueryname=display+interface+vbdif) command. The command output shows the physical status, link protocol status, IP address, and mask of a VBDIF interface.