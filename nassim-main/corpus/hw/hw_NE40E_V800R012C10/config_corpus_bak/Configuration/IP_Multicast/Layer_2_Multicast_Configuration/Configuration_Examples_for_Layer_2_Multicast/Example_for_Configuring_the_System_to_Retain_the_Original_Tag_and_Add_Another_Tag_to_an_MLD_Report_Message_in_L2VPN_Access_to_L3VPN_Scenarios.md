Example for Configuring the System to Retain the Original Tag and Add Another Tag to an MLD Report Message in L2VPN Access to L3VPN Scenarios
=============================================================================================================================================

This section provides an example for configuring the system to reserve the original tag and add another tag to an MLD Report message when the message is forwarded from an L2VE sub-interface to an L3VE QinQ VLAN tag termination sub-interface.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368009__fig_dc_vrp_l2mc_cfg_003401), the NPE resides on the IP/MPLS backbone network, whereas the UPE resides on the VPWS access network; a VPWS connection is established between the UPE and NPE using LDP signaling. The receiver sends MLD request messages to the UPE, and the source sends multicast streams. Create two virtual interfaces VE 0/0/10 and VE 0/0/20 on the NPE. VE 0/0/10 is an L2VE interface used to terminate the VPWS, whereas VE 0/0/20 is used to access the L3VPN in QinQ mode.

**Figure 1** Configuring the system to retain the original tag and add another tag to an MLD report message in L2VPN access to L3VPN scenarios![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, 3, and 4 in this example represent GE 0/1/0, GE 0/1/1, VE 0/0/10, and VE 0/0/20, respectively.


  
![](images/fig_feature_image_ipv6_protocol-packet_encapsulation.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPFv2 at each network layer to implement IPv4 interworking between the NPE and UPE. Configure an IPv6 static route to the source on the NPE.
2. Establish a VPWS neighbor relationship between the UPE and NPE.
3. Configure AC interfaces on the UPE.
4. Create a global L2VE interface and L3VE interface on the NPE, and bind them to the same VE-Group.
5. Configure single-tagged packet termination on the L2VE interface, and configure QinQ packet termination on the L3VE interface.
6. Enable IPv6 multicast and MLD snooping globally on the NPE and UPE.
7. Configure the system to retain the original tag and add another tag to an MLD report message in the VSI view of the UPE.

#### Data Preparation

To complete the configuration, you need the following data:

Interface IP addresses and OSPFv2 process ID

VE-Group number

LSR ID of each node

VSI name and VSI ID

VLAN ID of the UPE's AC interface: 10; VLAN ID for single-tagged packet termination: 5; VLAN IDs for double-tagged packet termination: 10 and 5


#### Procedure

1. Configure interface IP addresses.
   
   
   
   Configure an IP address for each interface (including a loopback interface). Establish an OSPFv2 neighbor relationship between the UPE and NPE. Use OSPFv2 to advertise the network segment connected to the two devices' IPv4 interfaces and the loopback interface routes. For configuration details, see Configuration Files in this section.
2. Establish a VPWS neighbor relationship between the UPE and NPE.
   
   
   
   # Configure the UPE.
   
   ```
   <~HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname UPE
   ```
   ```
   [~HUAWEI] commit
   ```
   ```
   [~UPE] mpls lsr-id 1.1.1.1
   ```
   ```
   [*UPE] mpls
   ```
   ```
   [*UPE-mpls] quit
   ```
   ```
   [*UPE] mpls ldp
   ```
   ```
   [*UPE-ldp] quit
   ```
   ```
   [*UPE] mpls ldp remote-peer 2.2.2.2
   ```
   ```
   [*UPE-ldp-remote-2.2.2.2] quit
   ```
   ```
   [*UPE] mpls l2vpn
   ```
   ```
   [*UPE-l2vpn] quit
   ```
   ```
   [*UPE] vsi vsi1 static
   ```
   ```
   [*UPE-vsi-vsi1] pwsignal ldp
   ```
   ```
   [*UPE-vsi-vsi1-ldp] vsi-id 1112
   ```
   ```
   [*UPE-vsi-vsi1-ldp] peer 2.2.2.2
   ```
   ```
   [*UPE-vsi-vsi1-ldp] quit
   ```
   ```
   [*UPE-vsi-vsi1] quit
   ```
   ```
   [*UPE] interface GigabitEthernet0/1/1
   ```
   ```
   [*UPE-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*UPE-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*UPE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   <~NPE> system-view
   ```
   ```
   [~NPE] mpls lsr-id 2.2.2.2
   ```
   ```
   [*NPE] mpls
   ```
   ```
   [*NPE-mpls] quit
   ```
   ```
   [*NPE] mpls ldp
   ```
   ```
   [*NPE-ldp] quit
   ```
   ```
   [*NPE] mpls ldp remote-peer 1.1.1.1
   ```
   ```
   [*NPE-ldp-remote-1.1.1.1] quit
   ```
   ```
   [*NPE] mpls l2vpn
   ```
   ```
   [*NPE-l2vpn] quit
   ```
   ```
   [*NPE] vsi vsi2 static
   ```
   ```
   [*NPE-vsi-vsi2] pwsignal ldp
   ```
   ```
   [*NPE-vsi-vsi2-ldp] vsi-id 1112
   ```
   ```
   [*NPE-vsi-vsi2-ldp] peer 1.1.1.1
   ```
   ```
   [*NPE-vsi-vsi2-ldp] quit
   ```
   ```
   [*NPE-vsi-vsi2] quit
   ```
   ```
   [*NPE] interface GigabitEthernet0/1/0
   ```
   ```
   [*NPE-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*NPE-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*NPE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*NPE] commit
   ```
3. On the UPE, bind GigabitEthernet 0/1/0.1 as an AC interface and set the VLAN ID is 10.
   
   
   
   # Configure the UPE.
   
   ```
   <~UPE> system-view
   ```
   ```
   [~UPE] interface GigabitEthernet0/1/0.1
   ```
   ```
   [*UPE-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*UPE-GigabitEthernet0/1/0.1] l2 binding vsi vsi1
   ```
   ```
   [*UPE-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*UPE] commit
   ```
4. Create two virtual interfaces VE 0/1/10 and VE 0/1/20 on the NPE, and bind them to the same VE-Group.
   
   
   
   # Configure the NPE.
   
   ```
   <~NPE> system-view
   ```
   ```
   [~NPE] interface Virtual-Ethernet 0/1/10
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/10] ve-group 1 l2-terminate
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/10] quit
   ```
   ```
   [*NPE] interface Virtual-Ethernet 0/1/20
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/20] ve-group 1 l3-access
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/20] quit
   ```
   ```
   [*NPE] commit
   ```
5. Configure single-tagged packet termination on VE 0/1/10.1, and configure QinQ packet termination on VE 0/1/20.1.
   
   
   
   # Bind VE 0/1/10.1 as an AC interface, and set the VLAN ID for single-tagged packet termination to 5.
   
   ```
   <~NPE> system-view
   ```
   ```
   [~NPE] interface Virtual-Ethernet 0/1/10.1
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/10.1] vlan-type dot1q 5
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/10.1] l2 binding vsi vsi2
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/10.1] quit
   ```
   ```
   [*NPE] commit
   ```
   
   # Configure QinQ termination on VE 0/1/20.1, and set the VLAN IDs for double-tagged packet termination to 5 and 10 respectively.
   
   ```
   <~NPE> system-view
   ```
   ```
   [~NPE] interface Virtual-Ethernet 0/1/20.1
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/20.1] encapsulation qinq-termination
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/20.1] qinq termination pe-vid 5 ce-vid 10
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/20.1] ipv6 enable
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/20.1] ipv6 address 2001:db8:4::1/64
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/20.1] quit
   ```
   ```
   [*NPE] commit
   ```
6. Enable IPv6 multicast and MLD snooping globally on the NPE and UPE.
   
   
   
   # Configure the UPE.
   
   ```
   <~UPE> system-view
   ```
   ```
   [~UPE] multicast ipv6 routing-enable
   ```
   ```
   [*UPE] mld-snooping enable
   ```
   ```
   [*UPE] vsi vsi1 static
   ```
   ```
   [*UPE-vsi-vsi1] mld-snooping enable
   ```
   ```
   [*UPE-vsi-vsi1] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   <~NPE> system-view
   ```
   ```
   [~NPE] multicast ipv6 routing-enable
   ```
   ```
   [*NPE] mld-snooping enable
   ```
   ```
   [*NPE] vsi vsi2 static
   ```
   ```
   [*NPE-vsi-vsi2] mld-snooping enable
   ```
   ```
   [*NPE-vsi-vsi2] quit
   ```
   ```
   [*NPE] commit
   ```
   ```
   [*NPE] interface Virtual-Ethernet 0/1/20.1
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/20.1] pim ipv6 sm
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/20.1] mld enable
   ```
   ```
   [*NPE-Virtual-Ethernet0/1/20.1] quit
   ```
   ```
   [*NPE] interface GigabitEthernet0/1/1
   ```
   ```
   [*NPE-interface GigabitEthernet0/1/1] pim ipv6 sm
   ```
   ```
   [*NPE-interface GigabitEthernet0/1/1] quit
   ```
   ```
   [*NPE] commit
   ```
7. Configure the system to retain the original tag and add another tag to an MLD report message in the VSI view of the UPE.
   
   
   ```
   [~NPE] vsi vsi2 static
   ```
   ```
   [*NPE-vsi-vsi2] l2-multicast ipv6 protocol-packet encapsulation raw
   ```
   ```
   [*NPE-vsi-vsi2] quit
   ```
   ```
   [*NPE] commit
   ```
8. Verify the configuration.
   
   
   
   Run the **display pim ipv6 routing-table** command on the NPE to view multicast traffic entries.
   
   ```
   [~NPE] display pim ipv6 routing-table 
    VPN-Instance: public net
    Total 1 (*, G) entry; 1 (S, G) entry
    
    (*, FF1E::1)
        RP: NULL
        Protocol: pim-sm, Flag: WC NIIF 
        UpTime: 00:02:12
        Upstream interface: NULL, Refresh time: 00:02:12
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: Virtual-Ethernet0/1/20.1
                Protocol: mld, UpTime: 00:02:12, Expires: -
    
    (2001:DB8:6::1, FF1E::1)
        RP: NULL
        Protocol: pim-sm, Flag: SPT LOC ACT 
        UpTime: 00:05:55
        Upstream interface: GigabitEthernet0/1/1, Refresh time: 00:05:55
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: Virtual-Ethernet0/1/20.1
                Protocol: pim-sm, UpTime: 00:02:12, Expires: -
   ```

#### Configuration Files

* NPE configuration file
  
  ```
  #
  sysname NPE
  #
  multicast ipv6 routing-enable
  #
  mld-snooping enable
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi2 static
   pwsignal ldp
    vsi-id 1112
    peer 1.1.1.1 
   mld-snooping enable
   l2-multicast ipv6 protocol-packet encapsulation raw
  #
  mpls ldp
  #
  mpls ldp remote-peer 1.1.1.1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/1/1
   undo negotiation auto
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:6::2/64
   pim ipv6 sm
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  interface Virtual-Ethernet0/1/10
   ve-group 1 l2-terminate
  #
  interface Virtual-Ethernet0/1/10.1
   vlan-type dot1q 5
   l2 binding vsi vsi2
  #
  interface Virtual-Ethernet0/1/20
   ve-group 1 l3-access
  #
  interface Virtual-Ethernet0/1/20.1
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64
   encapsulation qinq-termination
   qinq termination pe-vid 5 ce-vid 10
   pim ipv6 sm
   mld enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  return
  
  ```
* UPE configuration file
  
  ```
  #
  sysname UPE
  #
  multicast ipv6 routing-enable
  #
  mld-snooping enable
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi1 static
   pwsignal ldp
    vsi-id 1112
    peer 2.2.2.2 
   mld-snooping enable
  #
  mpls ldp
  #
  mpls ldp remote-peer 2.2.2.2
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
   mpls
   mpls ldp
   undo dcn
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   l2 binding vsi vsi1
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  return
  
  ```