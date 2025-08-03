EVPN VXLAN Fundamentals
=======================

EVPN VXLAN Fundamentals

#### Introduction

Ethernet virtual private network (EVPN) is a VPN technology used for Layer 2 internetworking. EVPN uses a mechanism similar to BGP or MPLS IP VPN and, based on BGP, defines a new type of Network Layer Reachability Information (NLRI), called EVPN NLRI. EVPN NLRI defines several new types of BGP EVPN routes to implement MAC address learning and advertisement between different sites on a Layer 2 network.

Because VXLAN does not have any control plane, VTEP discovery and host information (IP and MAC addresses, VNIs, and gateway VTEP IP address) learning are implemented by traffic flooding on the data plane, resulting in high traffic volumes on DCNs. To address this problem and eliminate unnecessary traffic flooding, VXLAN uses EVPN as the control plane, allowing VTEPs to exchange BGP EVPN routes to implement automatic VTEP discovery and host information advertisement.

In summary, EVPN extends BGP by defining several new types of BGP EVPN routes, which can be used to transmit VTEP addresses and host information. EVPN is applied to the VXLAN network to move VTEP discovery and host information learning from the data plane to the control plane.


#### BGP EVPN Routes

EVPN NLRI defines the following types of BGP EVPN routes applicable to the VXLAN control plane:

**Type 2 Route: MAC/IP Route**

The following figure shows the format of this type of route.

**Figure 1** Format of a MAC/IP route  
![](figure/en-us_image_0000001130784322.png)

The following table describes the fields in the route.

| Field | Description |
| --- | --- |
| Route Distinguisher | RD of an EVPN instance. |
| Ethernet Segment Identifier | Unique identifier of the connection between local and peer devices. |
| Ethernet Tag ID | VLAN ID configured on the local device. The Ethernet Tag ID in this route is all 0s.  NOTE:  In terms of BGP EVPN Type 2 routes, a device that has an all-zero Ethernet Tag ID cannot interoperate with another device that has a non-zero Ethernet Tag ID. |
| MAC Address Length | Length of the host MAC address carried in the route. |
| MAC Address | Host MAC address carried in the route. |
| IP Address Length | Mask length of the host IP address carried in the route. |
| IP Address | Host IP address carried in the route. |
| MPLS Label1 | L2VNI carried in the route. |
| MPLS Label2 | L3VNI carried in the route. |

Type 2 routes perform the following functions on the VXLAN control plane:

* MAC address advertisement
  
  To implement Layer 2 communication between hosts on the same subnet, the VTEPs at both ends must learn host MAC addresses from each other. They achieve this by exchanging MAC/IP routes after a BGP EVPN peer relationship is established between them to advertise host MAC addresses to each other. The MAC Address Length and MAC Address fields identify the MAC address of a host.
* ARP advertisement
  
  A MAC/IP route can carry both the MAC address and IP address of a host. As such, this type of route can be used to transmit host ARP entries between VTEPs, thereby implementing host ARP advertisement. The MAC Address and MAC Address Length fields identify the host's MAC address, whereas the IP Address and IP Address Length fields identify the host's IP address. In this case, MAC/IP routes are also called ARP routes. Host ARP advertisement applies to the following scenarios:
  
  1. ARP broadcast suppression: After a Layer 3 gateway learns the ARP entries of a host, it generates host information, including the host IP and MAC addresses, L2VNI, and gateway's VTEP IP address. The Layer 3 gateway then transmits an ARP route carrying the host information to a Layer 2 gateway. Upon receiving an ARP request, the Layer 2 gateway searches for host information corresponding to the destination IP address. If the host information exists, the gateway replaces the broadcast MAC address in the ARP request with the destination unicast MAC address, and encapsulates the packet into a unicast packet. In this way, ARP broadcast suppression is implemented.
  2. VM migration in a distributed gateway scenario: After a VM is migrated from one gateway to another, the new gateway learns the VM's ARP entries from gratuitous ARP packets sent by the VM. The new gateway generates host information (including host MAC and IP addresses, L2VNIs, and gateway VTEP IP addresses) and then advertises an ARP route to the original gateway to send the host information. Upon receipt, the original gateway detects the VM migration and triggers an ARP probe. If the original gateway fails to probe the target VM, it withdraws the ARP and host routes for the VM.
* Host IP route advertisement
  
  To implement Layer 3 communication between hosts on different subnets in a distributed gateway scenario, the VTEPs (functioning as Layer 3 gateways) at both ends must learn host IP routes from each other. They achieve this by exchanging MAC/IP routes after a BGP EVPN peer relationship is established between them to advertise host IP routes to each other. The IP Address Length and IP Address fields carried in the MAC/IP routes indicate the destination addresses of host IP routes, and the MPLS Label2 field must carry an L3VNI. In this case, MAC/IP routes are also called Integrated Routing and Bridge (IRB) routes.
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  An IRB route carries L3VNI information in addition to the host MAC address, host IP address, and L2VNI information carried in an ARP route. As such, an IRB route can be used to advertise both the host IP route and host ARP entry.
* ND entry flooding
  
  A MAC/IP route can carry both the MAC address and IPv6 address of a host. As such, this type of route can be used to transmit ND entries between VTEPs, implementing ND entry advertisement. The MAC Address and MAC Address Length fields identify the host's MAC address, whereas the IP Address and IP Address Length fields identify the host's IPv6 address. In this case, MAC/IP routes are also called ND routes. ND entry flooding applies to the following scenarios:
  
  + NS multicast suppression: After collecting information about a local IPv6 host, a VXLAN gateway generates an ND entry or proxy ND entry and floods the entry through a MAC/IP route. Each VXLAN gateway (BGP EVPN peer) that receives this MAC/IP route generates a local proxy ND entry. When a VXLAN gateway receives an NS message subsequently, it first searches the local proxy ND table. If the VXLAN gateway finds a corresponding entry, it directly performs proxy ND or multicast-to-unicast processing to reduce or suppress NS message flooding.
  + ND spoofing attack defense: In an ND spoofing attack, an attacker associates its MAC address with the IPv6 address of a host so that all traffic destined for the IPv6 address is sent to the attacker. After ND flooding is enabled, VXLAN gateways can synchronize the proxy ND entry of the same IPv6 host. When an attacker goes online, another proxy ND entry is repeatedly generated for the same IPv6 host and flooded to other VXLAN gateways. Through proxy ND entry conflict detection, an IPv6 address conflict alarm is triggered to remind users that an ND spoofing attack may have occurred.
  + IPv6 VM migration in a distributed gateway scenario: After an IPv6 VM is migrated from one gateway to another, the VM sends a gratuitous NA message. The new gateway receives this message and then generates and floods an ND entry to the original gateway through a MAC/IP route. Upon receipt of this message, the original gateway detects that the location of the IPv6 VM has changed and triggers NUD. Because the original gateway cannot detect the IPv6 VM at the original location, it deletes its local ND table and uses a MAC/IP route to instruct the new gateway to delete the old proxy ND table for the IPv6 VM.
* Host IPv6 route advertisement
  
  To implement Layer 3 communication between hosts on different subnets in a distributed gateway scenario, the VTEPs (functioning as Layer 3 gateways) must learn host IPv6 routes from each other. They achieve this by exchanging MAC/IP routes after a BGP EVPN peer relationship is established between them to advertise host IPv6 routes to each other. The IP Address Length and IP Address fields carried in the MAC/IP routes indicate the destination addresses of host IPv6 routes, and the MPLS Label2 field must carry an L3VNI. In this case, MAC/IP routes are also called IRBv6 routes.
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  An IRBv6 route carries L3VNI information in addition to the host MAC address, host IPv6 address, and L2VNI information carried in an ND route. As such, an IRBv6 route can be used to advertise both a host IPv6 route and host ND entry.

**Type 3 Route: Inclusive Multicast Route**

This type of route consists of a prefix and the PMSI attribute. The format of EVPN NLRI specific to inclusive multicast routes is shown in the following figure.

**Figure 2** Format of EVPN NLRI specific to inclusive multicast routes  
![](figure/en-us_image_0000001176743979.png)

The following table describes the fields in the route.

| Field | Description |
| --- | --- |
| Route Distinguisher | RD of an EVPN instance. |
| Ethernet Tag ID | VLAN ID on the current device. The Ethernet Tag ID in this route is all 0s.  NOTE:  In terms of BGP EVPN Type 3 routes, a device that has an all-zero Ethernet Tag ID cannot interoperate with another device that has a non-zero Ethernet Tag ID. |
| IP Address Length | Mask length of the local VTEP's IP address carried in the route. |
| Originating Router's IP Address | Local VTEP's IP address carried in the route. |
| Flags | Flags indicating whether leaf node information is required for the tunnel.  This field is not used in VXLAN scenarios. |
| Tunnel Type | Tunnel type carried in the route. |
| MPLS Label | L2VNI carried in the route. |
| Tunnel Identifier | Tunnel information carried in the route. In a VXLAN scenario, this field also indicates the local VTEP's IP address. |

Inclusive multicast routes are used for automatic VTEP discovery and dynamic VXLAN tunnel setup on the VXLAN control plane. Through these routes, VTEPs that function as BGP EVPN peers transmit L2VNIs and VTEPs' IP addresses. The Originating Router's IP Address and MPLS Label fields carried in the routes indicate the local VTEP's IP address and L2VNI, respectively. If the peer VTEP's IP address is routable, a VXLAN tunnel is established from the local VTEP to the peer VTEP. In addition, the local end creates a VNI-based ingress replication list and adds the peer VTEP IP address to the list for subsequent BUM packet forwarding.

**Type 5 Route: IP Prefix Route**

The following figure shows the format of this type of route.

**Figure 3** Format of an IP prefix route  
![](figure/en-us_image_0000001130624532.png)

The following table describes the fields in the route.

| Field | Description |
| --- | --- |
| Route Distinguisher | RD of a VPN instance. |
| Ethernet Segment Identifier | Unique identifier of the connection between local and peer devices. |
| Ethernet Tag ID | VLAN ID configured on the local device. |
| IP Prefix Length | Mask length of the IP prefix carried in the route. |
| IP Prefix | IP prefix carried in the route. |
| GW IP Address | Default gateway address. This field is not used in VXLAN scenarios. |
| MPLS Label | L3VNI carried in the route. |

The IP Prefix Length and IP Prefix fields carry a host IP address or network segment address:

* If a host IP address is carried, the route is used for IP route advertisement in distributed VXLAN gateway scenarios. In this case, the route functions the same as an IRB route on the VXLAN control plane.
* If a network segment address is carried, the route is used by VXLAN hosts to access an external network.