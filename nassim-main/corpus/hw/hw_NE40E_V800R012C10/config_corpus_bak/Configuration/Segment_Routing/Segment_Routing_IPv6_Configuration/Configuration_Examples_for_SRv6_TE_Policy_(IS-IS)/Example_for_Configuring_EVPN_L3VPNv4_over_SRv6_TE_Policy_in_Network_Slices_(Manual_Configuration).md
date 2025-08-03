Example for Configuring EVPN L3VPNv4 over SRv6 TE Policy in Network Slices (Manual Configuration)
=================================================================================================

This section provides an example for configuring EVPN L3VPNv4 over SRv6 TE Policy in network slices.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0317510809__fig3691666259), PE1, the P, and PE2 belong to the same AS and need to run IS-IS to implement IPv6 network connectivity. In addition, a bidirectional SRv6 TE Policy needs to be deployed between PE1 and PE2 to carry EVPN L3VPNv4 services. And to guarantee the SLAs of the VPN instance **vpn1** (between CE1 and CE2) and **vpn2** (between CE3 and CE4), two network slices (20 and 30) need to be created on the public network to respectively carry **vpn1**'s and **vpn2**'s services.

**Figure 1** Networking diagram for configuring EVPN L3VPNv4 over SRv6 TE Policy in network slices![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0317510810.png)

#### Precautions

1. SRv6 TE Policy configuration requires End or End.X SIDs. The SIDs can either be configured manually or be generated dynamically using an IGP. In scenarios where SRv6 TE Policies are configured manually, dynamic SIDs used for the SRv6 TE Policies may change after an IGP restart. In this case, you need to manually adjust the SRv6 TE Policies so that they remain up. For this reason, dynamic SIDs are not suitable for large-scale use. You are therefore advised to configure SIDs manually and not to use dynamic SIDs.
2. To implement color-based traffic steering into SRv6 TE Policies, you need to configure the color attribute using an import or export route-policy. You also need to configure a tunnel policy to allow routes to recurse to SRv6 TE Policies.
   
   After the preceding configurations are complete, if the color and next hop of a route are the same as the color and endpoint of an SRv6 TE Policy, respectively, the route can successfully recurse to the SRv6 TE Policy. This enables the traffic forwarded through the route to be steered into the SRv6 TE Policy.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for involved interfaces on PE1, the P, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on PE1, the P, and PE2.
3. Create network slice instances on PE1, the P, and PE2, specify base interfaces, and create network slice interfaces.
4. Configure an EVPN L3VPN instance on each PE and bind the EVPN L3VPN instance to an access-side interface.
5. Establish an EBGP peer relationship between each PE and its connected CE.
6. Establish a BGP EVPN peer relationship between the PEs.
7. Configure SRv6 SIDs and enable IS-IS SRv6 on PE1, the P, and PE2. In addition, configure PE1 and PE2 to advertise VPN routes carrying SIDs.
8. Configure an SRv6 TE Policy on PE1 and PE2 and specify slice IDs for the SRv6 TE Policy's candidate paths.
9. Configure a tunnel policy on PE1 and PE2 to import VPN traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 addresses of interfaces on PE1, the P, and PE2
* IS-IS process ID of PE1, the P, and PE2
* IS-IS level of PE1, the P, and PE2
* VPN instance names, RDs, and RTs on PE1 and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each involved interface.
   
   
   
   # Configure PE1. The configurations of the P and PE2 are similar to the configuration of PE1. For configuration details, see Configuration Files.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 64
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
2. Configure IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-1
   ```
   ```
   [*PE1-isis-1] cost-style wide
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*PE1-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface loopback1
   ```
   ```
   [*PE1-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] isis 1 
   ```
   ```
   [*P-isis-1] is-level level-1
   ```
   ```
   [*P-isis-1] cost-style wide
   ```
   ```
   [*P-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*P-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P-isis-1] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] interface loopback1
   ```
   ```
   [*P-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*P-LoopBack1] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-1
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*PE2-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface loopback1
   ```
   ```
   [*PE2-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured.
   
   # Display IS-IS neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
                            
     System Id     Interface         Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002* GE0/1/0           0000.0000.0002.01  Up   8s       L1       64 
   
   Total Peer(s): 1
   ```
3. Create network slice instances on PE1, the P, and PE2, specify base interfaces, and create network slice interfaces.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] network-slice instance 10
   ```
   ```
   [*PE1-network-slice-instance-10] description Basic
   ```
   ```
   [*PE1-network-slice-instance-10] quit
   ```
   ```
   [*PE1] network-slice instance 20
   ```
   ```
   [*PE1-network-slice-instance-20] description vpn1
   ```
   ```
   [*PE1-network-slice-instance-20] quit
   ```
   ```
   [*PE1] network-slice instance 30
   ```
   ```
   [*PE1-network-slice-instance-30] description vpn2
   ```
   ```
   [*PE1-network-slice-instance-30] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] network-slice 10 data-plane
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 11
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] ipv6 address auto link-local
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] mode channel enable 
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] mode channel bandwidth 500 
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] basic-slice 10 
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] network-slice 20 data-plane 
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0.2
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] vlan-type dot1q 22
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] ipv6 address auto link-local
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] mode channel enable 
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] mode channel bandwidth 500 
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] basic-slice 10 
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] network-slice 30 data-plane 
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] network-slice instance 10
   ```
   ```
   [*P-network-slice-instance-10] description Basic
   ```
   ```
   [*P-network-slice-instance-10] quit
   ```
   ```
   [*P] network-slice instance 20
   ```
   ```
   [*P-network-slice-instance-20] description vpn1
   ```
   ```
   [*P-network-slice-instance-20] quit
   ```
   ```
   [*P] network-slice instance 30
   ```
   ```
   [*P-network-slice-instance-30] description vpn2
   ```
   ```
   [*P-network-slice-instance-30] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] network-slice 10 data-plane
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*P-GigabitEthernet0/1/0.1] vlan-type dot1q 11
   ```
   ```
   [*P-GigabitEthernet0/1/0.1] ipv6 enable
   ```
   ```
   [*P-GigabitEthernet0/1/0.1] ipv6 address auto link-local
   ```
   ```
   [*P-GigabitEthernet0/1/0.1] mode channel enable 
   ```
   ```
   [*P-GigabitEthernet0/1/0.1] mode channel bandwidth 500 
   ```
   ```
   [*P-GigabitEthernet0/1/0.1] basic-slice 10 
   ```
   ```
   [*P-GigabitEthernet0/1/0.1] network-slice 20 data-plane 
   ```
   ```
   [*P-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0.2
   ```
   ```
   [*P-GigabitEthernet0/1/0.2] vlan-type dot1q 22
   ```
   ```
   [*P-GigabitEthernet0/1/0.2] ipv6 enable
   ```
   ```
   [*P-GigabitEthernet0/1/0.2] ipv6 address auto link-local
   ```
   ```
   [*P-GigabitEthernet0/1/0.2] mode channel enable 
   ```
   ```
   [*P-GigabitEthernet0/1/0.2] mode channel bandwidth 500 
   ```
   ```
   [*P-GigabitEthernet0/1/0.2] basic-slice 10 
   ```
   ```
   [*P-GigabitEthernet0/1/0.2] network-slice 30 data-plane 
   ```
   ```
   [*P-GigabitEthernet0/1/0.2] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] network-slice 10 data-plane
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*P-GigabitEthernet0/2/0.1] vlan-type dot1q 11
   ```
   ```
   [*P-GigabitEthernet0/2/0.1] ipv6 enable
   ```
   ```
   [*P-GigabitEthernet0/2/0.1] ipv6 address auto link-local
   ```
   ```
   [*P-GigabitEthernet0/2/0.1] mode channel enable 
   ```
   ```
   [*P-GigabitEthernet0/2/0.1] mode channel bandwidth 500 
   ```
   ```
   [*P-GigabitEthernet0/2/0.1] basic-slice 10 
   ```
   ```
   [*P-GigabitEthernet0/2/0.1] network-slice 20 data-plane 
   ```
   ```
   [*P-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0.2
   ```
   ```
   [*P-GigabitEthernet0/2/0.2] vlan-type dot1q 22
   ```
   ```
   [*P-GigabitEthernet0/2/0.2] ipv6 enable
   ```
   ```
   [*P-GigabitEthernet0/2/0.2] ipv6 address auto link-local
   ```
   ```
   [*P-GigabitEthernet0/2/0.1] mode channel enable 
   ```
   ```
   [*P-GigabitEthernet0/2/0.1] mode channel bandwidth 500 
   ```
   ```
   [*P-GigabitEthernet0/2/0.2] basic-slice 10 
   ```
   ```
   [*P-GigabitEthernet0/2/0.2] network-slice 30 data-plane 
   ```
   ```
   [*P-GigabitEthernet0/2/0.2] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] network-slice instance 10
   ```
   ```
   [*PE2-network-slice-instance-10] description Basic
   ```
   ```
   [*PE2-network-slice-instance-10] quit
   ```
   ```
   [*PE2] network-slice instance 20
   ```
   ```
   [*PE2-network-slice-instance-20] description vpn1
   ```
   ```
   [*PE2-network-slice-instance-20] quit
   ```
   ```
   [*PE2] network-slice instance 30
   ```
   ```
   [*PE2-network-slice-instance-30] description vpn2
   ```
   ```
   [*PE2-network-slice-instance-30] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] network-slice 10 data-plane
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] vlan-type dot1q 11
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] ipv6 enable
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] ipv6 address auto link-local
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] mode channel enable 
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] mode channel bandwidth 500
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] basic-slice 10 
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] network-slice 20 data-plane 
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0.2
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.2] vlan-type dot1q 22
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.2] ipv6 enable
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.2] ipv6 address auto link-local
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.2] mode channel enable 
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.2] mode channel bandwidth 500
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.2] basic-slice 10 
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.2] network-slice 30 data-plane 
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.2] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, perform the following operations to check the bindings between the base and slice interfaces in slice instances. The following example uses the command output on PE1.
   
   ```
   [~PE1] display network-slice 10 binding-list 
           Slice-ID            Basic-Interface          Slicing-Interface 
           10                  GigabitEthernet0/1/0     GigabitEthernet0/1/0.1
                                                        GigabitEthernet0/1/0.2
   ```
4. Configure an EVPN L3VPN instance on each PE and bind the EVPN L3VPN instance to an access-side interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 evpn
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.11.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] ip vpn-instance vpn2
   ```
   ```
   [*PE1-vpn-instance-vpn2] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn2-af-ipv4] route-distinguisher 100:2
   ```
   ```
   [*PE1-vpn-instance-vpn2-af-ipv4] vpn-target 2:2 evpn
   ```
   ```
   [*PE1-vpn-instance-vpn2-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpn2] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] ip binding vpn-instance vpn2
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] ip address 10.33.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpn1
   ```
   ```
   [*PE2-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 evpn
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.22.1.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] ip vpn-instance vpn2
   ```
   ```
   [*PE2-vpn-instance-vpn2] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpn2-af-ipv4] route-distinguisher 200:2
   ```
   ```
   [*PE2-vpn-instance-vpn2-af-ipv4] vpn-target 2:2 evpn
   ```
   ```
   [*PE2-vpn-instance-vpn2-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpn2] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] ip binding vpn-instance vpn2
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] ip address 10.44.1.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] commit
   ```
5. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-LoopBack1] ip address 11.1.1.1 32
   ```
   ```
   [*CE1-LoopBack1] quit
   ```
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] router-id 11.1.1.1
   ```
   ```
   [*CE1-bgp] peer 10.11.1.1 as-number 100
   ```
   ```
   [*CE1-bgp] import-route direct
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE3.
   
   ```
   [~CE3] interface loopback 1
   ```
   ```
   [*CE3-LoopBack1] ip address 33.3.3.3 32
   ```
   ```
   [*CE3-LoopBack1] quit
   ```
   ```
   [*CE3] bgp 65430
   ```
   ```
   [*CE3-bgp] router-id 33.3.3.3
   ```
   ```
   [*CE3-bgp] peer 10.33.1.1 as-number 100
   ```
   ```
   [*CE3-bgp] import-route direct
   ```
   ```
   [*CE3-bgp] quit
   ```
   ```
   [*CE3] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-vpn1] peer 10.11.1.2 as-number 65410
   ```
   ```
   [*PE1-bgp-vpn1] import-route direct
   ```
   ```
   [*PE1-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*PE1-bgp-vpn1] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpn2
   ```
   ```
   [*PE1-bgp-vpn2] peer 10.33.1.2 as-number 65430
   ```
   ```
   [*PE1-bgp-vpn2] import-route direct
   ```
   ```
   [*PE1-bgp-vpn2] advertise l2vpn evpn
   ```
   ```
   [*PE1-bgp-vpn2] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface loopback 1
   ```
   ```
   [*CE2-LoopBack1] ip address 22.2.2.2 32
   ```
   ```
   [*CE2-LoopBack1] quit
   ```
   ```
   [*CE2] bgp 65420
   ```
   ```
   [*CE2-bgp] router-id 22.2.2.2
   ```
   ```
   [*CE2-bgp] peer 10.22.1.1 as-number 100
   ```
   ```
   [*CE2-bgp] import-route direct
   ```
   ```
   [*CE2-bgp] quit
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure CE4.
   
   ```
   [~CE4] interface loopback 1
   ```
   ```
   [*CE4-LoopBack1] ip address 44.4.4.4 32
   ```
   ```
   [*CE4-LoopBack1] quit
   ```
   ```
   [*CE4] bgp 65440
   ```
   ```
   [*CE4-bgp] router-id 44.4.4.4
   ```
   ```
   [*CE4-bgp] peer 10.44.1.1 as-number 100
   ```
   ```
   [*CE4-bgp] import-route direct
   ```
   ```
   [*CE4-bgp] quit
   ```
   ```
   [*CE4] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [~PE2-bgp] router-id 3.3.3.3
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE2-bgp-vpn1] peer 10.22.1.2 as-number 65420
   ```
   ```
   [*PE2-bgp-vpn1] import-route direct
   ```
   ```
   [*PE2-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*PE2-bgp-vpn1] quit
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpn2
   ```
   ```
   [*PE2-bgp-vpn2] peer 10.44.1.2 as-number 65440
   ```
   ```
   [*PE2-bgp-vpn2] import-route direct
   ```
   ```
   [*PE2-bgp-vpn2] advertise l2vpn evpn
   ```
   ```
   [*PE2-bgp-vpn2] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 vpn-instance peer** command on each PE to check whether a BGP peer relationship has been established between the PE and its connected CE. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv4 vpn-instance vpn1 peer
   
    BGP local router ID : 1.1.1.1                               
    Local AS number : 100                             
   
    VPN-Instance vpn1, Router ID 1.1.1.1:                       
    Total number of peers : 1                 Peers in established state : 1                   
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv 
     10.11.1.2                        4       65410       16       19     0 00:10:44 Established        2 
   ```
6. Establish a BGP EVPN peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 enable
   ```
   ```
   [*PE1-bgp-af-evpn] quit
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
   [~PE2-bgp] peer 2001:DB8:1::1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 enable
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs to check whether a BGP EVPN peer relationship has been established between the PEs. If the **Established** state is displayed in the command output, the BGP EVPN peer relationship has been established successfully.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:3::3                    4         100       49       49     0 00:30:41 Established        2
   ```
7. Configure SRv6 SIDs and configure the PEs to advertise VPN routes carrying SIDs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] opcode ::10 end psp
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE1-segment-routing-ipv6] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-vpn1] segment-routing ipv6 traffic-engineer best-effort evpn
   ```
   ```
   [*PE1-bgp-vpn1] segment-routing ipv6 locator PE1 evpn
   ```
   ```
   [*PE1-bgp-vpn1] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpn2
   ```
   ```
   [*PE1-bgp-vpn2] segment-routing ipv6 traffic-engineer best-effort evpn
   ```
   ```
   [*PE1-bgp-vpn2] segment-routing ipv6 locator PE1 evpn
   ```
   ```
   [*PE1-bgp-vpn2] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] isis 1
   ```
   ```
   [*PE1-isis-1] segment-routing ipv6 locator PE1 auto-sid-disable
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] segment-routing ipv6
   ```
   ```
   [*P-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   ```
   ```
   [*P-segment-routing-ipv6] locator P ipv6-prefix 2001:DB8:120:: 64 static 32
   ```
   ```
   [*P-segment-routing-ipv6-locator] opcode ::20 end psp
   ```
   ```
   [*P-segment-routing-ipv6-locator] quit
   ```
   ```
   [*P-segment-routing-ipv6] quit
   ```
   ```
   [*P] isis 1
   ```
   ```
   [*P-isis-1] segment-routing ipv6 locator P auto-sid-disable
   ```
   ```
   [*P-isis-1] commit
   ```
   ```
   [~P-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   ```
   ```
   [*PE2-segment-routing-ipv6] locator PE2 ipv6-prefix 2001:DB8:130:: 64 static 32
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] opcode ::30 end psp
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE2-segment-routing-ipv6] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE2-bgp-vpn1] segment-routing ipv6 traffic-engineer best-effort evpn
   ```
   ```
   [*PE2-bgp-vpn1] segment-routing ipv6 locator PE2 evpn
   ```
   ```
   [*PE2-bgp-vpn1] quit
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpn2
   ```
   ```
   [*PE2-bgp-vpn2] segment-routing ipv6 traffic-engineer best-effort evpn
   ```
   ```
   [*PE2-bgp-vpn2] segment-routing ipv6 locator PE2 evpn
   ```
   ```
   [*PE2-bgp-vpn2] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] isis 1
   ```
   ```
   [*PE2-isis-1] segment-routing ipv6 locator PE2 auto-sid-disable
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end** **forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:100::10/128                         FuncType    : End
   Flavor      : PSP                                          SidCompress : NO
   LocatorName : PE1                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2021-08-30 01:46:05.713
   
   Total SID(s): 1
   ```
   ```
   [~PE2] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:130::30/128                         FuncType    : End
   Flavor      : PSP                                          SidCompress : NO
   LocatorName : PE2                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2021-08-30 01:47:26.426
   
   Total SID(s): 1
   ```
   ```
   [~P] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:120::20/128                         FuncType    : End
   Flavor      : PSP                                          SidCompress : NO
   LocatorName : P                                            LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2021-08-30 01:49:44.292
   
   Total SID(s): 1
   ```
8. Configure an SRv6 TE Policy and specify a slice ID for the SRv6 TE Policy's candidate path.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [~PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:120::20
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:130::30
   [*PE1-segment-routing-ipv6-segment-list-list1] commit
   [~PE1-segment-routing-ipv6-segment-list-list1] quit
   [~PE1-segment-routing-ipv6] srv6-te-policy locator PE1 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
   [*PE1-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy1-path] network-slice 20 data-plane 
   [*PE1-segment-routing-ipv6-policy-policy1-path] segment-list list1
   [*PE1-segment-routing-ipv6-policy-policy1-path] quit
   [*PE1-segment-routing-ipv6-policy-policy1] quit
   [*PE1-segment-routing-ipv6] srv6-te policy policy2 endpoint 2001:DB8:3::3 color 202
   [*PE1-segment-routing-ipv6-policy-policy2] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy2-path] network-slice 30 data-plane 
   [*PE1-segment-routing-ipv6-policy-policy2-path] segment-list list1
   [*PE1-segment-routing-ipv6-policy-policy2-path] quit
   [*PE1-segment-routing-ipv6-policy-policy2] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6 
   [~PE2-segment-routing-ipv6] segment-list list1 
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:120::20
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:100::10
   [*PE2-segment-routing-ipv6-segment-list-list1] commit
   [~PE2-segment-routing-ipv6-segment-list-list1] quit
   [~PE2-segment-routing-ipv6] srv6-te-policy locator PE2 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
   [*PE2-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy1-path] network-slice 20 data-plane 
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE2-segment-routing-ipv6-policy-policy1-path] quit
   [*PE2-segment-routing-ipv6-policy-policy1] quit
   [*PE2-segment-routing-ipv6] srv6-te policy policy2 endpoint 2001:DB8:1::1 color 202
   [*PE2-segment-routing-ipv6-policy-policy2] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy2-path] network-slice 30 data-plane 
   [*PE2-segment-routing-ipv6-policy-policy2-path] segment-list list1 
   [*PE2-segment-routing-ipv6-policy-policy2-path] quit
   [*PE2-segment-routing-ipv6-policy-policy2] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] commit
   ```
   
   After the configuration is complete, run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display srv6-te policy
   PolicyName : policy1             
   Color                   : 101                            Endpoint             : 2001:DB8:3::3 
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -  
   Policy State            : Up                             State Change Time    : 2021-02-05 07:04:45
   Admin State             : Up                             Traffic Statistics   : Disable  
   Backup Hot-Standby      : Disable                        BFD                  : Disable 
   Interface Index         : -                              Interface Name       : - 
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : -
   Candidate-path Count    : 1 
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary  
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0   
    Discriminator          : 100                            Binding SID          : - 
    GroupId                : 1                              Policy Name          : policy1
    Template ID            : 0                              Path Verification    : Disable  
    DelayTimerRemain       : -                              Network Slice ID     : 20 (data-plane) 
    Segment-List Count     : 1         
     Segment-List          : list1                       
      Segment-List ID      : 2                              XcIndex              : 2  
      List State           : Up                             DelayTimerRemain     : -   
      Verification State   : -                              SuppressTimeRemain   : -  
      PMTU                 : 9600                           Active PMTU          : 9600 
      Weight               : 1                              BFD State            : -   
      Loop Detection State : Up                             BFD Delay Remain     : - 
      Network Slice ID     : 20 (data-plane)   
      Binding SID          : -
      Reverse Binding ID   : -
      SID :                              
            2001:DB8:120::20
            2001:DB8:130::30
   
   PolicyName : policy2                                                        
   Color                   : 202                            Endpoint             : 2001:DB8:3::3                    
   TunnelId                : 2                                                       
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -                          
   Policy State            : Up                             State Change Time    : 2021-02-07 04:01:24                  
   Admin State             : Up                             Traffic Statistics   : Disable                       
   Backup Hot-Standby      : Disable                        BFD                  : Disable  
   Interface Index         : -                              Interface Name       : - 
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : -
   Candidate-path Count    : 1                                                 
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary                          
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0                    
    Discriminator          : 100                            Binding SID          : -                        
    GroupId                : 2                              Policy Name          : policy2
    Template ID            : 0                              Path Verification    : Disable                    
    DelayTimerRemain       : -                              Network Slice ID     : 30 (data-plane)  
    Segment-List Count     : 1                                                                      
     Segment-List          : list1                                                     
      Segment-List ID      : 129                            XcIndex              : 129                        
      List State           : Up                             DelayTimerRemain     : -                        
      Verification State   : -                              SuppressTimeRemain   : -                       
      PMTU                 : 9600                           Active PMTU          : 9600 
      Weight               : 1                              BFD State            : -    
      Loop Detection State : Up                             BFD Delay Remain     : -                 
      Network Slice ID     : 30 (data-plane)   
      Binding SID          : -
      Reverse Binding ID   : -
      SID :                                                                     
            2001:DB8:120::20
            2001:DB8:130::30
   ```
9. Configure a tunnel policy to import VPN traffic.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip ip-prefix p2 index 10 permit 22.2.2.2 32
   [*PE1] ip ip-prefix p2 index 20 permit 10.22.1.0 24
   [*PE1] ip ip-prefix p4 index 10 permit 44.4.4.4 32
   [*PE1] ip ip-prefix p4 index 20 permit 10.44.1.0 24
   [*PE1] route-policy rp1234 permit node 10
   [*PE1-route-policy] if-match ip-prefix p2
   [*PE1-route-policy] apply extcommunity color 0:101
   [*PE1-route-policy] quit
   [*PE1] route-policy rp1234 permit node 20
   [*PE1-route-policy] if-match ip-prefix p4
   [*PE1-route-policy] apply extcommunity color 0:202
   [*PE1-route-policy] quit
   [*PE1] bgp 100
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 route-policy rp1234 import 
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] quit
   [*PE1] tunnel-policy tp1234
   [*PE1-tunnel-policy-tp1234] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE1-tunnel-policy-tp1234] quit
   [*PE1] ip vpn-instance vpn1
   [*PE1-vpn-instance-vpn1] ipv4-family
   [*PE1-vpn-instance-vpn1-af-ipv4] tnl-policy tp1234 evpn
   [*PE1-vpn-instance-vpn1-af-ipv4] quit
   [*PE1-vpn-instance-vpn1] quit
   [*PE1] ip vpn-instance vpn2
   [*PE1-vpn-instance-vpn2] ipv4-family
   [*PE1-vpn-instance-vpn2-af-ipv4] tnl-policy tp1234 evpn
   [*PE1-vpn-instance-vpn2-af-ipv4] quit
   [*PE1-vpn-instance-vpn2] quit
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] ip ip-prefix p1 index 10 permit 11.1.1.1 32
   [*PE2] ip ip-prefix p1 index 20 permit 10.11.1.0 24
   [*PE2] ip ip-prefix p3 index 10 permit 33.3.3.3 32
   [*PE2] ip ip-prefix p3 index 20 permit 10.33.1.0 24
   [*PE2] route-policy rp1234 permit node 10
   [*PE2-route-policy] if-match ip-prefix p1
   [*PE2-route-policy] apply extcommunity color 0:101
   [*PE2-route-policy] quit
   [*PE2] route-policy rp1234 permit node 20
   [*PE2-route-policy] if-match ip-prefix p3
   [*PE2-route-policy] apply extcommunity color 0:202
   [*PE2-route-policy] quit
   [*PE2] bgp 100
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 route-policy rp1234 import 
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] quit
   [*PE2] tunnel-policy tp1234
   [*PE2-tunnel-policy-tp1234] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE2-tunnel-policy-tp1234] quit
   [*PE2] ip vpn-instance vpn1
   [*PE2-vpn-instance-vpn1] ipv4-family
   [*PE2-vpn-instance-vpn1-af-ipv4] tnl-policy tp1234 evpn
   [*PE2-vpn-instance-vpn1-af-ipv4] quit
   [*PE2-vpn-instance-vpn1] quit
   [*PE2] ip vpn-instance vpn2
   [*PE2-vpn-instance-vpn2] ipv4-family
   [*PE2-vpn-instance-vpn2-af-ipv4] tnl-policy tp1234 evpn
   [*PE2-vpn-instance-vpn2-af-ipv4] quit
   [*PE2-vpn-instance-vpn2] quit
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display ip routing-table vpn-instance vpn1** command to check the IPv4 routing table of the VPN instance. The command output shows that the VPN route has successfully recursed to the SRv6 TE Policy.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpn1
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route                 
   ------------------------------------------------------------------------------  
   Routing Table : vpn1        
            Destinations : 8        Routes : 8                                     
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface    
   
         10.11.1.0/24  Direct  0    0             D   10.11.1.1       GigabitEthernet0/2/0
         10.11.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
       10.11.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
         10.22.1.0/24  IBGP    255  0             RD  2001:DB8:3::3   policy1 
          11.1.1.1/32  EBGP    255  0             RD  10.11.1.2       GigabitEthernet0/2/0
          22.2.2.2/32  IBGP    255  0             RD  2001:DB8:3::3   policy1  
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0  
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0  
   ```
   ```
   [~PE1] display ip routing-table vpn-instance vpn1 22.2.2.2 verbose 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route 
   ------------------------------------------------------------------------------  
   Routing Table : vpn1        
   Summary Count : 1           
   
   Destination: 22.2.2.2/32    
        Protocol: IBGP               Process ID: 0                                 
      Preference: 255                      Cost: 0                                 
         NextHop: 2001:DB8:3::3       Neighbour: 2001:DB8:3::3                     
           State: Active Adv Relied         Age: 01h41m01s                          
             Tag: 0                    Priority: low                               
           Label: NULL                  QoSInfo: 0x0                               
      IndirectID: 0x10000DF            Instance:                                   
    RelayNextHop: ::                  Interface: policy1                    
        TunnelID: 0x000000003400000001    Flags: RD 
      RouteColor: 0 
   ```
10. Verify the configuration.
    
    
    
    Check that CEs belonging to the same VPN instance can ping each other. For example:
    
    ```
    [~CE1] ping -a 11.1.1.1 22.2.2.2                                                 
      PING 22.2.2.2: 56  data bytes, press CTRL_C to break                          
        Reply from 22.2.2.2: bytes=56 Sequence=1 ttl=253 time=7 ms                       
        Reply from 22.2.2.2: bytes=56 Sequence=2 ttl=253 time=4 ms                     
        Reply from 22.2.2.2: bytes=56 Sequence=3 ttl=253 time=3 ms                       
        Reply from 22.2.2.2: bytes=56 Sequence=4 ttl=253 time=4 ms                    
        Reply from 22.2.2.2: bytes=56 Sequence=5 ttl=253 time=3 ms                    
    
      --- 22.2.2.2 ping statistics ---                                        
        5 packet(s) transmitted                                                 
        5 packet(s) received                                                  
        0.00% packet loss                                            
        round-trip min/avg/max = 3/4/7 ms
    ```
    ```
    [~CE3] ping -a 33.3.3.3 44.4.4.4                                                 
      PING 44.4.4.4: 56  data bytes, press CTRL_C to break                          
        Reply from 44.4.4.4: bytes=56 Sequence=1 ttl=253 time=9 ms                       
        Reply from 44.4.4.4: bytes=56 Sequence=2 ttl=253 time=5 ms                     
        Reply from 44.4.4.4: bytes=56 Sequence=3 ttl=253 time=4 ms                       
        Reply from 44.4.4.4: bytes=56 Sequence=4 ttl=253 time=5 ms                    
        Reply from 44.4.4.4: bytes=56 Sequence=5 ttl=253 time=4 ms                    
    
      --- 44.4.4.4 ping statistics ---                                        
        5 packet(s) transmitted                                                 
        5 packet(s) received                                                  
        0.00% packet loss                                            
        round-trip min/avg/max = 4/5/9 ms
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy tp1234 evpn
  #
  ip vpn-instance vpn2
   ipv4-family
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity evpn
    tnl-policy tp1234 evpn      
  # 
  network-slice instance 10
   description Basic                                         
  #                                                    
  network-slice instance 20
   description vpn1 
  #                                                    
  network-slice instance 30
   description vpn2
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
    opcode ::10 end psp
   srv6-te-policy locator PE1
   segment-list list1
    index 5 sid ipv6 2001:DB8:120::20
    index 10 sid ipv6 2001:DB8:130::30
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
    candidate-path preference 100
     network-slice 20 data-plane
     segment-list list1 
   srv6-te policy policy2 endpoint 2001:DB8:3::3 color 202
    candidate-path preference 100
     network-slice 30 data-plane
     segment-list list1
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::1/64
   isis ipv6 enable 1 
   network-slice 10 data-plane
  #               
  interface GigabitEthernet0/1/0.1 
   vlan-type dot1q 11
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 20 data-plane
  #               
  interface GigabitEthernet0/1/0.2 
   vlan-type dot1q 22
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 30 data-plane
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpn1
   ip address 10.11.1.1 255.255.255.0
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip binding vpn-instance vpn2
   ip address 10.33.1.1 255.255.255.0
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE1 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 10.11.1.2 as-number 65410
   #              
   ipv4-family vpn-instance vpn2
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE1 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 10.33.1.2 as-number 65430
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 route-policy rp1234 import
    peer 2001:DB8:3::3 advertise encap-type srv6
  #     
  ip ip-prefix p2 index 10 permit 22.2.2.2 32  
  ip ip-prefix p2 index 20 permit 10.22.1.0 24                                 
  ip ip-prefix p4 index 10 permit 44.4.4.4 32
  ip ip-prefix p4 index 20 permit 10.44.1.0 24
  #
  route-policy rp1234 permit node 10                                                 
   if-match ip-prefix p2                                                   
   apply extcommunity color 0:101                                          
  #                                                
  route-policy rp1234 permit node 20                                       
   if-match ip-prefix p4                                      
   apply extcommunity color 0:202                                       
  #                                           
  tunnel-policy tp1234
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #               
  return 
  ```
* P configuration file
  
  ```
  #
  sysname P
  # 
  network-slice instance 10
   description Basic 
  #                                                    
  network-slice instance 20
   description vpn1
  #                                                    
  network-slice instance 30
   description vpn2
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator P ipv6-prefix 2001:DB8:120:: 64 static 32
    opcode ::20 end psp
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator P auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::2/64
   isis ipv6 enable 1
   network-slice 10 data-plane
  #               
  interface GigabitEthernet0/1/0.1 
   vlan-type dot1q 11
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 20 data-plane
  #               
  interface GigabitEthernet0/1/0.2 
   vlan-type dot1q 22
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 30 data-plane
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::1/64
   isis ipv6 enable 1
   network-slice 10 data-plane
  #               
  interface GigabitEthernet0/2/0.1
   vlan-type dot1q 11 
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 20 data-plane
  #               
  interface GigabitEthernet0/2/0.2 
   vlan-type dot1q 22
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 30 data-plane
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #               
  return 
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy tp1234 evpn
  #
  ip vpn-instance vpn2
   ipv4-family
    route-distinguisher 200:2
    apply-label per-instance
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity evpn
    tnl-policy tp1234 evpn        
  # 
  network-slice instance 10
   description Basic 
  #                                                    
  network-slice instance 20
   description vpn1
  #                                                    
  network-slice instance 30
   description vpn2
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator PE2 ipv6-prefix 2001:DB8:130:: 64 static 32
    opcode ::30 end psp
   srv6-te-policy locator PE2
   segment-list list1
    index 5 sid ipv6 2001:DB8:120::20
    index 10 sid ipv6 2001:DB8:100::10
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
    candidate-path preference 100
     network-slice 20 data-plane
     segment-list list1 
   srv6-te policy policy2 endpoint 2001:DB8:1::1 color 202
    candidate-path preference 100
     network-slice 30 data-plane
     segment-list list1 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1 
   network-slice 10 data-plane
  #               
  interface GigabitEthernet0/1/0.1 
   vlan-type dot1q 11
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 20 data-plane
  #               
  interface GigabitEthernet0/1/0.2 
   vlan-type dot1q 22
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 30 data-plane
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpn1
   ip address 10.22.1.1 255.255.255.0 
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip binding vpn-instance vpn2
   ip address 10.44.1.1 255.255.255.0
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 3.3.3.3
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE2 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 10.22.1.2 as-number 65420
   #              
   ipv4-family vpn-instance vpn2
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE2 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 10.44.1.2 as-number 65440
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 route-policy rp1234 import
    peer 2001:DB8:1::1 advertise encap-type srv6
  #               
  ip ip-prefix p1 index 10 permit 11.1.1.1 32
  ip ip-prefix p1 index 20 permit 10.11.1.0 24
  ip ip-prefix p3 index 10 permit 33.3.3.3 32 
  ip ip-prefix p3 index 20 permit 10.33.1.0 24
  #
  route-policy rp1234 permit node 10                                                 
   if-match ip-prefix p1                                                   
   apply extcommunity color 0:101                                          
  #                                                
  route-policy rp1234 permit node 20                                       
   if-match ip-prefix p3                                      
   apply extcommunity color 0:202                                       
  #                                           
  tunnel-policy tp1234
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #               
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.11.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 11.1.1.1 32
  #               
  bgp 65410       
   router-id 11.1.1.1
   peer 10.11.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.11.1.1 enable
  #  
  return 
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.22.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 22.2.2.2 32
  #               
  bgp 65420       
   router-id 22.2.2.2
   peer 10.22.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.22.1.1 enable
  #
  return
  ```
* CE3 configuration file
  
  ```
  #
  sysname CE3
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.33.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 33.3.3.3 32
  #               
  bgp 65430       
   router-id 33.3.3.3
   peer 10.33.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.33.1.1 enable
  #  
  return
  ```
* CE4 configuration file
  
  ```
  #
  sysname CE4
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.44.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 44.4.4.4 32
  #               
  bgp 65440       
   router-id 44.4.4.4
   peer 10.44.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.44.1.1 enable
  #
  return
  ```