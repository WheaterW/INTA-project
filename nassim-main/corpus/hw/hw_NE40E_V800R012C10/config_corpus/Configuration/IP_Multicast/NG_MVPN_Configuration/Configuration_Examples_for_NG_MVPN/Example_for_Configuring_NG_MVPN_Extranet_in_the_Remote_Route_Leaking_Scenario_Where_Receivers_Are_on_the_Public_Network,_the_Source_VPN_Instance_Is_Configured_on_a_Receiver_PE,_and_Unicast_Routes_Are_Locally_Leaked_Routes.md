Example for Configuring NG MVPN Extranet in the Remote Route Leaking Scenario Where Receivers Are on the Public Network, the Source VPN Instance Is Configured on a Receiver PE, and Unicast Routes Are Locally Leaked Routes
=============================================================================================================================================================================================================================

This section provides an example for configuring NG MVPN extranet in the remote route leaking scenario where receivers are on the public network, the source VPN instance is configured on a receiver PE, and unicast routes are locally leaked routes.

#### Networking Requirements

In an NG MVPN application, a service provider needs to provide multicast services from a VPN for users on the public network. In this case, service traffic needs to be imported from the VPN to the public network for multicast service distribution.

In the remote route leaking scenario shown in [Figure 1](#EN-US_TASK_0000001338984494__fig44631823184117), public network receivers want to receive multicast data from the source in VPN BLUE. To meet this requirement, you can deploy NG MVPN extranet by configuring the source VPN instance and local leaking of static unicast routes on the receiver PE.

**Figure 1** Configuring NG MVPN extranet in the remote route leaking scenario where receivers are on the public network, the source VPN instance is configured on a receiver PE, and unicast routes are locally leaked routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001338734166.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic functions of single-AS NG MVPN and GTM.
2. Configure a public network instance on PE2.
3. Configure an RP to serve the NG MVPN extranet group.
4. Configure local leaking of unicast routes for the public network instance on PE2, specify VPN BLUE as the VPN instance to which the outbound interfaces of the unicast routes destined for the public network RP and source belong, and allow the public network instance to be used as a multicast extranet receiver instance.

#### Data Preparation

To complete the configuration, you need the following data:

* RD and VPN target of VPN BLUE: 100:1; VPN target of MVPN routes: 1:1

#### Procedure

1. Configure NG MVPN and GTM functions.
   1. Configure an IPv6 address for each interface. The configuration of PE1 is used as an example. The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section. Similar details will be omitted in the rest of the document.
      
      
      
      # Configure PE1.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname PE1
      [*HUAWEI] commit
      [*PE1] interface gigabitethernet 0/1/0
      [*PE1-GigabitEthernet0/1/0] ipv6 enable
      [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:1::2 96
      [*PE1-GigabitEthernet0/1/0] quit
      [*PE1] interface LoopBack 1
      [*PE1-LoopBack1] ipv6 enable
      [*PE1-LoopBack1] ipv6 address 2001:DB8:10::1 128
      [*PE1-LoopBack1] quit
      [*PE1] commit
      ```
   2. Configure a unicast routing protocol on the public network to ensure that multicast routes on the public network are reachable. The configuration of PE1 is used as an example. The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
      
      
      ```
      [~PE1] isis 1
      [*PE1-isis-1] is-level level-2
      [*PE1-isis-1] cost-style wide
      [*PE1-isis-1] network-entity 10.0000.0000.0001.00
      [*PE1-isis-1] ipv6 enable topology ipv6
      [*PE1-isis-1] quit
      [*PE1] interface GigabitEthernet 0/1/0
      [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
      [*PE1-GigabitEthernet0/1/0] quit
      [*PE1] interface Loopback 1
      [*PE1-Loopback1] isis ipv6 enable 1
      [*PE1-Loopback1] quit
      [*PE1] commit
      ```
   3. Configure a VPN instance, and enable the IPv4 address family for the VPN instance on each PE. The configuration of PE1 is used as an example. The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
      
      
      ```
      [~PE1] ip vpn-instance BLUE
      [*PE1-vpn-instance-BLUE] ipv4-family
      [*PE1-vpn-instance-BLUE-af-ipv4] route-distinguisher 100:1
      [*PE1-vpn-instance-BLUE-af-ipv4] vpn-target 100:1 both
      [*PE1-vpn-instance-BLUE-af-ipv4] quit
      [*PE1-vpn-instance-BLUE] quit
      [*PE1] interface gigabitethernet 0/2/0
      [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance BLUE
      [*PE1-GigabitEthernet0/2/0] ip address 192.168.1.1 24
      [*PE1-GigabitEthernet0/2/0] quit
      [*PE1] commit
      ```
   4. Establish an EBGP peer relationship between each PE and the corresponding CE. The configuration of PE1 is used as an example. The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
      
      
      ```
      [~CE1] bgp 65410
      [*CE1-bgp] router-id 11.11.11.11
      [*CE1-bgp] peer 192.168.1.1 as-number 100
      [*CE1-bgp] quit
      [*CE1] commit
      [~PE1] bgp 100
      [*PE1-bgp] router-id 1.1.1.1
      [*PE1-bgp] ipv4-family vpn-instance BLUE
      [*PE1-bgp-VPNA] peer 192.168.1.2 as-number 65410
      [*PE1-bgp-VPNA] import-route direct
      [*PE1-bgp-VPNA] commit
      [*PE1-bgp-VPNA] quit
      [*PE1-bgp] quit
      [*PE1] commit
      ```
   5. Establish an MP-IBGP peer relationship between PEs, and configure a unicast routing protocol between each PE and the corresponding CE to ensure proper routing between them. The configuration of PE1 is used as an example. The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
      
      
      ```
      [~PE1] bgp 100
      [*PE1-bgp] peer 2001:DB8:20::1 as-number 100
      [*PE1-bgp] peer 2001:DB8:20::1 connect-interface LoopBack 1
      [*PE1-bgp] ipv4-family vpnv4
      [*PE1-bgp-af-vpnv4] peer 2001:DB8:20::1 enable
      [*PE1-bgp-af-vpnv4] quit
      [*PE1-bgp] quit
      [*PE1] commit
      ```
   6. Configure basic SRv6 functions and SRv6 SIDs. The configuration of PE1 is used as an example. The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
      
      
      ```
      [~PE1] segment-routing ipv6
      [*PE1-segment-routing-ipv6] encapsulation source-address 2001:db8:10::1
      [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
      [*PE1-segment-routing-ipv6-locator] quit
      [*PE1-segment-routing-ipv6] quit
      [*PE1] bgp 100
      [*PE1-bgp] ipv4-family vpnv4
      [*PE1-bgp-af-ipv4] peer 2001:DB8:20::1 prefix-sid
      [*PE1-bgp-af-ipv4] quit
      [*PE1-bgp] ipv4-family vpn-instance BLUE
      [*PE1-bgp-BLUE] segment-routing ipv6 best-effort
      [*PE1-bgp-BLUE] segment-routing ipv6 locator PE1
      [*PE1-bgp-BLUE] quit
      [*PE1-bgp] quit
      [*PE1] isis 1
      [*PE1-isis-1] segment-routing ipv6 locator PE1 auto-sid-disable
      [*PE1-isis-1] quit
      [*PE1] commit
      ```
   7. Configure basic BIERv6 functions and enable IS-ISv6 for BIERv6. The configuration of PE1 is used as an example. The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
      
      
      ```
      [~PE1] bier
      [*PE1-bier] sub-domain 0 ipv6
      [*PE1-bier-sub-domain-0-ipv6] bfr-id 1
      [*PE1-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
      [*PE1-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
      [*PE1-bier-sub-domain-0-ipv6] end-bier locator PE1 sid 2001:db8:100::3
      [*PE1-bier-sub-domain-0-ipv6] protocol isis
      [*PE1-bier-sub-domain-0-ipv6] quit
      [*PE1-bier] quit
      [*PE1] isis 1
      [*PE1-isis-1] bier enable
      [*PE1-isis-1] quit
      [*PE1] commit
      ```
   8. Establish a BGP MVPN peer relationship between PEs. The configuration of PE1 is used as an example. The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
      
      
      ```
      [~PE1] bgp 100
      [*PE1-bgp] ipv4-family mvpn
      [*PE1-bgp-af-mvpn] peer 2001:DB8:20::1 enable
      [*PE1-bgp-af-mvpn] quit
      [*PE1-bgp] quit
      [*PE1] commit
      ```
   9. Configure multicast traffic forwarding over a BIERv6 I-PMSI tunnel. The configuration of PE1 is used as an example. The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
      
      
      ```
      [~PE1] multicast routing-enable
      [*PE1] multicast mvpn ipv6-underlay 2001:DB8:10::1
      [*PE1] ip vpn-instance BLUE
      [*PE1-vpn-instance-BLUE] ipv4-family
      [*PE1-vpn-instance-BLUE-af-ipv4] multicast routing-enable
      [*PE1-vpn-instance-BLUE-af-ipv4] mvpn
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] vpn-target 1:1 both 
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] sender-enable
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] ipv6 underlay enable
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] src-dt4 locator PE1 sid 2001:DB8:100::2
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] rpt-spt mode
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] ipmsi-tunnel
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn-ipmsi] bier sub-domain 0 bsl 256
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn-ipmsi] quit
      [*PE1-vpn-instance-BLUE-af-ipv4-mvpn] quit
      [*PE1-vpn-instance-BLUE-af-ipv4] quit
      [*PE1-vpn-instance-BLUE] quit
      [*PE1] commit
      ```
   10. Enable PIM on PEs. The configuration of PE1 is used as an example. The configuration of PE2 is similar to that of PE1. For configuration details, see Configuration Files in this section.
       
       
       ```
       [~PE1] interface gigabitethernet 0/2/0
       [*PE1-GigabitEthernet0/2/0] pim sm
       [*PE1-GigabitEthernet0/2/0] quit
       [*PE1] interface Loopback 2
       [*PE1-Loopback2] ip binding vpn-instance BLUE
       [*PE1-Loopback2] ip address 10.1.1.1 255.255.255.255
       [*PE1-Loopback2] pim sm 
       [*PE1-Loopback2] quit
       ```
   11. Configure a unicast routing protocol and enable the multicast function for VPN BLUE and the GTM instance to ensure that multicast routes of the VPN instance are reachable.
       
       
       
       # Configure CE1.
       
       ```
       <HUAWEI> system-view
       [~HUAWEI] sysname CE1
       [*HUAWEI] commit
       [~CE1] multicast routing-enable
       [*CE1] interface gigabitethernet 0/1/0
       [*CE1-GigabitEthernet0/1/0] ip address 192.168.1.2 24
       [*CE1-GigabitEthernet0/1/0] pim sm
       [*CE1-GigabitEthernet0/1/0] quit
       [*CE1] interface gigabitethernet 0/2/0
       [*CE1-GigabitEthernet0/2/0] ip address 192.168.11.2 24
       [*CE1-GigabitEthernet0/2/0] pim sm
       [*CE1-GigabitEthernet0/2/0] quit
       [*CE1] bgp 65410
       [*CE1-bgp] router-id 11.11.11.11
       [*CE1-bgp] peer 192.168.1.1 as-number 100
       [*CE1-bgp] ipv4-family unicast
       [*CE1-bgp-af-ipv4] import-route direct
       [*CE1-bgp-af-ipv4] peer 192.168.1.1 enable
       [*CE1-bgp-af-ipv4] quit
       [*CE1-bgp] quit
       [*CE1] commit
       ```
       
       # Configure CE2.
       
       ```
       <HUAWEI> system-view
       [~HUAWEI] sysname CE2
       [*HUAWEI] commit
       [~CE2] multicast routing-enable
       [~CE2] interface gigabitethernet 0/1/0
       [*CE2-GigabitEthernet0/1/0] ip address 192.168.2.2 24
       [*CE2-GigabitEthernet0/1/0] pim sm
       [*CE2-GigabitEthernet0/1/0] quit
       [*CE2] interface gigabitethernet 0/2/0
       [*CE2-GigabitEthernet0/2/0] ip address 192.168.4.2 24
       [*CE2-GigabitEthernet0/2/0] pim sm
       [*CE2-GigabitEthernet0/2/0] quit
       [*CE2] bgp 65411
       [*CE2-bgp] router-id 12.12.12.12
       [*CE2-bgp] peer 192.168.2.1 as-number 100
       [*CE2-bgp] ipv4-family unicast
       [*CE2-bgp-af-ipv4] peer 192.168.2.1 enable
       [*CE2-bgp-af-ipv4] quit
       [*CE2-bgp] quit
       [*CE2] commit
       ```
2. Enable PIM on the public network interface of PE2.
   
   
   ```
   [~PE2] interface gigabitethernet 0/2/0
   [~PE2-GigabitEthernet0/2/0] pim sm
   [*PE2-GigabitEthernet0/2/0] quit
   [*PE2-GigabitEthernet0/2/0] commit
   ```
3. Configure an RP to serve the NG MVPN extranet group.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] pim
   [*CE1-pim] static-rp 10.1.1.1
   [*CE1-pim] quit
   [*CE1] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] pim vpn-instance BLUE
   [*PE1-pim-BLUE] static-rp 10.1.1.1
   [*PE1-pim-BLUE] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] pim
   [*PE2-pim] static-rp 10.1.1.1
   [*PE2-pim] quit
   [*PE2] pim vpn-instance BLUE
   [*PE2-pim-BLUE] static-rp 10.1.1.1
   [*PE2-pim-BLUE] quit
   [*PE2] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] pim
   [*CE2-pim] static-rp 10.1.1.1
   [*CE2-pim] quit
   [*CE2] commit
   ```
4. Configure local leaking of unicast routes for the public network instance on PE2, and specify VPN BLUE as the VPN instance to which the outbound interfaces of the unicast routes destined for the public network RP and source belong.
   
   
   ```
   [~PE2] ip route-static 10.1.1.1 255.255.255.255 vpn-instance BLUE 10.11.1.0
   [*PE2] ip route-static 192.168.11.0 255.255.255.255 vpn-instance BLUE 10.11.1.0
   [*PE2] multicast extranet receive-vpn-instance public enable
   [*PE2] commit
   ```
5. Verify the configuration.
   
   
   
   By checking the configuration result, you can verify that the receiver in the GTM instance receives multicast data from the multicast source in VPN BLUE.
   
   Run the **display pim routing-table** command on PE2 to check information about the PIM routing table. The following command output shows PIM routing entries of VPN BLUE whose receivers belong to the public network instance.
   
   ```
   [~PE2] display pim vpn-instance BLUE routing-table extranet receive-vpn-instance all
   ```
   ```
    VPN-Instance: BLUE 
    Total matched 1 (*, G) entry; 1 (S, G) entry
   
    (*, 228.0.0.1)
        RP: 10.1.1.1 
        Protocol: pim-sm, Flag: WC EXTRANWET 
        UpTime: 00:47:55
        Upstream interface: through-BGP, Refresh time: 00:47:55
            Upstream neighbor: 1.1.1.1
            RPF prime neighbor: 1.1.1.1
        Downstream interface(s) information:
        Total number of downstreams:none  
   
        Extranet receiver(s): 1
           1: _public_
        
    
    (192.168.11.0, 228.0.0.1)
        RP: 10.1.1.1 
        Protocol: pim-sm, Flag: SPT ACT 
        UpTime: 06:18:43
        Upstream interface: throught-BGP, Refresh time: 06:18:43
            Upstream neighbor: 1.1.1.1
            RPF prime neighbor: 1.1.1.1
        Downstream interface(s) information:
        Total number of downstreams: none
   
        Extranet receiver(s): 1
           1: _public_
   ```
   
   Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command on PE2 to check information about its PIM routing table. The following command output shows that the upstream interface of the RPF route selected by the PIM entry with 228.0.0.1 as the group address belongs to VPN BLUE.
   
   ```
   [~PE2] display pim routing-table 228.0.0.1 extranet source-vpn-instance vpn-instance BLUE
    VPN-Instance: public net 
    Total matched 1 (*, G) entry; 1 (S, G) entry
   
    (*, 228.0.0.1)
        RP: 10.1.1.1 
        Protocol: pim-sm, Flag: WC EXTRANWET 
        UpTime: 00:47:55
        Upstream interface: MCAST_Extranet(BLUE), Refresh time: 00:47:55
            Upstream neighbor: 1.1.1.1
            RPF prime neighbor: 1.1.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/2/0
                Protocol: pim-sm, UpTime: 00:47:55, Expires: 00:02:34
        
    (192.168.11.0, 228.0.0.1)
        RP: 10.1.1.1 
        Protocol: pim-sm, Flag: SPT ACT 
        UpTime: 06:18:43
        Upstream interface: MCAST_Extranet(BLUE), Refresh time: 06:18:43
            Upstream neighbor: 1.1.1.1
            RPF prime neighbor: 1.1.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/2/0
                Protocol: pim-sm, UpTime: 00:47:57, Expires: 00:02:32
   ```
   
   Run the **display multicast routing-table** command on PE2 to check information about the multicast routing table. The following command output shows that the upstream interface of the RPF route selected by the multicast route entry with 228.0.0.1 as the group address belongs to VPN BLUE.
   
   ```
   [~PE2] display multicast routing-table extranet source-vpn-instance vpn-instance BLUE
   ```
   ```
   Multicast routing table of VPN instance: _public_
    Total 0 (*, G) entry; 1 (S, G) entry, 1 matched
    
    00001: (192.168.11.0, 228.0.0.1)
          Uptime: 00:42:23     
          Upstream Interface: MCAST_Extranet(BLUE)
          List of 1 downstream interface
              1: GigabitEthernet0/2/0
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  multicast routing-enable
  #
  multicast mvpn ipv6-underlay 2001:DB8:10::1
  #
  ip vpn-instance BLUE
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 import-extcommunity
    multicast routing-enable
    mvpn
     vpn-target 1:1 export-extcommunity
     vpn-target 1:1 import-extcommunity
     ipv6 underlay enable
     sender-enable
     src-dt4 locator PE1 sid 2001:DB8:100::2
     rpt-spt mode
     ipmsi-tunnel
      bier sub-domain 0 bsl 256
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:10::1
   locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0001.00
   bier enable
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1 auto-sid-disable
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::2/96
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance BLUE
   ipv6 enable
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface LoopBack1
    ipv6 enable
    ipv6 address 2001:DB8:10::1/128
    isis ipv6 enable 1
  #
  interface LoopBack2
   ip binding vpn-instance BLUE
   ip address 10.1.1.1 255.255.255.255
   pim sm
  #
  bgp 100
   router-id 1.1.1.1
   peer 192.168.1.2 as-number 65410
   peer 2001:DB8:20::1 as-number 100
   peer 2001:DB8:20::1 connect-interface LoopBack1
   #
   ipv4-family unicast 
     undo synchronization 
     peer 192.168.1.2 enable 
     peer 2001:DB8:20::1 enable 
    # 
   ipv4-family mvpn
    policy vpn-target
    peer 2001:DB8:20::1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:20::1 enable
    peer 2001:DB8:20::1 prefix-sid
   #
   ipv4-family vpn-instance BLUE
    import-route direct
    segment-routing ipv6 locator PE1
    segment-routing ipv6 best-effort
    peer 192.168.1.2 as-number 65410
  #
  pim vpn-instance BLUE
   static-rp 10.1.1.1
  #
  bier
   sub-domain 0 ipv6       
    bfr-id 1
    bfr-prefix interface LoopBack1       
    protocol isis     
    end-bier locator PE1 sid 2001:DB8:100::3  
    encapsulation-type ipv6 bsl 256 max-si 0
  #  
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  multicast routing-enable
  #
  multicast extranet receive-vpn-instance public enable
  #
  multicast mvpn ipv6-underlay 2001:DB8:20::1
  #
  ip route-static 10.1.1.1 255.255.255.255 vpn-instance BLUE 10.11.1.0
  ip route-static 192.168.11.0 255.255.255.255 vpn-instance BLUE 10.11.1.0
  #
  ip vpn-instance BLUE
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 import-extcommunity
    multicast routing-enable
    mvpn
     vpn-target 1:1 export-extcommunity
     vpn-target 1:1 import-extcommunity
     ipv6 underlay enable
     c-multicast signaling bgp
     rpt-spt mode
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:20::1
   locator PE2 ipv6-prefix 2001:DB8:200:: 64 static 32
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0002.00
   bier enable
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2 auto-sid-disable
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::2/96
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  interface LoopBack1
    ipv6 enable
    ipv6 address 2001:DB8:20::1/128
    isis ipv6 enable 
  #
  interface LoopBack2 
    ip binding vpn-instance BLUE 
    ip address 20.1.1.1 255.255.255.0 
  #
  bgp 100
   router-id 1.1.1.2
   peer 192.168.2.2 as-number 65411
   peer 2001:DB8:10::1 as-number 100
   peer 2001:DB8:10::1 connect-interface LoopBack1
   #
   ipv4-family unicast 
     undo synchronization 
     peer 192.168.2.2 enable 
     peer 2001:DB8:10::1 enable 
   # 
   ipv4-family mvpn
    policy vpn-target
    peer 2001:DB8:10::1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:10::1 enable
    peer 2001:DB8:10::1 prefix-sid
   #
   ipv4-family vpn-instance BLUE
    segment-routing ipv6 locator PE2
    segment-routing ipv6 best-effort
  #
  pim
   static-rp 10.1.1.1
  #
  pim vpn-instance BLUE
   static-rp 10.1.1.1
  #
  bier
   sub-domain 0 ipv6       
    bfr-id 2
    bfr-prefix interface LoopBack1       
    protocol isis     
    end-bier locator PE2 sid 2001:DB8:200::3  
    encapsulation-type ipv6 bsl 256 max-si 0
  # 
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.11.2 255.255.255.0
   pim sm
  #
  bgp 65410
   router-id 11.11.11.11
   peer 192.168.1.1 as-number 100 
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 192.168.1.1 enable
  #
  pim
   static-rp 10.1.1.1
  #
  return 
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.4.2 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
  #
  bgp 65411
   router-id 12.12.12.12
   peer 192.168.2.1 as-number 100 
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.2.1 enable
  #
  pim
   static-rp 10.1.1.1
  #
  return 
  ```