Overview of VXLAN
=================

Overview of VXLAN

#### Definition

Virtual extensible local area network (VXLAN), defined in RFC 7348, is a Network Virtualization over Layer 3 (NVO3) technology that uses MAC-in-UDP encapsulation to extend Layer 2 networks.


#### Purpose

VXLAN is used to address some of the problems associated with server virtualization, which is a core cloud computing technology that can significantly reduce IT and O&M costs and improve service deployment flexibility.**Figure 1** Server virtualization networking  
![](figure/en-us_image_0000001176744091.png)
On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130624524__fig_dc_fd_vxlan_000101), a server is virtualized into multiple virtual machines (VMs), each of which functions as a host. A significant increase in the number of hosts can lead to the following problems:

* The VM scale is limited by network specifications.
  
  On a traditional Layer 2 network, data packets are forwarded based on MAC entries at Layer 2. The number of supported VMs is therefore limited by the MAC table capacity.
* Network isolation capabilities are limited.
  
  Most current mainstream networks use VLANs to implement network isolation. However, VLAN deployment on a large virtualized network has the following limitations:
  + The VLAN tag field, as defined in IEEE 802.1Q, has only 12 bits and can therefore support a maximum of only 4096 VLANs. This is insufficient to identify the large numbers of tenants and tenant groups on large Layer 2 networks.
  + VLANs cannot adapt to dynamic network adjustment on traditional Layer 2 networks.
* The VM migration scope is limited by the network architecture.
  
  After a VM is started, it may need to be migrated to a new server due to resource issues (such as high CPU usage and insufficient memory) on the original server. To ensure service continuity during VM migration, the VM's IP address must remain unchanged. This requires the service network to be a Layer 2 network that provides multipathing redundancy backup and reliability.

VXLAN addresses the preceding problems on large Layer 2 networks as follows:

* Eliminates VM scale limitations imposed by network specifications.
  
  VXLAN encapsulates data packets sent from VMs into UDP packets, and encapsulates IP and MAC addresses used on the physical network into the outer headers. As a result, the network is aware of only the encapsulated parameters and not the inner data. This significantly reduces the requirements of large Layer 2 networks on MAC address specifications.
* Provides greater network isolation capabilities.
  
  VXLAN uses 24-bit network segment IDs, known as VXLAN network identifiers (VNIs), to identify users. VNIs provide a similar function to VLAN IDs and can identify 16 million VXLAN segments.
* Eliminates VM migration scope limitations imposed by the network architecture.
  
  VXLAN utilizes MAC-in-UDP encapsulation to extend Layer 2 networks. It encapsulates Ethernet packets into IP packets for routing over networks and does not need to know the MAC addresses of VMs. Because Layer 3 networks are not limited by the network architecture, they are scalable and offer robust automatic fault rectification and load balancing capabilities. As such, VM migration is not constrained by the network architecture.


#### Benefits

With the rapid deployment of server virtualization on the physical network infrastructure in DCs, VXLAN â an NVO3 technology â offers the following benefits:

* Supports 16 million VXLAN segments by using 24-bit VNIs, enabling a DC to accommodate numerous tenants.
* Reduces the number of MAC addresses that must be learned and thereby enhances device performance (because only VXLAN network edge devices need to identify the MAC addresses of VMs).
* Extends Layer 2 networks by using MAC-in-UDP encapsulation, thereby decoupling physical and virtual networks and simplifying network management. Tenants can plan their own virtual networks, unrestricted by physical network IP addresses or BDs.