Example for Configuring Steering of Traffic Carried by a Dual-Device Hot Backup Protection Tunnel into an SR-MPLS BE Tunnel
===========================================================================================================================

This section provides an example for configuring steering of traffic carried by a dual-device hot backup protection tunnel into an SR-MPLS BE tunnel.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0175388114__fig_dc_ne_cfg_rui_003101), users are connected to BRAS1 and BRAS2 through SW1 (LAN switch). The two BRASs run the Virtual Router Redundancy Protocol (VRRP) to determine the master and backup status. Basic user access functions are configured on BRAS1 and BRAS2 so that users can go online from the master device. If the master device or the link on the network or user side of the master device fails, service traffic needs to be quickly switched to the backup device.

In the dual-device hot backup scenario, configure an SR-MPLS BE protection tunnel for route recursion so that user traffic can be forwarded over the SR-MPLS BE protection tunnel. This improves the robustness of dual-device hot backup. In this example, an IPv6 address pool is used.

**Figure 1** Configuring steering of traffic carried by a dual-device hot backup protection tunnel into an SR-MPLS BE tunnel![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/1 and GE 0/2/0, respectively.


  
![](images/fig_dc_ne_cfg_rui_003101.png)  

| **Device** | **Interface** | **IP Address** |
| --- | --- | --- |
| BRAS1 | GE 0/2/1.1 | 10.1.1.1/24 (address of the interface running VRRP  and BFD peer) |
| BRAS1 | GE0/2/1.2 | 10.1.10.1/24 (address of the interface running BFD link) |
| BRAS1 | GE0/2/1.333 | Interface through which users go online |
| BRAS1 | Loopback1 | 10.1.2.1/32 (IP address of BRAS1's interface with an RBS deployed) |
| BRAS2 | GE 0/2/1.1 | 10.1.1.2/24 (address of the interface running VRRP and BFD peer) |
| BRAS2 | GE0/2/1.332 | Interface through which users go online |
| BRAS2 | Loopback1 | 10.1.2.2/32 (address of BRAS2's interface with an RBS deployed) |
| SW1 | GE0/2/1.2 | 10.1.10.2/24 (address of the interface running BFD link) |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VRRP and BFD on the access side of the master and backup BRASs (BRAS1 and BRAS2) to determine the master/backup status and implement fault association.
2. Configure basic user access functions and ensure that the two devices for backup have the same configuration. The configuration includes configuring AAA schemes, a RADIUS server group, and an IPv6 address pool.
3. Configure an AAA domain and bind the IPv6 address pool to it.
4. Configure a BAS interface and enable IPv6 on the interface.
5. Configure a remote backup service (RBS) and a remote backup policy (RBP).
6. Configure MPLS and OSPF.
7. Enable segment routing (SR).
8. Configure a prefix segment ID (SID) for the IP address of a loopback interface.
9. Configure a protection tunnel between the master and backup devices. In this example, an SR-MPLS BE protection tunnel defined by a tunnel policy is configured.

#### Data Preparation

To complete the configuration, you need the following data:

* VRRP parameters such as a VRID and preemption delay
* BFD parameters such as the local and remote discriminators and expected minimum interval at which BFD control packets are sent and received
* IP address of each interface on BRAS1 and BRAS2
* Backup ID, which works together with an RBS to identify an RBP to which users belong
* User access parameters

#### Procedure

1. Configure VRRP and BFD on the access side of the master and backup BRASs (BRAS1 and BRAS2) to determine the master/backup status and implement fault association.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the access-side aggregation switch does not support BFD, skip this step. This example describes only the configuration on this product. For details about how to configure BFD sessions on the switch, see the related manual.
   
   
   
   # Configure a BFD session named **bfd-peer** between BRAS1 and BRAS2. The BFD session shares the same link with the access-side VRRP group. The following uses BRAS1 as an example. The configuration of BRAS2 is similar to that of BRAS1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS1
   [*HUAWEI] commit
   [~BRAS1] bfd
   [*BRAS1] quit
   [*BRAS1]  bfd bfd-peer bind peer-ip 10.1.1.2 source-ip 10.1.1.1
   [*BRAS1-bfd-session-bfd-peer] discriminator local 1
   [*BRAS1-bfd-session-bfd-peer] discriminator remote 1
   [*BRAS1-bfd-session-bfd-peer] commit
   [~BRAS1-bfd-session-bfd-peer] quit
   ```
   
   # Configure a BFD session **bfd-link** between BRAS1 and SW1.
   
   ```
   [~BRAS1] interface GigabitEthernet0/2/1.2
   [*BRAS1-GigabitEthernet0/2/1.2] vlan-type dot1q 2
   [*BRAS1-GigabitEthernet0/2/1.2] ip address 10.1.10.1 255.255.255.0
   [*BRAS1-GigabitEthernet0/2/1.2] commit
   [~BRAS1-GigabitEthernet0/2/1.2] quit
   [~BRAS1]bfd bfd-link bind peer-ip 192.168.2.2 source-ip 192.168.2.1
   [*BRAS1-bfd-session-bfd-link] discriminator local 2
   [*BRAS1-bfd-session-bfd-link] discriminator remote 2
   [*BRAS1-bfd-session-bfd-link] commit 
   [~BRAS1-bfd-session-bfd-link] quit 
   ```
   
   # Configure a VRRP group on an interface (GE0/2/1.1 is used as an example), and configure VRRP to track the BFD session and network-side interface status.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/2/1.1 
   [*BRAS1-GigabitEthernet0/2/1.1] vlan-type dot1q 1 
   [*BRAS1-GigabitEthernet0/2/1.1] ip address 10.1.1.1 255.255.255.0 
   [*BRAS1-GigabitEthernet0/2/1.1] vrrp vrid 1 virtual-ip 10.1.1.100 
   [*BRAS1-GigabitEthernet0/2/1.1] admin-vrrp vrid 1 
   [*BRAS1-GigabitEthernet0/2/1.1] vrrp vrid 1 priority 120 
   [*BRAS1-GigabitEthernet0/2/1.1] vrrp vrid 1 preempt-mode timer delay 60 
   [*BRAS1-GigabitEthernet0/2/1.1] vrrp vrid 1 track interface GigabitEthernet 0/2/0 reduced 50 
   [*BRAS1-GigabitEthernet0/2/1.1] vrrp vrid 1 track bfd-session 2 link
   [*BRAS1-GigabitEthernet0/2/1.1] commit
   [~BRAS1-GigabitEthernet0/2/1.1] quit
   ```
   ```
   [~BRAS2] interface GigabitEthernet 0/2/1.1 
   [*BRAS2-GigabitEthernet0/2/1.1] vlan-type dot1q 1 
   [*BRAS2-GigabitEthernet0/2/1.1] ip address 10.1.1.2 255.255.255.0
   [*BRAS2-GigabitEthernet0/2/1.1] vrrp vrid 1 virtual-ip 10.1.1.100 
   [*BRAS2-GigabitEthernet0/2/1.1] admin-vrrp vrid 1 
   [*BRAS2-GigabitEthernet0/2/1.1] vrrp vrid 1 track bfd-session 1 peer
   [*BRAS2-GigabitEthernet0/2/1.1] commit
   [~BRAS2-GigabitEthernet0/2/1.1] quit
   ```
2. Configure AAA schemes.
   1. Configure an authentication scheme.
      
      
      ```
      [~BRAS1] aaa
      [~BRAS1-aaa] authentication-scheme radius
      [*BRAS1-aaa-authen-radius] authentication-mode radius
      [*BRAS1-aaa-authen-radius] commit
      [~BRAS1-aaa-authen-radius] quit
      ```
   2. Configure an accounting scheme.
      
      
      ```
      [~BRAS1-aaa] accounting-scheme radius
      [*BRAS1-aaa-accounting-radius] accounting-mode radius
      [*BRAS1-aaa-accounting-radius] commit
      [~BRAS1-aaa-accounting-radius] quit
      [~BRAS1-aaa] quit
      ```
3. Configure a RADIUS server group.
   
   
   ```
   [~BRAS1] radius-server group radius
   ```
   ```
   [*BRAS1-radius-radius] radius-server authentication 192.168.7.249 1812
   ```
   ```
   [*BRAS1-radius-radius] radius-server accounting 192.168.7.249 1813
   ```
   ```
   [*BRAS1-radius-radius] radius-server shared-key-cipher YsHsjx_202206 
   ```
   ```
   [*BRAS1-radius-radius] quit
   ```
   ```
   [*BRAS1] commit
   ```
4. Configure an IPv6 address pool.
   1. Configure a local IPv6 prefix pool.
      
      
      ```
      [~BRAS1] ipv6 prefix prefix1 local
      [*BRAS1-ipv6-prefix-pre1] prefix 2001:db8:1::1/64
      [*BRAS1-ipv6-prefix-pre1] commit
      [~BRAS1-ipv6-prefix-pre1] quit
      ```
   2. Configure a local IPv6 address pool named **pool1** and bind the local IPv6 prefix pool to it.
      
      
      ```
      [~BRAS1] ipv6 pool pool1 bas local
      [*BRAS1-ipv6-pool-pool1] prefix prefix1
      [*BRAS1-ipv6-pool-pool1] commit
      [~BRAS1-ipv6-pool-pool1] quit
      ```
5. Configure an AAA domain and bind the IPv6 address pool to it.
   
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] domain dom1
   [*BRAS1-aaa-domain-dom1] authentication-scheme radius
   [*BRAS1-aaa-domain-dom1] accounting-scheme radius
   [*BRAS1-aaa-domain-dom1] radius-server group radius
   [*BRAS1-aaa-domain-dom1] commit
   [~BRAS1-aaa-domain-dom1] ipv6-pool pool1
   [~BRAS1-aaa-domain-dom1] quit
   [~BRAS1-aaa] quit
   ```
6. Configure a BAS interface and enable IPv6 on the interface.
   
   
   ```
   [~BRAS1] interface GigabitEthernet 0/2/1.333
   [~BRAS1-GigabitEthernet0/2/1.333] commit
   [~BRAS1-GigabitEthernet0/2/1.333] ipv6 enable
   [*BRAS1-GigabitEthernet0/2/1.333] ipv6 address auto link-local
   [*BRAS1-GigabitEthernet0/2/1.333] ipv6 nd autoconfig managed-address-flag                                         
   [*BRAS1-GigabitEthernet0/2/1.333] ipv6 nd autoconfig other-flag  
   [*BRAS1-GigabitEthernet0/2/1.333] remote-backup-profile p1
   [*BRAS1-GigabitEthernet0/2/1.333] commit
   [~BRAS1-GigabitEthernet0/2/1.333] user-vlan 1 10 qinq 100
   [~BRAS1-GigabitEthernet0/2/1.333-vlan-1-10-QinQ-100-100] bas
   [~BRAS1-GigabitEthernet0/2/1.333-bas] access-type layer2-subscriber default-domain authentication dom1
   [*BRAS1-GigabitEthernet0/2/1.333-bas] authentication-method-ipv6 bind
   [*BRAS1-GigabitEthernet0/2/1.333-bas] commit
   [~BRAS1-GigabitEthernet0/2/1.333-bas] quit
   [~BRAS1-GigabitEthernet0/2/1.333] quit
   ```
7. Configure an RBS and an RBP.
   
   
   
   # Configure an IP address for the backup channel. The route needs to be advertised.
   
   ```
   [~BRAS1] interface loopback1
   [*BRAS1-loopback1] ip address 10.1.2.1 255.255.255.255
   [*BRAS1-loopback1] commit
   [~BRAS1-loopback1] ospf prefix-sid index 10
   [~BRAS1-loopback1] quit
   ```
   
   # Configure an RBS.
   
   ```
   [~BRAS1] remote-backup-service rui
   [*BRAS1-rm-backup-srv-rui] peer 10.1.2.2 source 10.1.2.1 port 6001
   [*BRAS1-rm-backup-srv-rui] track interface GigabitEthernet0/2/0
   [*BRAS1-rm-backup-srv-rui] ipv6-pool pool1 
   [*BRAS1-rm-backup-srv-rui] commit
   [~BRAS1-rm-backup-srv-rui] quit
   ```
   
   # Configure an RBP.
   
   ```
   [~BRAS1] remote-backup-profile p1
   [*BRAS1-rm-backup-prf-p1] service-type bras
   [*BRAS1-rm-backup-prf-p1] backup-id 101 remote-backup-service rui
   [*BRAS1-rm-backup-prf-p1] peer-backup hot
   [*BRAS1-rm-backup-prf-p1] vrrp-id 1 interface gigabitethernet 0/2/1.1
   [*BRAS1-rm-backup-prf-p1] commit
   [~BRAS1-rm-backup-prf-p1] quit
   ```
   
   # Bind the RBP to the interface through which users go online.
   
   ```
   [~BRAS1] interface gigabitethernet 0/2/1.333
   [*BRAS1-GigabitEthernet0/2/1.333] remote-backup-profile p1
   [*BRAS1-GigabitEthernet0/2/1.333] commit
   [~BRAS1-GigabitEthernet0/2/1.333] quit
   ```
8. Configure MPLS.
   
   
   ```
   [~BRAS1] mpls lsr-id 10.1.2.1
   [~BRAS1] mpls
   [*BRAS1-mpls] commit
   [~BRAS1-mpls] mpls ldp
   [*BRAS1-mpls-ldp] commit
   [~BRAS1-mpls] quit
   ```
9. Configure OSPF.
   
   
   ```
   [~BRAS1] ospf 1
   [*BRAS1-ospf-1] import-route direct                                                             
   [*BRAS1-ospf-1] area 0.0.0.0                                                                    
   [*BRAS1-ospf-1] network 10.1.2.1 0.0.0.0
   [*BRAS1-ospf-1] commit
   [~BRAS1-ospf-1] quit
   ```
10. Enable SR.
    
    
    ```
    [~BRAS1] segment-routing
    [*BRAS1-segment-routing] tunnel-prefer segment-routing
    [*BRAS1-segment-routing] commit
    [~BRAS1-segment-routing] quit
    ```
11. Configure a prefix SID for the IP address of a loopback interface.
    
    
    ```
    [~BRAS1] ospf 1
    [*BRAS1-ospf-1] opaque-capability enable
    [*BRAS1-ospf-1] segment-routing mpls
    [*BRAS1-ospf-1] segment-routing global-block 160000 161000
    [*BRAS1-ospf-1] commit
    [~BRAS1-ospf-1] quit
    [~BRAS1] interface loopback1
    [*BRAS1-loopback1] ospf enable 1 area 1
    [*BRAS1-loopback1] ospf prefix-sid index 10
    [*BRAS1-loopback1] commit
    [~BRAS1-loopback1] quit
    ```
12. Configure a protection tunnel between the master and backup devices.
    * Configure the simplified protection tunnel mode.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Both IPv4 and IPv6 traffic can enter the tunnel.
      
      ```
      [~BRAS1] remote-backup-service rui
      [*BRAS1-rm-backup-srv-rui] protect lsp-tunnel for-all-instance peer-ip 10.1.2.2
      [*BRAS1-rm-backup-srv-rui] commit
      [~BRAS1-rm-backup-srv-rui] quit
      ```
    * Configure a tunnel policy that selects the SR-MPLS BE tunnel as the protection tunnel.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Only IPv4 public network traffic can enter the tunnel.
      
      ```
      [~BRAS1] remote-backup-service rui
      [*BRAS1-rm-backup-srv-rui] protect tnl-policy p1 peer-ip 10.1.2.2
      [*BRAS1] tunnel-policy p1
      [*BRAS1-tunnel-policy-p1] tunnel select-seq sr-lsp load-balance-number 1  
      [*BRAS1-tunnel-policy-p1] commit
      [~BRAS1-tunnel-policy-p1] quit
      [~BRAS1] tunnel-selector s1 permit node  10
      [*BRAS1-tunnel-selector] commit 
      [~BRAS1-tunnel-selector] apply tunnel-policy p1
      [*BRAS1-tunnel-selector] commit
      [~BRAS1-tunnel-selector] quit
      [~BRAS1] bgp 100
      [~BRAS1-bgp] ipv6-family unicast
      [*BRAS1-bgp-af-ipv6] unicast-route recursive-lookup tunnel tunnel-selector s1
      [*BRAS1-bgp-af-ipv6] commit
      [~BRAS1-bgp-af-ipv6] quit
      [~BRAS1-bgp] quit
      ```
13. Verify the configuration.
    
    
    
    # Run the following command. The command output shows that the SR-MPLS BE protection tunnel is successfully established.
    
    ```
    <BRAS1> display segment-routing prefix mpls forwarding 
    ```
    ```
     --------------------------------------------------------------------------------------------------------------
     Segment Routing Prefix MPLS Forwarding Information
     --------------------------------------------------------------------------------------------------------------
     Role : I-Ingress, T-Transit, E-Egress, I&T-Ingress And Transit
     Prefix          Label      OutLabel   Interface         NextHop          Role  MPLSMtu   Mtu     State          
     ---------------------------------------------------------------------------------------------------------------
     10.1.2.1/32     160010     160010     GE0/2/1           10.1.2.2         I&T   ---       1500    Active
     10.1.2.2/32     160030     NULL       Loopback1         10.1.2.1         I&T   ---       1500    Active
    ```

#### Configuration Files

* BRAS1 configuration file
  
  ```
  #
  sysname BRAS1
  #
  bfd
  #
  bfd bfd-peer bind peer-ip 10.1.1.2 source-ip 10.1.1.1
   discriminator local 1
   discriminator remote 1 
  # 
  bfd bfd-link bind peer-ip 10.1.10.2 source-ip 10.1.10.1
   discriminator local 2
   discriminator remote 2 
  #
  mpls lsr-id 10.1.2.1
  #
  mpls
  #
  mpls ldp
  #
  ipv6 prefix prefix1 local
   prefix 2001:db8:1::1/64
  #
  ipv6 pool pool1 bas local
   prefix prefix1
  #
  radius-server group radius
   radius-server shared-key-cipher %^%#glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$:978$$e:TY%^%
   radius-server authentication 192.168.7.249 1812 weight 0
   radius-server accounting 192.168.7.249 1813 weight 0
  #
  aaa
   authentication-scheme radius
   accounting-scheme radius
   #
   domain dom1 
    authentication-scheme radius
    accounting-scheme radius
    radius-server group radius 
    ipv6-pool pool1
  #
  remote-backup-service rui 
   peer 10.1.2.2 source 10.1.2.1 port 6001 
   protect lsp-tunnel for-all-instance peer-ip 10.1.2.2 
   track interface GigabitEthernet0/2/0 
   ipv6-pool pool1
   protect tnl-policy p1 peer-ip 10.1.2.2
  # 
  segment-routing
   tunnel-prefer segment-routing
  #
  tunnel-policy p1
   tunnel select-seq sr-lsp load-balance-number 1
  #
  tunnel-selector s1 permit node 10
   apply tunnel-policy p1
  #
  ospf 1
   import-route direct 
   area 0.0.0.0 
   network 10.1.2.1 0.0.0.0
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 160000 161000
  #
  bgp 100
  #
   ipv6-family unicast
    unicast-route recursive-lookup tunnel tunnel-selector s1
  #
  remote-backup-profile p1 
   service-type bras 
   backup-id 101 remote-backup-service rui 
   peer-backup hot 
   vrrp-id 1 interface GigabitEthernet0/2/1.1
  #
  interface GigabitEthernet0/2/1.1 
   vlan-type dot1q 1 
   ip address 10.1.1.1 255.255.255.0 
   vrrp vrid 1 virtual-ip 10.1.1.100 
   admin-vrrp vrid 1 
   vrrp vrid 1 priority 120
   vrrp vrid 1 preempt-mode timer delay 60 
   vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50 
   vrrp vrid 1 track bfd-session 2 link
  #
  interface GigabitEthernet0/2/1.2
   vlan-type dot1q 2
   ip address 10.1.10.1 255.255.255.0
  #
  interface GigabitEthernet0/2/1.333            
   ipv6 enable  
   ipv6 address auto link-local                  
   ipv6 nd autoconfig managed-address-flag       
   ipv6 nd autoconfig other-flag                           
   user-vlan 1 10 qinq 100  
   remote-backup-profile p1                       
   bas          
    access-type layer2-subscriber default-domain authentication dom1  
    authentication-method-ipv6 bind
  #
  interface LoopBack1
   ip address 10.1.2.1 255.255.255.255
   ospf enable 1 area 1
   ospf prefix-sid index 10
  #
  bfd bfd1 bind peer-ip 10.1.1.2
   discriminator local 8
   discriminator remote 6
   commit 
  #
   return 
  ```
* BRAS2 configuration file
  
  ```
  #
  sysname BRAS2
  #
  ipv6
  #
  bfd
  #
  bfd bfd-peer bind peer-ip 10.1.1.2 source-ip 10.1.1.1
   discriminator local 1 
   discriminator remote 1 
  #
  mpls lsr-id 10.1.2.2
  #
  mpls
  #
  mpls ldp
  #
  ipv6 prefix prefix1 local 
   prefix 2001:db8:1::1/64
  #
  ipv6 pool pool1 bas local rui-slave
   prefix prefix1
  #
  radius-server group radius
   radius-server shared-key-cipher %^%#glhJ;yPG#$=tC&(Is%q!S_";(k.Ef$:978$$e:TY%^%
   radius-server authentication 192.168.7.249 1812 weight 0
   radius-server accounting 192.168.7.249 1813 weight 0
  #
  aaa
   authentication-scheme radius
   accounting-scheme radius
   #
   domain dom1   
    authentication-scheme radius
    accounting-scheme radius
    radius-server group radius           
    ipv6-pool pool1
  #
  remote-backup-service rui
   peer 10.1.2.1 source 10.1.2.2 port 6001
   protect lsp-tunnel for-all-instance peer-ip 10.1.2.1
   track interface GigabitEthernet0/2/0
   ipv6-pool pool1
   protect tnl-policy p1 peer-ip 10.1.2.1 
  # 
  segment-routing
   tunnel-prefer segment-routing
  #
  tunnel-policy p1
   tunnel select-seq sr-lsp load-balance-number 1
  #
  tunnel-selector s1 permit node 10
   apply tunnel-policy p1
  #
  ospf 1
   import-route direct
   area 0.0.0.0
   network 10.1.2.2 0.0.0.0
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 160000 161000
  #
  bgp 100
  #
   ipv6-family unicast
    unicast-route recursive-lookup tunnel tunnel-selector s1
  #
  remote-backup-profile p2
   service-type bras
   backup-id 101 remote-backup-service rui
   peer-backup hot
   vrrp-id 1 interface GigabitEthernet0/2/1.1
  #
  interface GigabitEthernet0/2/1.1 
   vlan-type dot1q 1 
   ip address 10.1.1.2 255.255.255.0 
   vrrp vrid 1 virtual-ip 10.1.1.100 
   admin-vrrp vrid 1 
   vrrp vrid 1 track bfd-session 1 peer
  #
  interface GigabitEthernet 0/2/1.332          
   ipv6 enable  
   ipv6 address auto link-local                  
   ipv6 nd autoconfig managed-address-flag       
   ipv6 nd autoconfig other-flag                            
   user-vlan 1 10 qinq 100
   remote-backup-profile p2                      
   bas          
    access-type layer2-subscriber default-domain authentication dom1
    authentication-method-ipv6 bind
  #
  interface LoopBack1
   ip address 10.1.2.2 255.255.255.255
   ospf enable 1 area 1
   ospf prefix-sid index 20
  #
  return 
  ```