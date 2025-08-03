Example for Associating E-VRRP with 4PE PW Redundancy
=====================================================

In 4PE PW redundancy scenarios, the mVRRP status determines the master/backup status of PEs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369969__fig_dc_vrp_vpws_cfg_601801), PE1 and PE2 are connected over a bypass PW, and PE3 and PE4 are connected over another bypass PW. To allow communication between CEs and PEs in case a public network link or PE fails, associate E-VRRP with 4PE PW redundancy.

**Figure 1** Associating E-VRRP with 4PE PW redundancy![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 through 4 represent GE0/1/0, GE0/1/1, GE0/1/2, and GE0/1/3, respectively.


  
![](images/fig_dc_vrp_vpws_cfg_601801.png)  

**Table 1** Interfaces and IP addresses
| Device | Interface | IP Address | Device | Interface | IP Address |
| --- | --- | --- | --- | --- | --- |
| CE1 | GE 0/1/0 | - | CE2 | GE 0/1/0 | - |
| GE 0/1/1 | - | GE 0/1/1 | - |
| PE1 | GE 0/1/0.2 | 10.1.1.1/24 | PE2 | GE 0/1/0 | 10.7.1.2/24 |
| GE 0/1/1 | 10.4.1.1/24 | GE 0/1/1.2 | 10.1.1.2/24 |
| GE 0/1/2 | 10.3.1.1/24 | GE 0/1/2 | 10.3.1.2/24 |
| GE 0/1/3 | 10.5.1.1/24 | GE 0/1/3 | 10.6.1.2/24 |
| PE3 | GE 0/1/0.2 | 10.2.1.1/24 | PE4 | GE 0/1/0 | 10.7.1.1/24 |
| GE 0/1/1 | 10.4.1.3/24 | GE 0/1/1.2 | 10.2.1.2/24 |
| GE 0/1/2 | 10.8.1.3/24 | GE 0/1/2 | 10.8.1.4/24 |
| GE 0/1/3 | 10.6.1.3/24 | GE 0/1/3 | 10.5.1.4/24 |





#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses and a routing protocol and enable MPLS on the PEs.
2. Configure public network tunnels.
3. Configure service PWs.
4. Configure BFD for PW to detect PW connectivity.
5. Determine the VRRP master/backup status.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface numbers and types
* PE's LSR IDs
* L2VC's destination IP addresses, VC IDs, and VC types
* BFD session name and local and remote BFD session discriminators
* VRRP group ID and priority

#### Procedure

1. Assign an IP address to each interface and configure a routing protocol.
   
   
   
   Configure an IP address and mask for each involved interface according to [Figure 1](#EN-US_TASK_0172369969__fig_dc_vrp_vpws_cfg_601801). For detailed configurations, see Configuration Files.
   
   IS-IS is used in this example. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172369969__sec_dc_vrp_vpws_cfg_601801).
2. Configure public network tunnels.
   1. Enable MPLS, MPLS TE, and RSVP-TE globally on each node.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] mpls lsr-id 1.1.1.1
      ```
      ```
      [*PE1] mpls
      ```
      ```
      [*PE1] mpls te
      ```
      ```
      [*PE1] mpls rsvp-te
      ```
      ```
      [*PE1] mpls te cspf
      ```
      ```
      [*PE1-mpls] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/0
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] mpls te
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] mpls rsvp-te
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] mpls te
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] mpls rsvp-te
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] mpls te
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] mpls rsvp-te
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/3
      ```
      ```
      [*PE1-GigabitEthernet0/1/3] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/1/3] mpls te
      ```
      ```
      [*PE1-GigabitEthernet0/1/3] mpls rsvp-te
      ```
      ```
      [*PE1-GigabitEthernet0/1/3] quit
      ```
      ```
      [*PE1] commit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The configurations of PE2, PE3, and PE4 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172369969__sec_dc_vrp_vpws_cfg_601801).
   2. Establish LDP LSPs and configure remote LDP sessions.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] mpls ldp
      ```
      ```
      [*PE1-mpls-ldp] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] mpls ldp
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE1] mpls ldp remote-peer 1.1.1.1
      ```
      ```
      [*PE1-mpls-ldp-remote-1.1.1.1] remote-ip 2.2.2.2
      ```
      ```
      [*PE1-mpls-ldp-remote-1.1.1.1] quit
      ```
      ```
      [*PE1] commit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The configurations of PE2, PE3, and PE4 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172369969__sec_dc_vrp_vpws_cfg_601801).
      
      
      # Verify the configuration. Run the [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session) command on PE1 and PE2 to check whether the LDP session status is **Operational**. The following example uses the command output on PE1.
      
      ```
      [~PE1] display mpls ldp session
      ```
      ```
       LDP Session(s) in Public Network
       Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
       An asterisk (*) before a session means the session is being deleted.
       ------------------------------------------------------------------------------
       PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
       ------------------------------------------------------------------------------
       3.3.3.3:0          Operational DU   Passive  0000:00:46  187/187
       ------------------------------------------------------------------------------
       TOTAL: 1 session(s) Found.   
      ```
3. Configure PWE3.
   1. Create PW templates.
      
      
      ```
      [~PE1] tunnel-policy 4pe2
      ```
      ```
      [*PE1-tunnel-policy-4pe2] tunnel select-seq te load-balance-number 1
      ```
      ```
      [*PE1-tunnel-policy-4pe2] quit
      ```
      ```
      [~PE1] tunnel-policy 4pe3
      ```
      ```
      [*PE1-tunnel-policy-4pe3] tunnel select-seq te load-balance-number 1
      ```
      ```
      [*PE1-tunnel-policy-4pe3] quit
      ```
      ```
      [~PE1] tunnel-policy 4pe4
      ```
      ```
      [*PE1-tunnel-policy-4pe4] tunnel select-seq te load-balance-number 1
      ```
      ```
      [*PE1-tunnel-policy-4pe4] quit
      ```
      ```
      [~PE1] mpls l2vpn
      ```
      ```
      [*PE1-l2vpn] quit
      ```
      ```
      [*PE1] pw-template 4pe2
      ```
      ```
      [*PE1-pw-template-4pe2] peer-address 2.2.2.2
      ```
      ```
      [*PE1-pw-template-4pe2] control-word
      ```
      ```
      [*PE1-pw-template-4pe2] tnl-policy 4pe2
      ```
      ```
      [*PE1-pw-template-4pe2] commit
      ```
      ```
      [*PE1-pw-template-4pe2] quit
      ```
      ```
      [*PE1] pw-template 4pe3
      ```
      ```
      [*PE1-pw-template-4pe3] peer-address 3.3.3.3
      ```
      ```
      [*PE1-pw-template-4pe3] control-word
      ```
      ```
      [*PE1-pw-template-4pe3] tnl-policy 4pe3
      ```
      ```
      [*PE1-pw-template-4pe3] commit
      ```
      ```
      [*PE1-pw-template-4pe3] quit
      ```
      ```
      [*PE1] pw-template 4pe4
      ```
      ```
      [*PE1-pw-template-4pe4] peer-address 4.4.4.4
      ```
      ```
      [*PE1-pw-template-4pe4] control-word
      ```
      ```
      [*PE1-pw-template-4pe4] tnl-policy 4pe4
      ```
      ```
      [*PE1-pw-template-4pe4] commit
      ```
      ```
      [*PE1-pw-template-4pe4] quit
      ```
      ```
      [*PE1] commit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The configurations of PE2, PE3, and PE4 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172369969__sec_dc_vrp_vpws_cfg_601801).
   2. Create VCs.
      
      
      ```
      [~PE1] interface gigabitethernet 0/1/0.1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc pw-template 4pe3 300
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc pw-template 4pe4 400 secondary
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vpn redundancy independent
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc pw-template 4pe2 ac-bypass 200 pw-bypass 500
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vpn stream-dual-receiving
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE1] commit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The configurations of PE2, PE3, and PE4 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172369969__sec_dc_vrp_vpws_cfg_601801).
4. Configure BFD for ACs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bfd
   ```
   ```
   [*PE1-bfd] quit
   ```
   ```
   [*PE1] bfd link1 bind peer-ip 10.1.1.3 interface gigabitethernet 0/1/0.2
   ```
   ```
   [*PE1-bfd-lsp-session-link1] discriminator local 15
   ```
   ```
   [*PE1-bfd-lsp-session-link1] discriminator remote 51
   ```
   ```
   [*PE1-bfd-lsp-session-link1] commit
   ```
   ```
   [*PE1-bfd-lsp-session-link1] quit
   ```
   ```
   [*PE1] bfd peer bind peer-ip 10.1.1.2 interface gigabitethernet 0/1/0.2
   ```
   ```
   [*PE1-bfd-lsp-session-peer] discriminator local 1
   ```
   ```
   [*PE1-bfd-lsp-session-peer] discriminator remote 2
   ```
   ```
   [*PE1-bfd-lsp-session-peer] commit
   ```
   ```
   [*PE1-bfd-lsp-session-peer] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configurations of PE2, PE3, and PE4 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172369969__sec_dc_vrp_vpws_cfg_601801).
5. Determine the VRRP master/backup status.
   1. Configure mVRRP to determine the master/backup status of the PEs.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] interface gigabitethernet 0/1/0.2
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] vlan-type dot1q 2
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] ip address 10.1.1.1 24
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] commit
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] vrrp vrid 1 virtual-ip 10.1.1.254
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] vrrp vrid 1 priority 120
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] admin-vrrp vrid 1
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.2] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Verify the configuration. Run the [**display vrrp**](cmdqueryname=display+vrrp) command on PE1 and PE2 to check the master/backup status of them. The following example uses the command output on PE1. As PE1 has the VRRP priority of 120 and PE2 has the default VRRP priority of 100, the VRRP status of PE1 is **Master**.
      
      ```
      [*PE1] display vrrp
      ```
      ```
        GigabitEthernet0/1/1 | Virtual Router 1
          State           : Master
          Virtual IP      : 10.1.1.254
          Master IP       : 10.1.1.1
          Local IP        : 10.1.1.1
          PriorityRun     : 120
          PriorityConfig  : 120
          MasterPriority  : 120
          Preempt         : YES           Delay Time : 0
          Hold Multiplier : 3
          TimerRun        : 1
          TimerConfig     : 1
          Auth Type       : NONE
          Virtual Mac     :  00e0-fc00-1234
          Check TTL       : YES
          Config type     : admin-vrrp
          Config track link-bfd down-number : 0
          Create time      : 2011-04-21 11:23:10
          Last change time : 0000-00-00 00:00:00
      ```
   2. Bind the service PWs to the mVRRP group.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] interface gigabitethernet 0/1/0.1
      ```
      ```
      [~PE1-GigabitEthernet0/1/0.1] mpls l2vc track admin-vrrp interface gigabitethernet 0/1/0.2 vrid 1 pw-redundancy
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] mpls l2vc track admin-vrrp secondary
      ```
      ```
      [*PE1-GigabitEthernet0/1/0.1] quit
      ```
      ```
      [*PE1] commit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The configurations of PE2, PE3, and PE4 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172369969__sec_dc_vrp_vpws_cfg_601801).
6. Verify the configuration.
   1. Ping the virtual IP address of a service VRRP group from CE1.
      
      
      ```
      [~CE1] ping 10.2.1.254
      ```
      ```
      PING 10.2.1.254: 56  data bytes, press CTRL_C to break
          Reply from 10.2.1.254: bytes=56 Sequence=1 ttl=255 time=40 ms
          Reply from 10.2.1.254: bytes=56 Sequence=2 ttl=255 time=30 ms
          Reply from 10.2.1.254: bytes=56 Sequence=3 ttl=255 time=40 ms
          Reply from 10.2.1.254: bytes=56 Sequence=4 ttl=255 time=1 ms
          Reply from 10.2.1.254: bytes=56 Sequence=5 ttl=255 time=1 ms
      
        --- 10.2.1.254 ping statistics ---
          5 packet(s) transmitted
          5 packet(s) received
          0.00% packet loss
          round-trip min/avg/max = 1/22/40 ms  
      ```
   2. Simulate an interface fault and an interface fault recovery.
      
      
      
      # Disable GE 0/1/0 on PE1 to simulate an AC interface fault.
      
      ```
      [~PE1] interface gigabitethernet 0/1/0
      ```
      ```
      [~PE1-GigabitEthernet0/1/0] shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE1] commit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This step is used only to verify the configuration. Do not do this in practice.
      
      As the primary AC interface fails, the upstream traffic is transmitted along the path CE1 -> PE2 -> PE3 -> CE2. Run the **display mpls l2vc track admin-vrrp** command on PE1. The command output shows that the VRRP status is **Initialize**.
      
      [~PE1] **display mpls l2vc track admin-vrrp**
      
      ```
      Interface: GigabitEthernet0/1/0.2, admin-vrrp vrid: 1, state: Initialize
        PW Number : 2
       *Client Interface     : GigabitEtherne0/1/0.1
        VC State             : up
        VC ID                : 300
        VC Type              : VLAN
        Link State           : up
      
       *Client Interface     : GigabitEthernet0/1/0.1
        VC State             : up
        VC ID                : 400
        VC Type              : VLAN
        Link State           : down
      ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
   sysname CE1
  #
  bfd
  #
  interface Vlanif2
   ip address 10.1.1.3 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port trunk allow-pass vlan 2
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port trunk allow-pass vlan 2
  #
  bfd link1 bind peer-ip 10.1.1.1 interface Vlanif2
   discriminator local 51
   discriminator remote 15
  bfd link2 bind peer-ip 10.1.1.2 interface Vlanif2
   discriminator local 52
   discriminator remote 25
  #
  return                       
  ```
* CE2 configuration file
  
  ```
  #
   sysname CE2
  #
  bfd
  #
  interface Vlanif2
   ip address 10.2.1.3 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port trunk allow-pass vlan 2
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port trunk allow-pass vlan 2
  #
  bfd link1 bind peer-ip 10.2.1.1 interface Vlanif2
   discriminator local 61
   discriminator remote 16
  bfd link2 bind peer-ip 10.2.1.2 interface Vlanif2
   discriminator local 62
   discriminator remote 26
  #
  return                       
  ```
* PE1 configuration file
  
  ```
  #                                                                               
  sysname PE1                                                                    
  #                                                                               
  bfd                                                                            
  #                                                                               
  mpls lsr-id 1.1.1.1 
  #                                                           
  mpls                                                                           
   mpls te                                                                       
   mpls rsvp-te                                                                  
   mpls te cspf                                                                  
  #                                                                               
  mpls l2vpn                                                                     
  #
  pw-template 4pe2
   peer-address 2.2.2.2 
   control-word 
   tnl-policy 4pe2
  #
  pw-template 4pe3
   peer-address 3.3.3.3 
   control-word 
   tnl-policy 4pe3
  #
  pw-template 4pe4
   peer-address 4.4.4.4 
   control-word 
   tnl-policy 4pe4
  #
  mpls ldp                                                                        
  #                                                                               
  mpls ldp remote-peer 1.1.1.1                                                   
   remote-ip 2.2.2.2
  #                                                                               
  isis 1
   is-level level-1
   cost-style wide
   network-entity 00.0008.0000.0001.00
   traffic-eng level-1
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.4.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.5.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
   mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  bfd link1 bind peer-ip 10.1.1.3 interface GigabitEthernet0/1/0.2
   discriminator local 15
   discriminator remote 51
  #
  bfd peer bind peer-ip 10.1.1.2 interface GigabitEthernet0/1/0.2
   discriminator local 1
   discriminator remote 2
  #
  interface GigabitEthernet0/1/0.2
   vlan-type dot1q 2
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.254
   admin-vrrp vrid 1
   vrrp vrid 1 priority 120
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 1
   mpls l2vc pw-template 4pe3 300
   mpls l2vc track admin-vrrp interface Gigabitethernet0/1/0.2 vrid 1 pw-redundancy
   mpls l2vc pw-template 4pe4 400 secondary
   mpls l2vc track admin-vrrp secondary
   mpls l2vpn redundancy independent
   mpls l2vc pw-template 4pe2 ac-bypass 200 pw-bypass 500
   mpls l2vpn stream-dual-receiving
  #
  tunnel-policy 4pe2
   tunnel select-seq te load-balance-number 1
  #
  tunnel-policy 4pe3
   tunnel select-seq te load-balance-number 1
  #
  tunnel-policy 4pe4
   tunnel select-seq te load-balance-number 1
  #
  return                                                                          
  
  ```
* PE2 configuration file
  
  ```
  #                                                                               
  sysname PE2                                                                   
  #                                                                               
  bfd                                                                            
  #                                                                               
  mpls lsr-id 2.2.2.2
  #                                                           
  mpls                                                                           
   mpls te                                                                       
   mpls rsvp-te                                                                  
   mpls te cspf                                                                  
  #                                                                               
  mpls l2vpn                                                                     
  #
  pw-template 4pe1
   peer-address 1.1.1.1 
   control-word 
   tnl-policy 4pe1
  #
  pw-template 4pe3
   peer-address 3.3.3.3 
   control-word 
   tnl-policy 4pe3 
  #
  pw-template 4pe4
   peer-address 4.4.4.4 
   control-word 
   tnl-policy 4pe4
  #
  mpls ldp
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 00.0008.0000.0002.00
   traffic-eng level-1
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.6.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
   mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.7.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  bfd link2 bind peer-ip 10.1.1.3 interface GigabitEthernet0/1/1.2
   discriminator local 25
   discriminator remote 52
  #
  bfd peer bind peer-ip 10.1.1.1 interface GigabitEthernet0/1/1.2
   discriminator local 2
   discriminator remote 1
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 1
   mpls l2vc pw-template 4pe3 600
   mpls l2vc track admin-vrrp interface Gigabitethernet0/1/1.2 vrid 1 pw-redundancy
   mpls l2vc pw-template 4pe4 700 secondary
   mpls l2vc track admin-vrrp secondary
   mpls l2vpn redundancy independent
   mpls l2vc pw-template 4pe1 ac-bypass 500 pw-bypass 200
   mpls l2vpn stream-dual-receiving
  #
  interface GigabitEthernet0/1/1.2
   vlan-type dot1q 2
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.254
   admin-vrrp vrid 1
  #
  tunnel-policy 4pe1
   tunnel select-seq te load-balance-number 1
  #
  tunnel-policy 4pe3
   tunnel select-seq te load-balance-number 1
  #
  tunnel-policy 4pe4
   tunnel select-seq te load-balance-number 1
  #
  return
  
  ```
* PE3 configuration file
  
  ```
  #                                                                               
  sysname PE3                                                                   
  #                                                                               
  bfd                                                                            
  #                                                                               
  mpls lsr-id 3.3.3.3
  #                                                            
  mpls                                                                           
   mpls te                                                                       
   mpls rsvp-te    
   mpls rsvp-te hello
   mpls te cspf                                                                  
  #                                                                               
  mpls l2vpn                                                                     
  #
  pw-template 4pe1  
   peer-address 1.1.1.1 
   control-word 
   tnl-policy 4pe1 
  #
  pw-template 4pe2  
   peer-address 2.2.2.2 
   control-word 
   tnl-policy 4pe2 
  #
  pw-template 4pe4  
   peer-address 4.4.4.4 
   control-word 
   tnl-policy 4pe4 
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  isis 1
   is-level level-1
   cost-style wide
   network-entity 00.0008.0000.0003.00
   traffic-eng level-1
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.6.1.3 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
   mpls rsvp-te hello
   mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.4.1.3 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
   mpls rsvp-te hello
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.8.1.3 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  bfd link1 bind peer-ip 10.2.1.3 interface GigabitEthernet0/1/0.2
   discriminator local 16
   discriminator remote 61
  #
  bfd peer bind peer-ip 10.2.1.2 interface GigabitEthernet0/1/0.2
   discriminator local 26
   discriminator remote 62
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 1
   mpls l2vc pw-template 4pe1 300
   mpls l2vc track admin-vrrp interface Gigabitethernet0/1/0.2 vrid 1 pw-redundancy
   mpls l2vc pw-template 4pe2 600 secondary
   mpls l2vc track admin-vrrp secondary
   mpls l2vpn redundancy independent
   mpls l2vc pw-template 4pe4 ac-bypass 200 pw-bypass 500
   mpls l2vpn stream-dual-receiving
  #
  interface GigabitEthernet0/1/0.2
   vlan-type dot1q 2
   ip address 10.2.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.2.1.254
   admin-vrrp vrid 1
   vrrp vrid 1 priority 120
  #
  tunnel-policy 4pe1
   tunnel select-seq te  load-balance-number 1
  #
  tunnel-policy 4pe2
   tunnel select-seq te load-balance-number 1
  #
  tunnel-policy 4pe4
   tunnel select-seq te load-balance-number 1
  #
  return
  
  ```
* PE4 configuration file
  
  ```
  #                                                                               
  sysname PE4                                                                   
  #                                                                               
  bfd                                                                            
  #                                                                               
  mpls lsr-id 4.4.4.4
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls rsvp-te hello
   mpls te cspf
  #
  mpls l2vpn
  #
  pw-template 4pe1  
   peer-address 1.1.1.1 
   control-word 
   tnl-policy 4pe1 
  #
  pw-template 4pe2  
   peer-address 2.2.2.2 
   control-word 
   tnl-policy 4pe2 
  #
  pw-template 4pe3  
   peer-address 3.3.3.3 
   control-word 
   tnl-policy 4pe3 
  #
  mpls ldp
   #
   ipv4-family
  #
  e-trunk 1
   peer-address 3.3.3.3 source-address 4.4.4.4
   timer revert delay 10
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 00.0008.0000.0004.00
   traffic-eng level-1
  #
  interface Eth-Trunk1
   mode lacp-static
   e-trunk 1
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
   isis enable 1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.7.1.4 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
   mpls rsvp-te hello
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.8.1.4 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.5.1.4 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
   mpls rsvp-te hello
   mpls ldp
  #
  bfd link2 bind peer-ip 10.2.1.3 interface GigabitEthernet0/1/1.2
   discriminator local 61
   discriminator remote 16
  #
  bfd peer bind peer-ip 10.2.1.1 interface GigabitEthernet0/1/1.2
   discriminator local 62
   discriminator remote 26
  #
  interface GigabitEthernet0/1/1.1
   vlan-type dot1q 1
   mpls l2vc pw-template 4pe2 700 
   mpls l2vc track admin-vrrp interface Gigabitethernet0/1/1.2 vrid 1 pw-redundancy
   mpls l2vc pw-template 4pe1 400 secondary
   mpls l2vc track admin-vrrp secondary
   mpls l2vpn redundancy independent
   mpls l2vc pw-template 4pe3 ac-bypass 500 pw-bypass 200
   mpls l2vpn stream-dual-receiving
  #
  interface GigabitEthernet0/1/1.2
   vlan-type dot1q 2
   ip address 10.2.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.2.1.254
   admin-vrrp vrid 1
  #
  tunnel-policy 4pe1
   tunnel select-seq te load-balance-number 1
  #
  tunnel-policy 4pe2
   tunnel select-seq te load-balance-number 1
  #
  tunnel-policy 4pe3
   tunnel select-seq te load-balance-number 1
  #
  return
  
  ```