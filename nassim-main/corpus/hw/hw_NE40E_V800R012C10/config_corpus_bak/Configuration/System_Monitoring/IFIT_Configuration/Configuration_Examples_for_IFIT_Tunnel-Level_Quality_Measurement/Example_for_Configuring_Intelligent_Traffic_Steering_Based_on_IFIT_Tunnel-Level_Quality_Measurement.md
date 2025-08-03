Example for Configuring Intelligent Traffic Steering Based on IFIT Tunnel-Level Quality Measurement
===================================================================================================

This section describes how to configure IFIT to implement tunnel-level quality measurement in an EVPN L3VPNv4 over SRv6 TE flow group scenario.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001223107307__fig184238288365), a bidirectional SRv6 TE flow group is deployed between PE1 and PE2 to carry EVPN L3VPNv4 services. The paths PE1-P1-PE2 and PE1-P2-PE2 are two candidate paths for service flow forwarding. After the packet loss and delay indicators of each path are measured using IFIT, TE-Class-based traffic diversion can be used to implement intelligent traffic steering.

**Figure 1** Network diagram of configuring IFIT tunnel-level measurement in an EVPN L3VPNv4 over SRv6 TE flow group![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0000001223108085.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, P1, P2, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on PE1, P1, P2, and PE2.
3. Configure a VPN instance in the IPv4 address family on PE1 and PE2.
4. Establish an EBGP peer relationship between each PE and its connected CE.
5. Establish a BGP EVPN peer relationship between PEs.
6. Configure SRv6 SIDs and enable IS-IS SRv6 on PE1, P1, P2, and PE2. In addition, configure PE1 and PE2 to advertise VPN routes carrying SIDs.
7. Deploy an SRv6 TE Policy between PE1 and PE2.
8. Configure a TE-Class value on PE1 and PE2.
9. Configure SPR on PE1 and PE2.
10. Configure PE1 and PE2 to use TE-Class to divert traffic to the SRv6 TE Policy.
11. Configure a tunnel policy on PE1 and PE2 to preferentially use the SRv6 TE flow group for VPN traffic import.
12. Configure IFIT measurement for the SRv6 TE Policy on PE1 and PE2.
13. Configure an IFIT instance on PE1 and PE2.
14. Configure PE1 and PE2 to use telemetry (YANG model sampling) to report measurement data.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before performing IFIT measurement, ensure the following:

* A clock synchronization protocol has been configured to implement clock synchronization between devices. In this scenario, NTP is generally used because interworking with other types of devices may be required. For details, see *NTP Configuration*.
* The devices have been connected to the NMS.


#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on PE1, P1, P2, and PE2
* IS-IS process ID of each device (PE1, P1, P2, and PE2)
* IS-IS level of each device (PE1, P1, P2, and PE2)
* VPN instance names, RDs, and RTs on PE1 and PE2
* NMS's IPv4 address (192.168.1.1) and port number (10001), and reachable routes between the NMS and devices

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The configurations of P1, P2, and PE2 are similar to the configuration of PE1. For configuration details, see Configuration Files in this section.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface GigabitEthernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:11::1 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface GigabitEthernet 0/3/0
   [*PE1-GigabitEthernet0/3/0] ipv6 enable
   [*PE1-GigabitEthernet0/3/0] ipv6 address 2001:DB8:13::1 96
   [*PE1-GigabitEthernet0/3/0] quit
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
   [*PE1-isis-1] is-level level-1
   [*PE1-isis-1] cost-style wide
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   [*PE1-isis-1] ipv6 enable topology ipv6
   [*PE1-isis-1] quit
   [*PE1] interface GigabitEthernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface GigabitEthernet 0/3/0
   [*PE1-GigabitEthernet0/3/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/3/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] isis ipv6 enable 1
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] quit
   ```
   
   
   # Configure P1.
   ```
   [~P1] isis 1
   [*P1-isis-1] is-level level-1
   [*P1-isis-1] cost-style wide
   [*P1-isis-1] network-entity 10.0000.0000.0002.00
   [*P1-isis-1] ipv6 enable topology ipv6
   [*P1-isis-1] quit
   [*P1] interface GigabitEthernet 0/1/0
   [*P1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*P1-GigabitEthernet0/1/0] quit
   [*P1] interface GigabitEthernet 0/2/0
   [*P1-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*P1-GigabitEthernet0/2/0] quit
   [*P1] interface loopback1
   [*P1-LoopBack1] isis ipv6 enable 1
   [*P1-LoopBack1] commit
   [~P1-LoopBack1] quit
   ```
   
   
   # Configure PE2.
   ```
   [~PE2] isis 1
   [*PE2-isis-1] is-level level-1
   [*PE2-isis-1] cost-style wide
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   [*PE2-isis-1] ipv6 enable topology ipv6
   [*PE2-isis-1] quit
   [*PE2] interface GigabitEthernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface GigabitEthernet 0/3/0
   [*PE2-GigabitEthernet0/3/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/3/0] quit
   [*PE2] interface loopback1
   [*PE2-LoopBack1] isis ipv6 enable 1
   [*PE2-LoopBack1] commit
   [~PE2-LoopBack1] quit
   ```
   
   
   # Configure P2.
   ```
   [~P2] isis 1
   [*P2-isis-1] is-level level-1
   [*P2-isis-1] cost-style wide
   [*P2-isis-1] network-entity 10.0000.0000.0004.00
   [*P2-isis-1] ipv6 enable topology ipv6
   [*P2-isis-1] quit
   [*P2] interface GigabitEthernet 0/1/0
   [*P2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*P2-GigabitEthernet0/1/0] quit
   [*P2] interface GigabitEthernet 0/2/0
   [*P2-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*P2-GigabitEthernet0/2/0] quit
   [*P2] interface loopback1
   [*P2-LoopBack1] isis ipv6 enable 1
   [*P2-LoopBack1] commit
   [~P2-LoopBack1] quit
   ```
   
   
   
   After the configuration is complete, run the [**display isis peer**](cmdqueryname=display+isis+peer) command to check whether IS-IS has been configured successfully.
3. Configure a VPN instance on each PE and enable the IPv4 address family for the instance.
   
   # Configure PE1.
   ```
   [~PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] ipv4-family
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both evpn
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   [*PE1-vpn-instance-vpna] quit
   [*PE1] interface GigabitEthernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] commit
   ```
   
   
   # Configure PE2.
   ```
   [~PE2] ip vpn-instance vpna
   [*PE2-vpn-instance-vpna] ipv4-family
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both evpn
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   [*PE2-vpn-instance-vpna] quit
   [*PE2] interface GigabitEthernet 0/2/0
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*PE2-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   [*PE2-GigabitEthernet0/2/0] quit
   [*PE2] commit
   ```
   
   
   
   After the configuration is complete, run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) command to check the VPN instance configuration.
4. Establish an EBGP peer relationship between each PE and its connected CE.
   
   # Configure CE1.
   ```
   [~CE1] interface loopback 1
   [*CE1-LoopBack1] ip address 11.11.11.11 32
   [*CE1-LoopBack1] quit
   [*CE1] bgp 65410
   [*CE1-bgp] router-id 11.11.11.11
   [*CE1-bgp] peer 10.1.1.1 as-number 100
   [*CE1-bgp] import-route direct
   [*CE1-bgp] quit
   [*CE1] commit
   ```
   
   
   # Configure PE1.
   ```
   [~PE1] bgp 100
   [*PE1-bgp] router-id 1.1.1.1
   [*PE1-bgp] ipv4-family vpn-instance vpna
   [*PE1-bgp-vpna] peer 10.1.1.2 as-number 65410
   [*PE1-bgp-vpna] import-route direct
   [*PE1-bgp-vpna] advertise l2vpn evpn
   [*PE1-bgp-vpna] commit
   [~PE1-bgp-vpna] quit
   [~PE1-bgp] quit
   ```
   
   
   # Configure CE2.
   ```
   [~CE2] interface loopback 1
   [*CE2-LoopBack1] ip address 22.22.22.22 32
   [*CE2-LoopBack1] quit
   [*CE2] bgp 65420
   [*CE2-bgp] router-id 22.22.22.22
   [*CE2-bgp] peer 10.2.1.1 as-number 100
   [*CE2-bgp] import-route direct
   [*CE2-bgp] quit
   [*CE2] commit
   ```
   
   
   # Configure PE2.
   ```
   [~PE2] bgp 100
   [*PE2-bgp] router-id 2.2.2.2
   [*PE2-bgp] ipv4-family vpn-instance vpna
   [*PE2-bgp-vpna] peer 10.2.1.2 as-number 65420
   [*PE2-bgp-vpna] import-route direct
   [*PE2-bgp-vpna] advertise l2vpn evpn
   [*PE2-bgp-vpna] commit
   [~PE2-bgp-vpna] quit
   [~PE2-bgp] quit
   ```
   
   
   
   After the configuration is complete, run the [**display bgp vpnv4 vpn-instance peer**](cmdqueryname=display+bgp+vpnv4+vpn-instance+peer) command to check the EBGP peer relationship established between PE1 and CE1.
5. Establish a BGP EVPN peer relationship between PEs.
   
   # Configure PE1.
   ```
   [~PE1] bgp 100
   [*PE1-bgp] peer 2001:DB8:3::3 as-number 100
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 enable
   [*PE1-bgp-af-evpn] commit
   [~PE1-bgp-af-evpn] quit
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   ```
   [~PE2] bgp 100
   [*PE2-bgp] peer 2001:DB8:1::1 as-number 100
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 enable
   [*PE2-bgp-af-evpn] commit
   [~PE2-bgp-af-evpn] quit
   [~PE2-bgp] quit
   ```
   
   After completing the configuration, run the [**display bgp evpn peer**](cmdqueryname=display+bgp+evpn+peer) command to check the BGP EVPN peer relationship established between PEs.
6. Configure SRv6 SIDs, and configure the PEs to advertise VPN routes carrying SIDs.
   
   # Configure PE1.
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*PE1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32
   [*PE1-segment-routing-ipv6-locator] opcode ::100 end psp
   [*PE1-segment-routing-ipv6-locator] opcode ::200 end no-flavor
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] bgp 100
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] ipv4-family vpn-instance vpna
   [*PE1-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort evpn
   [*PE1-bgp-vpna] segment-routing ipv6 locator as1 evpn
   [*PE1-bgp-vpna] commit
   [~PE1-bgp-vpna] quit
   [~PE1-bgp] quit
   [~PE1] isis 1
   [*PE1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*PE1-isis-1] commit
   [~PE1-isis-1] quit
   ```
   
   # Configure P1.
   ```
   [~P1] segment-routing ipv6
   [*P1-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   [*P1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:200:: 64 static 32
   [*P1-segment-routing-ipv6-locator] opcode ::100 end psp
   [*P1-segment-routing-ipv6-locator] opcode ::200 end no-flavor
   [*P1-segment-routing-ipv6-locator] quit
   [*P1-segment-routing-ipv6] quit
   [*P1] isis 1
   [*P1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*P1-isis-1] commit
   [~P1-isis-1] quit
   ```
   
   # Configure PE2.
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   [*PE2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32
   [*PE2-segment-routing-ipv6-locator] opcode ::100 end psp
   [*PE2-segment-routing-ipv6-locator] opcode ::200 end no-flavor
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] bgp 100
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] ipv4-family vpn-instance vpna
   [*PE2-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort evpn
   [*PE2-bgp-vpna] segment-routing ipv6 locator as1 evpn
   [*PE2-bgp-vpna] commit
   [~PE2-bgp-vpna] quit
   [~PE2-bgp] quit
   [*PE2] isis 1
   [*PE2-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*PE2-isis-1] commit
   [~PE2-isis-1] quit
   ```
   
   # Configure P2.
   ```
   [~P2] segment-routing ipv6
   [*P2-segment-routing-ipv6] encapsulation source-address 2001:DB8:4::4
   [*P2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:400:: 64 static 32
   [*P2-segment-routing-ipv6-locator] opcode ::100 end psp
   [*P2-segment-routing-ipv6-locator] opcode ::200 end no-flavor
   [*P2-segment-routing-ipv6-locator] quit
   [*P2-segment-routing-ipv6] quit
   [*P2] isis 1
   [*P2-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*P2-isis-1] commit
   [~P2-isis-1] quit
   ```
   
   After completing the configuration, run the [**display segment-routing ipv6 locator**](cmdqueryname=display+segment-routing+ipv6+locator) command to check SRv6 locator information.
7. Configure an SRv6 TE Policy.
   
   # Configure PE1.
   ```
   [~PE1] segment-routing ipv6 
   [*PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:200::100
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:300::100
   [*PE1-segment-routing-ipv6-segment-list-list1] quit
   [*PE1-segment-routing-ipv6] segment-list list2 
   [*PE1-segment-routing-ipv6-segment-list-list2] index 5 sid ipv6 2001:DB8:400::100
   [*PE1-segment-routing-ipv6-segment-list-list2] index 10 sid ipv6 2001:DB8:300::100
   [*PE1-segment-routing-ipv6-segment-list-list2] quit
   [*PE1-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:3::3 color 10
   [*PE1-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:100::900
   [*PE1-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy1-path] segment-list list1 binding-sid 2001:DB8:100::800 reverse-binding-sid 2001:DB8:300::800
   [*PE1-segment-routing-ipv6-policy-policy1-path] quit
   [*PE1-segment-routing-ipv6-policy-policy1] quit
   [*PE1-segment-routing-ipv6] srv6-te policy policy2 endpoint 2001:DB8:3::3 color 20
   [*PE1-segment-routing-ipv6-policy-policy2] binding-sid 2001:DB8:100::901
   [*PE1-segment-routing-ipv6-policy-policy2] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy2-path] segment-list list2 binding-sid 2001:DB8:100::801 reverse-binding-sid 2001:DB8:300::801
   [*PE1-segment-routing-ipv6-policy-policy2-path] commit
   [~PE1-segment-routing-ipv6-policy-policy2-path] quit
   [~PE1-segment-routing-ipv6-policy-policy2] quit
   [~PE1-segment-routing-ipv6] quit
   ```
   
   # Configure PE2.
   ```
   [~PE2] segment-routing ipv6 
   [*PE2-segment-routing-ipv6] segment-list list1 
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:200::100
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:100::100
   [*PE2-segment-routing-ipv6-segment-list-list1] quit
   [*PE2-segment-routing-ipv6] segment-list list2 
   [*PE2-segment-routing-ipv6-segment-list-list2] index 5 sid ipv6 2001:DB8:400::100
   [*PE2-segment-routing-ipv6-segment-list-list2] index 10 sid ipv6 2001:DB8:100::100
   [*PE2-segment-routing-ipv6-segment-list-list2] quit
   [*PE2-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 10
   [*PE2-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:300::900
   [*PE2-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list1 binding-sid 2001:DB8:300::800 reverse-binding-sid 2001:DB8:100::800
   [*PE2-segment-routing-ipv6-policy-policy1-path] quit
   [*PE2-segment-routing-ipv6-policy-policy1] quit
   [*PE2-segment-routing-ipv6] srv6-te policy policy2 endpoint 2001:DB8:1::1 color 20
   [*PE2-segment-routing-ipv6-policy-policy2] binding-sid 2001:DB8:300::901
   [*PE2-segment-routing-ipv6-policy-policy2] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy2-path] segment-list list2 binding-sid 2001:DB8:300::801 reverse-binding-sid 2001:DB8:100::801
   [*PE2-segment-routing-ipv6-policy-policy2-path] commit
   [~PE2-segment-routing-ipv6-policy-policy2-path] quit
   [~PE2-segment-routing-ipv6-policy-policy2] quit
   [~PE2-segment-routing-ipv6] quit
   ```
   
   After completing the configuration, run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information.
8. Configure a TE-Class value.
   
   # Configure PE1.
   ```
   [~PE1] acl number 3333
   [*PE1-acl-advance-3333] rule 5 permit ip source 11.11.11.11 0 destination 22.22.22.22 0
   [*PE1-acl-advance-3333] rule 10 permit ip source 22.22.22.22 0 destination 11.11.11.11 0
   [*PE1-acl-advance-3333] commit
   [~PE1-acl-advance-3333] quit
   [~PE1] traffic classifier c1
   [*PE1-classifier-c1] if-match acl 3333
   [*PE1-classifier-c1] commit
   [~PE1-classifier-c1] quit
   [~PE1] traffic behavior b1
   [*PE1-behavior-b1] remark te-class 1
   [*PE1-behavior-b1] commit
   [~PE1-behavior-b1] quit
   [~PE1] traffic policy p1
   [*PE1-trafficpolicy-p1] classifier c1 behavior b1
   [*PE1-trafficpolicy-p1] share-mode
   [*PE1-trafficpolicy-p1] statistics enable
   [*PE1-trafficpolicy-p1] quit
   [*PE1] interface GigabitEthernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] traffic-policy p1 inbound
   [*PE1-GigabitEthernet0/2/0] commit
   [~PE1-GigabitEthernet0/2/0] quit
   ```
   
   
   # Configure PE2.
   ```
   [~PE2] acl number 3333
   [*PE2-acl-advance-3333] rule 5 permit ip source 22.22.22.22 0 destination 11.11.11.11 0
   [*PE2-acl-advance-3333] rule 10 permit ip source 11.11.11.11 0 destination 22.22.22.22 0
   [*PE2-acl-advance-3333] commit
   [~PE2-acl-advance-3333] quit
   [~PE2] traffic classifier c1
   [*PE2-classifier-c1] if-match acl 3333
   [*PE2-classifier-c1] commit
   [~PE2-classifier-c1] quit
   [~PE2] traffic behavior b1
   [*PE2-behavior-b1] remark te-class 1
   [*PE2-behavior-b1] commit
   [~PE2-behavior-b1] quit
   [~PE2] traffic policy p1
   [*PE2-trafficpolicy-p1] classifier c1 behavior b1
   [*PE2-trafficpolicy-p1] share-mode
   [*PE2-trafficpolicy-p1] statistics enable
   [*PE2-trafficpolicy-p1] quit
   [*PE2] interface GigabitEthernet 0/2/0
   [*PE2-GigabitEthernet0/2/0] traffic-policy p1 inbound
   [*PE2-GigabitEthernet0/2/0] commit
   [~PE2-GigabitEthernet0/2/0] quit
   ```
9. Configure SPR.
   
   # Configure PE1.
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] smart-policy-route
   [*PE1-segment-routing-ipv6-spr] spr-policy spr1
   [*PE1-segment-routing-ipv6-spr-policy-spr1] delay threshold 1000
   [*PE1-segment-routing-ipv6-spr-policy-spr1] loss threshold 300
   [*PE1-segment-routing-ipv6-spr-policy-spr1] jitter threshold 1000
   [*PE1-segment-routing-ipv6-spr-policy-spr1] cmi threshold 5000
   [*PE1-segment-routing-ipv6-spr-policy-spr1] srv6-te-policy color 10 priority 1
   [*PE1-segment-routing-ipv6-spr-policy-spr1] srv6-te-policy color 20 priority 2
   [*PE1-segment-routing-ipv6-spr-policy-spr1] commit
   [~PE1-segment-routing-ipv6-spr-policy-spr1] quit
   [~PE1-segment-routing-ipv6-spr] quit
   [~PE1-segment-routing-ipv6] quit
   ```
   
   
   # Configure PE2.
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] smart-policy-route
   [*PE2-segment-routing-ipv6-spr] spr-policy spr1
   [*PE2-segment-routing-ipv6-spr-policy-spr1] delay threshold 1000
   [*PE2-segment-routing-ipv6-spr-policy-spr1] loss threshold 300
   [*PE2-segment-routing-ipv6-spr-policy-spr1] jitter threshold 1000
   [*PE2-segment-routing-ipv6-spr-policy-spr1] cmi threshold 5000
   [*PE2-segment-routing-ipv6-spr-policy-spr1] srv6-te-policy color 10 priority 1
   [*PE2-segment-routing-ipv6-spr-policy-spr1] srv6-te-policy color 20 priority 2
   [*PE2-segment-routing-ipv6-spr-policy-spr1] commit
   [~PE2-segment-routing-ipv6-spr-policy-spr1] quit
   [~PE2-segment-routing-ipv6-spr] quit
   [~PE2-segment-routing-ipv6] quit
   ```
10. Configure TE-Class-based traffic steering into an SRv6 TE Policy.
    
    
    
    In TE-Class-based traffic steering, the headend recurses traffic based on the next hop of the corresponding route in compliance with the configured tunnel policy. If traffic recursion to an SRv6 TE flow group is configured, the headend matches the traffic with an SRv6 mapping policy that has the same color value as the route. If such an SRv6 mapping policy exists, the headend dynamically generates an SRv6 TE flow group that contains multiple SRv6 TE Policies with the same endpoint but different color values.
    
    # Configure PE1.
    ```
    [~PE1] segment-routing ipv6
    [*PE1-segment-routing-ipv6] mapping-policy p1 color 101
    [*PE1-segment-routing-ipv6-mapping-policy-p1] match-type te-class
    [*PE1-segment-routing-ipv6-mapping-policy-p1-te-class] index 10 te-class 1 match spr-policy spr1 
    [*PE1-segment-routing-ipv6-mapping-policy-p1-te-class] commit
    [~PE1-segment-routing-ipv6-mapping-policy-p1-te-class] quit
    [~PE1-segment-routing-ipv6-mapping-policy-p1] quit
    [~PE1-segment-routing-ipv6] quit
    ```
    
    # Configure PE2.
    ```
    [~PE2] segment-routing ipv6
    [*PE2-segment-routing-ipv6] mapping-policy p1 color 101
    [*PE2-segment-routing-ipv6-mapping-policy-p1] match-type te-class
    [*PE2-segment-routing-ipv6-mapping-policy-p1-te-class] index 10 te-class 1 match spr-policy spr1 
    [*PE2-segment-routing-ipv6-mapping-policy-p1-te-class] commit
    [~PE2-segment-routing-ipv6-mapping-policy-p1-te-class] quit
    [~PE2-segment-routing-ipv6-mapping-policy-p1] quit
    [~PE2-segment-routing-ipv6] quit
    ```
11. Configure a tunnel policy and import VPN traffic.
    
    # Configure PE1.
    ```
    [~PE1] route-policy p1 permit node 10
    [*PE1-route-policy] apply extcommunity color 0:101
    [*PE1-route-policy] quit
    [*PE1] bgp 100
    [*PE1-bgp] l2vpn-family evpn
    [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 route-policy p1 import 
    [*PE1-bgp-af-evpn] quit
    [*PE1-bgp] quit
    [*PE1] tunnel-policy p1
    [*PE1-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
    [*PE1-tunnel-policy-p1] quit
    [*PE1] ip vpn-instance vpna
    [*PE1-vpn-instance-vpna] ipv4-family
    [*PE1-vpn-instance-vpna-af-ipv4] tnl-policy p1 evpn
    [*PE1-vpn-instance-vpna-af-ipv4] commit
    [~PE1-vpn-instance-vpna-af-ipv4] quit
    [~PE1-vpn-instance-vpna] quit
    ```
    
    # Configure PE2.
    ```
    [~PE2] route-policy p1 permit node 10
    [*PE2-route-policy] apply extcommunity color 0:101
    [*PE2-route-policy] quit
    [*PE2] bgp 100
    [*PE2-bgp] l2vpn-family evpn
    [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 route-policy p1 import 
    [*PE2-bgp-af-evpn] quit
    [*PE2-bgp] quit
    [*PE2] tunnel-policy p1
    [*PE2-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
    [*PE2-tunnel-policy-p1] quit
    [*PE2] ip vpn-instance vpna
    [*PE2-vpn-instance-vpna] ipv4-family
    [*PE2-vpn-instance-vpna-af-ipv4] tnl-policy p1 evpn
    [*PE2-vpn-instance-vpna-af-ipv4] commit
    [~PE2-vpn-instance-vpna-af-ipv4] quit
    [~PE2-vpn-instance-vpna] quit
    ```
    
    After completing the configuration, run the [**display srv6-te flow-group**](cmdqueryname=display+srv6-te+flow-group) command to check the SRv6 TE flow group status. You can also run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) command to check the IPv4 routing table of a VPN instance and check whether VPN routes are successfully recursed to the SRv6 TE Policy.
12. Configure IFIT measurement for the SRv6 TE Policy.
    
    # Configure PE1.
    ```
    [~PE1] segment-routing ipv6
    [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:3::3 color 10
    [*PE1-segment-routing-ipv6-policy-policy1] ifit loss-measure enable
    [*PE1-segment-routing-ipv6-policy-policy1] ifit delay-measure enable
    [*PE1-segment-routing-ipv6-policy-policy1] quit
    [*PE1-segment-routing-ipv6] srv6-te policy policy2 endpoint 2001:DB8:3::3 color 20
    [*PE1-segment-routing-ipv6-policy-policy2] ifit loss-measure enable
    [*PE1-segment-routing-ipv6-policy-policy2] ifit delay-measure enable
    [*PE1-segment-routing-ipv6-policy-policy2] commit
    [~PE1-segment-routing-ipv6-policy-policy2] quit
    [~PE1-segment-routing-ipv6] quit
    ```
    
    
    # Configure PE2.
    ```
    [~PE2] segment-routing ipv6
    [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 10
    [*PE2-segment-routing-ipv6-policy-policy1] ifit loss-measure enable
    [*PE2-segment-routing-ipv6-policy-policy1] ifit delay-measure enable
    [*PE2-segment-routing-ipv6-policy-policy1] quit
    [*PE2-segment-routing-ipv6] srv6-te policy policy2 endpoint 2001:DB8:1::1 color 20
    [*PE2-segment-routing-ipv6-policy-policy2] ifit loss-measure enable
    [*PE2-segment-routing-ipv6-policy-policy2] ifit delay-measure enable
    [*PE2-segment-routing-ipv6-policy-policy2] commit
    [~PE2-segment-routing-ipv6-policy-policy2] quit
    [~PE2-segment-routing-ipv6] quit
    ```
13. Configure an IFIT instance.
    
    # Configure PE1.
    ```
    [~PE1] ifit
    [*PE1-ifit] node-id 10
    [*PE1-ifit] work-mode mcp
    [*PE1-ifit-work-mode-mcp] service-type srv6-segment-list
    [*PE1-ifit-work-mode-mcp] commit
    [~PE1-ifit-work-mode-mcp] quit
    [~PE1-ifit] quit
    ```
    
    # Configure PE2.
    ```
    [~PE2] ifit
    [*PE2-ifit] node-id 20
    [*PE2-ifit] work-mode dcp
    [*PE2-ifit-work-mode-dcp] service-type srv6-segment-list
    [*PE2-ifit-work-mode-dcp] commit
    [~PE2-ifit-work-mode-dcp] quit
    [~PE2-ifit] quit
    ```
14. Configure the device to send statistics to the NMS through telemetry. The following example uses the configuration on PE1. The configuration of PE2 is similar to the configuration of PE1.
    
    
    ```
    [~PE1] telemetry
    [~PE1-telemetry] destination-group ifit
    [*PE1-telemetry-destination-group-ifit] ipv4-address 192.168.1.1 port 10001 protocol grpc
    [*PE1-telemetry-destination-group-ifit] quit
    [*PE1-telemetry] sensor-group ifit
    [*PE1-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-sr-policy-statistics/flow-sr-policy-statistic
    [*PE1-telemetry-sensor-group-ifit-path] quit
    [*PE1-telemetry-sensor-group-ifit] quit
    [*PE1-telemetry] subscription ifit
    [*PE1-telemetry-subscription-ifit] sensor-group ifit sample-interval 0
    [*PE1-telemetry-subscription-ifit] destination-group ifit
    [*PE1-telemetry-subscription-ifit] commit
    ```
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    You are advised to configure devices to send data using a secure TLS encryption mode. For details, see *Telemetry Configuration*.

#### Verifying the Configuration

# Check unidirectional packet loss statistics of an IFIT flow.
```
[~PE1] display ifit statistic-type one-way-loss flow-id 1572866
Latest one-way loss statistics:
-------------------------------------------------------------------------------------------------------------------------------
  Period                 Local-Loss             Local-Loss-Ratio      Remote-Loss            Remote-Loss-Ratio     Error-Info
-------------------------------------------------------------------------------------------------------------------------------
  818051526              0                      0                     0                      0                     OK            
  818051525              0                      0                     0                      0                     OK            
  818051524              0                      0                     0                      0                     OK            
  818051523              0                      0                     0                      0                     OK            
  818051522              0                      0                     0                      0                     OK            
  818051521              0                      0                     0                      0                     OK            
  818051520              0                      0                     0                      0                     OK            
  818051519              0                      0                     0                      0                     OK            
  818051518              0                      0                     0                      0                     OK            
  818051517              0                      0                     0                      0                     OK            
  818051516              0                      0                     0                      0                     OK            
  818051515              0                      0                     0                      0                     OK            
  818051514              0                      0                     0                      0                     OK            
  818051513              0                      0                     0                      0                     OK            
  818051512              0                      0                     0                      0                     OK            
  818051511              0                      0                     0                      0                     OK            
  818051510              0                      0                     0                      0                     OK            
  818051509              0                      0                     0                      0                     OK            
  818051508              0                      0                     0                      0                     OK            
  818051507              0                      0                     0                      0                     OK            
  818051506              0                      0                     0                      0                     OK            
  818051505              0                      0                     0                      0                     OK            
  818051504              0                      0                     0                      0                     OK            
  818051503              0                      0                     0                      0                     OK            
  818051502              0                      0                     0                      0                     OK            
  818051501              0                      0                     0                      0                     OK            
  818051500              0                      0                     0                      0                     OK            
  818051499              0                      0                     0                      0                     OK            
  818051498              0                      0                     0                      0                     OK            
  818051497              0                      0                     0                      0                     OK            
-------------------------------------------------------------------------------------------------------------------------------
Info: The actual loss ratio is the value displayed in the Loss-Ratio column divided by 10^6.
```

# Check one-way delay information of an IFIT flow.
```
[~PE1] display ifit statistic-type one-way-delay flow-id 1572866
Latest one-way delay statistics(nsec):
-----------------------------------------------------------------------------------------------------------------------------
  Period                 Local-Delay       Local-Delay-Jitter       Remote-Delay       Remote-Delay-Jitter       Error-Info
-----------------------------------------------------------------------------------------------------------------------------
  818051332              0                 0		                0                  0                         OK          
  818051331              0                 0		                0                  0                         OK          
  818051330              0                 0		                0                  0                         OK          
  818051329              0                 0		                0                  0                         OK          
  818051328              0                 0		                0                  0                         OK          
  818051327              0                 0		                0                  0                         OK          
  818051326              0                 0		                0                  0                         OK          
  818051325              0                 0		                0                  0                         OK          
  818051324              0                 0		                0                  0                         OK          
  818051323              0                 0		                0                  0                         OK          
  818051322              0                 0		                0                  0                         OK          
  818051321              0                 0		                0                  0                         OK          
  818051320              0                 0		                0                  0                         OK          
  818051319              0                 0		                0                  0                         OK          
  818051318              0                 0		                0                  0                         OK          
  818051317              0                 0		                0                  0                         OK          
  818051316              0                 0		                0                  0                         OK          
  818051315              0                 0		                0                  0                         OK          
  818051314              0                 0		                0                  0                         OK          
  818051313              0                 0		                0                  0                         OK          
  818051312              0                 0		                0                  0                         OK          
  818051311              0                 0		                0                  0                         OK          
  818051310              0                 0		                0                  0                         OK          
  818051309              0                 0		                0                  0                         OK          
  818051308              0                 0		                0                  0                         OK          
  818051307              0                 0		                0                  0                         OK          
  818051306              0                 0		                0                  0                         OK          
  818051305              0                 0		                0                  0                         OK          
  818051304              0                 0		                0                  0                         OK          
  818051303              0                 0		                0                  0                         OK          
-----------------------------------------------------------------------------------------------------------------------------
```

# Check two-way delay information of an IFIT flow.
```
[~PE1] display ifit statistic-type two-way-delay flow-id 1572866
Latest two-way delay statistics(nsec):
--------------------------------------------------------------------------------------------
  Period                 Delay(Avg)                 Jitter(Avg)                 Error-Info
--------------------------------------------------------------------------------------------
  818051332              1000000                    0                           OK          
  818051331              1000000                    0                           OK          
  818051330              1000000                    0                           OK          
  818051329              1000000                    0                           OK          
  818051328              1000000                    0                           OK          
  818051327              1000000                    0                           OK          
  818051326              1000000                    0                           OK          
  818051325              1000000                    0                           OK          
  818051324              1000000                    0                           OK          
  818051323              1000000                    0                           OK          
  818051322              1000000                    0                           OK          
  818051321              1000000                    0                           OK          
  818051320              1000000                    0                           OK          
  818051319              1000000                    0                           OK          
  818051318              1000000                    0                           OK          
  818051317              1000000                    0                           OK          
  818051316              1000000                    0                           OK          
  818051315              1000000                    0                           OK          
  818051314              1000000                    0                           OK          
  818051313              1000000                    0                           OK          
  818051312              1000000                    0                           OK          
  818051311              1000000                    0                           OK          
  818051310              1000000                    0                           OK          
  818051309              1000000                    0                           OK          
  818051308              1000000                    0                           OK          
  818051307              1000000                    0                           OK          
  818051306              1000000                    0                           OK          
  818051305              1000000                    0                           OK          
  818051304              1000000                    0                           OK          
  818051303              1000000                    0                           OK          
--------------------------------------------------------------------------------------------
```

# Check SRv6 TE Policy measurement instance information.
```
[~PE1] display ifit srv6-segment-list
-------------------------------------------------------------------------
Flow Classification                     : srv6-segment-list
Instance Id                             : 2
Flow Id                                 : 1572866
Flow Type                               : unidirectional
Loss Measure                            : enable
Delay Measure                           : enable
Measure Mode                            : e2e
Interval                                : 30(s)
Color                                   : 10
Segment List Id                         : 1
Binding SID                             : 2001:DB8:100::800
Reverse Binding SID                     : 2001:DB8:300::800 
EndPoint                                : 2001:DB8:3::3
-------------------------------------------------------------------------
Flow Classification                     : srv6-segment-list
Instance Id                             : 3
Flow Id                                 : 1572867
Flow Type                               : unidirectional
Loss Measure                            : enable
Delay Measure                           : enable
Measure Mode                            : e2e
Interval                                : 30(s)
Color                                   : 20
Segment List Id                         : 2
Binding SID                             : 2001:DB8:100::801
Reverse Binding SID                     : 2001:DB8:300::801
EndPoint                                : 2001:DB8:3::3
```


#### Configuration Scripts

* PE1
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    tnl-policy p1 evpn
    apply-label per-instance
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
  #
  acl number 3333
   rule 5 permit ip source 11.11.11.11 0 destination 22.22.22.22 0
   rule 10 permit ip source 22.22.22.22 0 destination 11.11.11.11 0
  #
  traffic classifier c1
   if-match acl 3333
  #
  traffic behavior b1
   remark te-class 1
  #        
  traffic policy p1
   share-mode
   statistics enable
   classifier c1 behavior b1 precedence 1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1                                              
   locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32                                     
    opcode ::100 end psp      
    opcode ::200 end no-flavor
   srv6-te-policy locator as1 
   segment-list list1        
    index 5 sid ipv6 2001:DB8:200::100  
    index 10 sid ipv6 2001:DB8:300::100 
   segment-list list2        
    index 5 sid ipv6 2001:DB8:400::100  
    index 10 sid ipv6 2001:DB8:300::100 
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 10                                  
    binding-sid 2001:DB8:100::900  
    ifit loss-measure enable
    ifit delay-measure enable
    candidate-path preference 100     
     segment-list list1 binding-sid 2001:DB8:100::800 reverse-binding-sid 2001:DB8:300::800        
   srv6-te policy policy2 endpoint 2001:DB8:3::3 color 20                                  
    binding-sid 2001:DB8:100::901 
    ifit loss-measure enable
    ifit delay-measure enable
    candidate-path preference 100 
     segment-list list2 binding-sid 2001:DB8:100::801 reverse-binding-sid 2001:DB8:300::801       
   smart-policy-route
    spr-policy spr1
     delay threshold 1000
     jitter threshold 1000
     loss threshold 300
     cmi threshold 5000
     srv6-te-policy color 10 priority 1
     srv6-te-policy color 20 priority 2
   mapping-policy p1 color 101     
    match-type te-class 
     index 10 te-class 1 match spr-policy spr1
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:11::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
   traffic-policy p1 inbound
  #               
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:13::1/96
   isis ipv6 enable 1
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
   ipv4-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator as1 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 10.1.1.2 as-number 65410
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 route-policy p1 import
    peer 2001:DB8:3::3 advertise encap-type srv6 
  #
  ifit
   node-id 10
   work-mode mcp
    service-type srv6-segment-list
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-sr-policy-statistics/flow-sr-policy-statistic
   #
   destination-group ifit
    ipv4-address 192.168.1.1 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 0
    destination-group ifit
  #               
  return
  ```
* P1
  ```
  #
  sysname P1        
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator as1 ipv6-prefix 2001:DB8:200:: 64 static 32
    opcode ::100 end psp
    opcode ::200 end no-flavor
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:11::2/96
   isis ipv6 enable 1 
  # 
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:12::1/96
   isis ipv6 enable 1  
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #               
  return
  ```
* PE2
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    tnl-policy p1 evpn
    apply-label per-instance
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
  #
  acl number 3333
   rule 5 permit ip source 22.22.22.22 0 destination 11.11.11.11 0
   rule 10 permit ip source 11.11.11.11 0 destination 22.22.22.22 0
  #
  traffic classifier c1
   if-match acl 3333
  #
  traffic behavior b1
   remark te-class 1
  #        
  traffic policy p1
   share-mode
   statistics enable
   classifier c1 behavior b1 precedence 1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3                                              
   locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32                                     
    opcode ::100 end psp      
    opcode ::200 end no-flavor
   srv6-te-policy locator as1 
   segment-list list1        
    index 5 sid ipv6 2001:DB8:200::100  
    index 10 sid ipv6 2001:DB8:100::100 
   segment-list list2        
    index 5 sid ipv6 2001:DB8:400::100  
    index 10 sid ipv6 2001:DB8:100::100 
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 10                                  
    binding-sid 2001:DB8:300::900  
    ifit loss-measure enable
    ifit delay-measure enable
    candidate-path preference 100     
     segment-list list1 binding-sid 2001:DB8:300::800 reverse-binding-sid 2001:DB8:100::800       
   srv6-te policy policy2 endpoint 2001:DB8:1::1 color 20                                  
    binding-sid 2001:DB8:300::901 
    ifit loss-measure enable
    ifit delay-measure enable
    candidate-path preference 100 
     segment-list list2 binding-sid 2001:DB8:300::801 reverse-binding-sid 2001:DB8:100::801       
   smart-policy-route
    spr-policy spr1
     delay threshold 1000
     jitter threshold 1000
     loss threshold 300
     cmi threshold 5000
     srv6-te-policy color 10 priority 1
     srv6-te-policy color 20 priority 2
   mapping-policy p1 color 101     
    match-type te-class 
     index 10 te-class 1 match spr-policy spr1
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable             
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:12::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
   traffic-policy p1 inbound
  #               
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:14::2/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 2.2.2.2
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator as1 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 10.2.1.2 as-number 65420
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 route-policy p1 import
    peer 2001:DB8:1::1 advertise encap-type srv6 
  #
  ifit
   node-id 20
   work-mode dcp
    service-type srv6-segment-list
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-sr-policy-statistics/flow-sr-policy-statistic
   #
   destination-group ifit
    ipv4-address 192.168.1.1 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 0
    destination-group ifit
  #               
  return
  ```
* P2
  ```
  #
  sysname P2        
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:4::4
   locator as1 ipv6-prefix 2001:DB8:400::1 64 static 32
    opcode ::100 end psp
    opcode ::200 end no-flavor
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:13::2/96
   isis ipv6 enable 1 
  # 
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:14::1/96
   isis ipv6 enable 1  
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:4::4/128
   isis ipv6 enable 1
  #               
  return 
  ```
* CE1
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 11.11.11.11 255.255.255.255
  #               
  bgp 65410
   router-id 11.11.11.11 
   peer 10.1.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct 
    peer 10.1.1.1 enable
  #               
  return 
  ```
* CE2
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 22.22.22.22 255.255.255.255
  #
  bgp 65420
   router-id 22.22.22.22
   peer 10.2.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.2.1.1 enable
  #
  return
  ```