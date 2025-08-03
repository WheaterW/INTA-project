Example for Configuring IPv4 PIM IPsec
======================================

On a PIM-SM network, you can configure IPv4 PIM IPsec on the interfaces setting up PIM neighbor relationships to protect the devices against forged IPv4 PIM protocol packets.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172366945__fig_dc_vrp_multicast_cfg_224901), the multicast service is deployed. Device A and Device B set a PIM neighbor relationship and exchange IPv4 PIM protocol packets to maintain their neighbor relationship and multicast routing entries. If forged IPv4 PIM protocol packets exist, Device A and Device B may not forward multicast data properly. To prevent attacks, configure IPv4 PIM IPsec on the interfaces of Device A and Device B to authenticate the IPv4 PIM protocol packets transmitted between them. In this manner, malicious attacks are prevented, and users can receive multicast data from multicast sources.

Device B exchanges IGMP protocol packets with its connected users to maintain their member relationships. To protect Device B against forged IGMP protocols packets, configure IGMP IPsec on interfaces that connect Device B to users.

**Figure 1** Configuring IPv4 PIM IPsec  
![](images/fig_dc_vrp_multicast_cfg_224901.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| Device A | Interface1: GE 0/1/0 | 192.168.1.1/24 |
| Interface2: GE 0/1/1 | 192.168.2.1/24 |
| Loopback0 | 1.1.1.1/32 |
| Device B | Interface1: GE 0/1/0 | 192.168.2.2/24 |
| Interface2: GE 0/1/1 | 192.168.3.1/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each Router interface and configure IS-IS to implement IP interworking.
2. Enable multicast routing on each Router and PIM-SM on each Router interface.
3. Enable IGMP on interfaces connecting Routers to hosts.
4. Configure C-BSRs and C-RPs to implement dynamic RP selection.
5. Configure basic IPsec functions.
6. Configure global IPv4 PIM IPsec to authenticate unicast IPv4 PIM protocol packets.
7. Configure IPv4 PIM IPsec on interfaces to authenticate multicast IPv4 PIM protocol packets.
8. Configure IGMP IPsec on interfaces to authenticate IGMP protocol packets.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast source address: 192.168.1.2
* Multicast group address: 225.1.1.1
* Security association (SA) name: sa1

#### Procedure

1. Assign an IP address to each Router interface and configure IS-IS to implement IP interworking.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 192.168.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ip address 192.168.2.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface LoopBack 0
   ```
   ```
   [*DeviceA-LoopBack0] ip address 1.1.1.1 255.255.255.255
   ```
   ```
   [*DeviceA-LoopBack0] isis enable 1
   ```
   ```
   [*DeviceA-LoopBack0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ip address 192.168.2.2 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] ip address 192.168.3.1 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceB] commit
   ```
2. Enable multicast routing on each Router and PIM-SM on each Router interface. Enable IGMP on interfaces connecting Routers to hosts.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] multicast routing-enable
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface LoopBack 0
   ```
   ```
   [*DeviceA-LoopBack0] pim sm
   ```
   ```
   [*DeviceA-LoopBack0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] multicast routing-enable
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] igmp enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] igmp static-group 225.1.1.1 source 192.168.1.2
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceB] commit
   ```
3. Configure dynamic RP selection.
   
   
   
   # Specify loopback 0 on Device A as a C-BSR and a C-RP.
   
   ```
   [~DeviceA] pim
   ```
   ```
   [*DeviceA-pim] c-bsr Loopback 0
   ```
   ```
   [*DeviceA-pim] c-rp Loopback 0
   ```
   ```
   [*DeviceA-pim] quit
   ```
   ```
   [*DeviceA] commit
   ```
4. Configure basic IPsec functions.
   
   
   * Configure the IPsec transmission mode.
     
     # Configure Device A.
     
     ```
     [~DeviceA] ipsec proposal aaa
     ```
     ```
     [*DeviceA-ipsec-proposal-aaa] transform ah
     ```
     ```
     [*DeviceA-ipsec-proposal-aaa] encapsulation-mode transport
     ```
     ```
     [*DeviceA-ipsec-proposal-aaa] quit
     ```
     ```
     [*DeviceA] commit
     ```
     
     # Configure Device B.
     
     ```
     [~DeviceB] ipsec proposal aaa
     ```
     ```
     [*DeviceB-ipsec-proposal-aaa] encapsulation-mode transport
     ```
     ```
     [*DeviceB-ipsec-proposal-aaa] transform ah
     ```
     ```
     [*DeviceB-ipsec-proposal-aaa] quit
     ```
     ```
     [*DeviceB] commit
     ```
   * Configure IPsec SAs.
     
     # Configure Device A.
     
     ```
     [~DeviceA] ipsec sa sa1
     ```
     ```
     [*DeviceA-ipsec-sa-sa1] proposal aaa
     ```
     ```
     [*DeviceA-ipsec-sa-sa1] sa spi inbound ah 300
     ```
     ```
     [*DeviceA-ipsec-sa-sa1] sa spi outbound ah 300
     ```
     ```
     [*DeviceA-ipsec-sa-sa1] sa string-key inbound ah YsHsjx_202206
     ```
     ```
     [*DeviceA-ipsec-sa-sa1] sa string-key outbound ah YsHsjx_202206
     ```
     ```
     [*DeviceA-ipsec-sa-sa1] quit
     ```
     ```
     [*DeviceA] commit
     ```
     
     # Configure Device B.
     
     ```
     [~DeviceB] ipsec sa sa1
     ```
     ```
     [*DeviceB-ipsec-sa-sa1] proposal aaa
     ```
     ```
     [*DeviceB-ipsec-sa-sa1] sa spi inbound ah 300
     ```
     ```
     [*DeviceB-ipsec-sa-sa1] sa spi outbound ah 300
     ```
     ```
     [*DeviceB-ipsec-sa-sa1] sa string-key inbound ah YsHsjx_202206
     ```
     ```
     [*DeviceB-ipsec-sa-sa1] sa string-key outbound ah YsHsjx_202206
     ```
     ```
     [*DeviceB-ipsec-sa-sa1] quit
     ```
     ```
     [*DeviceB] commit
     ```
5. Configure global IPv4 PIM IPsec to authenticate unicast IPv4 PIM protocol packets.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] pim
   ```
   ```
   [*DeviceA-pim] ipsec unicast-message sa sa1
   ```
   ```
   [*DeviceA-pim] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] pim
   ```
   ```
   [*DeviceB-pim] ipsec unicast-message sa sa1
   ```
   ```
   [*DeviceB-pim] quit
   ```
   ```
   [*DeviceB] commit
   ```
6. Configure IPv4 PIM IPsec on interfaces.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] pim ipsec sa sa1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] pim ipsec sa sa1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
7. Configure IGMP IPsec on interfaces.
   
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] igmp ipsec sa sa1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceB] commit
   ```
8. Verify the configuration.
   
   
   
   # Configure the multicast source 192.168.1.2 to send data to the multicast group 225.1.1.1. Configure a receiver to send an IGMP Report message to join the multicast group. Ensure that the receiver receives data from the multicast source. Run the **display pim interface verbose** command. The command outputs show detailed configurations of IPv4 PIM IPsec on interfaces between Routers.
   
   ```
   [~DeviceA] display pim interface gigabitethernet 0/1/1 verbose
   ```
   ```
    VPN-Instance: public net
    Interface: GigabitEthernet0/1/1, 192.168.2.1
        PIM version: 2
        PIM mode: Sparse
        PIM state: up
        PIM DR: 192.168.2.1 (local)
        PIM DR Priority (configured): 1
        PIM neighbor count: 0
        PIM hello interval: 30 s
        PIM LAN delay (negotiated): 500 ms
        PIM LAN delay (configured): 500 ms
        PIM hello override interval (negotiated): 2500 ms
        PIM hello override interval (configured): 2500 ms
        PIM Silent: disabled
        PIM neighbor tracking (negotiated): disabled
        PIM neighbor tracking (configured): disabled
        PIM generation ID: 0x2C24084
        PIM require-GenID: disabled
        PIM hello hold interval: 105 s
        PIM assert hold interval: 180 s
        PIM triggered hello delay: 5 s
        PIM J/P interval: 60 s
        PIM J/P hold interval: 210 s
        PIM BSR domain border: disabled
        PIM BFD: disabled
        PIM dr-switch-delay timer: not configured
        Number of routers on link not using DR priority: 0
        Number of routers on link not using LAN delay: 0
        Number of routers on link not using neighbor tracking: 1
        ACL of PIM neighbor policy: -
        ACL of PIM ASM join policy: -
        ACL of PIM SSM join policy: -
        ACL of PIM join policy: -
        PIM ipsec: enabled(sa-name: sa1)
   ```
   ```
   [~DeviceB] display pim interface gigabitethernet 0/1/0 verbose
   ```
   ```
    VPN-Instance: public net
    Interface: GigabitEthernet0/1/0, 192.168.2.2
        PIM version: 2
        PIM mode: Sparse
        PIM state: up
        PIM DR: 192.168.2.2 (local)
        PIM DR Priority (configured): 1
        PIM neighbor count: 0
        PIM hello interval: 30 s
        PIM LAN delay (negotiated): 500 ms
        PIM LAN delay (configured): 500 ms
        PIM hello override interval (negotiated): 2500 ms
        PIM hello override interval (configured): 2500 ms
        PIM Silent: disabled
        PIM neighbor tracking (negotiated): disabled
        PIM neighbor tracking (configured): disabled
        PIM generation ID: 0x30F1A3DD
        PIM require-GenID: disabled
        PIM hello hold interval: 105 s
        PIM assert hold interval: 180 s
        PIM triggered hello delay: 5 s
        PIM J/P interval: 60 s
        PIM J/P hold interval: 210 s
        PIM BSR domain border: disabled
        PIM BFD: disabled
        PIM dr-switch-delay timer: not configured
        Number of routers on link not using DR priority: 0
        Number of routers on link not using LAN delay: 0
        Number of routers on link not using neighbor tracking: 1
        ACL of PIM neighbor policy: -
        ACL of PIM ASM join policy: -
        ACL of PIM SSM join policy: -
        ACL of PIM join policy: -
        PIM ipsec: enabled(sa-name: sa1)
   ```
   
   # Run the **display igmp interface verbose** command. The command outputs show detailed configurations of IGMP IPsec on interfaces connected to users.
   
   ```
   [~DeviceB] display igmp interface gigabitethernet 0/1/1 verbose
   ```
   ```
   Interface information of VPN-Instance: public net
    Gigabitethernet0/1/1(192.168.3.1):
      IGMP is enabled
      Current IGMP version is 2
      IGMP state: up
      IGMP group policy: none
      IGMP limit: -
      Value of query interval for IGMP (negotiated): -
      Value of query interval for IGMP (configured): 60 s
      Value of other querier timeout for IGMP: 0 s
      Value of maximum query response time for IGMP: 10 s
      Value of last member query time: 2 s
      Value of last member query interval: 1 s
      Value of startup query interval: 15 s
      startup query count: 2
      General query timer expiry (hours:minutes:seconds): 00:00:58
      Querier for IGMP: 192.168.3.1 (this router)
      IGMP activity: 0 joins, 0 leaves
      Robustness (negotiated): -
      Robustness (configured): 2
      Require-router-alert: disabled
      Send-router-alert: enabled
      Ip-source-policy: disabled
      Query Ip-source-policy: disabled
      Prompt-leave: disabled
      SSM-Mapping: disabled
      Startup-query-timer-expiry: off
      Other-querier-present-timer-expiry: off
      IGMP ipsec: enabled(sa-name: sa1)
   ```
   
   The preceding command outputs show the following information: IPv4 PIM IPsec is configured on the downstream interface GE 0/1/1 of Device A and the upstream interface GE 0/1/0 of Device B. IGMP IPsec is configured on the downstream interface GE 0/1/1 of Device B, and the SA name is **sa1**.
   
   # Run the **display pim routing-table** command to check the IPv4 PIM routing table. The command output shows that multicast routing entries exist on Device B.
   
   ```
   [~DeviceB] display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (192.168.1.2, 225.1.1.1)
        RP: 1.1.1.1
        Protocol: pim-sm, Flag: SPT NIIF SG_RCVR
        UpTime: 00:31:41
        Upstream interface: Gigabitethernet0/1/0, Refresh time: 00:31:41
            Upstream neighbor: 192.168.2.1
            RPF prime neighbor: 192.168.2.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: Gigabitethernet0/1/1
                Protocol: static, UpTime: 00:31:41, Expires: -     
   ```
   
   The preceding command output shows that multicast data is received by the receiver.

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  ipsec proposal aaa
   encapsulation-mode transport
   transform ah
  #
  ipsec sa sa1
   proposal aaa
   sa spi inbound ah 300
   sa string-key inbound ah cipher @%@%QV3G<F;#>(tQfj-P_31%&R.v@%@%
   sa spi outbound ah 300
   sa string-key outbound ah cipher @%@%StJa=GZQXOj#,G.F9n^,&R/S@%@%
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0001.00  
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface Gigabitethernet0/1/1
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   pim sm
   pim ipsec sa sa1
   isis enable 1  
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   pim sm
   isis enable 1 
  #
  pim
   c-bsr LoopBack0
   c-rp LoopBack0
   ipsec unicast-message sa sa1
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  ipsec proposal aaa
   encapsulation-mode transport
   transform ah  
  #
  ipsec sa sa1
   proposal aaa
   sa spi inbound ah 300
   sa string-key inbound ah cipher @%@%gbFH@o`[IC!-*3DM![X$&R&.@%@%
   sa spi outbound ah 300
   sa string-key outbound ah cipher @%@%M\a(7*eg-J8r|+'9`_~A&R-C@%@%   
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0002.00     
  #
  interface Gigabitethernet0/1/1
   undo shutdown
   ip address 192.168.3.1 255.255.255.0
   pim sm
   igmp enable
   igmp ipsec sa sa1
   igmp static-group 225.1.1.1 source 192.168.1.2
   isis enable 1
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
   pim ipsec sa sa1
   isis enable 1
  #
  pim
   ipsec unicast-message sa sa1
  #
  return
  ```