Example for Associating CFM with VRRP to Resolve a Dual-Master Problem
======================================================================

This section provides an example for associating connectivity fault management (CFM) with Virtual Router Redundancy Protocol (VRRP) to resolve a dual-master problem.

#### Networking Requirements

Generally, network administrators deploy various detection protocols to improve service reliability. As shown in [Figure 1](#EN-US_TASK_0172361980__fig_dc_vrp_cfm_cfg_00002601), VRRP is deployed on each network provider edge (NPE) to provide gateway access services, and CFM is deployed on each user-end provider edge (UPE) to detect link faults.

**Figure 1** Associating CFM with VRRP  
![](images/fig_dc_vrp_cfm_cfg_00002601.png)  

In this network, NPE1 is the master device. User2's traffic is transmitted along the path CE2 -> UPE2 -> UPE1 -> NPE1. If the link between UPE1 and UPE2 fails, NPE1's VRRP status remains Master and NPE2 changes its VRRP status from Backup to Master after a period of three times the interval at which VRRP Advertisement packets are sent. As a result, both NPE1 and NPE2 serve as master devices. Because UPE2 is still transmitting traffic over the faulty link, user-side traffic is interrupted.

CFM can be deployed on UPE2 and each NPE to monitor the link connectivity between them. When CFM detects a fault on the link between UPE2 and NPE1, it notifies the VRRP group of the fault. NPE1 changes its VRRP status to Initialize, and NPE2 changes its VRRP status from Backup to Master after a period of three times the interval at which VRRP Advertisement packets are sent. This process prevents a VRRP group from having two master devices.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Because CFM can detect only local link faults, NPE2 cannot detect remote link faults. To enable NPE2 to transmit traffic, NPE2 must exchange VRRP Advertisement packets with NPE1 to switch to the Master state. This exchange causes lengthy service interruptions. To reduce the service interruption time, associate VRRP with peer Bidirectional Forwarding Detection (BFD) to accelerate VRRP switchovers. When CFM detects a fault on the link between UPE2 and NPE1:
  + Both peer BFD and local CFM on NPE1 go down, which triggers NPE1 to change its VRRP status to Initialize.
  + Peer BFD on NPE2 goes down but local CFM on NPE2 remains up, which triggers NPE2 to change its VRRP status to Master.
* In the preceding scenario, if CFM is associated with VRRP and VRRP is associated with peer BFD, a rapid VRRP switchover is performed when CFM detects a link fault. User-side traffic can be rapidly forwarded through the backup device, reducing the service interruption time. Because a provider edge (PE) on the network side cannot detect master/backup VRRP switchovers, network-side traffic is still transmitted to NPE1, which wastes bandwidth resources and interrupts services. To resolve this issue, associate VRRP with direct routes. When a master/backup VRRP switchover is performed, the priorities of the direct routes decrease to ensure that both user- and network-side traffic are transmitted along the same path.

To implement quick master/backup VRRP switchovers, reduce user- and network-side traffic interruption times, and ensure that both user- and network-side traffic are transmitted along the same path, associate CFM with VRRP, peer BFD with VRRP, and VRRP with direct routes.

[Figure 2](#EN-US_TASK_0172361980__fig_dc_vrp_cfm_cfg_00002602) shows a combination of these associations.

**Figure 2** Association combination![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_cfm_cfg_00002602.png)  

The implementation is as follows:

* When CFM detects a fault on the link between UPE1 and UPE2, it notifies NPE1 of the fault.
* NPE1 changes its VRRP status to Initialize based on the statuses of peer BFD and local CFM. Then, NPE1 increases the cost of the route to PE1.
* NPE2 changes its VRRP status to Master based on the statuses of peer BFD and local CFM. Then, NPE2 decreases the cost of the route to PE1.
* The path for transmitting user-side traffic changes from UPE2 -> UPE1 -> NPE1 to UPE2 -> UPE3 -> NPE2. The path for transmitting network-side traffic changes from PE1 -> NPE1 to PE1 -> NPE2.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Add each UPE's interfaces to a virtual local area network (VLAN) so that the UPE can forward CFM packets.
2. Configure basic CFM functions on each NPE and UPE to implement end-to-end link fault detection between the NPE and UPE.
3. Configure VRRP on each NPE to improve device reliability.
4. Configure BFD on each NPE, associate BFD with VRRP, and associate CFM with VRRP to implement user-side traffic path switching during a master/backup VRRP switchover.
5. Associate VRRP with direct routes on each NPE to implement network-side traffic path switching during a master/backup VRRP switchover.


#### Data Preparation

To complete the configuration, you need the following data:

* Maintenance domain (MD) name, maintenance association (MA) name, and maintenance association end point (MEP) ID for configuring basic CFM functions
* Interface number and virtual router ID (VRID) for configuring basic VRRP functions
* Session name, local discriminator, and remote discriminator for configuring basic BFD functions


#### Procedure

1. Configure basic CFM functions on each NPE and UPE.
   
   
   
   # Configure NPE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname NPE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~NPE1] cfm enable
   ```
   ```
   [*NPE1] cfm version standard
   ```
   ```
   [*NPE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*NPE1-gigabitethernet0/1/0.1] undo shutdown
   ```
   ```
   [*NPE1-gigabitethernet0/1/0.1] vlan-type dot1q 2
   ```
   ```
   [*NPE1-gigabitethernet0/1/0.1] quit
   ```
   ```
   [*NPE1] cfm md mdforvrrp
   ```
   ```
   [*NPE1-md-mdforvrrp] ma ma1
   ```
   ```
   [*NPE1-md-mdforvrrp-ma-ma1] mep mep-id 1 interface GigabitEthernet 0/1/0.1 vlan 2 outward 
   ```
   ```
   [*NPE1-md-mdforvrrp-ma-ma1] remote-mep mep-id 2
   ```
   ```
   [*NPE1-md-mdforvrrp-ma-ma1] remote-mep ccm-receive enable
   ```
   ```
   [*NPE1-md-mdforvrrp-ma-ma1] mep ccm-send mep-id 1 enable
   ```
   ```
   [*NPE1-md-mdforvrrp-ma-ma1] quit
   ```
   ```
   [*NPE1-md-mdforvrrp] quit
   ```
   ```
   [*NPE1] commit
   ```
   
   
   
   # Configure NPE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname NPE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~NPE2] cfm enable
   ```
   ```
   [*NPE2] cfm version standard
   ```
   ```
   [*NPE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*NPE2-gigabitethernet0/1/0.1] undo shutdown
   ```
   ```
   [*NPE2-gigabitethernet0/1/0.1] vlan-type dot1q 2
   ```
   ```
   [*NPE2-gigabitethernet0/1/0.1] quit
   ```
   ```
   [*NPE2] cfm md mdforvrrp
   ```
   ```
   [*NPE2-md-mdforvrrp] ma ma2
   ```
   ```
   [*NPE2-md-mdforvrrp-ma-ma2] mep mep-id 4 interface GigabitEthernet 0/1/0.1 vlan 2 outward
   ```
   ```
   [*NPE2-md-mdforvrrp-ma-ma2] remote-mep mep-id 3
   ```
   ```
   [*NPE2-md-mdforvrrp-ma-ma2] remote-mep ccm-receive enable
   ```
   ```
   [*NPE2-md-mdforvrrp-ma-ma2] mep ccm-send mep-id 4 enable
   ```
   ```
   [*NPE2-md-mdforvrrp-ma-ma2] quit
   ```
   ```
   [*NPE2-md-mdforvrrp] quit
   ```
   ```
   [*NPE2] commit
   ```
   
   
   
   # Configure UPE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname UPE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~UPE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*UPE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*UPE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*UPE1-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
   ```
   ```
   [*UPE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*UPE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*UPE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*UPE1-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*UPE1-GigabitEthernet0/1/0] port trunk allow-pass vlan 2
   ```
   ```
   [*UPE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*UPE1] commit
   ```
   
   
   
   # Configure UPE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname UPE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~UPE2] cfm enable
   ```
   ```
   [*UPE2] cfm version standard
   ```
   ```
   [*UPE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*UPE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*UPE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*UPE2-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
   ```
   ```
   [*UPE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*UPE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*UPE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*UPE2-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*UPE2-GigabitEthernet0/1/0] port trunk allow-pass vlan 2
   ```
   ```
   [*UPE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*UPE2] cfm md mdforvrrp
   ```
   ```
   [*UPE2-md-mdforvrrp] ma ma1
   ```
   ```
   [*UPE2-md-mdforvrrp-ma-ma1] mep mep-id 2 interface GigabitEthernet 0/1/1 outward
   ```
   ```
   [*UPE2-md-mdforvrrp-ma-ma1] remote-mep mep-id 1
   ```
   ```
   [*UPE2-md-mdforvrrp-ma-ma1] remote-mep ccm-receive enable
   ```
   ```
   [*UPE2-md-mdforvrrp-ma-ma1] mep ccm-send mep-id 2 enable
   ```
   ```
   [*UPE2-md-mdforvrrp-ma-ma1] quit
   ```
   ```
   [*UPE2-md-mdforvrrp] ma ma2
   ```
   ```
   [*UPE2-md-mdforvrrp-ma-ma2] mep mep-id 3 interface GigabitEthernet 0/1/0 outward
   ```
   ```
   [*UPE2-md-mdforvrrp-ma-ma2] remote-mep mep-id 4
   ```
   ```
   [*UPE2-md-mdforvrrp-ma-ma2] remote-mep ccm-receive enable
   ```
   ```
   [*UPE2-md-mdforvrrp-ma-ma2] mep ccm-send enable
   ```
   ```
   [*UPE2-md-mdforvrrp-ma-ma2] quit
   ```
   ```
   [*UPE2-md-mdforvrrp] quit
   ```
   ```
   [*UPE2] commit
   ```
   
   
   
   # Configure UPE3.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname UPE3
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~UPE3] interface gigabitethernet 0/1/1
   ```
   ```
   [*UPE3-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*UPE3-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*UPE3-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
   ```
   ```
   [*UPE3-GigabitEthernet0/1/1] quit
   ```
   ```
   [*UPE3] interface gigabitethernet 0/1/0
   ```
   ```
   [*UPE3-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*UPE3-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*UPE3-GigabitEthernet0/1/0] port trunk allow-pass vlan 2
   ```
   ```
   [*UPE3-GigabitEthernet0/1/0] quit
   ```
   ```
   [*UPE3] commit
   ```
2. Verify the CFM configuration.
   
   
   
   After the configuration is complete, run the [**display cfm remote-mep**](cmdqueryname=display+cfm+remote-mep) command. The command output shows that basic CFM functions have been configured. The following example uses the command output on UPE2.
   
   ```
   [~UPE2] display cfm remote-mep
   ```
   ```
   The total number of RMEPs is : 1
   The status of RMEPs : 1 up, 0 down, 0 disable
   --------------------------------------------------
    MD Name            : mdforvrrp
    Level              : 0
    MA Name            : ma2
    RMEP ID            : 4
    VLAN ID            : 2 
    VSI Name           : --
    L2VC ID            : --
    L2VPN Name         : --  CE ID              : --  CE Offset          : --
    L2TPV3 Tunnel Name            : --  L2TPV3 Local Connection Name  : --
    MAC                : 00e0-fc12-7890
    CCM Receive        : enabled
    Trigger-If-Down    : enabled
    CFM Status         : up
    Alarm Status       : none
    Interface TLV      : --
    Port Status TLV    : --
   ```
3. Configure basic VRRP functions on each NPE.
   
   
   
   # Configure NPE1.
   
   ```
   [*NPE1] interface GigabitEthernet 0/1/0.1
   ```
   ```
   [*NPE1-GigabitEthernet0/1/0.1] ip address 192.168.1.2 24
   ```
   ```
   [*NPE1-GigabitEthernet0/1/0.1] vrrp vrid 1 virtual-ip 192.168.1.11
   ```
   ```
   [*NPE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*NPE1] commit
   ```
   
   
   
   # Configure NPE2.
   
   ```
   [*NPE2] interface GigabitEthernet 0/1/0.1
   ```
   ```
   [*NPE2-GigabitEthernet0/1/0.1] ip address 192.168.1.3 24
   ```
   ```
   [*NPE2-GigabitEthernet0/1/0.1] vrrp vrid 1 virtual-ip 192.168.1.11
   ```
   ```
   [*NPE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*NPE2] commit
   ```
4. Verify the VRRP configuration.
   
   
   
   After the configuration is complete, run the [**display vrrp**](cmdqueryname=display+vrrp) command on each NPE to view its VRRP status.
   
   ```
   [~NPE1] display vrrp
   ```
   ```
   GigabitEthernet0/1/0.1 | Virtual Router 1
   State          : Master
   Virtual IP     : 192.168.1.11
   Master IP      : 192.168.1.2
   Local IP       : 192.168.1.2
   PriorityRun    : 200
   PriorityConfig : 200
   MasterPriority : 200
   Preempt        : YES   Delay Time : 0 s
   Hold Multiplier: 4
   TimerRun       : 1 s
   TimerConfig    : 1 s
   Auth type      : NONE
   Virtual MAC    : 00e0-fc12-7880
   Check TTL      : YES
   Config type    : normal-vrrp
   Backup-forward : disabled
   Config track link-bfd down-number : 0
   Track BFD          : 1  
   type               : peer
   BFD-session state  : DOWN
   Create time        : 2011-11-23 10:55:13    
   Last change time   : 2011-11-23 14:45:05          
   ```
   ```
   [~NPE2] display vrrp
   ```
   ```
   GigabitEthernet0/1/0.1 | Virtual Router 1
   State          : Backup
   Virtual IP     : 192.168.1.11
   Master IP      : 192.168.1.2
   Local IP       : 192.168.1.3
   PriorityRun    : 100
   PriorityConfig : 100
   MasterPriority : 200
   Preempt        : YES   Delay Time : 0 s
   Hold Multiplier: 4
   TimerRun       : 1 s
   TimerConfig    : 1 s
   Auth type      : NONE
   Virtual MAC    : 00e0-fc12-7880
   Check TTL      : YES
   Config type    : normal-vrrp
   Backup-forward : disabled
   Config track link-bfd down-number : 0
   Track BFD          : 2  
   type               : peer
   BFD-session state  : UP
   Create time        : 2011-11-23 10:15:28    
   Last change time   : 2011-11-23 14:04:29        
   ```
5. Establish a BFD session between NPE1 and NPE2.
   
   
   
   # Configure NPE1.
   
   ```
   [*NPE1] bfd
   ```
   ```
   [*NPE1-bfd] quit
   ```
   ```
   [*NPE1] bfd NPE1toNPE2 bind peer-ip 192.168.1.3 interface GigabitEthernet0/1/0.1
   ```
   ```
   [*NPE1-bfd-session-NPE1toNPE2] discriminator local 1
   ```
   ```
   [*NPE1-bfd-session-NPE1toNPE2] discriminator remote 2
   ```
   ```
   [*NPE1-bfd-session-NPE1toNPE2] commit
   ```
   ```
   [*NPE1-bfd-session-NPE1toNPE2] quit
   ```
   
   # Configure NPE2.
   
   ```
   [*NPE2] bfd
   ```
   ```
   [*NPE2-bfd] quit
   ```
   ```
   [*NPE2] bfd NPE2toNPE1 bind peer-ip 192.168.1.2 interface GigabitEthernet0/1/0.1
   ```
   ```
   [*NPE2-bfd-session-NPE2toNPE1] discriminator local 2
   ```
   ```
   [*NPE2-bfd-session-NPE2toNPE1] discriminator remote 1
   ```
   ```
   [*NPE2-bfd-session-NPE2toNPE1] commit
   ```
   ```
   [*NPE2-bfd-session-NPE2toNPE1] quit
   ```
6. Verify the BFD configuration.
   
   
   
   After the configuration is complete, run the [**display bfd session**](cmdqueryname=display+bfd+session) command on each NPE to view its BFD session status. The following example uses the command output on NPE1.
   
   ```
   [*NPE1] display bfd session all
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local Remote PeerIpAddr      State     Type        InterfaceName
   --------------------------------------------------------------------------------
   1     2      192.168.1.3        Up        S_IP_IF     GigabitEthernet0/1/0.1
   --------------------------------------------------------------------------------
        Total UP/DOWN Session Number : 1/0                                       
   ```
7. Configure routes on each NPE and PE1.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] interface GigabitEthernet 0/1/2
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] ip address 192.168.3.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] ip address 192.168.2.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] default cost inherit-metric
   ```
   ```
   [*PE1-ospf-1] import-route direct
   ```
   ```
   [*PE1-ospf-1] area 0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE1-ospf-1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   
   
   # Configure NPE1.
   
   ```
   [~NPE1] interface GigabitEthernet 0/1/2
   ```
   ```
   [*NPE1-GigabitEthernet0/1/2] ip address 192.168.2.1 24
   ```
   ```
   [*NPE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*NPE1] ospf 1
   ```
   ```
   [*NPE1-ospf-1] default cost inherit-metric
   ```
   ```
   [*NPE1-ospf-1] import-route direct
   ```
   ```
   [*NPE1-ospf-1] area 0
   ```
   ```
   [*NPE1-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   ```
   ```
   [*NPE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*NPE1-ospf-1] quit
   ```
   ```
   [*NPE1] commit
   ```
   
   
   
   # Configure NPE2.
   
   ```
   [*NPE2] interface GigabitEthernet 0/1/2
   ```
   ```
   [*NPE2-GigabitEthernet0/1/2] ip address 192.168.3.1 24
   ```
   ```
   [*NPE2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*NPE2] ospf 1
   ```
   ```
   [*NPE2-ospf-1] default cost inherit-metric
   ```
   ```
   [*NPE2-ospf-1] import-route direct
   ```
   ```
   [*NPE2-ospf-1] area 0
   ```
   ```
   [*NPE2-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255
   ```
   ```
   [*NPE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*NPE2-ospf-1] quit
   ```
   ```
   [*NPE2] commit
   ```
8. Verify the route configuration.
   
   
   
   After the configuration is complete, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on PE1 to view information about the route to the network segment 192.168.1.0.
   
   ```
   [~PE1] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: Public
            Destinations : 19       Routes : 19
   
   Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface
   
        10.137.0.0/16  Static  60   0          RD   10.137.130.1    GigabitEthernet0/1/0
      10.137.130.0/23  Static  60   0          RD   10.137.130.1    GigabitEthernet0/1/0
      10.137.130.0/24  Direct  0    0           D   10.137.130.47   GigabitEthernet0/1/0
     10.137.130.47/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/00
    10.137.130.255/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/0
        10.138.0.0/15  Static  60   0          RD   10.137.130.1    GigabitEthernet0/1/0
         10.1.2.0/24   O_ASE   150  0           D   192.168.3.1     GigabitEthernet0/1/2
         127.0.0.0/8   Direct  0    0           D   127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0           D   127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0           D   127.0.0.1       InLoopBack0
       192.168.1.0/24  O_ASE   150  0           D   192.168.2.1     GigabitEthernet0/1/1
      192.168.1.11/32  O_ASE   150  0           D   192.168.2.1     GigabitEthernet0/1/1
       192.168.2.0/24  Direct  0    0           D   192.168.2.2     GigabitEthernet0/1/1
       192.168.2.2/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/1
     192.168.2.255/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/1
       192.168.3.0/24  Direct  0    0           D   192.168.3.2     GigabitEthernet0/1/2
       192.168.3.2/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/2
     192.168.3.255/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/2
   255.255.255.255/32  Direct  0    0           D   127.0.0.1       InLoopBack0
   
   
   ```
9. Associate CFM with VRRP on each NPE.
   
   
   
   # Configure NPE1.
   
   ```
   [~NPE1] oam-mgr
   ```
   ```
   [*NPE1-oam-mgr] oam-bind ingress cfm md mdforvrrp ma ma1 egress vrrp vrid 1 interface GigabitEthernet 0/1/0.1
   ```
   ```
   [*NPE1-oam-mgr] quit
   ```
   ```
   [*NPE1] commit
   ```
   
   # Configure NPE2.
   
   ```
   [*NPE2] oam-mgr
   ```
   ```
   [*NPE2-oam-mgr] oam-bind ingress cfm md mdforvrrp ma ma2 egress vrrp vrid 1 interface GigabitEthernet 0/1/0.1
   ```
   ```
   [*NPE2-oam-mgr] quit
   ```
   ```
   [*NPE2] commit
   ```
10. Associate VRRP with peer BFD on each NPE.
    
    
    
    # Configure NPE1.
    
    ```
    [~NPE1] interface GigabitEthernet 0/1/0.1
    ```
    ```
    [*NPE1-GigabitEthernet0/1/0.1] vrrp vrid 1 track bfd-session 1 peer
    ```
    ```
    [*NPE1-GigabitEthernet0/1/0.1] quit
    ```
    ```
    [*NPE1] commit
    ```
    
    # Configure NPE2.
    
    ```
    [*NPE2] interface GigabitEthernet 0/1/0.1
    ```
    ```
    [*NPE2-GigabitEthernet0/1/0.1] vrrp vrid 1 track bfd-session 2 peer
    ```
    ```
    [*NPE2-GigabitEthernet0/1/0.1] quit
    ```
    ```
    [*NPE2] commit
    ```
11. Verify the association between VRRP and peer BFD.
    
    
    
    After the configuration is complete, run the [**display vrrp**](cmdqueryname=display+vrrp) command on each NPE to view the association between VRRP and peer BFD. The following example uses the command output on NPE2.
    
    ```
    [~NPE2] display vrrp
    ```
    ```
      GigabitEthernet0/1/0.1 | Virtual Router 1
        State : Master
        Virtual IP : 192.168.1.11
        Master IP : 192.168.1.2
        Local IP : 192.168.1.3
        PriorityRun : 200
        PriorityConfig : 200
        MasterPriority : 200
        Preempt : YES   Delay Time : 0 s
        Hold Multiplier: 4
        TimerRun : 1 s
        TimerConfig : 1 s
        Auth type : NONE
        Virtual MAC : 00e0-fc12-7880
        Check TTL : YES
        Config type : normal-vrrp
        Backup-forward    : disabled
        Config track link-bfd down-number : 0
        Track BFD : 1  type: peer
        BFD-session state : UP
        Create time : 2011-11-23 10:55:13
        Last change time : 2011-11-23 14:45:05           
    ```
12. Associate VRRP with direct routes on each NPE.
    
    
    
    # Configure NPE1.
    
    ```
    [~NPE1] interface GigabitEthernet 0/1/0.1
    ```
    ```
    [*NPE1-GigabitEthernet0/1/0.1] direct-route track vrrp vrid 1 degrade-cost 200
    ```
    ```
    [*NPE1-GigabitEthernet0/1/0.1] quit
    ```
    ```
    [*NPE1] commit
    ```
    
    # Configure NPE2.
    
    ```
    [*NPE2] interface GigabitEthernet 0/1/0.1
    ```
    ```
    [*NPE2-GigabitEthernet0/1/0.1] direct-route track vrrp vrid 1 degrade-cost 10
    ```
    ```
    [*NPE2-GigabitEthernet0/1/0.1] quit
    ```
    ```
    [*NPE2] commit
    ```
13. Verify the configuration.
    
    
    
    After the configuration is complete, run the [**shutdown**](cmdqueryname=shutdown) command on UPE1's GE 0/1/1 to simulate a link fault. The **display vrrp** command outputs show that NPE1's and NPE2's VRRP statuses have changed. The **display ip routing-table** command output shows that the outbound interface of the route to the user side has changed.
    
    ```
    [~NPE1] display vrrp
    ```
    ```
      GigabitEthernet0/1/0.1 | Virtual Router 1
        State : Initialize
        Virtual IP : 192.168.1.11
        Master IP : 0.0.0.0
        Local IP : 192.168.1.2
        PriorityRun : 200
        PriorityConfig : 200
        MasterPriority : 0
        Preempt : YES   Delay Time : 0 s
        Hold Multiplier: 4
        TimerRun : 1 s
        TimerConfig : 1 s
        Auth type : NONE
        Virtual MAC : 00e0-fc12-7880
        Check TTL : YES
        Config type : normal-vrrp
        Backup-forward    : disabled
        Config track link-bfd down-number : 0
        Track BFD : 1  type: peer
        BFD-session state : DOWN
        Create time : 2011-11-23 10:55:13
        Last change time : 2011-11-23 14:38:02       
    ```
    ```
    [~NPE2] display vrrp
    ```
    ```
      GigabitEthernet0/1/0.1 | Virtual Router 1
        State : Master
        Virtual IP : 192.168.1.11
        Master IP : 192.168.1.3
        Local IP : 192.168.1.3
        PriorityRun : 100
        PriorityConfig : 100
        MasterPriority : 100
        Preempt : YES   Delay Time : 0 s
        Hold Multiplier: 4
        TimerRun : 1 s
        TimerConfig : 1 s
        Auth type : NONE
        Virtual MAC : 00e0-fc12-7880
        Check TTL : YES
        Config type : normal-vrrp
        Backup-forward    : disabled
        Config track link-bfd down-number : 0
        Track BFD : 2  type: peer
        BFD-session state : DOWN
        Create time : 2011-11-23 10:15:28
        Last change time : 2011-11-23 13:57:24        
    ```
    ```
    [~PE] display ip routing-table
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table: Public
             Destinations : 19       Routes : 19
    
    Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface
    
         10.137.0.0/16  Static  60   0          RD   10.137.130.1    GigabitEthernet0/1/0
       10.137.130.0/23  Static  60   0          RD   10.137.130.1    GigabitEthernet0/1/0
       10.137.130.0/24  Direct  0    0           D   10.137.130.47   GigabitEthernet0/1/0
      10.137.130.47/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/0
     10.137.130.255/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/0
         10.138.0.0/15  Static  60   0          RD   10.137.130.1    GigabitEthernet0/1/0
          10.1.2.0/24   O_ASE   150  0           D   192.168.3.1     GigabitEthernet0/1/2
          127.0.0.0/8   Direct  0    0           D   127.0.0.1       InLoopBack0
          127.0.0.1/32  Direct  0    0           D   127.0.0.1       InLoopBack0
    127.255.255.255/32  Direct  0    0           D   127.0.0.1       InLoopBack0
        192.168.1.0/24  O_ASE   150  0           D   192.168.3.1     GigabitEthernet0/1/2
       192.168.1.11/32  O_ASE   150  0           D   192.168.3.1     GigabitEthernet0/1/2
        192.168.2.0/24  Direct  0    0           D   192.168.2.2     GigabitEthernet0/1/1
        192.168.2.2/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/1
      192.168.2.255/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/1
        192.168.3.0/24  Direct  0    0           D   192.168.3.2     GigabitEthernet0/1/2
        192.168.3.2/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/2
      192.168.3.255/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/2
    255.255.255.255/32  Direct  0    0           D   127.0.0.1       InLoopBack0  
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #                                                                               
  sysname PE1                                                   
  #                                              
  cfm version standard                                                            
  cfm enable
  #                                                                           
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 192.168.2.2 255.255.255.0                                           
  #                                                                           
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 192.168.3.2 255.255.255.0                                           
  #                                                                               
  interface LoopBack0                                                           
   ip address 1.1.1.1 255.255.255.255                                             
  #                                                              
  ospf 1                                                                          
   default cost inherit-metric                                                    
   import-route direct                                                            
   area 0.0.0.0 
    network 1.1.1.1 0.0.0.0                                                                  
    network 192.168.2.0 0.0.0.255                                                 
    network 192.168.3.0 0.0.0.255                                                 
  #                                                                 
  return        
  ```
* NPE1 configuration file
  
  ```
  #                                                                               
  sysname NPE1                                                                      
  #                                            
  cfm version standard                                                            
  cfm enable                                                                      
  #                                                                               
  bfd 
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
  #                                                                               
  interface GigabitEthernet0/1/0.1                                                
   vlan-type dot1q 2                                                              
   ip address 192.168.1.2 255.255.255.0                                              
   vrrp vrid 1 virtual-ip 192.168.1.11                                               
   vrrp vrid 1 track bfd-session 1 peer                                           
   direct-route track vrrp vrid 1 degrade-cost 200                                
  #                                                                 
  interface GigabitEthernet0/1/2                                                 
   undo shutdown                                                                  
   ip address 192.168.2.1 255.255.255.0                  
  #                                                                               
  bfd NPE1toNPE2 bind peer-ip 192.168.1.3 interface GigabitEthernet0/1/0.1           
   discriminator local 1                                                          
   discriminator remote 2                                                         
   commit                                                                         
  #                                                                               
  ospf 1                                                                          
   default cost inherit-metric                                                    
   import-route direct                                                            
   area 0.0.0.0                                                                   
    network 192.168.2.0 0.0.0.255                                                 
  #                                                                               
  cfm md mdforvrrp                                                                
   ma ma1                                                                         
    mep mep-id 1 interface GigabitEthernet0/1/0.1 vlan 2 outward                  
    mep ccm-send mep-id 1 enable                                                  
    remote-mep mep-id 2                                                           
    remote-mep ccm-receive mep-id 2 enable                                        
  #                                                                            
  oam-mgr                                                                         
   oam-bind ingress cfm md mdforvrrp ma ma1 egress vrrp vrid 1 interface GigabitEthernet0/1/0.1 
  #                                                                                
  return   
  ```
* UPE2 configuration file
  
  ```
  #                                                                               
  sysname UPE2                                                                      
  #                                              
  cfm version standard                                                            
  cfm enable                                                                      
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
  cfm md mdforvrrp                                                                
   ma ma1                                                                         
    map vlan 2                                                                    
    mep mep-id 2 interface GigabitEthernet0/1/1 outward                           
    mep ccm-send mep-id 2 enable                                                  
    remote-mep mep-id 1                                                           
    remote-mep ccm-receive mep-id 1 enable                                        
   ma ma2                                                                         
    map vlan 2                                                                    
    mep mep-id 3 interface GigabitEthernet0/1/0 outward                           
    mep ccm-send mep-id 3 enable                                                  
    remote-mep mep-id 4                                                           
    remote-mep ccm-receive mep-id 4 enable                                        
  #                                                                           
  return     
  ```
* NPE2 configuration file
  
  ```
  #                                                                               
  sysname NPE2                                                                      
  #                                                                               
  FTP server enable                                                               
  #                                    
  cfm version standard                                                            
  cfm enable                              
  #                                                                               
  bfd                                                                   
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 192.168.3.1 255.255.255.0                                           
  #                                                                         
  interface GigabitEthernet0/1/0.1                                                
   vlan-type dot1q 2                                                              
   ip address 192.168.1.3 255.255.255.0                                              
   vrrp vrid 1 virtual-ip 192.168.1.11                                               
   vrrp vrid 1 track bfd-session 2 peer                                           
   direct-route track vrrp vrid 1 degrade-cost 10                                 
  #                                                                              
  interface LoopBack100                                                           
   ip address 3.3.3.3 255.255.255.255                                             
  # 
  bfd NPE2toNPE1 bind peer-ip 192.168.1.2 interface GigabitEthernet0/1/0.1           
   discriminator local 2                                                          
   discriminator remote 1                                                         
   commit                                                                         
  #                                                                               
  ospf 1                                                                          
   default cost inherit-metric                                                    
   import-route direct                                                            
   area 0.0.0.0                                                                   
    network 192.168.3.0 0.0.0.255                                                 
  #                                                             
  cfm md mdforvrrp                                                                
   ma ma2                                                                         
    mep mep-id 4 interface GigabitEthernet0/1/0.1 vlan 2 outward                  
    mep ccm-send mep-id 4 enable                                                  
    remote-mep mep-id 3                                                           
    remote-mep ccm-receive mep-id 3 enable                                        
  #  
  oam-mgr                                                                         
   oam-bind ingress cfm md mdforvrrp ma ma2 egress vrrp vrid 1 interface GigabitEthernet0/1/0.1 
  #
  return  
  ```
* UPE1 configuration file
  
  ```
  #                                                                               
  sysname UPE1                                                                      
  #                                                                               
  FTP server enable                                                               
  #                                      
  cfm version standard                                                            
  cfm enable                                                                      
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
  return 
  ```
* UPE3 configuration file
  
  ```
  #                                                                               
  sysname UPE3                                                                      
  #                                                                               
  FTP server enable                                                               
  #                                      
  cfm version standard                                                            
  cfm enable                                                                      
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
  return 
  ```