Example for Configuring Multicast Traffic Forwarding in a VPN Scenario
======================================================================

This section provides an example for configuring multicast traffic forwarding in a VPN scenario.

#### Networking Requirements

As shown in the following figure, DeviceA resides in AS 65001 and is connected to the Internet and the IPTV multicast source. DeviceB resides in AS 65002 and is connected to the IPTV receiver. The network administrator requires that C-multicast traffic of AS 65001 be forwarded to the user side in AS 65002.

**Figure 1** Configuring multicast traffic forwarding in a VPN scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.

![](figure/en-us_image_0000001199743974.png)


**Table 1** Device interface information
| Device | Interface | IP Address |
| --- | --- | --- |
| DeviceA | Loopback0 | 1.1.1.1/32 |
| GE0/2/0 | 10.1.1.1/24 |
| GE0/1/0 | 192.168.1.1/24 |
| DeviceB | Loopback0 | 3.3.3.3/32 |
| GE0/1/0 | 10.1.3.1/24 |
| GE0/2/0 | 10.1.1.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on each device.
2. Configure a VPN instance on each device.
3. Establish MBGP peer relationships to generate inter-AS multicast routes.
4. Configure routes.
5. Enable the multicast function on each device.
6. Configure the BSR boundary on inter-AS connected interfaces.
7. Verify the configuration.

#### Procedure

1. Assign an IP address and mask to each interface on each device according to [Table 1](#EN-US_TASK_0000001215650505__table_01). For configuration details, see Configuration Files in this section.
2. Configure a VPN instance on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ip vpn-instance VPNA
   [*DeviceA-vpn-instance-VPNA] ipv4-family
   [*DeviceA-vpn-instance-VPNA-af-ipv4] route-distinguisher 100:1
   [*DeviceA-vpn-instance-VPNA-af-ipv4] vpn-target 3:3
   [*DeviceA-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   [*DeviceA-vpn-instance-VPNA-af-ipv4] quit
   [*DeviceA-vpn-instance-VPNA] quit
   [*DeviceA] interface gigabitethernet 0/2/0
   [*DeviceA-GigabitEthernet0/2/0] ip binding vpn-instance VPNA
   [*DeviceA-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   [*DeviceA-GigabitEthernet0/2/0] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ip vpn-instance VPNA
   [*DeviceB-vpn-instance-VPNA] ipv4-family
   [*DeviceB-vpn-instance-VPNA-af-ipv4] route-distinguisher 300:1
   [*DeviceB-vpn-instance-VPNA-af-ipv4] vpn-target 3:3
   [*DeviceB-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   [*DeviceB-vpn-instance-VPNA-af-ipv4] quit
   [*DeviceB-vpn-instance-VPNA] quit
   [*DeviceB] interface gigabitethernet 0/2/0
   [*DeviceB-GigabitEthernet0/2/0] ip binding vpn-instance VPNA
   [*DeviceB-GigabitEthernet0/2/0] ip address 10.1.1.2 24
   [*DeviceB-GigabitEthernet0/2/0] quit
   [*DeviceB] commit
   ```
3. Configure IS-IS routes.
   
   
   
   # Configure IS-IS routes on DeviceA.
   
   ```
   [~DeviceA] isis 2 vpn-instance VPNA
   [*DeviceA-isis-2] is-level level-2
   [*DeviceA-isis-2] cost-style wide
   [*DeviceA-isis-2] network-entity 32.0000.0001.0000.00
   [*DeviceA-isis-2] quit
   [*DeviceA] commit
   ```
   
   # Configure IS-IS routes on DeviceB.
   
   ```
   [~DeviceB] isis 2 vpn-instance VPNA
   [*DeviceB-isis-2] is-level level-2
   [*DeviceB-isis-2] cost-style wide
   [*DeviceB-isis-2] network-entity 32.0000.0003.0000.00
   [*DeviceB-isis-2] quit
   [*DeviceB] commit
   ```
4. Configure BGP, enable MBGP, establish an MBGP peer relationship, and import routes.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 65001
   [*DeviceA-bgp] vpn-instance VPNA
   [*DeviceA-bgp-instance-VPNA] peer 3.3.3.3 as-number 65002
   [*DeviceA-bgp-instance-VPNA] peer 3.3.3.3 connect-interface LoopBack0
   [*DeviceA-bgp-instance-VPNA] quit
   [*DeviceA-bgp] ipv4-multicast vpn-instance VPNA
   [*DeviceA-bgp-multicast-VPNA] import-route direct
   [*DeviceA-bgp-multicast-VPNA] import-route isis 2
   [*DeviceA-bgp-multicast-VPNA] peer 3.3.3.3 enable
   [*DeviceA-bgp-multicast-VPNA] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 65002
   [*DeviceB-bgp] vpn-instance VPNA
   [*DeviceB-bgp-instance-VPNA] peer 1.1.1.1 as-number 65001 
   [*DeviceB-bgp-instance-VPNA] peer 1.1.1.1 connect-interface LoopBack0
   [*DeviceB-bgp-instance-VPNA] quit
   [*DeviceB-bgp] ipv4-multicast vpn-instance VPNA
   [*DeviceB-bgp-multicast-VPNA] import-route direct
   [*DeviceB-bgp-multicast-VPNA] import-route isis 2
   [*DeviceB-bgp-multicast-VPNA] peer 1.1.1.1 enable
   [*DeviceB-bgp-multicast-VPNA] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
5. Enable the multicast function on the devices and on involved interfaces of the devices.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface GigabitEthernet 0/1/0
   [*DeviceA-GigabitEthernet0/1/0] ip binding vpn-instance VPNA
   [*DeviceA-GigabitEthernet0/1/0] pim sm
   [*DeviceA-GigabitEthernet0/1/0] isis enable 2 
   [*DeviceA-GigabitEthernet0/1/0] quit
   [*DeviceA] interface GigabitEthernet 0/2/0
   [*DeviceA-GigabitEthernet0/2/0] ip binding vpn-instance VPNA
   [*DeviceA-GigabitEthernet0/2/0] pim sm
   [*DeviceA-GigabitEthernet0/2/0] isis enable 2
   [*DeviceA-GigabitEthernet0/2/0] quit
   [*DeviceA] interface loopback 0
   [*DeviceA-LoopBack1] ip binding vpn-instance VPNA
   [*DeviceA-LoopBack1] isis enable 2
   [*DeviceA-LoopBack1] pim sm
   [*DeviceA-LoopBack1] commit
   [~DeviceA-LoopBack1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] multicast routing-enable
   [*DeviceB] interface GigabitEthernet 0/2/0
   [*DeviceB-GigabitEthernet0/1/0] ip binding vpn-instance VPNA
   [*DeviceB-GigabitEthernet0/1/0] pim sm
   [*DeviceB-GigabitEthernet0/1/0] isis enable 2
   [*DeviceB-GigabitEthernet0/1/0] quit
   [*DeviceB] interface GigabitEthernet 0/1/0
   [*DeviceB-GigabitEthernet0/3/0] ip binding vpn-instance VPNA
   [*DeviceB-GigabitEthernet0/3/0] pim sm
   [*DeviceB-GigabitEthernet0/3/0] igmp enable
   [*DeviceB-GigabitEthernet0/3/0] igmp version 3
   [*DeviceB-GigabitEthernet0/3/0] isis enable 2
   [*DeviceB-GigabitEthernet0/3/0] quit
   [*DeviceB] interface loopback 0
   [*DeviceB-LoopBack1] ip binding vpn-instance VPNA
   [*DeviceB-LoopBack1] isis enable 2
   [*DeviceB-LoopBack1] pim sm
   [*DeviceB-LoopBack1] commit
   [~DeviceB-LoopBack1] quit
   ```
6. Configure the C-BSR and C-RP in each AS.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] pim vpn-instance VPNA
   [*DeviceA-pim-VPNA] c-bsr loopback 0
   [*DeviceA-pim-VPNA] c-rp loopback 0
   [*DeviceA-pim-VPNA] commit
   [~DeviceA-pim-VPNA] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] pim vpn-instance VPNA
   [*DeviceB-pim-VPNA] c-bsr loopback 0
   [*DeviceB-pim-VPNA] c-rp loopback 0
   [*DeviceB-pim-VPNA] commit
   [~DeviceB-VPNA] quit
   ```
7. Configure the BSR boundary on inter-AS connected interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA] interface GigabitEthernet0/2/0
   [*DeviceA-GigabitEthernet0/2/0] pim bsr-boundary
   [*DeviceA-GigabitEthernet0/2/0] commit
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface GigabitEthernet 0/2/0
   [*DeviceB-GigabitEthernet0/1/0] pim bsr-boundary
   [*DeviceB-GigabitEthernet0/1/0] commit
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
8. Establish an MSDP peer relationship.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] msdp vpn-instance VPNA
   [*DeviceA-msdp] peer 10.1.1.2 connect-interface GigabitEthernet 0/2/0
   [*DeviceA-msdp] commit
   [~DeviceA-msdp] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] msdp vpn-instance VPNA
   [*DeviceB-msdp] peer 10.1.1.1 connect-interface GigabitEthernet 0/2/0
   [*DeviceB-msdp] commit
   [~DeviceB-msdp] quit
   ```
9. Verify the configuration.
   
   
   
   # Run the **display msdp brief** command to check whether an MSDP peer relationship is established between the devices. For example, the brief information about the MSDP peer relationship displayed on DeviceA is as follows:
   
   ```
   [~DeviceA] display msdp brief
   ```
   ```
   MSDP Peer Brief Information of VPN-Instance: public net
     Configured   Up           Listen       Connect      Shutdown     Down
     2            2            0            0            0            0
   
     Peer's Address   State     Up/Down time    AS          SA Count   Reset Count
     10.1.1.2         Up        01:04:26        65002       0          0
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable 
  #
  isis 2 vpn-instance VPNA
   is-level level-2
   cost-style wide
   network-entity 32.0000.0001.0000.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.1.1 255.255.255.0
   pim sm
   isis enable 2
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 10.1.1.1 255.255.255.0
   pim bsr-boundary
   pim sm
   isis enable 2
  #
  interface LoopBack0
   ip binding vpn-instance VPNA
   ip address 1.1.1.1 255.255.255.255
   pim sm
   isis enable 2
  #
  bgp 65001
   private-4-byte-as enable
   #
   ipv4-family unicast
   undo synchronization
   #
   ipv4-family vpnv4
    policy vpn-target
   #
   vpn-instance VPNA
    peer 3.3.3.3 as-number 65002
    peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-multicast vpn-instance VPNA
    import-route direct
    import-route isis 2
    peer 3.3.3.3 enable
  #
  pim vpn-instance VPNA
   c-bsr LoopBack0
   c-rp LoopBack0
  #
  msdp vpn-instance VPNA
   peer 10.1.1.2 connect-interface GigabitEthernet0/2/0
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 300:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable  
  #
  isis 2 vpn-instance VPNA
   is-level level-2
   cost-style wide
   network-entity 32.0000.0003.0000.00
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 10.1.1.2 255.255.255.0
   pim bsr-boundary
   pim sm
   isis enable 2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 10.1.3.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
   isis enable 2
  #
  interface LoopBack0
   ip binding vpn-instance VPNA
   ip address 3.3.3.3 255.255.255.255
   pim sm
   isis enable 2
  #
  bgp 65002
   private-4-byte-as enable
   #
   ipv4-family unicast
   undo synchronization
   #
   ipv4-family vpnv4
    policy vpn-target
   #
   vpn-instance VPNA
    peer 1.1.1.1 as-number 65001
    peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-multicast vpn-instance VPNA
    import-route direct
    import-route isis 2
    peer 1.1.1.1 enable
  #
  pim vpn-instance VPNA
   c-bsr LoopBack0
   c-rp LoopBack0
  #
  msdp vpn-instance VPNA
   peer 10.1.1.1 connect-interface GigabitEthernet0/2/0
  #
  return
  ```