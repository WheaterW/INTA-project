Example for Configuring Distributed NAT444 Inter-Chassis Hot Backup (Global VE Interface Scenario)
==================================================================================================

This section provides an example for configuring NAT inter-chassis hot backup (global VE interface scenario) in distributed deployment mode.

#### Networking Requirements

In distributed deployment networking shown in [Figure 1](#EN-US_TASK_0295928544__fig144014448151), NAT service boards are installed in slot 1 on BRAS1 and slot 1 on BRAS2, respectively. A VRRP channel is established between the two BRASs through global VE interfaces. CPU 0 on the NAT service board in slot 1 of BRAS1 work with CPU 0 on the NAT service board in slot 1 of BRAS2 to implement NAT inter-chassis hot backup. The NAT service's master/backup status is determined by VRRP, and the service board status is associated with VRRP.

**Figure 1** Networking diagram of configuring distributed dual-device inter-chassis backup![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1, interface 2.2, interface 3, and interface 4 in this example represent global VE 1.1, GE 0/1/2.2, GE 0/1/3, and GE 0/1/4, respectively.


  
![](figure/en-us_image_0305262333.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set the number of sessions supported by the service board in slot 1 to 6M.
2. Configure HA hot backup, with NAT service information backed up.
3. Assign IP addresses to interfaces, configure routes, and enable MPLS on loopback interfaces.
4. Create global VE interfaces on the master and backup devices.
5. Create a service-location group, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel between BRAS1 and BRAS2.
6. Create and configure VRRP groups.
7. Configure BFD and configure the VRRP groups to track the BFD session status.
8. Associate HA with VRRP.
9. Bind the service-location group to the VRRP groups.
10. Create a service-instance group and bind it to the service-location group.
11. Create NAT instances.
12. Configure user information (user group, IP address pool, user domain, and AAA), configure RADIUS authentication on the BRAS, and bind the user group to the NAT instance.
13. Configure a NAT traffic diversion policy and a NAT conversion policy on BRAS1 and BRAS2.
14. Configure a user-side VRRP group on BRAS1 and BRAS2 that are connected to the switch.
15. Configure an RBS and bind a service-instance group to the RBS.
16. Configure RUI to back up BRAS information of users.
17. Bind the NAT instance to the service-instance group.
18. Configure a user-side sub-interface.

#### Data Preparation

To complete the configuration, you need the following data:

| No. | Data |
| --- | --- |
| 1 | Index of a service-location group |
| 2 | Slot ID and CPU ID of the active CPU on a service board of BRAS1 (CPU 0 in slot 1 in this example) |
| 3 | Slot ID and CPU ID of the standby CPU on a service board of BRAS2 (CPU 0 in slot 1 in this example) |
| 4 | IP addresses of interfaces on BRAS1 and BRAS2 |
| 5 | Names of global VE interfaces on BRAS1 and BRAS2 |
| 4 | Names of VRRP interfaces on BRAS1 and BRAS2 |
| 5 | IP addresses of VRRP interfaces on BRAS1 and BRAS2 |
| 6 | ID of a VRRP group |
| 7 | Virtual IP address of a VRRP group |
| 8 | Priorities of VRRP group members |
| 9 | VRRP preemption delay |
| 10 | Name of a service-instance group |
| 11 | Name and index of a NAT instance |
| 12 | IP address pool, IP address of the address pool gateway, and IP address segment of BRAS1 and BRAS2 |
| 13 | Names of the user group and user domain, and AAA schemes on the devices at both ends |
| 14 | Remote backup identifiers for RUI backup of BRAS1 and BRAS2 |
| 15 | Names of user-side interfaces on BRAS1 and BRAS2 |
| 16 | IP addresses of user-side interfaces on BRAS1 and BRAS2 |
| 17 | Index of the user-side VRRP groups on BRAS1 and BRAS2 |
| 18 | Virtual IP address of the user-side VRRP groups on BRAS1 and BRAS2 |
| 19 | User-side VRRP priorities on BRAS1 and BRAS2 |
| 20 | Preemption delay of the user-side VRRP groups on the devices at both ends |




#### Procedure

1. Set the number of sessions supported by the service boards in slot 1 on the master and backup devices to 6M.
   
   # Configure BRAS1.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS1] vsm on-board-mode disable
   ```
   ```
   [*BRAS1] commit
   ```
   ```
   [~BRAS1] license
   ```
   ```
   [~BRAS1-license] active nat session-table size 6 slot 1 
   ```
   ```
   [*BRAS1-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS1-license] commit
   ```
   ```
   [~BRAS1-license] quit
   ```
   # Configure BRAS2.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS2] vsm on-board-mode disable
   ```
   ```
   [*BRAS2] commit
   ```
   ```
   [~BRAS2] license
   ```
   ```
   [*BRAS2-license] active nat session-table size 6 slot 1 
   ```
   ```
   [*BRAS2-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS2-license] commit
   ```
   ```
   [~BRAS2-license] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The method for configuring bandwidth resources varies according to the board type. As such, determine whether to run the **active nat bandwidth-enhance** command and the corresponding parameters based on the board type.
2. Enable HA hot backup on BRAS1 and BRAS2.
   
   
   
   # Enable HA hot backup on BRAS1.
   
   ```
   [~BRAS1] service-ha hot-backup enable
   ```
   ```
   [*BRAS1] commit
   ```
   
   # Enable HA hot backup on BRAS2.
   
   ```
   [~BRAS2] service-ha hot-backup enable
   ```
   ```
   [*BRAS2] commit
   ```
3. Configure IP addresses for interfaces.
   
   # Configure IP addresses for interfaces on BRAS1.
   ```
   [~BRAS1] interface LoopBack0
   ```
   ```
   [*BRAS1-LoopBack0] ip address 1.1.1.1 255.255.255.255
   ```
   ```
   [*BRAS1-LoopBack0] commit
   ```
   ```
   [~BRAS1-LoopBack0] qui
   ```
   ```
   [~BRAS1] interface GigabitEthernet0/1/3
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/3] ip address 10.2.1.1 255.255.255.255
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/3] commit
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/3] quit
   ```
   
   # Configure IP addresses for interfaces on BRAS2.
   
   ```
   [~BRAS2] interface LoopBack0
   ```
   ```
   [*BRAS2-LoopBack0] ip address 1.1.1.2 255.255.255.255
   ```
   ```
   [*BRAS2-LoopBack0] commit
   ```
   ```
   [~BRAS2-LoopBack0] quit
   ```
   ```
   [~BRAS1] interface GigabitEthernet0/1/4
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/4] ip address 10.3.1.2 255.255.255.255
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/4] commit
   ```
   ```
   [~BRAS1-GigabitEthernet0/1/4] quit
   ```
   
   # Configure IP addresses for interfaces on the CR.
   
   ```
   [~CR] interface GigabitEthernet0/1/3
   ```
   ```
   [*CR-GigabitEthernet0/1/3] ip address 10.2.1.2 255.255.255.255
   ```
   ```
   [*CR-GigabitEthernet0/1/3] quit
   ```
   ```
   [*CR] interface GigabitEthernet0/1/4
   ```
   ```
   [*CR-GigabitEthernet0/1/4] ip address 10.3.1.1 255.255.255.255
   ```
   ```
   [*CR-GigabitEthernet0/1/4] quit
   ```
   ```
   [*CR] commit
   ```
4. Enable OSPF.
   
   
   
   # Enable OSPF on BRAS1.
   
   ```
   [~BRAS1] ospf 1
   ```
   ```
   [*BRAS1-ospf-1] area 0
   ```
   ```
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*BRAS1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*BRAS1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*BRAS1-ospf-1] commit
   ```
   
   
   
   # Enable OSPF on BRAS2.
   
   ```
   [~BRAS2] ospf 1
   ```
   ```
   [*BRAS2-ospf-1] area 1
   ```
   ```
   [*BRAS2-ospf-1-area-0.0.0.1] network 10.3.1.0 0.0.0.255
   ```
   ```
   [*BRAS2-ospf-1-area-0.0.0.1] network 1.1.1.2 0.0.0.0
   ```
   ```
   [*BRAS2-ospf-1-area-0.0.0.1] quit
   ```
   ```
   [*BRAS2-ospf-1] commit
   ```
   
   
   
   # Enable OSPF on the CR.
   
   ```
   [~BRAS2] ospf 1
   ```
   ```
   [*BRAS2-ospf-1] area 0
   ```
   ```
   [*BRAS2-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*BRAS2-ospf-1] area 1
   ```
   ```
   [*BRAS2-ospf-1-area-0.0.0.1] network 10.3.1.0 0.0.0.255
   ```
   ```
   [*BRAS2-ospf-1-area-0.0.0.1] quit
   ```
   ```
   [*BRAS2-ospf-1] commit
   ```
5. Enable MPLS.
   
   
   
   # Configure MPLS on BRAS1.
   
   ```
   [~BRAS1] mpls lsr-id 1.1.1.1
   ```
   ```
   [*BRAS1] mpls
   ```
   ```
   [*BRAS1-mpls] quit
   ```
   ```
   [*BRAS1] mpls ldp
   ```
   ```
   [*BRAS1-mpls-ldp] quit
   ```
   ```
   [*BRAS1] interface GigabitEthernet0/1/3
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/3] mpls
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/3] mpls ldp
   ```
   ```
   [*BRAS1-GigabitEthernet0/1/3] quit
   ```
   ```
   [*BRAS1] commit
   ```
   ```
   [~BRAS1] mpls ldp
   ```
   ```
   [*BRAS1-mpls-ldp] ipv4-family
   ```
   ```
   [*BRAS1-mpls-ldp-ipv4] commit
   ```
   ```
   [~BRAS1-mpls-ldp-ipv4] quit
   ```
   ```
   [~BRAS1] mpls l2vpn
   ```
   ```
   [*BRAS1-l2vpn] commit
   ```
   ```
   [~BRAS1-l2vpn] quit
   ```
   ```
   [~BRAS1] mpls ldp remote-peer peer-bas
   ```
   ```
   [*BRAS1-mpls-ldp-remote-peer-bas] remote-ip 1.1.1.2 
   ```
   ```
   [*BRAS1] commit 
   ```
   
   # Configure MPLS on BRAS2.
   
   ```
   [~BRAS2] mpls lsr-id 1.1.1.2
   ```
   ```
   [*BRAS2] mpls
   ```
   ```
   [*BRAS2-mpls] quit
   ```
   ```
   [*BRAS2] mpls ldp
   ```
   ```
   [*BRAS2-mpls-ldp] quit
   ```
   ```
   [*BRAS2] interface GigabitEthernet0/1/4
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/4] mpls
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/4] mpls ldp
   ```
   ```
   [*BRAS2-GigabitEthernet0/1/4] quit
   ```
   ```
   [*BRAS2] commit
   ```
   ```
   [~BRAS2] mpls ldp
   ```
   ```
   [*BRAS2-mpls-ldp] ipv4-family
   ```
   ```
   [*BRAS2-mpls-ldp-ipv4] commit
   ```
   ```
   [~BRAS2-mpls-ldp-ipv4] quit
   ```
   ```
   [~BRAS2] mpls l2vpn
   ```
   ```
   [*BRAS2-l2vpn] commit
   ```
   ```
   [~BRAS2-l2vpn] quit
   ```
   ```
   [~BRAS2] mpls ldp remote-peer peer-bas
   ```
   ```
   [*BRAS2-mpls-ldp-remote-peer-bas] remote-ip 1.1.1.1 
   ```
   ```
   [*BRAS2] commit 
   ```
   
   # Enable MPLS on the CR.
   
   ```
   [~CR] mpls lsr-id 1.1.1.3
   ```
   ```
   [*CR] mpls
   ```
   ```
   [*CR-mpls] quit
   ```
   ```
   [*CR] mpls ldp
   ```
   ```
   [*CR-mpls-ldp] quit
   ```
   ```
   [*CR] interface GigabitEthernet0/1/3
   ```
   ```
   [*CR-GigabitEthernet0/1/3] mpls
   ```
   ```
   [*CR-GigabitEthernet0/1/3] mpls ldp
   ```
   ```
   [*CR-GigabitEthernet0/1/3] quit
   ```
   ```
   [*CR] interface GigabitEthernet0/1/4
   ```
   ```
   [*CR-GigabitEthernet0/1/4] mpls
   ```
   ```
   [*CR-GigabitEthernet0/1/4] mpls ldp
   ```
   ```
   [*CR-GigabitEthernet0/1/4] quit
   ```
   ```
   [*CR] commit
   ```
6. Create global VE interfaces on the master and backup devices.
   
   
   
   # Create global VE interfaces on BRAS1.
   
   ```
   [~BRAS1] interface Global-VE0
   ```
   ```
   [*BRAS1-Global-VE0] ve-group 2001 l2-terminate 
   ```
   ```
   [*BRAS1-Global-VE0] commit
   ```
   ```
   [~BRAS1-Global-VE0] quit
   ```
   ```
   [~BRAS1] interface Global-VE0.1
   ```
   ```
   [*BRAS1-Global-VE0.1] vlan-type dot1q 2001
   ```
   ```
   [*BRAS1-Global-VE0.1] mpls l2vc 1.1.1.2 2001
   ```
   ```
   [*BRAS1-Global-VE0.1] commit
   ```
   ```
   [~BRAS1-Global-VE0.1] quit
   ```
   ```
   [~BRAS1] interface Global-VE1
   ```
   ```
   [*BRAS1-Global-VE1] ve-group 2001 l3-access 
   ```
   ```
   [*BRAS1-Global-VE1] commit
   ```
   ```
   [~BRAS1-Global-VE1] quit
   ```
   ```
   [~BRAS1] interface Global-VE1.1
   ```
   ```
   [*BRAS1-Global-VE1.1] vlan-type dot1q 2001
   ```
   ```
   [*BRAS1-Global-VE1.1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*BRAS1-Global-VE1.1] commit
   ```
   ```
   [~BRAS1-Global-VE1.1] quit
   ```
   
   # Create global VE interfaces on BRAS2.
   
   ```
   [~BRAS2] interface Global-VE0
   ```
   ```
   [*BRAS2-Global-VE0] ve-group 2001 l2-terminate 
   ```
   ```
   [*BRAS2-Global-VE0] commit
   ```
   ```
   [~BRAS2-Global-VE0] quit
   ```
   ```
   [~BRAS2] interface Global-VE0.1
   ```
   ```
   [*BRAS2-Global-VE0.1] vlan-type dot1q 2001
   ```
   ```
   [*BRAS2-Global-VE0.1] mpls l2vc 1.1.1.1 2001
   ```
   ```
   [*BRAS2-Global-VE0.1] commit
   ```
   ```
   [~BRAS2-Global-VE0.1] quit
   ```
   ```
   [~BRAS2] interface Global-VE1
   ```
   ```
   [*BRAS2-Global-VE1] ve-group 2001 l3-access 
   ```
   ```
   [*BRAS2-Global-VE1] commit
   ```
   ```
   [~BRAS2-Global-VE1] quit
   ```
   ```
   [~BRAS2] interface Global-VE1.1
   ```
   ```
   [*BRAS2-Global-VE1.1] vlan-type dot1q 2001
   ```
   ```
   [*BRAS2-Global-VE1.1] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*BRAS2-Global-VE1.1] commit
   ```
   ```
   [~BRAS2-Global-VE1.1] quit
   ```
7. Create a service-location group on BRAS1 and BRAS2, configure members for HA dual-device inter-chassis backup, and configure a VRRP channel.
   
   
   
   # Create service-location group 1 on BRAS1, add CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to global VE 1.1 and the peer IP address to 10.1.1.2.
   
   ```
   [~BRAS1] service-location 1
   ```
   ```
   [*BRAS1-service-location-1] location slot 1 
   ```
   ```
   [*BRAS1-service-location-1] remote-backup interface Global-VE1.1 peer 10.1.1.2
   ```
   ```
   [*BRAS1-service-location-1] commit
   ```
   ```
   [~BRAS1-service-location-1] quit
   ```
   
   # Create service-location group 1 on BRAS2, add CPU 0 in slot 1 as an HA dual-device inter-chassis backup member, and set the local VRRP outbound interface to global VE 1.1 and the peer IP address to 10.1.1.1.
   
   ```
   [~BRAS2] service-location 1
   ```
   ```
   [*BRAS2-service-location-1] location slot 1 
   ```
   ```
   [*BRAS2-service-location-1] remote-backup interface Global-VE1.1 peer 10.1.1.1
   ```
   ```
   [*BRAS2-service-location-1] commit
   ```
   ```
   [~BRAS2-service-location-1] quit
   ```
8. Configure a VRRP group on BRAS1 and BRAS2.
   
   
   
   # On BRAS1, enter the view of global VE 1.1 interface, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. Configure the VRRP group as an mVRRP group, and set BRAS1's priority in the VRRP group to 200, the VRRP preemption delay to 1500s, and the VRRP recovery delay to 20s.
   
   ```
   [~BRAS1] interface Global-VE1.1
   ```
   ```
   [~BRAS1-Global-VE1.1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*BRAS1-Global-VE1.1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*BRAS1-Global-VE1.1] vrrp vrid 1 priority 200
   ```
   ```
   [*BRAS1-Global-VE1.1] vrrp vrid 1 preempt-mode timer delay 1500
   ```
   ```
   [*BRAS1-Global-VE1.1] vrrp recover-delay 20
   ```
   ```
   [*BRAS1-Global-VE1.1] commit
   ```
   ```
   [~BRAS1-Global-VE1.1] quit
   ```
   
   # On BRAS2, enter the view of global VE 1.1 interface, create VRRP group 1, and set the virtual IP address of the VRRP group to 10.1.1.3. Configure the VRRP group as an mVRRP group, set BRAS2's priority in the VRRP group to 150, and set the VRRP recovery delay to 15s.
   
   ```
   [~BRAS2] interface Global-VE1.1
   ```
   ```
   [*BRAS2-Global-VE1.1] vrrp vrid 1 virtual-ip 10.1.1.3
   ```
   ```
   [*BRAS2-Global-VE1.1] admin-vrrp vrid 1 ignore-if-down
   ```
   ```
   [*BRAS2-Global-VE1.1] vrrp vrid 1 priority 150
   ```
   ```
   [*BRAS2-Global-VE1.1] vrrp recover-delay 15
   ```
   ```
   [*BRAS2-Global-VE1.1] commit
   ```
   ```
   [~BRAS2-Global-VE1.1] quit
   ```
9. Enable BFD on the master and backup devices and configure VRRP groups to track the BFD session status.
   
   
   
   In a global VE scenario, associate VRRP with BFD. Otherwise, delayed VRRP switchback may not take effect after the entire chassis is restarted, causing users to be logged out.
   
   
   
   # Enable BFD on BRAS1 and configure the VRRP group to track the BFD session status.
   
   ```
   [~BRAS1] bfd
   ```
   ```
   [*BRAS1-bfd] commit
   ```
   ```
   [~BRAS1-bfd] quit
   ```
   ```
   [~BRAS1] bfd peer1 bind peer-ip 10.1.1.2 source-ip 10.1.1.1 auto
   ```
   ```
   [*BRAS1-bfd-session-peer1] commit
   ```
   ```
   [~BRAS1-bfd-session-peer1] quit
   ```
   ```
   [~BRAS1] interface Global-VE1.1
   ```
   ```
   [*BRAS1-Global-VE1.1] vrrp vrid 1 timer advertise 20
   ```
   ```
   [*BRAS1-Global-VE1.1] vrrp vrid 1 track bfd-session session-name peer1 peer
   ```
   ```
   [*BRAS1-Global-VE1.1] commit
   ```
   ```
   [~BRAS1-Global-VE1.1] quit
   ```
   
   # Enable BFD on BRAS2 and configure the VRRP group to track the BFD session status.
   
   ```
   [~BRAS2] bfd
   ```
   ```
   [*BRAS2-bfd] commit
   ```
   ```
   [~BRAS2-bfd] quit
   ```
   ```
   [~BRAS2] bfd peer1 bind peer-ip 10.1.1.1 source-ip 10.1.1.2 auto
   ```
   ```
   [*BRAS2-bfd-session-peer1] commit
   ```
   ```
   [~BRAS2-bfd-session-peer1] quit
   ```
   ```
   [~BRAS2] interface Global-VE1.1
   ```
   ```
   [*BRAS2-Global-VE1.1] vrrp vrid 1 timer advertise 20
   ```
   ```
   [*BRAS2-Global-VE1.1] vrrp vrid 1 track bfd-session session-name peer1 peer
   ```
   ```
   [*BRAS2-Global-VE1.1] commit
   ```
   ```
   [~BRAS2-Global-VE1.1] quit
   ```
10. Associate HA with VRRP on the master and backup devices.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    This configuration is optional on the backup device. You can determine whether to perform this step based on network requirements.
    
    
    
    # On BRAS1, enter the view of the global VE 1.1 interface, and associate service-location group 1 with VRRP group 1.
    
    ```
    [~BRAS1] interface Global-VE1.1
    ```
    ```
    [~BRAS1-Global-VE1.1] vrrp vrid 1 track service-location 1 reduced 60
    ```
    ```
    [*BRAS1-Global-VE1.1] commit
    ```
    ```
    [~BRAS1-Global-VE1.1] quit
    ```
    
    # On BRAS2, enter the view of the global VE 1.1 interface, and associate service-location group 1 with VRRP group 1.
    
    ```
    [~BRAS2] interface Global-VE1.1
    ```
    ```
    [~BRAS2-Global-VE1.1] vrrp vrid 1 track service-location 1 reduced 60
    ```
    ```
    [*BRAS2-Global-VE1.1] commit
    ```
    ```
    [~BRAS2-Global-VE1.1] quit
    ```
    
    # Run the [**display vrrp 1**](cmdqueryname=display+vrrp+1) command on BRAS1 and BRAS2 to view the master/backup VRRP status, which reflects the master/backup status of the service-location group. **State** in the command output indicates the BRAS status.
    
    ```
    [~BRAS1] display vrrp 1
    Global-VE1.1 | Virtual Router 1                                                                                      
        State                    : Master 
        Virtual IP               : 10.1.1.3  
        Master IP                : 10.1.1.1 
        Local IP                 : 10.1.1.1
        PriorityRun              : 200    
        PriorityConfig           : 200    
        MasterPriority           : 200    
        Preempt                  : YES    Delay Time      : 400 s    
        Hold Multiplier          : 3                                                                            
        TimerRun                 : 1 s    
        TimerConfig              : 1 s   
        Auth Type                : NONE    
        Virtual MAC              : 00e0-fc12-3456 
        Check TTL                : YES      
        Config Type              : admin-vrrp 
        Backup-forward           : disabled   
        Fast-resume              : disabled     
        Track Service-location   : 1   Priority Reduced : 60                                                         
        Service-location State   : UP                                                               
        Create Time              : 2011-10-18 11:14:48 UTC+10:59   
        Last Change Time         : 2011-10-18 14:02:46 UTC+10:59
    ```
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    **Master** in the command output indicates that BRAS1 is the master device.
    
    ```
    [~BRAS2] display vrrp 1
    Global-VE1.1 | Virtual Router 1                                                                                       
        State                   : Backup  
        Virtual IP              : 10.1.1.3   
        Master IP               : 10.1.1.1
        Local IP                : 10.1.1.2
        PriorityRun             : 150      
        PriorityConfig          : 150     
        MasterPriority          : 200    
        Preempt                 : YES     Delay Time    : 0 s  
        Hold Multiplier         : 3                                                              
        TimerRun                : 1 s     
        TimerConfig             : 1 s     
        Auth Type               : NONE    
        Virtual MAC             : 00e0-fc12-3456  
        Check TTL               : YES       
        Config Type             : admin-vrrp   
        Backup-forward          : disabled    
        Fast-resume             : disabled
        Track Service-location  : 1   Priority Reduced : 60                                                         
        Service-location State : UP   
        Create Time            : 2011-10-18 11:26:40 UTC+08:00  
        Last change Time       : 2011-10-18 14:02:22 UTC+08:00
    ```
11. Bind the service-location group to the VRRP group on BRAS1 and BRAS2.
    
    
    
    # Bind service-location group 1 to VRRP group 1 on BRAS1.
    
    ```
    [~BRAS1] service-location 1
    ```
    ```
    [~BRAS1-service-location-1] vrrp vrid 1 interface Global-VE1.1
    ```
    ```
    [*BRAS1-service-location-1] commit
    ```
    ```
    [~BRAS1-service-location-1] quit
    ```
    
    # Bind service-location group 1 to VRRP group 1 on BRAS2.
    
    ```
    [~BRAS2] service-location 1
    ```
    ```
    [~BRAS2-service-location-1] vrrp vrid 1 interface Global-VE1.1
    ```
    ```
    [*BRAS2-service-location-1] commit
    ```
    ```
    [~BRAS2-service-location-1] quit
    ```
12. Create a service-instance group on BRAS1 and BRAS2 and bind them to the service-location group.
    
    
    
    # Create a service-instance group named **group1** on BRAS1 and bind it to service-location group 1.
    
    ```
    [~BRAS1] service-instance-group group1
    ```
    ```
    [*BRAS1-service-instance-group-group1] service-location 1
    ```
    ```
    [*BRAS1-service-instance-group-group1] commit
    ```
    ```
    [~BRAS1-service-instance-group-group1] quit
    ```
    
    # Create a service-instance group named **group1** on BRAS2 and bind it to service-location group 1.
    
    ```
    [~BRAS2] service-instance-group group1
    ```
    ```
    [*BRAS2-service-instance-group-group1] service-location 1
    ```
    ```
    [*BRAS2-service-instance-group-group1] commit
    ```
    ```
    [~BRAS2-service-instance-group-group1] quit
    ```
    
    # Run the [**display service-location 1**](cmdqueryname=display+service-location+1) command on BRAS1 and BRAS2 to view HA information. **Vrrp state** in the command output indicates the status of a service-location group, which must be consistent with the BRAS's VRRP status. **Batch-backup state** in the command output indicates whether batch backup has been finished.
    
    ```
    [~BRAS1] display service-location 1
     service-location 1                                                                                                                
     Backup scene type: inter-box                                                                                                       
     Location slot ID: 1                                                                                                    
     Remote-backup interface: Global-VE1.1                                                                                     
     Peer: 10.1.1.2                                                                                                                   
     Vrrp ID: 1                                                                                                                       
     Vrrp bind interface: Global-VE1.1                                                                                         
     Vrrp state: master                                                                                                                 
     Bound service-instance-group number: 1                                                                                             
     Batch-backup state: finished
    ```
    ```
    [~BRAS2] display service-location 1
     service-location 1                                                                                                                
     Backup scene type: inter-box                                                                                                       
     Location slot ID: 1                                                                                                    
     Remote-backup interface: Global-VE1.1                                                                                      
     Peer: 10.1.1.1                                                                                                                   
     Vrrp ID: 1                                                                                                                       
     Vrrp bind interface: Global-VE1.1                                                                                          
     Vrrp state: slave                                                                                                                 
     Bound service-instance-group number: 1                                                                                             
     Batch-backup state: NA
    ```
13. Create a NAT instance on both master and backup devices.
    
    
    
    # Create a NAT instance named **nat** on BRAS1.
    
    ```
    [~BRAS1] nat instance nat id 1
    ```
    ```
    [*BRAS1-nat-instance-nat] commit
    ```
    ```
    [~BRAS1-nat-instance-nat] quit
    ```
    
    # Create a NAT instance named **nat** on BRAS2.
    
    ```
    [~BRAS2] nat instance nat id 1
    ```
    ```
    [*BRAS2-nat-instance-nat] commit
    ```
    ```
    [~BRAS2-nat-instance-nat] quit
    ```
14. Configure user information (user group named **natbras**, IP address pool named **natbras**, user domain named **natbras**, and AAA) and bind the user group to the NAT instance named **nat** on each of the master and backup devices.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] user-group natbras
    ```
    ```
    [~BRAS1] commit
    ```
    ```
    [~BRAS1] ip pool natbras bas local
    ```
    ```
    [*BRAS1-ip-pool-natbras] gateway 192.168.0.1 255.255.0.0
    ```
    ```
    [*BRAS1-ip-pool-natbras] commit
    ```
    ```
    [~BRAS1-ip-pool-natbras] section 0 192.168.0.2 192.168.0.254
    ```
    ```
    [~BRAS1-ip-pool-natbras] quit
    ```
    ```
    [~BRAS1] radius-server group rd1
    ```
    ```
    [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
    ```
    ```
    [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
    ```
    ```
    [*BRAS1-radius-rd1] radius-server shared-key YsHsjx_202206
    ```
    ```
    [*BRAS1-radius-rd1] commit
    ```
    ```
    [~BRAS1-radius-rd1] radius-server type plus11
    ```
    ```
    [~BRAS1-radius-rd1] radius-server traffic-unit kbyte
    ```
    ```
    [~BRAS1-radius-rd1] quit
    ```
    ```
    [~BRAS1] aaa
    ```
    ```
    [~BRAS1-aaa] authentication-scheme auth1
    ```
    ```
    [*BRAS1-aaa-authen-auth1] authentication-mode radius
    ```
    ```
    [*BRAS1-aaa-authen-auth1] commit
    ```
    ```
    [~BRAS1-aaa-authen-auth1] quit
    ```
    ```
    [~BRAS1-aaa] accounting-scheme acct1
    ```
    ```
    [*BRAS1-aaa-accounting-acct1] accounting-mode radius
    ```
    ```
    [~BRAS1-aaa-accounting-acct1] commit
    ```
    ```
    [~BRAS1-aaa-accounting-acct1] quit
    ```
    ```
    [~BRAS1-aaa] domain natbras
    ```
    ```
    [*BRAS1-aaa-domain-natbras] authentication-scheme auth1
    ```
    ```
    [*BRAS1-aaa-domain-natbras] accounting-scheme acct1
    ```
    ```
    [*BRAS1-aaa-domain-natbras] radius-server group rd1
    ```
    ```
    [*BRAS1-aaa-domain-natbras] commit
    ```
    ```
    [~BRAS1-aaa-domain-natbras] ip-pool natbras
    ```
    ```
    [~BRAS1-aaa-domain-natbras] user-group natbras bind nat instance nat
    ```
    ```
    [~BRAS1-aaa-domain-natbras] quit
    ```
    ```
    [~BRAS1-aaa] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] user-group natbras
    ```
    ```
    [~BRAS2] commit
    ```
    ```
    [~BRAS2] ip pool natbras bas local
    ```
    ```
    [*BRAS2-ip-pool-natbras] gateway 192.168.0.1 255.255.0.0
    ```
    ```
    [*BRAS2-ip-pool-natbras] commit
    ```
    ```
    [~BRAS2-ip-pool-natbras] section 0 192.168.0.2 192.168.0.254
    ```
    ```
    [~BRAS2-ip-pool-natbras] quit
    ```
    ```
    [~BRAS2] radius-server group rd1
    ```
    ```
    [*BRAS2-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
    ```
    ```
    [*BRAS2-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
    ```
    ```
    [*BRAS2-radius-rd1] radius-server shared-key YsHsjx_202206
    ```
    ```
    [*BRAS2-radius-rd1] commit
    ```
    ```
    [~BRAS2-radius-rd1] radius-server type plus11
    ```
    ```
    [~BRAS2-radius-rd1] radius-server traffic-unit kbyte
    ```
    ```
    [~BRAS2-radius-rd1] quit
    ```
    ```
    [~BRAS2] aaa
    ```
    ```
    [~BRAS2-aaa] authentication-scheme auth1
    ```
    ```
    [*BRAS2-aaa-authen-auth1] authentication-mode radius
    ```
    ```
    [*BRAS2-aaa-authen-auth1] commit
    ```
    ```
    [~BRAS2-aaa-authen-auth1] quit
    ```
    ```
    [~BRAS2-aaa] accounting-scheme acct1
    ```
    ```
    [*BRAS2-aaa-accounting-acct1] accounting-mode radius
    ```
    ```
    [~BRAS2-aaa-accounting-acct1] commit
    ```
    ```
    [~BRAS2-aaa-accounting-acct1] quit
    ```
    ```
    [~BRAS2-aaa] domain natbras
    ```
    ```
    [*BRAS2-aaa-domain-natbras] authentication-scheme auth1
    ```
    ```
    [*BRAS2-aaa-domain-natbras] accounting-scheme acct1
    ```
    ```
    [*BRAS2-aaa-domain-natbras] radius-server group rd1
    ```
    ```
    [*BRAS2-aaa-domain-natbras] commit
    ```
    ```
    [~BRAS2-aaa-domain-natbras] ip-pool natbras
    ```
    ```
    [~BRAS2-aaa-domain-natbras] user-group natbras bind nat instance nat
    ```
    ```
    [~BRAS2-aaa-domain-natbras] quit
    ```
    ```
    [~BRAS2-aaa] quit
    ```
15. Configure traffic classification rules, NAT behaviors, and NAT traffic diversion policies, and apply the NAT traffic diversion policies on the master and backup devices. For details, see "Example for Configuring Distributed NAT" in *IPv6 Transition > NAT Configuration*.
    
    
    
    # Configure a NAT conversion policy on BRAS1.
    
    1. Configure an ACL numbered 6001 and an ACL rule numbered 1.
       
       ```
       [~BRAS1] acl 6001
       ```
       ```
       [*BRAS1-acl-ucl-6001] rule 1 permit ip source user-group natbras
       ```
       ```
       [*BRAS1-acl-ucl-6001] commit
       ```
       ```
       [~BRAS1-acl-ucl-6001] quit
       ```
    2. Configure an ACL numbered 3001.
       
       ```
       [~BRAS1] acl 3001
       ```
       ```
       [*BRAS1-acl4-advance-3001] rule 10 permit ip source 192.168.0.0 0.0.255.255
       ```
       ```
       [*BRAS1-acl4-advance-3001] commit
       ```
       ```
       [~BRAS1-acl4-advance-3001] quit
       ```
    3. Configure a traffic classifier.
       
       ```
       [~BRAS1] traffic classifier c1
       ```
       ```
       [*BRAS1-classifier-c1] if-match acl 6001
       ```
       ```
       [*BRAS1-classifier-c1] commit
       ```
       ```
       [~BRAS1-classifier-c1] quit
       ```
    4. Configure a traffic behavior.
       
       ```
       [~BRAS1] traffic behavior b1 
       ```
       ```
       [*BRAS1-behavior-b1] nat bind instance nat
       ```
       ```
       [*BRAS1-behavior-b1] commit
       ```
       ```
       [~BRAS1-behavior-b1] quit
       ```
    5. Define a traffic policy to associate the traffic classifier with the traffic behavior.
       
       ```
       [~BRAS1] traffic policy p1
       ```
       ```
       [*BRAS1-trafficpolicy-p1] classifier c1 behavior b1
       ```
       ```
       [*BRAS1-trafficpolicy-p1] commit
       ```
       ```
       [~BRAS1-trafficpolicy-p1] quit
       ```
    6. Apply the NAT traffic diversion policy in the system view.
       
       ```
       [~BRAS1] traffic-policy p1 inbound
       ```
       ```
       [*BRAS1] commit
       ```
    7. Configure a NAT conversion policy.
       
       ```
       [~BRAS1] nat instance nat
       ```
       ```
       [~BRAS1-nat-instance-nat] nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
       ```
       ```
       [*BRAS1-nat-instance-nat] nat outbound 3001 address-group address-group1
       ```
       ```
       [*BRAS1-nat-instance-nat] commit
       ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration of BRAS2 is similar to that of BRAS1. For configuration details, see [BRAS2 configuration file](#EN-US_TASK_0295928544__config_02) in this section.
16. On each of the master and backup devices, configure a user-side VRRP group (between BRAS1/BRAS2 and SWITCH) and enable it to track the service-location group. If the service-location group is not tracked, a CGN board failure cannot trigger a master/backup BRAS switchover. As a result, new distributed NAT users cannot go online.
    
    
    
    # Configure BRAS1 (between BRAS1 and SWITCH).
    
    ```
    [~BRAS1] interface GigabitEthernet0/1/2.2
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.2] vlan-type dot1q 2002
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] ip address 192.168.2.10 255.255.255.0
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 2 virtual-ip 192.168.2.200
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] admin-vrrp vrid 2
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 2 priority 150
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 2 preempt-mode timer delay 1500
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp recover-delay 20
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] vrrp vrid 2 track service-location 1 reduced 50
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.2] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.2] quit
    ```
    
    # Configure BRAS2 (between BRAS2 and SWITCH).
    
    ```
    [~BRAS2] interface GigabitEthernet0/1/2.2
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.2] vlan-type dot1q 2002
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] ip address 192.168.2.100 255.255.255.0
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 2 virtual-ip 192.168.2.200
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] admin-vrrp vrid 2
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 2 priority 120
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] vrrp vrid 2 track service-location 1
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.2] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.2] quit
    ```
17. Configure an RBS and bind a service-instance group to the RBS.
    1. Configure an RBS on BRAS1 and BRAS2.
       
       
       
       # Configure an RBS on BRAS1.
       
       ```
       [~BRAS1] remote-backup-service natbras
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] peer 1.1.1.2 source 1.1.1.1 port 2001
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] protect lsp-tunnel for-all-instance peer-ip 1.1.1.2
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] ip-pool natbras
       ```
       ```
       [*BRAS1-rm-backup-srv-natbras] commit
       ```
       ```
       [~BRAS1-rm-backup-srv-natbras] quit
       ```
       
       # Configure an RBS on BRAS2.
       
       ```
       [~BRAS2] remote-backup-service natbras
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] peer 1.1.1.1 source 1.1.1.2 port 2001
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] protect lsp-tunnel for-all-instance peer-ip 1.1.1.1
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] ip-pool natbras
       ```
       ```
       [*BRAS2-rm-backup-srv-natbras] commit
       ```
       ```
       [~BRAS2-rm-backup-srv-natbras] quit
       ```
    2. Bind the service-instance group to the RBS.
       
       
       
       # Configure BRAS1.
       
       ```
       [~BRAS1] service-instance-group group1
       ```
       ```
       [*BRAS1-service-instance-group-group1] remote-backup-service natbras
       ```
       ```
       [*BRAS1-service-instance-group-group1] commit
       ```
       ```
       [~BRAS1-service-instance-group-group1] quit
       ```
       
       # Configure BRAS2.
       
       ```
       [~BRAS2] service-instance-group group1
       ```
       ```
       [*BRAS2-service-instance-group-group1] remote-backup-service natbras
       ```
       ```
       [*BRAS2-service-instance-group-group1] commit
       ```
       ```
       [~BRAS2-service-instance-group-group1] quit
       ```
18. Configure RUI to back up BRAS information of users.
    
    
    
    # Configure an RBP named **natbras** on BRAS1.
    
    ```
    [~BRAS1] remote-backup-profile natbras
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] service-type bras
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] backup-id 10 remote-backup-service natbras
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] peer-backup hot
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] vrrp-id 2 interface GigabitEthernet0/1/2.2
    ```
    ```
    [*BRAS1-rm-backup-prf-natbras] commit
    ```
    ```
    [~BRAS1-rm-backup-prf-natbras] quit
    ```
    
    # Configure an RBP named **natbras** on BRAS2.
    
    ```
    [~BRAS2] remote-backup-profile natbras
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] service-type bras
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] backup-id 10 remote-backup-service natbras
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] peer-backup hot
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] vrrp-id 2 interface GigabitEthernet0/1/2.2
    ```
    ```
    [*BRAS2-rm-backup-prf-natbras] commit
    ```
    ```
    [~BRAS2-rm-backup-prf-natbras] quit
    ```
19. Bind service-instance groups to NAT instances.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] nat instance nat id 1
    ```
    ```
    [~BRAS1-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*BRAS1-nat-instance-nat] commit
    ```
    ```
    [~BRAS1-nat-instance-nat] quit
    ```
    
    # Configure BRAS2.
    
    
    
    ```
    [~BRAS2] nat instance nat id 1
    ```
    ```
    [~BRAS2-nat-instance-nat] service-instance-group group1
    ```
    ```
    [*BRAS2-nat-instance-nat] commit
    ```
    ```
    [~BRAS2-nat-instance-nat] quit
    ```
20. Configure user-side sub-interfaces on BRAS1 and BRAS2.
    
    
    
    # Configure a user-side sub-interface on BRAS1.
    
    ```
    [~BRAS1] interface GigabitEthernet0/1/2.10
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.10] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10] user-vlan 2010
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10-vlan-2010-2010] quit
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.10] remote-backup-profile natbras
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.10] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10] bas
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10-bas] access-type layer2-subscriber default-domain authentication natbras
    ```
    ```
    [*BRAS1-GigabitEthernet0/1/2.10-bas] commit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10-bas] quit
    ```
    ```
    [~BRAS1-GigabitEthernet0/1/2.10] quit
    ```
    
    # Configure a user-side sub-interface on BRAS2.
    
    ```
    [~BRAS2] interface GigabitEthernet0/1/2.10
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.10] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10] user-vlan 2010
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10-vlan-2010-2010] quit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10] remote-backup-profile natbras
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.10] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10] bas
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10-bas] access-type layer2-subscriber default-domain authentication natbras
    ```
    ```
    [*BRAS2-GigabitEthernet0/1/2.10-bas] commit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10-bas] quit
    ```
    ```
    [~BRAS2-GigabitEthernet0/1/2.10] quit
    ```

#### Configuration Files

* BRAS1 configuration file
  
  ```
  #
  sysname BRAS1
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #
  radius-server group rd1
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
   radius-server type plus11
   radius-server traffic-unit kbyte
  #
  acl number 3001
   rule 10 permit ip source 192.168.0.0 0.0.255.255
  #
  acl number 6001
   rule 1 permit ip source user-group natbras
  #
  traffic classifier c1 operator or
   if-match acl 6001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat
  #
  traffic policy p1
   share-mode
   classifier c1 behavior b1 precedence 1
  #
  traffic-policy p1 inbound
  #
  service-ha hot-backup enable
  service-ha delay-time 10
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface Global-VE1.1
   remote-backup interface Global-VE1.1 peer 10.1.1.2
  #
  service-instance-group group1
   service-location 1
   remote-backup-service natbras
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
   nat outbound 3001 address-group address-group1
  #
  bfd
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
   #
   ipv4-family
  #
  mpls ldp remote-peer peer-bas
   remote-ip 1.1.1.2
  #
  user-group natbras
  #
  ip pool natbras bas local
   gateway 192.168.0.1 255.255.0.0
   section 0 192.168.0.2 192.168.0.254
  #
  aaa
   authentication-scheme auth1
    authentication-mode radius
   accounting-scheme acct1
    accounting-mode radius
   domain natbras
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    ip-pool natbras
    user-group natbras bind nat instance nat
  #
  bfd peer1 bind peer-ip 10.1.1.2 source-ip 10.1.1.1 auto
  #
  remote-backup-service natbras
   peer 1.1.1.2 source 1.1.1.1 port 2001
   protect lsp-tunnel for-all-instance peer-ip 1.1.1.2
   ip-pool natbras
  #
  remote-backup-profile natbras
   service-type bras
   backup-id 10 remote-backup-service natbras
   peer-backup hot
   vrrp-id 2 interface GigabitEthernet0/1/2.2
  #
  interface Virtual-Template1
   ppp authentication-mode auto
  #
  interface Global-VE0
   ve-group 2001 l2-terminate
  #
  interface Global-VE0.1
   undo shutdown
   vlan-type dot1q 2001
   mpls l2vc 1.1.1.2 2001
  #
  interface Global-VE1
   ve-group 2001 l3-access
  #
  interface Global-VE1.1
   undo shutdown
   vlan-type dot1q 2001
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 200
   vrrp vrid 1 preempt-mode timer delay 1500
   vrrp recover-delay 20
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp vrid 1 timer advertise 20
   vrrp vrid 1 track bfd-session session-name peer1 peer
  #
  interface GigabitEthernet0/1/2.10
   user-vlan 2010
   remote-backup-profile natbras
   pppoe-server bind Virtual-Template 1
   bas
    access-type layer2-subscriber default-domain authentication natbras
    authentication-method ppp
  #
  interface GigabitEthernet0/1/2.2
   vlan-type dot1q 2002
   ip address 192.168.2.10 255.255.255.0
   vrrp vrid 2 virtual-ip 192.168.2.200
   admin-vrrp vrid 2
   vrrp vrid 2 priority 150
   vrrp vrid 2 preempt-mode timer delay 1500
   vrrp recover-delay 20
   vrrp vrid 2 track service-location 1 reduced 50
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.2.1.1 255.255.255.255
   mpls
   mpls ldp
  #                
  ospf 1            
   area 0.0.0.0
   network 10.2.1.0 0.0.0.255
   network 1.1.1.1 0.0.0.0
  #
  return
  ```
* BRAS2 configuration file
  
  ```
  #
  sysname BRAS2
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 6 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #
  radius-server group rd1
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
   radius-server type plus11
   radius-server traffic-unit kbyte
  #
  acl number 3001
   rule 10 permit ip source 192.168.0.0 0.0.255.255
  #
  acl number 6001
   rule 1 permit ip source user-group natbras
  #
  traffic classifier c1 operator or
   if-match acl 6001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat
  #
  traffic policy p1
   share-mode
   classifier c1 behavior b1 precedence 1
  #
  traffic-policy p1 inbound
  #
  service-ha hot-backup enable
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  service-location 1
   location slot 1 
   vrrp vrid 1 interface Global-VE1.1
   remote-backup interface Global-VE1.1 peer 10.1.1.1
  #
  service-instance-group group1
   service-location 1
   remote-backup-service natbras
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
   nat outbound 3001 address-group address-group1
  #
  bfd
  #
  mpls lsr-id 1.1.1.2
  #
  mpls
  #
  mpls l2vpn
  #
  mpls ldp
   #
   ipv4-family
  #
  mpls ldp remote-peer peer-bas
   remote-ip 1.1.1.1
  #
  user-group natbras
  #
  ip pool natbras bas local
   gateway 192.168.0.1 255.255.0.0
   section 0 192.168.0.2 192.168.0.254
  #
  aaa
   authentication-scheme auth1
    authentication-mode radius
   accounting-scheme acct1
    accounting-mode radius
   domain natbras
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    ip-pool natbras
    user-group natbras bind nat instance nat
  #
  bfd peer1 bind peer-ip 10.1.1.1 source-ip 10.1.1.2 auto
  #
  remote-backup-service natbras
   peer 1.1.1.1 source 1.1.1.2 port 2001
   protect lsp-tunnel for-all-instance peer-ip 1.1.1.1
   ip-pool natbras
  #
  remote-backup-profile natbras
   service-type bras
   backup-id 10 remote-backup-service natbras
   peer-backup hot
   vrrp-id 2 interface GigabitEthernet0/1/2.2
  #
  interface Virtual-Template1
   ppp authentication-mode auto
  #
  interface Global-VE0
   ve-group 2001 l2-terminate
  #
  interface Global-VE0.1
   undo shutdown
   vlan-type dot1q 2001
   mpls l2vc 1.1.1.1 2001
  #
  interface Global-VE1
   ve-group 2001 l3-access
  #
  interface Global-VE1.1
   undo shutdown
   vlan-type dot1q 2001
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.3
   admin-vrrp vrid 1 ignore-if-down
   vrrp vrid 1 priority 150
   vrrp vrid 1 track service-location 1 reduced 60
   vrrp recover-delay 15
   vrrp vrid 1 timer advertise 20
   vrrp vrid 1 track bfd-session session-name peer1 peer
  #
  interface GigabitEthernet0/1/2.10
   user-vlan 2010
   pppoe-server bind Virtual-Template 1
   remote-backup-profile natbras
   bas
    access-type layer2-subscriber default-domain authentication natbras
    authentication-method ppp
  #
  interface GigabitEthernet0/1/2.2
   vlan-type dot1q 2002
   ip address 192.168.2.100 255.255.255.0
   vrrp vrid 2 virtual-ip 192.168.2.200
   admin-vrrp vrid 2
   vrrp vrid 2 priority 120
   vrrp vrid 2 track service-location 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.3.1.2 255.255.255.255
   mpls
   mpls ldp
  #                
  ospf 1            
   area 0.0.0.0
  area 1
   network 10.3.1.0 0.0.0.255
   network 1.1.1.2 0.0.0.0
  #
  return
  ```
* CR configuration file
  ```
  #
  sysname CR
  #
  mpls lsr-id 1.1.1.3
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 10.2.1.2 255.255.255.255
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ip address 10.3.1.1 255.255.255.255
   mpls
   mpls ldp
  #            
  ospf 1            
   area 0.0.0.0
   network 10.2.1.0 0.0.0.255
   area 0.0.0.1
  area 1 
   network 10.3.1.0 0.0.0.255
  #
  return
  ```