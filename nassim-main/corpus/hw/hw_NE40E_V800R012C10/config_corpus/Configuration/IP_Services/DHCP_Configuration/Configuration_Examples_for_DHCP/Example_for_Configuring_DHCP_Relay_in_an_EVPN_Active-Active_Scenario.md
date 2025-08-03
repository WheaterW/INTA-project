Example for Configuring DHCP Relay in an EVPN Active-Active Scenario
====================================================================

Example for Configuring DHCP Relay in an EVPN Active-Active Scenario

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0207660591__fig_dc_vrp_evpn_cfg_001701), to allow the CE and PEs to communicate, configure EVPN. DHCP needs to be deployed so that the DHCP server can assign an IP address to the DHCP client. PE1 and PE2 function as gateways, and DHCP relay needs to be deployed on them. PE3 is connected to the DHCP server.

**Figure 1** EVPN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0207888427.png)

**Table 1** Interface IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| PE1 | GE 0/2/0 | 192.168.2.1/24 |
| GE 0/3/0 | 192.168.1.2/24 |
| Loopback 1 | 12.1.1.1/32 |
| LoopBack2 | 14.1.1.1/32 |
| PE2 | GE 0/2/0 | 192.168.2.2/24 |
| GE 0/3/0 | 172.16.1.1/24 |
| Loopback 1 | 13.1.1.1/32 |
| LoopBack2 | 15.1.1.1/32 |
| PE3 | GE 0/1/0 | 192.168.1.1/24 |
| GE 0/2/0 | 172.16.1.2/24 |
| GE 0/3/0 | 30.1.1.1/24 |
| Loopback 1 | 11.1.1.1/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface on the CE and PEs.
2. Configure an IGP on the backbone network to allow the PEs to communicate.
3. Configure basic MPLS functions, enable MPLS LDP, and establish LDP LSPs on the backbone network.
4. Configure an EVPN instance on each PE.
5. Bind the EVPN instance to a BD on each PE.
6. Configure a VPN instance on each PE, and bind the PE's loopback interface to the VPN instance to import loopback routes from the CE.
7. Configure a source address on each PE.
8. Configure an Eth-Trunk interface for connecting PE1 and PE2 to the CE.
9. Configure an ESI for the Eth-Trunk interface on PE1 and PE2.
10. Configure a service access point on PE1 and PE2.
11. Enable the BGP-EVPN address family, and configure peers on each PE.
12. Enable EVPN to generate and advertise IP prefix routes and IRB routes in a VPN instance.
13. Enable the VPN instance to advertise IP routes to the EVPN instance on each PE.
14. Establish a BGP EVPN peer relationship between the PEs.
15. Configure the CE, PE1, and PE2 to communicate.
16. Configure DHCP relay on PE1 and PE2.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evpna
* EVPN instance **evpna**'s RD and RT on each PE: 1:1

#### Procedure

1. Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0207660591__fig_dc_vrp_evpn_cfg_001701). For configuration details, see [Configuration Files](#EN-US_TASK_0207660591__file1) in this section.
   
   
   
   Using the local loopback interface address of each PE as the source address is recommended.
2. Configure an IGP on the backbone network to allow the PEs to communicate. OSPF is used as an IGP in this example.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] area 0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 12.1.1.1 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 20.1.1.1 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255 
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE1-ospf-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] area 0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 13.1.1.1 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 20.1.1.1 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE2-ospf-1] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ospf 1
   ```
   ```
   [*PE3-ospf-1] area 0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 11.1.1.1 0.0.0.0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE3-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE3-ospf-1] quit
   ```
3. Configure basic MPLS functions, enable MPLS LDP, and establish LDP LSPs on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 12.1.1.1
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/3/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 13.1.1.1
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] quit
   ```
   ```
   [*PE2] interface GigabitEthernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] interface GigabitEthernet 0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/3/0] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls lsr-id 11.1.1.1
   ```
   ```
   [*PE3] mpls
   ```
   ```
   [*PE3-mpls] quit
   ```
   ```
   [*PE3] mpls ldp
   ```
   ```
   [*PE3-mpls-ldp] quit
   ```
   ```
   [*PE3] interface GigabitEthernet 0/1/0
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE3] interface GigabitEthernet 0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
4. Configure an EVPN instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evpna bd-mode
   ```
   ```
   [*PE1-evpn-instance-evpna] route-distinguisher 1:1
   ```
   ```
   [*PE1-evpn-instance-evpna] vpn-target 1:1 
   ```
   ```
   [*PE1-evpn-instance-evpna] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evpna bd-mode
   ```
   ```
   [*PE2-evpn-instance-evpna] route-distinguisher 1:1
   ```
   ```
   [*PE2-evpn-instance-evpna] vpn-target 1:1
   ```
   ```
   [*PE2-evpn-instance-evpna] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evpna bd-mode
   ```
   ```
   [*PE3-evpn-instance-evpna] route-distinguisher 1:1
   ```
   ```
   [*PE3-evpn-instance-evpna] vpn-target 1:1
   ```
   ```
   [*PE3-evpn-instance-evpna] quit
   ```
   ```
   [*PE3] commit
   ```
5. Bind the EVPN instance to a BD on each PE.
   
   
   
   # Configure PE1.
   
   
   
   ```
   [~PE1] bridge-domain 1
   ```
   ```
   [*PE1-bd1] evpn binding vpn-instance evpna
   ```
   ```
   [*PE1-bd1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] bridge-domain 1
   ```
   ```
   [*PE2-bd1] evpn binding vpn-instance evpna
   ```
   ```
   [*PE2-bd1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] bridge-domain 1
   ```
   ```
   [*PE3-bd1] evpn binding vpn-instance evpna
   ```
   ```
   [*PE3-bd1] quit
   ```
   ```
   [*PE3] commit
   ```
6. Configure a VPN instance on each PE, and bind the PE's loopback interface to the VPN instance to import loopback routes from the CE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 100:1 export-extcommunity
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 100:1 export-extcommunity evpn
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 100:1 import-extcommunity
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 100:1 import-extcommunity evpn
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpna] quit
   ```
   ```
   [*PE1] interface LoopBack2
   ```
   ```
   [*PE1-LoopBack2] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-LoopBack2] ip address 14.1.1.1 255.255.255.255
   ```
   ```
   [*PE1-LoopBack2] commit
   ```
   ```
   [*PE1-LoopBack2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configurations of PE2 and PE3 are similar to the configuration of PE1.
7. Configure a source address on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 12.1.1.1
   ```
   ```
   [*PE1] evpn
   ```
   ```
   [*PE1-evpn] vlan-extend private enable
   ```
   ```
   [*PE1-evpn] vlan-extend redirect enable
   ```
   ```
   [*PE1-evpn] local-remote frr enable
   ```
   ```
   [*PE1-evpn] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 13.1.1.1
   ```
   ```
   [*PE2] evpn
   ```
   ```
   [*PE2-evpn] vlan-extend private enable
   ```
   ```
   [*PE2-evpn] vlan-extend redirect enable
   ```
   ```
   [*PE2-evpn] local-remote frr enable
   ```
   ```
   [*PE2-evpn] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn source-address 11.1.1.1
   ```
   ```
   [*PE3] evpn
   ```
   ```
   [*PE3-evpn] vlan-extend private enable
   ```
   ```
   [*PE3-evpn] vlan-extend redirect enable
   ```
   ```
   [*PE3-evpn] local-remote frr enable
   ```
   ```
   [*PE3-evpn] quit
   ```
   ```
   [*PE3] commit
   ```
8. Configure an Eth-Trunk interface for connecting PE1 and PE2 to the CE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] lacp e-trunk system-id 00e0-fc12-3456
   ```
   ```
   [*PE1] e-trunk 1
   ```
   ```
   [*PE1-e-trunk-1] priority 50
   ```
   ```
   [*PE1-e-trunk-1] peer-address 13.1.1.1 source-address 12.1.1.1
   ```
   ```
   [*PE1-e-trunk-1] quit
   ```
   ```
   [*PE1] interface eth-trunk 1
   ```
   ```
   [*PE1-Eth-Trunk1] mode lacp-static
   ```
   ```
   [*PE1-Eth-Trunk1] e-trunk 1
   ```
   ```
   [*PE1-Eth-Trunk1] e-trunk mode force-master
   ```
   ```
   [*PE1-Eth-Trunk1] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] eth-trunk 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] lacp e-trunk system-id 00e0-fc12-3456
   ```
   ```
   [*PE2] e-trunk 1
   ```
   ```
   [*PE2-e-trunk-1] priority 10
   ```
   ```
   [*PE2-e-trunk-1] peer-address 12.1.1.1 source-address 13.1.1.1
   ```
   ```
   [*PE2-e-trunk-1] quit
   ```
   ```
   [*PE2] interface eth-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk1] mode lacp-static
   ```
   ```
   [*PE2-Eth-Trunk1] e-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk1] e-trunk mode force-master
   ```
   ```
   [*PE2-Eth-Trunk1] quit
   ```
   ```
   [*PE2] interface GigabitEthernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] eth-trunk 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure the CE.
   
   ```
   [~CE] interface eth-trunk 1
   ```
   ```
   [*CE-Eth-Trunk1] mode lacp-static
   ```
   ```
   [*CE-Eth-Trunk1] quit
   ```
   ```
   [*CE] interface Ethernet 0/1/0
   ```
   ```
   [*CE-Ethernet0/1/0] eth-trunk 1
   ```
   ```
   [*CE-Ethernet0/1/0] quit
   ```
   ```
   [*CE] commit
   ```
   ```
   [*CE] interface Ethernet 0/2/0
   ```
   ```
   [*CE-Ethernet0/2/0] eth-trunk 1
   ```
   ```
   [*CE-Ethernet0/2/0] quit
   ```
   ```
   [*CE] commit
   ```
9. Configure an ESI for the Eth-Trunk interface on PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface eth-trunk 1
   ```
   ```
   [*PE1-Eth-Trunk1] esi 0000.0000.0000.0000.1111
   ```
   ```
   [*PE1-Eth-Trunk1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface eth-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk1] esi 0000.0000.0000.0000.1111
   ```
   ```
   [*PE2-Eth-Trunk1] quit
   ```
   ```
   [*PE2] commit
   ```
10. Configure a service access point on PE1 and PE2.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] interface Eth-Trunk1.1 mode l2
    ```
    ```
    [~PE1-Eth-trunk1.1] encapsulation dot1q vid 100
    ```
    ```
    [*PE1-Eth-trunk1.1] rewrite pop single
    ```
    ```
    [*PE1-Eth-trunk1.1] bridge-domain 1
    ```
    ```
    [*PE1-Eth-trunk1.1] quit
    ```
    ```
    [*PE1] commit
    ```
    
    # Configure PE2.
    
    ```
    [~PE2] interface Eth-Trunk1.1 mode l2
    ```
    ```
    [~PE2-Eth-trunk1.1] encapsulation dot1q vid 100
    ```
    ```
    [*PE2-Eth-trunk1.1] rewrite pop single
    ```
    ```
    [*PE2-Eth-trunk1.1] bridge-domain 1
    ```
    ```
    [*PE2-Eth-trunk1.1] quit
    ```
    ```
    [*PE2] commit
    ```
11. Enable the BGP-EVPN address family, and configure peers on each PE.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] bgp 100
    ```
    ```
    [*PE1-bgp] l2vpn-family evpn
    ```
    ```
    [*PE1-bgp-af-evpn] peer 11.1.1.1 enable
    ```
    ```
    [*PE1-bgp-af-evpn] peer 11.1.1.1 advertise irb
    ```
    ```
    [*PE1-bgp-af-evpn] peer 13.1.1.1 enable
    ```
    ```
    [*PE1-bgp-af-evpn] peer 13.1.1.1 advertise irb
    ```
    ```
    [*PE1-bgp-af-evpn] quit
    ```
    ```
    [*PE1] commit
    ```
    
    # Configure PE2.
    
    ```
    [~PE2] bgp 100
    ```
    ```
    [*PE2-bgp] l2vpn-family evpn
    ```
    ```
    [*PE2-bgp-af-evpn] peer 11.1.1.1 enable
    ```
    ```
    [*PE2-bgp-af-evpn] peer 11.1.1.1 advertise irb
    ```
    ```
    [*PE2-bgp-af-evpn] peer 12.1.1.1 enable
    ```
    ```
    [*PE2-bgp-af-evpn] peer 12.1.1.1 advertise irb
    ```
    ```
    [*PE2-bgp-af-evpn] quit
    ```
    ```
    [*PE2] commit
    ```
    
    # Configure PE3.
    
    ```
    [~PE3] bgp 100
    ```
    ```
    [*PE3-bgp] l2vpn-family evpn
    ```
    ```
    [*PE3-bgp-af-evpn] peer 12.1.1.1 enable
    ```
    ```
    [*PE3-bgp-af-evpn] peer 12.1.1.1 advertise irb
    ```
    ```
    [*PE3-bgp-af-evpn] peer 13.1.1.1 enable
    ```
    ```
    [*PE3-bgp-af-evpn] peer 13.1.1.1 advertise irb
    ```
    ```
    [*PE3-bgp-af-evpn] quit
    ```
    ```
    [*PE3] commit
    ```
12. Enable EVPN to generate and advertise IP prefix routes and IRB routes in a VPN instance.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] ip vpn-instance vpna
    ```
    ```
    [~PE1-vpn-instance-vpna] ipv4-family
    ```
    ```
    [~PE1-vpn-instance-vpna-af-ipv4] evpn mpls routing-enable
    ```
    ```
    [*PE1-vpn-instance-vpna-af-ipv4] quit
    ```
    ```
    [*PE1] commit
    ```
    
    # Configure PE2.
    
    ```
    [~PE2] ip vpn-instance vpna
    ```
    ```
    [~PE2-vpn-instance-vpna] ipv4-family
    ```
    ```
    [~PE2-vpn-instance-vpna-af-ipv4] evpn mpls routing-enable
    ```
    ```
    [*PE2-vpn-instance-vpna-af-ipv4] quit
    ```
    ```
    [*PE2] commit
    ```
    
    # Configure PE3.
    
    ```
    [~PE3] ip vpn-instance vpna
    ```
    ```
    [~PE3-vpn-instance-vpna] ipv4-family
    ```
    ```
    [~PE3-vpn-instance-vpna-af-ipv4] evpn mpls routing-enable
    ```
    ```
    [*PE3-vpn-instance-vpna-af-ipv4] quit
    ```
    ```
    [*PE3] commit
    ```
13. Enable the VPN instance to advertise IP routes to the EVPN instance on each PE.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] bgp 100
    ```
    ```
    [*PE1-bgp] ipv4-family vpn-instance vpna
    ```
    ```
    [*PE1-bgp-vpna] import-route direct
    ```
    ```
    [*PE1-bgp-vpna] advertise l2vpn evpn
    ```
    ```
    [*PE1-bgp-vpna] quit
    ```
    ```
    [*PE1] commit
    ```
    
    # Configure PE2.
    
    ```
    [~PE2] bgp 100
    ```
    ```
    [*PE2-bgp] ipv4-family vpn-instance vpna
    ```
    ```
    [*PE2-bgp-vpna] import-route direct
    ```
    ```
    [*PE2-bgp-vpna] advertise l2vpn evpn
    ```
    ```
    [*PE2-bgp-vpna] quit
    ```
    ```
    [*PE2] commit
    ```
    
    # Configure PE3.
    
    ```
    [~PE3] bgp 100
    ```
    ```
    [*PE3-bgp] ipv4-family vpn-instance vpna
    ```
    ```
    [*PE3-bgp-vpna] import-route direct
    ```
    ```
    [*PE3-bgp-vpna] advertise l2vpn evpn
    ```
    ```
    [*PE3-bgp-vpna] quit
    ```
    ```
    [*PE3] commit
    ```
14. Establish a BGP EVPN peer relationship between the PEs.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] bgp 100
    ```
    ```
    [*PE1-bgp] peer 11.1.1.1 as-number 100
    ```
    ```
    [*PE1-bgp] peer 11.1.1.1 connect-interface loopback 1
    ```
    ```
    [*PE1-bgp] peer 13.1.1.1 as-number 100
    ```
    ```
    [*PE1-bgp] peer 13.1.1.1 connect-interface loopback 1
    ```
    ```
    [*PE1-bgp] peer 192.168.1.1 as-number 100
    ```
    ```
    [*PE1-bgp] peer 192.168.2.2 as-number 100
    ```
    ```
    [*PE1-bgp] quit
    ```
    ```
    [*PE1] commit
    ```
    
    # Configure PE2.
    
    ```
    [~PE2] bgp 100
    ```
    ```
    [*PE2-bgp] peer 11.1.1.1 as-number 100
    ```
    ```
    [*PE2-bgp] peer 11.1.1.1 connect-interface loopback 1
    ```
    ```
    [*PE2-bgp] peer 12.1.1.1 as-number 100
    ```
    ```
    [*PE2-bgp] peer 12.1.1.1 connect-interface loopback 1
    ```
    ```
    [*PE2-bgp] peer 172.16.1.2 as-number 100
    ```
    ```
    [*PE2-bgp] peer 192.168.2.1 as-number 100
    ```
    ```
    [*PE2-bgp] quit
    ```
    ```
    [*PE2] commit
    ```
    
    # Configure PE3.
    
    ```
    [~PE3] bgp 100
    ```
    ```
    [*PE3-bgp] peer 12.1.1.1 as-number 100
    ```
    ```
    [*PE3-bgp] peer 12.1.1.1 connect-interface loopback 1
    ```
    ```
    [*PE3-bgp] peer 13.1.1.1 as-number 100
    ```
    ```
    [*PE3-bgp] peer 13.1.1.1 connect-interface loopback 1
    ```
    ```
    [*PE3-bgp] peer 192.168.1.2 as-number 100
    ```
    ```
    [*PE3-bgp] peer 172.16.1.1 as-number 100
    ```
    ```
    [*PE3-bgp] quit
    ```
    ```
    [*PE3] commit
    ```
15. Configure the CE, PE1, and PE2 to communicate.
    
    
    
    # Configure the CE.
    
    ```
    [~CE] vlan batch 100
    ```
    ```
    [*CE] interface Eth-Trunk1
    ```
    ```
    [*CE-Eth-Trunk20] portswitch
    ```
    ```
    [*CE-Eth-Trunk20] port link-type trunk
    ```
    ```
    [*CE-Eth-Trunk20] port trunk allow-pass vlan 100
    ```
    ```
    [*CE-Eth-Trunk20] quit
    ```
    ```
    [*CE] interface ethernet0/3/0
    ```
    ```
    [*CE-Ethernet0/3/0] portswitch
    ```
    ```
    [*CE-Ethernet0/3/0] port link-type trunk
    ```
    ```
    [*CE-Ethernet0/3/0] port trunk allow-pass vlan 100
    ```
    ```
    [*CE-Ethernet0/3/0] quit
    ```
    ```
    [*CE] commit
    ```
    
    # Configure PE1.
    
    ```
    [~PE1] vlan batch 100
    ```
    ```
    [*PE1] interface GigabitEthernet0/1/0
    ```
    ```
    [*PE1-GigabitEthernet0/1/0] eth-trunk 1
    ```
    ```
    [*PE1-GigabitEthernet0/1/0] quit
    ```
    ```
    [*PE1] commit
    ```
    
    
    
    # Configure PE2.
    
    ```
    [~PE2] vlan batch 100
    ```
    ```
    [*PE2] interface GigabitEthernet0/1/0
    ```
    ```
    [*PE2-GigabitEthernet0/1/0] eth-trunk 1
    ```
    ```
    [*PE2-GigabitEthernet0/1/0] quit
    ```
    ```
    [*PE2] commit
    ```
16. Configure DHCP relay on PE1 and PE2.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] interface Vbdif 1
    ```
    ```
    [*PE1-Vbdif1] ip binding vpn-instance vpna
    ```
    ```
    [*PE1-Vbdif1] ip address 10.1.1.1 255.255.255.0
    ```
    ```
    [*PE1-Vbdif1] arp broadcast-detect enable
    ```
    ```
    [*PE1-Vbdif1] arp expire-time 86400
    ```
    ```
    [*PE1-Vbdif1] dhcp select relay
    ```
    ```
    [*PE1-Vbdif1] ip relay address 30.1.1.2
    ```
    ```
    [*PE1-Vbdif1] ip relay giaddr 10.1.1.1
    ```
    ```
    [*PE1-Vbdif1] dhcp option82 vendor-specific insert enable
    ```
    ```
    [*PE1-Vbdif1] dhcp option82 vendor-specific format vendor-sub-option 1 source-ip-address 14.1.1.1
    ```
    ```
    [*PE1-Vbdif1] anycast-gateway enable
    ```
    ```
    [*PE1-Vbdif1] arp collect host enable
    ```
    ```
    [*PE1-Vbdif1] quit
    ```
    ```
    [*PE1] commit
    ```
    
    # Configure PE2.
    
    ```
    [~PE2] interface Vbdif 1
    ```
    ```
    [*PE2-Vbdif1] ip binding vpn-instance vpna
    ```
    ```
    [*PE2-Vbdif1] ip address 10.1.1.1 255.255.255.0
    ```
    ```
    [*PE2-Vbdif1] arp expire-time 86400
    ```
    ```
    [*PE2-Vbdif1] dhcp select relay
    ```
    ```
    [*PE2-Vbdif1] ip relay address 30.1.1.2
    ```
    ```
    [*PE2-Vbdif1] ip relay giaddr 10.1.1.1
    ```
    ```
    [*PE2-Vbdif1] dhcp option82 vendor-specific insert enable
    ```
    ```
    [*PE2-Vbdif1] dhcp option82 vendor-specific format vendor-sub-option 1 source-ip-address 15.1.1.1
    ```
    ```
    [*PE2-Vbdif1] anycast-gateway enable
    ```
    ```
    [*PE2-Vbdif1] arp collect host enable
    ```
    ```
    [*PE2-Vbdif1] quit
    ```
    ```
    [*PE2] commit
    ```
17. Verify the configuration.
    
    
    
    # Run the **display dhcp relay address** command on PE1 and PE2 to check the DHCP relay configuration on VBDIF 1. The following example uses the command output on PE1.
    
    ```
    [PE1] display dhcp relay address interface Vbdif 1  
        **  Vbdif1 DHCP Relay Address  ** 
     Dhcp Option          Relay Agent IP       Server IP             
     *                    10.1.1.1             30.1.1.2    
    ```
    
    
    
    The configuration succeeds if the DHCP client obtains an IP address from the DHCP server through the DHCP relay-enabled gateway and goes online successfully.

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  vlan batch 100
  #
  lacp e-trunk system-id 00e0-fc12-3456
  #
  evpn
   vlan-extend private enable
   vlan-extend redirect enable
   local-remote frr enable
   #
   mac-duplication
  #
  evpn vpn-instance evpna bd-mode
   route-distinguisher 1:1
   vpn-target 1:1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 export-extcommunity evpn
    vpn-target 100:1 import-extcommunity
    vpn-target 100:1 import-extcommunity evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 12.1.1.1
  #
  mpls
  #
  bridge-domain 1
   evpn binding vpn-instance evpna
  #
  mpls ldp
   #
   ipv4-family
  #
  e-trunk 1          
   priority 50
   peer-address 13.1.1.1 source-address 12.1.1.1
  #
  interface Vbdif1
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
   arp broadcast-detect enable
   arp expire-time 86400
   dhcp select relay
   ip relay address 30.1.1.2
   ip relay giaddr 10.1.1.1
   dhcp option82 vendor-specific insert enable
   dhcp option82 vendor-specific format vendor-sub-option 1 source-ip-address 14.1.1.1
   anycast-gateway enable
   arp collect host enable
  #
  interface Eth-Trunk1           
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.0000.0000.0000.1111
  #
  interface Eth-Trunk1.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 1
  #
  interface GigabitEthernet0/2/0                     
   ip address 192.168.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0                    
   ip address 192.168.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/0                     
   eth-trunk 1
  #
  interface LoopBack1
   ip address 12.1.1.1 255.255.255.255
  #
  interface LoopBack2
   ip binding vpn-instance vpna
   ip address 14.1.1.1 255.255.255.255
  #
  bgp 100
   peer 11.1.1.1 as-number 100
   peer 11.1.1.1 connect-interface LoopBack 1
   peer 13.1.1.1 as-number 100
   peer 13.1.1.1 connect-interface LoopBack 1
   peer 192.168.1.1 as-number 100
   peer 192.168.2.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 11.1.1.1 enable
    peer 13.1.1.1 enable
    peer 192.168.1.1 enable
    peer 192.168.2.2 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    policy vpn-target
    peer 11.1.1.1 enable
    peer 11.1.1.1 advertise irb
    peer 13.1.1.1 enable
    peer 13.1.1.1 advertise irb
  #
  ospf 1
   area 0.0.0.0
    network 12.1.1.1 0.0.0.0
    network 20.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  evpn source-address 12.1.1.1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  vlan batch 100
  #
  lacp e-trunk system-id 00e0-fc12-3456
  #
  evpn
   vlan-extend private enable
   vlan-extend redirect enable
   local-remote frr enable
   #
   mac-duplication
  #
  evpn vpn-instance evpna bd-mode
   route-distinguisher 1:1
   vpn-target 1:1
   #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 export-extcommunity evpn
    vpn-target 100:1 import-extcommunity
    vpn-target 100:1 import-extcommunity evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 13.1.1.1
  #
  mpls
  #
  bridge-domain 1
   evpn binding vpn-instance evpna
  #
  mpls ldp
   #
   ipv4-family
  #
  e-trunk 1       
   priority 10
   peer-address 12.1.1.1 source-address 13.1.1.1
  #
  interface Vbdif1
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
   arp expire-time 86400
   dhcp select relay
   ip relay address 30.1.1.2
   ip relay giaddr 10.1.1.1
   dhcp option82 vendor-specific insert enable
   dhcp option82 vendor-specific format vendor-sub-option 1 source-ip-address 15.1.1.1
   anycast-gateway enable
   arp collect host enable
  #
  interface Eth-Trunk1        
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0000.0000.0000.0000.1111
  #
  interface Eth-Trunk1.1 mode l2
   encapsulation dot1q vid 100
   rewrite pop single
   bridge-domain 1
  #
  interface GigabitEthernet0/2/0                     
   ip address 192.168.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0                     
   ip address 172.16.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/0                     
   eth-trunk 1
  #
  interface LoopBack1
   ip address 13.1.1.1 255.255.255.255
  #
  interface LoopBack2
   ip binding vpn-instance vpna
   ip address 15.1.1.1 255.255.255.255
  #
  bgp 100
   peer 11.1.1.1 as-number 100
   peer 11.1.1.1 connect-interface LoopBack 1
   peer 12.1.1.1 as-number 100
   peer 12.1.1.1 connect-interface LoopBack 1
   peer 172.16.1.2 as-number 100
   peer 192.168.2.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 11.1.1.1 enable
    peer 12.1.1.1 enable
    peer 172.16.1.2 enable
    peer 192.168.2.1 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    policy vpn-target
    peer 11.1.1.1 enable
    peer 11.1.1.1 advertise irb
    peer 12.1.1.1 enable
    peer 12.1.1.1 advertise irb
  #
  ospf 1
   area 0.0.0.0
    network 13.1.1.1 0.0.0.0
    network 20.1.1.1 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  evpn source-address 13.1.1.1
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  # 
  evpn
   vlan-extend private enable
   vlan-extend redirect enable
   local-remote frr enable
  #
  evpn vpn-instance evpna bd-mode
   route-distinguisher 1:1
   vpn-target 1:1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 export-extcommunity evpn
    vpn-target 100:1 import-extcommunity
    vpn-target 100:1 import-extcommunity evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 11.1.1.1
  #
  mpls
  #
  bridge-domain 1
   evpn binding vpn-instance evpna
  #
  mpls ldp
   #
   ipv4-family
  #
  interface GigabitEthernet0/2/0                    
   ip address 172.16.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0                     
   ip binding vpn-instance vpna
   ip address 30.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/0                   
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 11.1.1.1 255.255.255.255
  #
  bgp 100
   peer 12.1.1.1 as-number 100
   peer 12.1.1.1 connect-interface LoopBack 1
   peer 13.1.1.1 as-number 100
   peer 13.1.1.1 connect-interface LoopBack 1
   peer 192.168.1.2 as-number 100
   peer 172.16.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 12.1.1.1 enable
    peer 13.1.1.1 enable
    peer 192.168.1.2 enable
    peer 172.16.1.1 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    policy vpn-target
    peer 12.1.1.1 enable
    peer 12.1.1.1 advertise irb
    peer 13.1.1.1 enable
    peer 13.1.1.1 advertise irb
  #
  ospf 1
   area 0.0.0.0
    network 11.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 172.16.1.0 0.0.0.255
  #
  evpn source-address 11.1.1.1
  #
  return
  ```
* CE configuration file
  
  ```
  #
  sysname CE
  #
  vlan batch 100
  #
  interface Eth-Trunk1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100
   mode lacp-static
  #
  interface Ethernet0/3/0                   
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100
  #
  interface Ethernet0/1/0                  
   eth-trunk 1
  #
  interface Ethernet0/2/0                   
   eth-trunk 1
  #
  return
  ```