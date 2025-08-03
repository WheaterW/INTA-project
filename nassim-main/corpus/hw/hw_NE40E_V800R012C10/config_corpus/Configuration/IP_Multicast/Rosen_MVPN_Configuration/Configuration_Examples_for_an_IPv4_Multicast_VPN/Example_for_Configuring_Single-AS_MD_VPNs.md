Example for Configuring Single-AS MD VPNs
=========================================

This section provides an example for configuring single-AS multicast domain (MD) VPN on an MPLS/BGP network to enable the transmission of multicast data of private networks over a public network to receivers.

#### Networking Requirements

In the single-AS MPLS/BGP VPN shown in [Figure 1](#EN-US_TASK_0000001225672704__fig66771216144217), configure MD to deploy multicast services.

**Figure 1** Configuring single-AS MD VPNs  
![](figure/en-us_image_0000001225352876.png)

The networking requirements are described in [Table 1](#EN-US_TASK_0000001225672704__tab_dc_vrp_multicast_cfg_213401):

**Table 1** Networking requirements of single-AS MD VPNs
| Item | Networking Requirements |
| --- | --- |
| Multicast source/receiver | The multicast source of VPN RED is Source 1. The receivers include PC1, PC2, and PC3. The multicast source of VPN BLUE is Source 2. The receiver is PC4. In the VPN RED, the Share-Group address is 239.1.1.1 and Switch-Group pool address ranges from 225.2.2.1 to 225.2.2.16. In the VPN BLUE, the Share-Group address is 239.2.2.2 and Switch-Group pool address ranges from 225.4.4.1 to 225.4.4.16. |
| VPN instance to which the interfaces on PEs belong | On PE-A, GE2 and GE3 belong to VPN-RED, and GE1 and Loopback1 belong to the public network instance. On PE-B, GE2 belongs to VPN-BLUE, GE3 belongs to VPN-RED, and GE1 and Loopback1 belong to the public network instance. On PE-C, GE2 belongs to VPN-RED, GE3 and Loopback2 belong to VPN-BLUE, and GE1 and Loopback1 belong to the public network instance. |
| Routing protocol and MPLS | Configure Open Shortest Path First (OSPF) on the public network. Enable the Routing Information Protocol (RIP) on PE and CE devices. Establish BGP peer relationships and transmit all private network routes between Loopback1 interfaces on PE-A, PE-B, and PE-C. Enable MPLS forwarding on the public network. |
| Multicast function | Enable multicast on the P. Enable multicast on the public network instance on PE-A, PE-B, and PE-C. Enable multicast on the VPN-RED on PE-A, PE-B, and PE-C. Enable multicast on the VPN-BLUE on PE-B and PE-C. Enable multicast on CE-Ra, CE-Rb, CE-Rc, CE-Bb, and CE-Bc. |
| IGMP function | Enable the Internet Group Management Protocol (IGMP) on GE2 of PE-A. Enable IGMP on GE1 interfaces of CE-Rb, CE-Rc, and CE-Bc. |
| PIM function | Enable PIM-SM on all the VPN interfaces in VPN-RED. Enable PIM-SM on all the VPN interfaces in VPN-BLUE. Enable PIM-SM on all the interfaces of the P and CEs, and the public network interfaces of PEs. Configure Loopback1 on the P as the Candidate-BootStrap Router (C-BSR) and Candidate-Rendezvous Point (C-RP) of the public network (serving all multicast groups). Configure Loopback1 on CE-Rb as the C-BSR and C-RP of VPN-RED (serving all multicast groups). Configure Loopback2 on PE-C as the C-BSR and C-RP of VPN-BLUE (serving all multicast groups). |

[Table 2](#EN-US_TASK_0000001225672704__tab_dc_vrp_multicast_cfg_213402) lists the IP addresses planned for the interfaces shown in [Figure 1](#EN-US_TASK_0000001225672704__fig66771216144217) based on the networking requirements.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

GE1, GE2, and GE3 represent GigabitEthernet 0/1/0, GigabitEthernet 0/1/1, and GigabitEthernet 0/1/2, respectively.


**Table 2** Configuration information about interfaces on the devices
| Device | Interface IP Address | Remarks |
| --- | --- | --- |
| P | GE1: 192.168.6.2/24 | - |
| GE2: 192.168.7.2/24 | - |
| GE3: 192.168.8.2/24 | - |
| Loopback 1: 2.2.2.2/32 | Loopback1 functions as a C-RP on the public network. |
| PE-A | GE1: 192.168.6.1/24 | GE1 belongs to the public network instance. |
| GE2: 10.110.1.1/24 | GE2 belongs to the VPN-RED instance. |
| GE3: 10.110.2.1/24 | GE3 belongs to the VPN-RED instance. |
| Loopback 1: 1.1.1.1/32 | Loopback1 belongs to the public network instance.  Internal Border Gateway Protocol (IBGP) peer relationships are set up among Loopback 1 interfaces of PE-A, PE-B, and PE-C. |
| PE-B | GE1: 192.168.7.1/24 | GE1 belongs to the public network instance. |
| GE2: 10.110.3.1/24 | GE2 belongs to the VPN-BLUE instance. |
| GE3: 10.110.4.1/24 | GE3 belongs to the VPN-RED instance. |
| Loopback 1: 1.1.1.2/32 | Loopback1 belongs to the public network instance.  IBGP peer relationships are set up among Loopback 1 interfaces of PE-A, PE-B, and PE-C. |
| PE-C | GE1: 192.168.8.1/24 | GE1 belongs to the public network instance. |
| GE2: 10.110.5.1/24 | GE2 belongs to the VPN-RED instance. |
| GE3: 10.110.6.1/24 | GE3 belongs to the VPN-BLUE instance. |
| Loopback1: 1.1.1.3/32 | Loopback1 belongs to the public network instance.  IBGP peer relationships are set up among Loopback 1 interfaces of PE-A, PE-B, and PE-C. |
| Loopback 2: 9.9.9.9/32 | Loopback2 belongs to VPN-BLUE and functions as a VPN C-RP. |
| CE-Ra | GE1: 10.110.7.1/24 | - |
| GE2: 10.110.2.2/24 | - |
| CE-Bb | GE1: 10.110.8.1/24 | - |
| GE2: 10.110.3.2/24 | - |
| Loopback 2: 8.8.8.8/32 | - |
| CE-Rb | GE1: 10.110.9.1/24 | - |
| GE2: 10.110.4.2/24 | - |
| GE3: 10.110.12.1/24 | - |
| Loopback 1: 7.7.7.7/32 | Loopback1 belongs to VPN-RED and functions as a VPN C-RP. |
| CE-Rc | GE1: 10.110.10.1/24 | - |
| GE2: 10.110.5.2/24 | - |
| GE3: 10.110.12.2/24 | - |
| CE-Bc | GE1: 10.110.11.1/24 | - |
| GE2: 10.110.6.2/24 | - |
| Source 1 | 10.110.7.2/24 | Multicast source in VPN-RED |
| Source 2 | 10.110.8.2/24 | Multicast source in VPN-BLUE |
| PC1 | 10.110.1.2/24 | Multicast receiver in VPN-RED |
| PC2 | 10.110.9.2/24 | Multicast receiver in VPN-RED |
| PC3 | 10.110.10.2/24 | Multicast receiver in VPN-RED |
| PC4 | 10.110.11.2/24 | Multicast receiver in VPN-BLUE |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure MPLS/BGP VPN to ensure that the VPN network works properly and unicast routes are reachable.
2. Enable multicast routing and PIM on the entire network. Enable public network instance multicast on the PEs and P, and enable VPN instance multicast with the IPv4 address family on PEs and CEs.
3. Configure the same share-group address, the same MTI, and the same switch-group-pool range of a switch-MDT for the same VPN instance enabled with the IPv4 address family on each PE. Set the automatic configuration mode for the MTI.

![](../../../../public_sys-resources/note_3.0-en-us.png) This example does not involve the following situations:

* Multicast VPN is not supported on an interface board.
* The current device is an ingress PE, and the VPN inbound interface is a logical interface.
* The current device is an egress PE, and the public network inbound interface is a logical interface.

If any of the preceding situations exists in the actual networking, you need to enable IP multicast VPN to allow multicast traffic to be properly forwarded. For configuration details, see [(Optional) Enabling IP Multicast VPN](../ne/dc_ne_mcast_cfg_2001.html).


#### Data Preparation

See [Figure 1](#EN-US_TASK_0000001225672704__fig66771216144217).


#### Procedure

1. Configure PE-A.
   
   
   
   # Configure an ID for PE-A, enable public-network IP multicast routing, configure an MPLS LSR-ID, and enable LDP.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE-A
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE-A] router id 1.1.1.1
   ```
   ```
   [*PE-A] multicast routing-enable
   ```
   ```
   [*PE-A] mpls lsr-id 1.1.1.1
   ```
   ```
   [*PE-A] mpls
   ```
   ```
   [*PE-A-mpls] quit
   ```
   ```
   [*PE-A] mpls ldp
   ```
   ```
   [*PE-A-mpls-ldp] quit
   ```
   ```
   [*PE-A] commit
   ```
   
   # Configure an IP address and enable PIM-SM on Loopback1.
   
   ```
   [~PE-A] interface loopback 1
   ```
   ```
   [*PE-A-LoopBack1] ip address 1.1.1.1 32
   ```
   ```
   [*PE-A-LoopBack1] pim sm
   ```
   ```
   [*PE-A-LoopBack1] commit
   ```
   ```
   [~PE-A-LoopBack1] quit
   ```
   
   # Create a VPN instance named VPN RED, and enable the IPv4 address family for it. In the VPN instance IPv4 address family view, configure a VPN IPv4 prefix and create import and export VPN targets for the instance. Enable IP multicast routing, configure a share-group, specify an MTI bound to the VPN instance, and set the range of the switch-MDT switch-address-pool. In addition, set the IP address of a specified interface as the default IP address of an MTI.
   
   ```
   [~PE-A] ip vpn-instance RED
   ```
   ```
   [*PE-A-vpn-instance-RED] ipv4-family
   ```
   ```
   [*PE-A-vpn-instance-RED-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE-A-vpn-instance-RED-af-ipv4] vpn-target 100:1 export-extcommunity 
   ```
   ```
   [*PE-A-vpn-instance-RED-af-ipv4] vpn-target 100:1 import-extcommunity
   ```
   ```
   [*PE-A-vpn-instance-RED-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE-A-vpn-instance-RED-af-ipv4] multicast-domain share-group 239.1.1.1 binding mtunnel 0
   ```
   ```
   [*PE-A-vpn-instance-RED-af-ipv4] multicast-domain source-interface loopback 1
   ```
   ```
   [*PE-A-vpn-instance-RED-af-ipv4] multicast-domain switch-group-pool 225.2.2.1 28
   ```
   ```
   [*PE-A-vpn-instance-RED-af-ipv4] quit
   ```
   ```
   [*PE-A-vpn-instance-RED] commit
   ```
   ```
   [~PE-A-vpn-instance-RED] quit
   ```
   
   # Enable LDP and PIM-SM on the public network interface GigabitEthernet 0/1/0.
   
   ```
   [~PE-A] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE-A-GigabitEthernet0/1/0] ip address 192.168.6.1 24
   ```
   ```
   [*PE-A-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*PE-A-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE-A-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE-A-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE-A-GigabitEthernet0/1/0] quit
   ```
   
   # Bind GigabitEthernet 0/1/1 to VPN RED, and enable IGMP and PIM-SM.
   
   ```
   [~PE-A] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE-A-GigabitEthernet0/1/1] ip binding vpn-instance RED
   ```
   ```
   [*PE-A-GigabitEthernet0/1/1] ip address 10.110.1.1 24
   ```
   ```
   [*PE-A-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*PE-A-GigabitEthernet0/1/1] igmp enable
   ```
   ```
   [*PE-A-GigabitEthernet0/1/1] commit
   ```
   ```
   [~PE-A-GigabitEthernet0/1/1] quit
   ```
   
   # Bind GigabitEthernet 0/1/2 to VPN RED, and enable PIM-SM.
   
   ```
   [~PE-A] interface gigabitethernet 0/1/2
   ```
   ```
   [~PE-A-GigabitEthernet0/1/2] ip binding vpn-instance RED
   ```
   ```
   [*PE-A-GigabitEthernet0/1/2] ip address 10.110.2.1 24
   ```
   ```
   [*PE-A-GigabitEthernet0/1/2] pim sm
   ```
   ```
   [*PE-A-GigabitEthernet0/1/2] commit
   ```
   ```
   [~PE-A-GigabitEthernet0/1/2] quit
   ```
   
   # Configure BGP, OSPF, and RIP for unicast routing.
   
   ```
   [~PE-A] bgp 100
   ```
   ```
   [*PE-A-bgp] group VPN-G internal 
   ```
   ```
   [*PE-A-bgp] peer VPN-G connect-interface LoopBack1
   ```
   ```
   [*PE-A-bgp] peer 1.1.1.2 group VPN-G
   ```
   ```
   [*PE-A-bgp] peer 1.1.1.3 group VPN-G
   ```
   ```
   [*PE-A-bgp] ipv4-family vpn-instance RED
   ```
   ```
   [*PE-A-bgp-RED] import-route rip 2
   ```
   ```
   [*PE-A-bgp-RED] import-route direct 
   ```
   ```
   [*PE-A-bgp-RED] quit
   ```
   ```
   [*PE-A-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE-A-bgp-af-vpnv4] peer VPN-G enable
   ```
   ```
   [*PE-A-bgp-af-vpnv4] peer 1.1.1.2 group VPN-G
   ```
   ```
   [*PE-A-bgp-af-vpnv4] peer 1.1.1.3 group VPN-G
   ```
   ```
   [*PE-A-bgp-af-vpnv4] quit
   ```
   ```
   [*PE-A-bgp] commit
   ```
   ```
   [~PE-A-bgp] quit
   ```
   ```
   [~PE-A] ospf 1
   ```
   ```
   [*PE-A-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE-A-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0 
   ```
   ```
   [*PE-A-ospf-1-area-0.0.0.0] network 192.168.0.0 0.0.255.255 
   ```
   ```
   [*PE-A-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE-A-ospf-1] commit
   ```
   ```
   [~PE-A-ospf-1] quit
   ```
   ```
   [~PE-A] rip 2 vpn-instance RED
   ```
   ```
   [*PE-A-rip-2] network 10.0.0.0
   ```
   ```
   [*PE-A-rip-2] import-route bgp cost 3 
   ```
   ```
   [*PE-A-rip-2] commit
   ```
2. Configure PE-B.
   
   
   
   # Configure an ID for PE-B, enable public-network IP multicast routing, configure an MPLS LSR-ID, and enable LDP.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE-B
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE-B] router id 1.1.1.2
   ```
   ```
   [*PE-B] multicast routing-enable
   ```
   ```
   [*PE-B] mpls lsr-id 1.1.1.2
   ```
   ```
   [*PE-B] mpls
   ```
   ```
   [*PE-B-mpls] quit
   ```
   ```
   [*PE-B] mpls ldp
   ```
   ```
   [*PE-B-mpls-ldp] quit
   ```
   ```
   [*PE-B] commit
   ```
   
   # Configure an IP address and enable PIM-SM on Loopback1.
   
   ```
   [~PE-B] interface loopback 1
   ```
   ```
   [*PE-B-LoopBack1] ip address 1.1.1.2 32
   ```
   ```
   [*PE-B-LoopBack1] pim sm
   ```
   ```
   [*PE-B-LoopBack1] commit
   ```
   ```
   [~PE-B-LoopBack1] quit
   ```
   
   # Create a VPN instance named VPN BLUE, and enable the IPv4 address family for it. In the VPN instance IPv4 address family view, configure a VPN IPv4 prefix and set import and export VPN targets for the instance. Enable IP multicast routing, configure a share-group, specify an MTI to be bound to the VPN instance, and set the range of the switch-MDT switch-address-pool. Set the automatic configuration mode for the MTI.
   
   ```
   [~PE-B] ip vpn-instance BLUE
   ```
   ```
   [*PE-B-vpn-instance-BLUE] ipv4-family
   ```
   ```
   [*PE-B-vpn-instance-BLUE-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE-B-vpn-instance-BLUE-af-ipv4] vpn-target 200:1 export-extcommunity 
   ```
   ```
   [*PE-B-vpn-instance-BLUE-af-ipv4] vpn-target 200:1 import-extcommunity 
   ```
   ```
   [*PE-B-vpn-instance-BLUE-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE-B-vpn-instance-BLUE-af-ipv4] multicast-domain share-group 239.2.2.2 binding mtunnel 1
   ```
   ```
   [*PE-B-vpn-instance-BLUE-af-ipv4] multicast-domain source-interface loopback 1
   ```
   ```
   [*PE-B-vpn-instance-BLUE-af-ipv4] multicast-domain switch-group-pool 225.4.4.1 28
   ```
   ```
   [*PE-B-vpn-instance-BLUE-af-ipv4] quit
   ```
   ```
   [*PE-B-vpn-instance-BLUE] commit
   ```
   ```
   [~PE-B-vpn-instance-BLUE] quit
   ```
   
   # Create a VPN instance named VPN RED, and enable the IPv4 address family for it. In the VPN instance IPv4 address family view, configure a VPN IPv4 prefix and set import and export VPN targets for the instance. Enable IP multicast routing, configure a share-group, specify an MTI to be bound to the VPN instance, and set the range of the switch-MDT switch-address-pool. Set the automatic configuration mode for the MTI.
   
   ```
   [~PE-B] ip vpn-instance RED
   ```
   ```
   [*PE-B-vpn-instance-RED] ipv4-family
   ```
   ```
   [*PE-B-vpn-instance-RED-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE-B-vpn-instance-RED-af-ipv4] vpn-target 100:1 export-extcommunity 
   ```
   ```
   [*PE-B-vpn-instance-RED-af-ipv4] vpn-target 100:1 import-extcommunity 
   ```
   ```
   [*PE-B-vpn-instance-RED-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE-B-vpn-instance-RED-af-ipv4] multicast-domain share-group 239.1.1.1 binding mtunnel 0
   ```
   ```
   [*PE-B-vpn-instance-RED-af-ipv4] multicast-domain source-interface loopback 1
   ```
   ```
   [*PE-B-vpn-instance-RED-af-ipv4] multicast-domain switch-group-pool 225.2.2.1 28
   ```
   ```
   [*PE-B-vpn-instance-RED-af-ipv4] quit
   ```
   ```
   [*PE-B-vpn-instance-RED] commit
   ```
   ```
   [~PE-B-vpn-instance-RED] quit
   ```
   
   # Enable LDP and PIM-SM on the public network interface GigabitEthernet 0/1/0.
   
   ```
   [~PE-B] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE-B-GigabitEthernet0/1/0] ip address 192.168.7.1 24
   ```
   ```
   [*PE-B-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*PE-B-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE-B-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE-B-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE-B-GigabitEthernet0/1/0] quit
   ```
   
   # Bind GigabitEthernet 0/1/1 to VPN BLUE, and enable PIM-SM.
   
   ```
   [~PE-B] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE-B-GigabitEthernet0/1/1] ip binding vpn-instance BLUE
   ```
   ```
   [*PE-B-GigabitEthernet0/1/1] ip address 10.110.3.1 24
   ```
   ```
   [*PE-B-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*PE-B-GigabitEthernet0/1/1] commit
   ```
   ```
   [~PE-B-GigabitEthernet0/1/1] quit
   ```
   
   # Bind GigabitEthernet 0/1/2 to VPN RED, and enable PIM-SM.
   
   ```
   [~PE-B] interface gigabitethernet 0/1/2
   ```
   ```
   [~PE-B-GigabitEthernet0/1/2] ip binding vpn-instance RED
   ```
   ```
   [*PE-B-GigabitEthernet0/1/2] ip address 10.110.4.1 24
   ```
   ```
   [*PE-B-GigabitEthernet0/1/2] pim sm
   ```
   ```
   [*PE-B-GigabitEthernet0/1/2] commit
   ```
   ```
   [~PE-B-GigabitEthernet0/1/2] quit
   ```
   
   # Configure BGP, OSPF, and RIP for unicast routing.
   
   ```
   [~PE-B] bgp 100
   ```
   ```
   [*PE-B-bgp] group VPN-G internal 
   ```
   ```
   [*PE-B-bgp] peer VPN-G connect-interface LoopBack1
   ```
   ```
   [*PE-B-bgp] peer 1.1.1.1 group VPN-G
   ```
   ```
   [*PE-B-bgp] peer 1.1.1.3 group VPN-G
   ```
   ```
   [*PE-B-bgp] ipv4-family vpn-instance RED
   ```
   ```
   [*PE-B-bgp-RED] import-route rip 2
   ```
   ```
   [*PE-B-bgp-RED] import-route direct 
   ```
   ```
   [*PE-B-bgp-RED] quit
   ```
   ```
   [*PE-B-bgp] ipv4-family vpn-instance BLUE
   ```
   ```
   [*PE-B-bgp-BLUE] import-route rip 3
   ```
   ```
   [*PE-B-bgp-BLUE] import-route direct 
   ```
   ```
   [*PE-B-bgp-BLUE] quit
   ```
   ```
   [*PE-B-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE-B-bgp-af-vpnv4] peer VPN-G enable
   ```
   ```
   [*PE-B-bgp-af-vpnv4] peer 1.1.1.1 group VPN-G
   ```
   ```
   [*PE-B-bgp-af-vpnv4] peer 1.1.1.3 group VPN-G
   ```
   ```
   [*PE-B-bgp-af-vpnv4] quit
   ```
   ```
   [*PE-B-bgp] commit
   ```
   ```
   [~PE-B-bgp] quit
   ```
   ```
   [~PE-B] ospf 1
   ```
   ```
   [*PE-B-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE-B-ospf-1-area-0.0.0.0] network 1.1.1.2 0.0.0.0 
   ```
   ```
   [*PE-B-ospf-1-area-0.0.0.0] network 192.168.0.0 0.0.255.255 
   ```
   ```
   [*PE-B-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE-B-ospf-1] commit
   ```
   ```
   [~PE-B-ospf-1] quit
   ```
   ```
   [~PE-B] rip 2 vpn-instance RED
   ```
   ```
   [*PE-B-rip-2] network 10.0.0.0
   ```
   ```
   [*PE-B-rip-2] import-route bgp cost 3 
   ```
   ```
   [*PE-B-rip-2] commit
   ```
   ```
   [~PE-B-rip-2] quit
   ```
   ```
   [~PE-B] rip 3 vpn-instance BLUE
   ```
   ```
   [*PE-B-rip-3] network 10.0.0.0
   ```
   ```
   [*PE-B-rip-3] import-route bgp cost 3 
   ```
   ```
   [*PE-B-rip-3] commit
   ```
3. Configure PE-C.
   
   
   
   # Configure an ID for PE-C, enable public-network IP multicast routing, configure an MPLS LSR-ID, and enable LDP.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE-C
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE-C] router id 1.1.1.3
   ```
   ```
   [*PE-C] multicast routing-enable
   ```
   ```
   [*PE-C] mpls lsr-id 1.1.1.3
   ```
   ```
   [*PE-C] mpls
   ```
   ```
   [*PE-C-mpls] quit
   ```
   ```
   [*PE-C] mpls ldp
   ```
   ```
   [*PE-C-mpls-ldp] quit
   ```
   ```
   [*PE-C] commit
   ```
   
   # Configure an IP address and enable PIM-SM on Loopback1.
   
   ```
   [~PE-C] interface loopback 1
   ```
   ```
   [*PE-C-LoopBack1] ip address 1.1.1.3 32
   ```
   ```
   [*PE-C-LoopBack1] pim sm
   ```
   ```
   [*PE-C-LoopBack1] commit
   ```
   ```
   [~PE-C-LoopBack1] quit
   ```
   
   # Create a VPN instance named VPN RED enabled with the IPv4 address family and enter the VPN instance IPv4 address family view. Configure a VPN IPv4 prefix and create egress and ingress routes for the instance. Enable IP multicast routing, configure a share-group, specify an MTI bound to the VPN instance, and set the range of the switch-MDT switch-address-pool. Set the automatic configuration mode for the MTI.
   
   ```
   [~PE-C] ip vpn-instance RED
   ```
   ```
   [*PE-C-vpn-instance-RED] ipv4-family
   ```
   ```
   [*PE-C-vpn-instance-RED-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE-C-vpn-instance-RED-af-ipv4] vpn-target 100:1 export-extcommunity 
   ```
   ```
   [*PE-C-vpn-instance-RED-af-ipv4] vpn-target 100:1 import-extcommunity 
   ```
   ```
   [*PE-C-vpn-instance-RED-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE-C-vpn-instance-RED-af-ipv4] multicast-domain share-group 239.1.1.1 binding mtunnel 0
   ```
   ```
   [*PE-C-vpn-instance-RED-af-ipv4] multicast-domain source-interface loopback 1
   ```
   ```
   [*PE-C-vpn-instance-RED-af-ipv4] multicast-domain switch-group-pool 225.2.2.1 28
   ```
   ```
   [*PE-C-vpn-instance-RED-af-ipv4] quit
   ```
   ```
   [*PE-C-vpn-instance-RED] commit
   ```
   ```
   [~PE-C-vpn-instance-RED] quit
   ```
   
   # Create a VPN instance named VPN BLUE enabled with the IPv4 address family and enter the VPN instance IPv4 address family view. Configure a VPN IPv4 prefix and create egress and ingress routes for the instance. Enable IP multicast routing, configure a share-group, specify an MTI bound to the VPN instance, and set the range of the switch-MDT switch-address-pool. Set the automatic configuration mode for the MTI.
   
   ```
   [~PE-C] ip vpn-instance BLUE
   ```
   ```
   [*PE-C-vpn-instance-BLUE] ipv4-family
   ```
   ```
   [*PE-C-vpn-instance-BLUE-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE-C-vpn-instance-BLUE-af-ipv4] vpn-target 200:1 export-extcommunity 
   ```
   ```
   [*PE-C-vpn-instance-BLUE-af-ipv4] vpn-target 200:1 import-extcommunity 
   ```
   ```
   [*PE-C-vpn-instance-BLUE-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE-C-vpn-instance-BLUE-af-ipv4] multicast-domain share-group 239.2.2.2 binding mtunnel 1
   ```
   ```
   [*PE-C-vpn-instance-BLUE-af-ipv4] multicast-domain source-interface loopback 1
   ```
   ```
   [*PE-C-vpn-instance-BLUE-af-ipv4] multicast-domain switch-group-pool 225.4.4.1 28
   ```
   ```
   [*PE-C-vpn-instance-BLUE-af-ipv4] quit
   ```
   ```
   [*PE-C-vpn-instance-BLUE] commit
   ```
   ```
   [~PE-C-vpn-instance-BLUE] quit
   ```
   
   # Enable LDP and PIM-SM on the public network interface GigabitEthernet 0/1/0.
   
   ```
   [~PE-C] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE-C-GigabitEthernet0/1/0] ip address 192.168.8.1 24
   ```
   ```
   [*PE-C-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*PE-C-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE-C-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE-C-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE-C-GigabitEthernet0/1/0] quit
   ```
   
   # Bind GigabitEthernet 0/1/1 to VPN RED, and enable PIM-SM.
   
   ```
   [~PE-C] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE-C-GigabitEthernet0/1/1] ip binding vpn-instance RED
   ```
   ```
   [*PE-C-GigabitEthernet0/1/1] ip address 10.110.5.1 24
   ```
   ```
   [*PE-C-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*PE-C-GigabitEthernet0/1/1] commit
   ```
   ```
   [~PE-C-GigabitEthernet0/1/1] quit
   ```
   
   # Bind GigabitEthernet 0/1/2 to VPN BLUE, and enable PIM-SM.
   
   ```
   [~PE-C] interface gigabitethernet 0/1/2
   ```
   ```
   [~PE-C-GigabitEthernet0/1/2] ip binding vpn-instance BLUE
   ```
   ```
   [*PE-C-GigabitEthernet0/1/2] ip address 10.110.6.1 24
   ```
   ```
   [*PE-C-GigabitEthernet0/1/2] pim sm
   ```
   ```
   [*PE-C-GigabitEthernet0/1/2] commit
   ```
   ```
   [~PE-C-GigabitEthernet0/1/2] quit
   ```
   
   # Bind Loopback 2 to VPN BLUE, and enable PIM-SM.
   
   ```
   [~PE-C] interface loopback 2
   ```
   ```
   [*PE-C-LoopBack2] ip binding vpn-instance BLUE
   ```
   ```
   [*PE-C-LoopBack2] ip address 9.9.9.9 32
   ```
   ```
   [*PE-C-LoopBack2] pim sm
   ```
   ```
   [*PE-C-LoopBack2] commit
   ```
   ```
   [~PE-C-LoopBack2] quit
   ```
   
   # Configure Loopback 2 as C-BSR and C-RP for VPN BLUE.
   
   ```
   [~PE-C] pim vpn-instance BLUE
   ```
   ```
   [*PE-C-pim-blue] c-bsr Loopback2 
   ```
   ```
   [*PE-C-pim-blue] c-rp Loopback2
   ```
   ```
   [*PE-C-pim-blue] commit
   ```
   ```
   [~PE-C-pim-blue] quit
   ```
   
   # Configure BGP, OSPF, and RIP for unicast routing.
   
   ```
   [~PE-C] bgp 100
   ```
   ```
   [*PE-C-bgp] group VPN-G internal 
   ```
   ```
   [*PE-C-bgp] peer VPN-G connect-interface LoopBack1
   ```
   ```
   [*PE-C-bgp] peer 1.1.1.1 group VPN-G
   ```
   ```
   [*PE-C-bgp] peer 1.1.1.2 group VPN-G
   ```
   ```
   [*PE-C-bgp] ipv4-family vpn-instance RED
   ```
   ```
   [*PE-C-bgp-RED] import-route rip 2
   ```
   ```
   [*PE-C-bgp-RED] import-route direct 
   ```
   ```
   [*PE-C-bgp-RED] quit
   ```
   ```
   [*PE-C-bgp] ipv4-family vpn-instance BLUE
   ```
   ```
   [*PE-C-bgp-BLUE] import-route rip 3
   ```
   ```
   [*PE-C-bgp-BLUE] import-route direct 
   ```
   ```
   [*PE-C-bgp-BLUE] quit
   ```
   ```
   [*PE-C-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE-C-bgp-af-vpnv4] peer VPN-G enable
   ```
   ```
   [*PE-C-bgp-af-vpnv4] peer 1.1.1.1 group VPN-G
   ```
   ```
   [*PE-C-bgp-af-vpnv4] peer 1.1.1.2 group VPN-G
   ```
   ```
   [*PE-C-bgp-af-vpnv4] quit
   ```
   ```
   [*PE-C-bgp] commit
   ```
   ```
   [~PE-C-bgp] quit
   ```
   ```
   [~PE-C] ospf 1
   ```
   ```
   [*PE-C-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE-C-ospf-1-area-0.0.0.0] network 1.1.1.3 0.0.0.0 
   ```
   ```
   [*PE-C-ospf-1-area-0.0.0.0] network 192.168.0.0 0.0.255.255 
   ```
   ```
   [*PE-C-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE-C-ospf-1] commit
   ```
   ```
   [~PE-C-ospf-1] quit
   ```
   ```
   [~PE-C] rip 2 vpn-instance RED
   ```
   ```
   [*PE-C-rip-2] network 10.0.0.0
   ```
   ```
   [*PE-C-rip-2] import-route bgp cost 3 
   ```
   ```
   [*PE-C-rip-2] commit
   ```
   ```
   [~PE-C-rip-2] quit
   ```
   ```
   [~PE-C] rip 3 vpn-instance BLUE
   ```
   ```
   [*PE-C-rip-3] network 10.0.0.0
   ```
   ```
   [*PE-C-rip-3] import-route bgp cost 3
   ```
   ```
   [*PE-C-rip-3] commit
   ```
4. Configure the P.
   
   
   
   # Enable public-network IP multicast routing, configure an MPLS LSR-ID, and enable LDP.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~P] multicast routing-enable
   ```
   ```
   [*P] mpls lsr-id 2.2.2.2
   ```
   ```
   [*P] mpls
   ```
   ```
   [*P-mpls] quit
   ```
   ```
   [*P] mpls ldp
   ```
   ```
   [*P-mpls-ldp] quit
   ```
   ```
   [*P] commit
   ```
   
   # Enable LDP and PIM-SM on the public network interface GigabitEthernet 0/1/0.
   
   ```
   [~P] interface gigabitethernet 0/1/0
   ```
   ```
   [~P-GigabitEthernet0/1/0] ip address 192.168.6.2 24
   ```
   ```
   [*P-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*P-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*P-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/1/0] commit
   ```
   ```
   [~P-GigabitEthernet0/1/0] quit
   ```
   
   # Enable LDP and PIM-SM on the public network interface GigabitEthernet 0/1/1.
   
   ```
   [~P] interface gigabitethernet 0/1/1
   ```
   ```
   [~P-GigabitEthernet0/1/1] ip address 192.168.7.2 24
   ```
   ```
   [*P-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*P-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*P-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/1/1] commit
   ```
   ```
   [~P-GigabitEthernet0/1/1] quit
   ```
   
   # Enable LDP and PIM-SM on the public network interface GigabitEthernet 0/1/2.
   
   ```
   [~P] interface gigabitethernet 0/1/2
   ```
   ```
   [~P-GigabitEthernet0/1/2] ip address 192.168.8.2 24
   ```
   ```
   [*P-GigabitEthernet0/1/2] pim sm
   ```
   ```
   [*P-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*P-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/1/2] commit
   ```
   ```
   [~P-GigabitEthernet0/1/2] quit
   ```
   
   # Configure an IP address and enable PIM-SM on Loopback1.
   
   ```
   [~P] interface loopback 1
   ```
   ```
   [*P-LoopBack1] ip address 2.2.2.2 32
   ```
   ```
   [*P-LoopBack1] pim sm
   ```
   ```
   [*P-LoopBack1] commit
   ```
   ```
   [~P-LoopBack1] quit
   ```
   
   # Configure Loopback 1 as the C-BSR and C-RP of the public network instance.
   
   ```
   [~P] pim
   ```
   ```
   [*P-pim] c-bsr Loopback1 
   ```
   ```
   [*P-pim] c-rp Loopback1
   ```
   ```
   [*P-pim] commit
   ```
   ```
   [~P-pim] quit
   ```
   
   # Perform configurations for OSPF unicast routing.
   
   ```
   [~P] ospf 1
   ```
   ```
   [*P-ospf-1] area 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0 
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 192.168.0.0 0.0.255.255 
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*P-ospf-1] commit
   ```
5. Configure CE-Ra.
   
   
   
   # Enable IP multicast routing.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE-Ra
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE-Ra] multicast routing-enable
   ```
   
   # Enable PIM-SM on the VPN interface GigabitEthernet 0/1/0.
   
   ```
   [*CE-Ra] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE-Ra-GigabitEthernet0/1/0] ip address 10.110.7.1 24
   ```
   ```
   [*CE-Ra-GigabitEthernet0/1/0] pim sm
   ```
   
   # Enable PIM-SM on the VPN interface GigabitEthernet 0/1/1.
   
   ```
   [*CE-Ra] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE-Ra-GigabitEthernet0/1/1] ip address 10.110.2.2 24
   ```
   ```
   [*CE-Ra-GigabitEthernet0/1/1] pim sm
   ```
   
   # Perform configurations for RIP unicast routing.
   
   ```
   [*CE-Ra] rip 2
   ```
   ```
   [*CE-Ra-rip-2] network 10.0.0.0
   ```
   ```
   [*CE-Ra-rip-2] import-route direct
   ```
   ```
   [*CE-Ra-rip-2] commit
   ```
6. Configure CE-Bb.
   
   
   
   # Enable IP multicast routing.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE-Bb
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE-Bb] multicast routing-enable
   ```
   
   # Enable PIM-SM on the VPN interface GigabitEthernet 0/1/0.
   
   ```
   [*CE-Bb] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE-Bb-GigabitEthernet0/1/0] ip address 10.110.8.1 24
   ```
   ```
   [*CE-Bb-GigabitEthernet0/1/0] pim sm
   ```
   
   # Enable PIM-SM on the VPN interface GigabitEthernet 0/1/1.
   
   ```
   [*CE-Bb] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE-Bb-GigabitEthernet0/1/1] ip address 10.110.3.2 24
   ```
   ```
   [*CE-Bb-GigabitEthernet0/1/1] pim sm
   ```
   
   # Configure an IP address and enable PIM-SM on Loopback2.
   
   ```
   [*CE-Bb] interface LoopBack2
   ```
   ```
   [*CE-Bb-LoopBack2] ip address 8.8.8.8 255.255.255.255
   ```
   ```
   [*CE-Bb-LoopBack2] pim sm
   ```
   
   # Perform configurations for RIP unicast routing.
   
   ```
   [*CE-Bb] rip 3
   ```
   ```
   [*CE-Bb-rip-3] network 10.0.0.0
   ```
   ```
   [*CE-Bb-rip-3] import-route direct
   ```
   ```
   [*CE-Bb-rip-3] commit
   ```
7. Configure CE-Rb.
   
   
   
   # Enable IP multicast routing.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE-Rb
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE-Rb] multicast routing-enable
   ```
   
   # Enable PIM-SM and IGMP on the VPN interface GigabitEthernet 0/1/0.
   
   ```
   [*CE-Rb] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE-Rb-GigabitEthernet0/1/0] ip address 10.110.9.1 24
   ```
   ```
   [*CE-Rb-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*CE-Rb-GigabitEthernet0/1/0] igmp enable
   ```
   
   # Enable PIM-SM on the VPN interface GigabitEthernet 0/1/1.
   
   ```
   [*CE-Rb] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE-Rb-GigabitEthernet0/1/1] ip address 10.110.4.2 24
   ```
   ```
   [*CE-Rb-GigabitEthernet0/1/1] pim sm
   ```
   
   # Enable PIM-SM on the VPN interface GigabitEthernet 0/1/2.
   
   ```
   [*CE-Rb] interface gigabitethernet 0/1/2
   ```
   ```
   [*CE-Rb-GigabitEthernet0/1/2] ip address 10.110.12.1 24
   ```
   ```
   [*CE-Rb-GigabitEthernet0/1/2] pim sm
   ```
   
   # Configure an IP address and enable PIM-SM on Loopback1.
   
   ```
   [*CE-Rb] interface loopback 1
   ```
   ```
   [*CE-Rb-LoopBack1] ip address 7.7.7.7 32
   ```
   ```
   [*CE-Rb-LoopBack1] pim sm
   ```
   ```
   [*CE-Rb-LoopBack1] quit
   ```
   
   # Configure Loopback 1 as the C-BSR and C-RP of VPN RED.
   
   ```
   [*CE-Rb] pim
   ```
   ```
   [*CE-Rb-pim] c-bsr Loopback1
   ```
   ```
   [*CE-Rb-pim] c-rp Loopback1
   ```
   ```
   [*CE-Rb-pim] quit
   ```
   
   # Perform configurations for RIP unicast routing.
   
   ```
   [*CE-Rb] rip 2
   ```
   ```
   [*CE-Rb-rip-2] network 10.0.0.0
   ```
   ```
   [*CE-Rb-rip-2] network 10.0.0.0
   ```
   ```
   [*CE-Rb-rip-2] import-route direct
   ```
   ```
   [*CE-Rb-rip-2] commit
   ```
8. Configure CE-Rc.
   
   
   
   # Enable IP multicast routing.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE-Rc
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE-Rc] multicast routing-enable
   ```
   
   # Enable PIM-SM and IGMP on the VPN interface GigabitEthernet 0/1/0.
   
   ```
   [*CE-Rc] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE-Rc-GigabitEthernet0/1/0] ip address 10.110.10.1 24
   ```
   ```
   [*CE-Rc-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*CE-Rc-GigabitEthernet0/1/0] igmp enable
   ```
   
   # Enable PIM-SM on the VPN interface GigabitEthernet 0/1/1.
   
   ```
   [*CE-Rc] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE-Rc-GigabitEthernet0/1/1] ip address 10.110.5.2 24
   ```
   ```
   [*CE-Rc-GigabitEthernet0/1/1] pim sm
   ```
   
   # Enable PIM-SM on the VPN interface GigabitEthernet 0/1/2.
   
   ```
   [*CE-Rc] interface gigabitethernet 0/1/2
   ```
   ```
   [*CE-Rc-GigabitEthernet0/1/2] ip address 10.110.12.2 24
   ```
   ```
   [*CE-Rc-GigabitEthernet0/1/2] pim sm
   ```
   
   # Perform configurations for RIP unicast routing.
   
   ```
   [*CE-Rc] rip 2
   ```
   ```
   [*CE-Rc-rip-2] network 10.0.0.0
   ```
   ```
   [*CE-Rc-rip-2] import-route direct
   ```
   ```
   [*CE-Rc-rip-2] commit
   ```
9. Configure CE-Bc.
   
   
   
   # Enable IP multicast routing.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE-Bc
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE-Bc] multicast routing-enable
   ```
   
   # Enable PIM-SM and IGMP on the VPN interface GigabitEthernet 0/1/0.
   
   ```
   [*CE-Bc] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE-Bc-GigabitEthernet0/1/0] ip address 10.110.11.1 24
   ```
   ```
   [*CE-Bc-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*CE-Bc-GigabitEthernet0/1/0] igmp enable
   ```
   
   # Enable PIM-SM on the VPN interface GigabitEthernet 0/1/1.
   
   ```
   [*CE-Bc] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE-Bc-GigabitEthernet0/1/1] ip address 10.110.6.2 24
   ```
   ```
   [*CE-Bc-GigabitEthernet0/1/1] pim sm
   ```
   
   # Perform configurations for RIP unicast routing.
   
   ```
   [*CE-Bc] rip 3
   ```
   ```
   [*CE-Bc-rip-3] network 10.0.0.0
   ```
   ```
   [*CE-Bc-rip-3] import-route direct
   ```
   ```
   [*CE-Bc-rip-3] commit
   ```
10. Configure an IP address for the MTunnel interface.
    
    
    
    # Configure PE-A.
    
    ```
    [~PE-A] interface MTunnel 0 
    [~PE-A-MTunnel0] ip address 1.1.1.1 32 
    [*PE-A-MTunnel0] quit 
    [*PE-A] commit
    ```
    
    # Configure PE-B.
    
    ```
    [~PE-B] interface MTunnel 0 
    [~PE-B-MTunnel0] ip address 1.1.1.2 32 
    [*PE-B-MTunnel0] quit 
    [*PE-B] commit
    [~PE-B] interface MTunnel 1 
    [~PE-B-MTunnel11] ip address 1.1.1.2 32 
    [*PE-B-MTunnel1] quit 
    [*PE-B] commit
    ```
    
    # Configure PE-C.
    
    ```
    [~PE-C] interface MTunnel 0 
    [~PE-C-MTunnel0] ip address 1.1.1.3 32 
    [*PE-C-MTunnel0] quit 
    [*PE-C] commit
    [~PE-C] interface MTunnel 1 
    [~PE-C-MTunnel1] ip address 1.1.1.3 32 
    [*PE-C-MTunnel1] quit 
    [*PE-C] commit
    ```
11. Verify the configuration.
    
    
    
    # Run the **display pim vpn-instance neighbor** command on PE-C and PE-B to check the neighbors of each MTI bound to a specific VPN. For example:
    
    ```
    [~PE-C] display pim vpn-instance BLUE neighbor
    VPN-Instance: BLUE
    
     Total Number of Neighbors = 2 
    
     Neighbor        Interface           Uptime   Expires    Dr-Priority    BFD-Session
     10.110.6.2      GE0/1/2             1d:01h   00:01:42   1              N
     1.1.1.2         MTun1               1d:01h   00:01:29  1              N
    ```
    ```
    [~PE-B] display pim vpn-instance BLUE neighbor
    VPN-Instance: BLUE
    
     Total Number of Neighbors = 2 
    
     Neighbor        Interface           Uptime   Expires    Dr-Priority    BFD-Session
     10.110.3.2      GE0/1/1             1d:01h   00:01:39   1              N
     1.1.1.3         MTun1               1d:02h   00:01:19  1              N
    ```
    
    The preceding command output shows that the multicast VPN neighbor relationship can be established on the MTunnel interface, indicating that the multicast VPN channel is successfully established.
    
    # Run the **display pim vpn-instance routing-table** command on PE-C to view the PIM routing table. For example:
    
    ```
    [~PE-C] display pim vpn-instance BLUE routing-table
    ```
    ```
     VPN-Instance: BLUE
     Total 0 (*, G) entry; 1 (S, G) entry
    
     (8.8.8.8, 227.111.1.2)
         RP: 9.9.9.9(local)
         Protocol: pim-sm, Flag: SPT
         UpTime: 06:39:55
         Upstream interface: MTunnel1, Refresh time: 06:39:55
              Upstream neighbor: 1.1.1.2
              RPF prime neighbor: 1.1.1.2
         Downstream interface(s) information:
         Total number of downstreams: 1
           1: GigabitEthernet0/1/2
                 Protocol: pim-sm, UpTime: 06:38:41, Expires: 00:02:49
    
    ```
    
    The preceding command output shows that PIM routing entries are created for VPNs on PE-C.
    
    # Run the **display multicast vpn-instance forwarding-table** command on PE-C to check forwarding entries created for VPNs. For example:
    
    ```
    [~PE-C] display multicast vpn-instance BLUE forwarding-table
    Multicast Forwarding Table of VPN-Instance: BLUE
    Total 1 entry, 1 matched
    
    1.(8.8.8.8, 227.111.1.2)
         MID: 3, Flags: -
         Uptime: 06:53:54, Timeout in: 00:00:00
         Incoming interface: MTunnel1
         List of 1 outgoing interfaces:
           1: GigabitEthernet0/1/2
         Matched rate: 328938 packets/sec, 215783368 bits/sec
         Matched 38264 packets(1071392 bytes), Wrong If 0 packets
         Forwarded 38264 packets(1071392 bytes)
    ```
    
    The preceding command output shows that forwarding entries are created for VPNs on PE-C and traffic is forwarded properly.
    
    # Run the **display pim routing-table** command on CE-Bb connected to a source and CE-Bc connected to receivers to check the PIM routing tables established for the public network. For example:
    
    ```
    [~CE-Bb] display pim routing-table
    ```
    ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
    
     (8.8.8.8, 227.111.1.2)
         RP: 9.9.9.9
         Protocol: pim-sm, Flag: SPT LOC
         UpTime: 00:01:29
         Upstream interface: LoopBack1, Refresh time: 00:01:29
             Upstream neighbor: NULL
             RPF prime neighbor: NULL
         Downstream interface(s) information:
         Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                 Protocol: pim-sm, UpTime: 00:00:15, Expires: 00:03:15
    ```
    ```
    [~CE-Bc] display pim routing-table
    ```
    ```
    VPN-Instance: public net
     Total 0 (*, G) entry; 1 (S, G) entry
    
     (8.8.8.8, 227.111.1.2)
         RP: NULL
         Protocol: pim-sm, Flag: SPT SG_RCVR
         UpTime: 00:00:11
         Upstream interface: GigabitEthernet0/1/1, Refresh time: 00:00:11
             Upstream neighbor: 10.110.6.1
             RPF prime neighbor: 10.110.6.1
         Downstream interface(s) information:
         Total number of downstreams: 1
           1: GigabitEthernet0/1/0
                 Protocol: static, UpTime: 00:00:11, Expires: -
    ```
    
    The preceding command output shows that PIM routing entries are created for the public network on CE-Bb and CE-Bc.
    
    # Run the **display multicast forwarding-table** command on CE-Bb connected to a source and CE-Bc connected to receivers to check the PIM forwarding tables established for the public network. For example:
    
    ```
    [~CE-Bb] display multicast forwarding-table
    ```
    ```
    Multicast Forwarding Table of VPN-Instance: public_net
    Total 1 entry, 1 matched
    
    1.(8.8.8.8, 227.111.1.2)
         MID: 1, Flags: -
         Uptime: 05:25:35, Timeout in: 00:00:00
         Incoming interface: Mcast_In_IF
         List of 1 outgoing interfaces:
           1: GigabitEthernet0/1/1       
             Activetime: 02:35:57
         Matched rate: 328938 packets/sec, 215783368 bits/sec
         Matched 38264 packets(1071392 bytes), Wrong If 0 packets
         Forwarded 38264 packets(1071392 bytes)
    ```
    ```
    [~CE-Bc] display multicast forwarding-table
    ```
    ```
    Multicast Forwarding Table of VPN-Instance: public_net
    
    Total 1 entry, 1 matched
    
    1.(8.8.8.8, 227.111.1.2)
         MID: 1, Flags: -
         Uptime: 05:25:35, Timeout in: 00:00:00
         Incoming interface: Mcast_In_IF
         List of 1 outgoing interfaces:
           1: GigabitEthernet0/1/0
             Activetime: 02:35:57
         Matched rate: 328938 packets/sec, 215783368 bits/sec
         Matched 38264 packets(1071392 bytes), Wrong If 0 packets
         Forwarded 38264 packets(1071392 bytes)
    ```
    
    The preceding command output shows that PIM forwarding entries are created for the public network on CE-Bb and CE-Bc and traffic is forwarded properly.
    
    After the preceding configurations are performed, PC4 can receive multicast packets from source 2. Similarly, PC1, PC2, and PC3 can receive multicast packets from source 1.

#### Configuration Files

* PE-A configuration file
  
  ```
  #
  ```
  ```
  sysname PE-A
  ```
  ```
  #
  ```
  ```
  router id 1.1.1.1
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 1.1.1.1
  ```
  ```
  mpls
  ```
  ```
  #
  ```
  ```
  mpls ldp
  ```
  ```
   #
  ```
  ```
   ipv4-family
  ```
  ```
  #
  ```
  ```
  ip vpn-instance RED
  ```
  ```
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 import-extcommunity
    multicast routing-enable
    multicast-domain share-group 239.1.1.1 binding MTunnel 0
    multicast-domain switch-group-pool 225.2.2.0 255.255.255.240
    multicast-domain source-interface loopback 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.6.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip binding vpn-instance RED
  ```
  ```
   ip address 10.110.1.1 255.255.255.0 
  ```
  ```
   pim sm 
  ```
  ```
   igmp enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip binding vpn-instance RED
  ```
  ```
   ip address 10.110.2.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface MTunnel0
  ```
  ```
   ip binding vpn-instance RED
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   group VPN-G internal
  ```
  ```
   peer VPN-G connect-interface LoopBack1
  ```
  ```
   peer 1.1.1.2 as-number 100
  ```
  ```
   peer 1.1.1.2 group VPN-G
  ```
  ```
   peer 1.1.1.3 as-number 100
  ```
  ```
   peer 1.1.1.3 group VPN-G
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    peer VPN-G enable
  ```
  ```
    peer 1.1.1.2 enable 
  ```
  ```
    peer 1.1.1.2 group VPN-G
  ```
  ```
    peer 1.1.1.3 enable
  ```
  ```
    peer 1.1.1.3 group VPN-G
  ```
  ```
   #
  ```
  ```
   ipv4-family vpnv4
  ```
  ```
    policy vpn-target
  ```
  ```
    peer VPN-G enable
  ```
  ```
    peer 1.1.1.2 enable
  ```
  ```
    peer 1.1.1.2 group VPN-G
  ```
  ```
    peer 1.1.1.3 enable
  ```
  ```
    peer 1.1.1.3 group VPN-G
  ```
  ```
  #
  ```
  ```
   ipv4-family vpn-instance RED
  ```
  ```
    import-route rip 2
  ```
  ```
    import-route direct 
  ```
  ```
  #
  ```
  ```
  ospf 1 
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 1.1.1.1 0.0.0.0 
  ```
  ```
    network 192.168.0.0 0.0.255.255 
  ```
  ```
  #
  ```
  ```
  rip 2 vpn-instance RED
  ```
  ```
    network 10.0.0.0
  ```
  ```
    import-route bgp cost 3 
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE-B configuration file
  
  ```
  #
  ```
  ```
  sysname PE-B
  ```
  ```
  #
  ```
  ```
  router id 1.1.1.2
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 1.1.1.2
  ```
  ```
  mpls 
  ```
  ```
  #
  ```
  ```
  mpls ldp
  ```
  ```
   #
  ```
  ```
   ipv4-family
  ```
  ```
  #
  ```
  ```
  ip vpn-instance BLUE
  ```
  ```
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 200:1 export-extcommunity
    vpn-target 200:1 import-extcommunity
    multicast routing-enable
    multicast-domain share-group 239.2.2.2 binding MTunnel 1
    multicast-domain switch-group-pool 225.4.4.0 255.255.255.240
    multicast-domain source-interface loopback 1
  ```
  ```
  #
  ```
  ```
  ip vpn-instance RED
  ```
  ```
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 import-extcommunity
    multicast routing-enable
    multicast-domain share-group 239.1.1.1 binding MTunnel 0
    multicast-domain switch-group-pool 225.2.2.0 255.255.255.240
    multicast-domain source-interface loopback 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.7.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
   mpls
  ```
  ```
   mpls ldp 
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip binding vpn-instance BLUE
  ```
  ```
   ip address 10.110.3.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip binding vpn-instance RED
  ```
  ```
   ip address 10.110.4.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 1.1.1.2 255.255.255.255
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface MTunnel0
  ```
  ```
   ip binding vpn-instance RED
   ip address 1.1.1.2 255.255.255.255
  ```
  ```
  #
  ```
  ```
  interface MTunnel1
  ```
  ```
   ip binding vpn-instance BLUE
   ip address 1.1.1.2 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   group VPN-G internal
  ```
  ```
   peer VPN-G connect-interface LoopBack1
  ```
  ```
   peer 1.1.1.1 as-number 100
  ```
  ```
   peer 1.1.1.1 group VPN-G
  ```
  ```
   peer 1.1.1.3 as-number 100
  ```
  ```
   peer 1.1.1.3 group VPN-G
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    peer VPN-G enable
  ```
  ```
    peer 1.1.1.1 enable
  ```
  ```
    peer 1.1.1.1 group VPN-G
  ```
  ```
    peer 1.1.1.3 enable
  ```
  ```
    peer 1.1.1.3 group VPN-G
  ```
  ```
   #
  ```
  ```
   ipv4-family vpnv4
  ```
  ```
    policy vpn-target
  ```
  ```
    peer VPN-G enable
  ```
  ```
    peer 1.1.1.1 enable
  ```
  ```
    peer 1.1.1.1 group VPN-G
  ```
  ```
    peer 1.1.1.3 enable
  ```
  ```
    peer 1.1.1.3 group VPN-G
  ```
  ```
   #
  ```
  ```
   ipv4-family vpn-instance RED
  ```
  ```
    import-route rip 2
  ```
  ```
    import-route direct 
  ```
  ```
   #
  ```
  ```
   ipv4-family vpn-instance BLUE
  ```
  ```
    import-route rip 3
  ```
  ```
    import-route direct 
  ```
  ```
  #
  ```
  ```
  ospf 1 
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 1.1.1.2 0.0.0.0 
  ```
  ```
    network 192.168.0.0 0.0.255.255 
  ```
  ```
  #
  ```
  ```
  rip 2 vpn-instance RED
  ```
  ```
   network 10.0.0.0
  ```
  ```
   import-route bgp cost 3 
  ```
  ```
  #
  ```
  ```
  rip 3 vpn-instance BLUE
  ```
  ```
   network 10.0.0.0
  ```
  ```
   import-route bgp cost 3 
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE-C configuration file
  
  ```
  #
  ```
  ```
  sysname PE-C
  ```
  ```
  # 
  ```
  ```
  router id 1.1.1.3
  ```
  ```
  # 
  ```
  ```
  multicast routing-enable
  ```
  ```
  # 
  ```
  ```
  mpls lsr-id 1.1.1.3
  ```
  ```
  mpls 
  ```
  ```
  # 
  ```
  ```
  mpls ldp
  ```
  ```
   #
  ```
  ```
   ipv4-family
  ```
  ```
  # 
  ```
  ```
  ip vpn-instance RED
  ```
  ```
   ipv4-family 
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 import-extcommunity
    multicast routing-enable
    multicast-domain share-group 239.1.1.1 binding MTunnel 0
    multicast-domain switch-group-pool 225.2.2.0 255.255.255.240
    multicast-domain source-interface loopback 1
  ```
  ```
  # 
  ```
  ```
  ip vpn-instance BLUE
  ```
  ```
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 200:1 export-extcommunity
    vpn-target 200:1 import-extcommunity
    multicast routing-enable
    multicast-domain share-group 239.2.2.2 binding MTunnel 1
    multicast-domain switch-group-pool 225.4.4.0 255.255.255.240
    multicast-domain source-interface loopback 1
  ```
  ```
  # 
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.8.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
   mpls 
  ```
  ```
   mpls ldp 
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip binding vpn-instance RED
  ```
  ```
   ip address 10.110.5.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  # 
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip binding vpn-instance BLUE
  ```
  ```
   ip address 10.110.6.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  # 
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 1.1.1.3 255.255.255.255
  ```
  ```
   pim sm
  ```
  ```
  # 
  ```
  ```
  interface LoopBack2
  ```
  ```
   ip binding vpn-instance BLUE
  ```
  ```
   ip address 9.9.9.9 255.255.255.255 
  ```
  ```
   pim sm
  ```
  ```
  # 
  ```
  ```
  pim vpn-instance BLUE
  ```
  ```
   c-bsr LoopBack2 
  ```
  ```
   c-rp LoopBack2
  ```
  ```
  # 
  ```
  ```
  interface MTunnel0
  ```
  ```
   ip binding vpn-instance RED
   ip address 1.1.1.3 255.255.255.255
  ```
  ```
  # 
  ```
  ```
  interface MTunnel1
  ```
  ```
   ip binding vpn-instance BLUE
   ip address 1.1.1.3 255.255.255.255
  ```
  ```
  # 
  ```
  ```
  bgp 100
  ```
  ```
   group VPN-G internal
  ```
  ```
   peer VPN-G connect-interface LoopBack1
  ```
  ```
   peer 1.1.1.1 as-number 100
  ```
  ```
   peer 1.1.1.1 group VPN-G
  ```
  ```
   peer 1.1.1.2 as-number 100
  ```
  ```
   peer 1.1.1.2 group VPN-G
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    peer VPN-G enable
  ```
  ```
    peer 1.1.1.1 enable
  ```
  ```
    peer 1.1.1.1 group VPN-G
  ```
  ```
    peer 1.1.1.2 enable
  ```
  ```
    peer 1.1.1.2 group VPN-G
  ```
  ```
   #
  ```
  ```
   ipv4-family vpnv4
  ```
  ```
    policy vpn-target
  ```
  ```
    peer VPN-G enable
  ```
  ```
    peer 1.1.1.1 enable
  ```
  ```
    peer 1.1.1.1 group VPN-G
  ```
  ```
    peer 1.1.1.2 enable
  ```
  ```
    peer 1.1.1.2 group VPN-G
  ```
  ```
   #
  ```
  ```
   ipv4-family vpn-instance RED
  ```
  ```
    import-route rip 2
  ```
  ```
    import-route direct 
  ```
  ```
   #         
  ```
  ```
   ipv4-family vpn-instance BLUE
  ```
  ```
    import-route rip 3
  ```
  ```
    import-route direct 
  ```
  ```
  #         
  ```
  ```
  ospf 1     
  ```
  ```
   area  0.0.0.0
  ```
  ```
    network 1.1.1.3 0.0.0.0 
  ```
  ```
    network 192.168.0.0 0.0.255.255 
  ```
  ```
  #
  ```
  ```
  rip 2 vpn-instance RED 
  ```
  ```
   network 10.0.0.0
  ```
  ```
   import-route bgp cost 3 
  ```
  ```
  #               
  ```
  ```
  rip 3 vpn-instance BLUE 
  ```
  ```
   network 10.0.0.0
  ```
  ```
   import-route bgp cost 3 
  ```
  ```
  #
  ```
  ```
  return
  ```
* P configuration file
  
  ```
  #
  ```
  ```
  sysname P
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 2.2.2.2
  ```
  ```
  mpls 
  ```
  ```
  #
  ```
  ```
  mpls ldp
  ```
  ```
   #
  ```
  ```
   ipv4-family
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.6.2 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.7.2 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.8.2 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
   mpls
  ```
  ```
   mpls ldp 
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
   c-bsr Loopback1
  ```
  ```
   c-rp Loopback1
  ```
  ```
  #
  ```
  ```
  ospf 1 
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 2.2.2.2 0.0.0.0 
  ```
  ```
    network 192.168.0.0 0.0.255.255 
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE-Ra configuration file
  
  ```
  #
  ```
  ```
  sysname CE-Ra
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.7.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.2.2 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  rip 2
  ```
  ```
   network 10.0.0.0
  ```
  ```
   import-route direct
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE-Bb configuration file
  
  ```
  #
  ```
  ```
  sysname CE-Bb
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.8.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.3.2 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface LoopBack2
  ```
  ```
   ip address 8.8.8.8 255.255.255.255
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  rip 3
  ```
  ```
   network 10.0.0.0
  ```
  ```
   import-route direct
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE-Rb configuration file
  
  ```
  #
  ```
  ```
  sysname CE-Rb
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.9.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
   igmp enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.4.2 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.12.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
   interface loopback 1
  ```
  ```
   ip address 7.7.7.7 32
  ```
  ```
   pim sm
  ```
  ```
  #       
  ```
  ```
  pim
  ```
  ```
   c-bsr Loopback1 
  ```
  ```
   c-rp Loopback1
  ```
  ```
  #
  ```
  ```
  rip 2
  ```
  ```
   network 10.0.0.0 
  ```
  ```
   network 10.0.0.0
  ```
  ```
   import-route direct
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE-Rc configuration file
  
  ```
  #
  ```
  ```
  sysname CE-Rc
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.10.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
   igmp enable
  ```
  ```
   igmp version 3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.5.2 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.12.2 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  rip 2
  ```
  ```
   network 10.0.0.0
  ```
  ```
   import-route direct
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE-Bc configuration file
  
  ```
  #
  ```
  ```
  sysname CE-Bc
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.11.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
   igmp enable
  ```
  ```
   igmp version 3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.6.2 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  rip 3
  ```
  ```
   network 10.0.0.0
  ```
  ```
   import-route direct
  ```
  ```
  #
  ```
  ```
  return
  ```