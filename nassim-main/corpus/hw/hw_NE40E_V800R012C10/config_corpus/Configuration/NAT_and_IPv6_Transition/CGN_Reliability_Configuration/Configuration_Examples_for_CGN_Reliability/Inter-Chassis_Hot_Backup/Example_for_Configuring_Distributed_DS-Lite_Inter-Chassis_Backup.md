Example for Configuring Distributed DS-Lite Inter-Chassis Backup
================================================================

This section provides an example for configuring inter-chassis backup for DS-Lite services in distributed deployment scenarios.

#### Networking Requirements

In distributed deployment, a CGN board is installed on BRAS1 and BRAS2. The two BRASs use GE interfaces to establish a VRRP channel. To implement inter-chassis HA backup for DS-Lite services, configure VRRP to determine the master/backup CGN status, and associate HA with VRRP. As shown in [Figure 1](#EN-US_TASK_0000001177668526__fig_dc_ne_cgn-reliability_cfg_003801), home users using private IPv4 addresses access an IPv6 MAN through the CPE that supports dual stack and DS-Lite. A DS-Lite tunnel is established between the CPE and DS-Lite device. The CPE transmits traffic with the private IPv4 address along the DS-Lite tunnel to the DS-Lite device. The DS-Lite device decapsulates traffic, uses NAT to translate the private IPv4 address to a public IPv4 address, and forwards the traffic to the IPv4 Internet.

**Figure 1** Inter-chassis backup networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, and interface3 in this example represent GE0/1/1, GE0/1/2, and GE0/1/3, respectively.


  
![](figure/en-us_image_0000001177509978.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a license.
2. Enable HA inter-chassis hot backup.
3. Create an HA backup group, add members to the group, and configure a VRRP channel.
4. Create and configure a VRRP group.
5. Associate HA with VRRP.
6. Bind the HA backup group to the VRRP group.
7. Create a service-instance group and bind it to the HA backup group.
8. Create a DS-Lite instance, bind the DS-Lite instance to the service-instance group, and configure an address pool.
9. Configure DS-Lite user information and RADIUS authentication on the BRAS.
10. Configure a traffic diversion policy for the DS-Lite tunnel.
11. Configure a DS-Lite conversion policy.
12. Configure user-side VRRP.
13. Configure a remote backup service (RBS) and a remote backup profile (RBP), and bind the service-instance group to the RBS.
14. Configure a user-side interface.

#### Data Preparation

To complete the configuration, you need the following data:

| No. | Data |
| --- | --- |
| 1 | ID of the HA backup group |
| 2 | Slot ID and CPU ID of BRAS1's active service board (CPU 0 in slot 1) |
| 3 | Slot ID and CPU ID of BRAS2's standby service board (CPU 0 in slot 2) |
| 4 | VRRP channel's interface and its IP address on the master and backup devices |
| 5 | Index, virtual IP address, member priority, and preemption delay of the VRRP group on the master and backup devices |
| 6 | Name of the service-instance group |
| 7 | Name and index of the DS-Lite instance |
| 8 | DS-Lite user group name |
| 9 | Index, virtual IP address, member priority, and preemption delay of the VRRP group on the user side |
| 10 | RBS name |
| 11 | RBP name |
| 12 | User-side interface |



#### Procedure

1. Configure a license.
   
   
   
   # Configure BRAS1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS1
   [*HUAWEI] commit
   [~BRAS1] vsm on-board-mode disable
   [~BRAS1] vsm on-board-mode disable
   [*BRAS1] commit
   [~BRAS1] license
   [~BRAS1-license] active ds-lite vsuf slot 2
   [*BRAS1-license] active nat session-table size 16 slot 2 
   [*BRAS1-license] active nat bandwidth-enhance 40 slot 2
   [*BRAS1-license] commit
   [~BRAS1-license] quit
   ```
   
   # Configure BRAS2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS2
   [*HUAWEI] commit
   [~BRAS1] vsm on-board-mode disable
   [*BRAS2] commit
   [~BRAS2] license
   [~BRAS2-license] active ds-lite vsuf slot 2
   [*BRAS2-license] active nat session-table size 16 slot 2 
   [*BRAS2-license] active nat bandwidth-enhance 40 slot 2
   [*BRAS2-license] commit
   [~BRAS2-license] quit
   ```
2. Enable HA hot backup on the master and backup devices.
   
   
   
   # Configure BRAS1.
   
   ```
   [~BRAS1] service-ha hot-backup enable
   [*BRAS1] commit
   ```
   
   # Configure BRAS2.
   
   ```
   [~BRAS2] service-ha hot-backup enable
   [*BRAS2] commit
   ```
3. Create an HA backup group on the two devices, add members to the group, and configure a VRRP channel.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Service-location IDs and the number of service-location groups configured on the master and backup devices must be the same. Otherwise, backup may fail, affecting services.
   
   
   
   # Create HA backup group 21 on BRAS1, add CPU 0 in slot 1 to the group, and set the local VRRP outbound interface to GE 0/1/3 and the peer IP address to 10.0.0.2.
   
   ```
   [~BRAS1] service-location 21
   [*BRAS1-service-location-21] location slot 1 
   [*BRAS1-service-location-21] remote-backup interface GigabitEthernet 0/1/3 peer 10.0.0.2
   [*BRAS1-service-location-21] quit
   [*BRAS1] commit
   ```
   
   # Create HA backup group 21 on BRAS2, add CPU 0 in slot 2 to the group, and set the local VRRP outbound interface to GE 0/1/3 and the peer IP address to 10.0.0.1.
   
   ```
   [~BRAS2] service-location 21
   [*BRAS2-service-location-21] location slot 2 
   [*BRAS2-service-location-21] remote-backup interface GigabitEthernet 0/1/3 peer 10.0.0.1
   [*BRAS2-service-location-21] quit
   [*BRAS2] commit
   ```
4. Create and configure a VRRP group on the two devices.
   
   
   
   # On BRAS1, enter the GE0/1/3 interface view, create VRRP group 10, and set the virtual IP address of the VRRP group to 10.0.0.3. Configure the VRRP group as an mVRRP group and enable the VRRP group to ignore an interface Down event. Set BRAS1's priority in the VRRP group to 150 and the VRRP preemption delay to 1500s. Configure VRRP to track GE0/1/2. If GE0/1/2 goes down, the priority of the device in VRRP group 10 decreases by 50.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/3
   [~BRAS1-GigabitEthernet0/1/3] ip address 10.0.0.1 255.255.255.0
   [*BRAS1-GigabitEthernet0/1/3] vrrp vrid 10 virtual-ip 10.0.0.3
   [*BRAS1-GigabitEthernet0/1/3] admin-vrrp vrid 10 ignore-if-down
   [*BRAS1-GigabitEthernet0/1/3] vrrp vrid 10 priority 150
   [*BRAS1-GigabitEthernet0/1/3] vrrp vrid 10 preempt-mode timer delay 1500
   [*BRAS1-GigabitEthernet0/1/3] vrrp recover-delay 20
   [*BRAS1-GigabitEthernet0/1/3] vrrp vrid 10 track interface GigabitEthernet 0/1/2 reduced 50
   [*BRAS1-GigabitEthernet0/1/3] quit
   [*BRAS1] commit
   ```
   
   # On BRAS2, enter the GE0/1/3 interface view, create VRRP group 10, and set the virtual IP address of the VRRP group to 10.0.0.3. Configure the VRRP group as an mVRRP group and enable the VRRP group to ignore an interface Down event. Set BRAS2's priority in the VRRP group to 120.
   
   ```
   [~BRAS2] interface GigabitEthernet 0/1/3
   [~BRAS2-GigabitEthernet0/1/3] ip address 10.0.0.2 255.255.255.0
   [*BRAS2-GigabitEthernet0/1/3] vrrp vrid 10 virtual-ip 10.0.0.3
   [*BRAS2-GigabitEthernet0/1/3] admin-vrrp vrid 10 ignore-if-down
   [*BRAS2-GigabitEthernet0/1/3] vrrp vrid 10 priority 120
   [*BRAS2-GigabitEthernet0/1/3] quit
   [*BRAS2] commit
   ```
5. Associate HA with VRRP on the two devices.
   
   
   
   # On BRAS1, enter the GE0/1/3 interface view and associate HA backup group 21 with VRRP group 10.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/3
   [~BRAS1-GigabitEthernet0/1/3] vrrp vrid 10 track service-location 21 reduced 50
   [*BRAS1-GigabitEthernet0/1/3] quit
   [*BRAS1] commit
   ```
   
   # On BRAS2, enter the GE0/1/3 interface view and associate HA backup group 21 with VRRP group 10.
   
   ```
   [~BRAS2] interface GigabitEthernet 0/1/3
   [~BRAS2-GigabitEthernet0/1/3] vrrp vrid 10 track service-location 21 reduced 50
   [*BRAS2-GigabitEthernet0/1/3] quit
   [*BRAS2] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Run the [**display vrrp 10**](cmdqueryname=display+vrrp+10) command on the two BRAS devices to check the master/backup VRRP status, which reflects the master/backup status of the HA backup group. **Master** in the command output indicates that the BRAS is the master device.
6. Bind the HA backup group to the VRRP group on the two devices.
   
   
   
   # On BRAS1, bind HA backup group 21 to VRRP group 10 and specify the interface for establishing a VRRP channel with the peer device as GE0/1/3.
   
   ```
   [~BRAS1] service-location 21
   [~BRAS1-service-location-21] vrrp vrid 10 interface GigabitEthernet 0/1/3
   [*BRAS1-service-location-21] quit
   [*BRAS1] commit
   ```
   
   # On BRAS2, bind HA backup group 21 to VRRP group 10, and specify the interface for establishing a VRRP channel with the peer device as GE0/1/3.
   
   ```
   [~BRAS2] service-location 21
   [~BRAS2-service-location-21] vrrp vrid 10 interface GigabitEthernet 0/1/3
   [*BRAS2-service-location-21] quit
   [*BRAS2] commit
   ```
7. Create a service-instance group on the two devices and bind it to the HA backup group.
   
   
   
   # On BRAS1, create service-instance group 21 and bind it to HA backup group 21.
   
   ```
   [~BRAS1] service-instance-group 21
   [*BRAS1-service-instance-group-21] service-location 21
   [*BRAS1-service-instance-group-21] quit
   [*BRAS1] commit
   ```
   
   # On BRAS2, create service-instance group 21 and bind it to HA backup group 21.
   
   ```
   [~BRAS2] service-instance-group 21
   [*BRAS2-service-instance-group-21] service-location 21
   [*BRAS2-service-instance-group-21] quit
   [*BRAS2] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Run the [**display service-location 21**](cmdqueryname=display+service-location+21) command on the two BRAS devices to check HA information. **Vrrp state** in the command output reflects the status of HA backup group 21, which must be consistent with the VRRP status. **Batch-backup state** in the command output indicates whether batch backup has completed.
8. Create a DS-Lite instance on the two devices, bind the instance to the service-instance group, and configure an address pool.
   
   
   
   # Create a DS-Lite instance named **dslite1** on BRAS1.
   
   ```
   [~BRAS1] ds-lite instance dslite1 id 21
   [*BRAS1-ds-lite-instance-dslite1] port-range 4096
   [*BRAS1-ds-lite-instance-dslite1] service-instance-group 21
   [*BRAS1-ds-lite-instance-dslite1] ds-lite address-group group1 group-id 1 11.11.11.100 11.11.11.110
   [*BRAS1-ds-lite-instance-dslite1] commit
   [~BRAS1-ds-lite-instance-dslite1] local-ipv6 2001:db8:2::12 prefix-length 128
   [*BRAS1-ds-lite-instance-dslite1] remote-ipv6 2001:db8:1:: prefix-length 41
   [*BRAS1-ds-lite-instance-dslite1] ds-lite alg all
   [*BRAS1-ds-lite-instance-dslite1] ds-lite filter mode full-cone
   [*BRAS1-ds-lite-instance-dslite1] quit
   [*BRAS1] commit
   ```
   
   # Create a DS-Lite instance named **dslite1** on BRAS2.
   
   ```
   [~BRAS2] ds-lite instance dslite1 id 21
   [*BRAS2-ds-lite-instance-dslite1] port-range 4096
   [*BRAS2-ds-lite-instance-dslite1] service-instance-group 21
   [*BRAS2-ds-lite-instance-dslite1] ds-lite address-group group1 group-id 1 11.11.11.100 11.11.11.110
   [*BRAS2-ds-lite-instance-dslite1] commit
   [~BRAS2-ds-lite-instance-dslite1] local-ipv6 2001:db8:2::12 prefix-length 128
   [*BRAS2-ds-lite-instance-dslite1] remote-ipv6 2001:db8:1:: prefix-length 41
   [*BRAS2-ds-lite-instance-dslite1] ds-lite alg all
   [*BRAS2-ds-lite-instance-dslite1] ds-lite filter mode full-cone
   [*BRAS2-ds-lite-instance-dslite1] quit
   [*BRAS2] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For details about how to configure basic DS-Lite services, see "DS-Lite Configuration".
9. Configure DS-Lite user information.
   1. Configure the BRAS service on the devices so that users can go online. For detailed configurations, see "User Access" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide*.
   2. Configure a user group.
      
      
      
      # Configure BRAS1.
      
      
      
      ```
      [~BRAS1] user-group group1
      [*BRAS1] commit
      ```
      
      
      
      # Configure BRAS2.
      
      
      
      ```
      [~BRAS2] user-group group2
      [*BRAS2] commit
      ```
   3. Specify the RADIUS server and the domain to which the user belongs.
      
      
      
      # Configure BRAS1.
      
      
      
      ```
      [~BRAS1] radius-server group rd1
      [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
      [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
      [*BRAS1-radius-rd1] radius-server shared-key YsHsjx_202206
      [*BRAS1-radius-rd1] commit
      [~BRAS1-radius-rd1] radius-server type plus11
      [~BRAS1-radius-rd1] radius-server traffic-unit kbyte
      [~BRAS1-radius-rd1] quit
      [~BRAS1] aaa
      [~BRAS1-aaa] authentication-scheme auth1
      [*BRAS1-aaa-authen-auth1] authentication-mode radius
      [*BRAS1-aaa-authen-auth1] commit
      [~BRAS1-aaa-authen-auth1] quit
      [~BRAS1-aaa] accounting-scheme acct1
      [*BRAS1-aaa-accounting-acct1] accounting-mode radius
      [~BRAS1-aaa-accounting-acct1] commit
      [~BRAS1-aaa-accounting-acct1] quit
      [~BRAS1-aaa] domain dslite1
      [*BRAS1-aaa-domain-dslite1] authentication-scheme auth1
      [*BRAS1-aaa-domain-dslite1] accounting-scheme acct1
      [*BRAS1-aaa-domain-dslite1] radius-server group rd1
      [*BRAS1-aaa-domain-dslite1] commit
      [~BRAS1-aaa-domain-dslite1] user-group group1 bind ds-lite instance dslite1
      [*BRAS1-aaa-domain-dslite1] commit
      [~BRAS1-aaa-domain-dslite1] quit
      [~BRAS1-aaa] quit
      ```
      
      # Configure BRAS2.
      
      ```
      [~BRAS2] radius-server group rd1
      [*BRAS2-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
      [*BRAS2-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
      [*BRAS2-radius-rd1] radius-server shared-key YsHsjx_202206
      [*BRAS2-radius-rd1] commit
      [~BRAS2-radius-rd1] radius-server type plus11
      [~BRAS2-radius-rd1] radius-server traffic-unit kbyte
      [~BRAS2-radius-rd1] quit
      [~BRAS2] aaa
      [~BRAS2-aaa] authentication-scheme auth1
      [*BRAS2-aaa-authen-auth1] authentication-mode radius
      [*BRAS2-aaa-authen-auth1] commit
      [~BRAS2-aaa-authen-auth1] quit
      [~BRAS2-aaa] accounting-scheme acct1
      [*BRAS2-aaa-accounting-acct1] accounting-mode radius
      [~BRAS2-aaa-accounting-acct1] commit
      [~BRAS2-aaa-accounting-acct1] quit
      [~BRAS2-aaa] domain dslite1
      [*BRAS2-aaa-domain-dslite1] authentication-scheme auth1
      [*BRAS2-aaa-domain-dslite1] accounting-scheme acct1
      [*BRAS2-aaa-domain-dslite1] radius-server group rd1
      [*BRAS2-aaa-domain-dslite1] commit
      [~BRAS2-aaa-domain-dslite1] user-group group1 bind ds-lite instance dslite1
      [*BRAS2-aaa-domain-dslite1] commit
      [~BRAS2-aaa-domain-dslite1] quit
      [~BRAS2-aaa] quit
      ```
10. Configure a traffic diversion policy for the DS-Lite tunnel.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] acl ipv6 6001
    [*BRAS1-acl6-ucl-6001] rule 1 permit ipv6 source user-group group1
    [*BRAS1-acl6-ucl-6001] commit
    [~BRAS1-acl6-ucl-6001] quit
    [~BRAS1] traffic classifier c1
    [*BRAS1-classifier-c1] if-match ipv6 acl 6001
    [*BRAS1-classifier-c1] commit
    [~BRAS1-classifier-c1] quit
    [~BRAS1] traffic behavior b1
    [*BRAS1-behavior-b1] ds-lite bind instance dslite1
    [*BRAS1-behavior-b1] commit
    [~BRAS1-behavior-b1] quit
    [~BRAS1] traffic policy p1
    [*BRAS1-trafficpolicy-p1] classifier c1 behavior b1
    [*BRAS1-trafficpolicy-p1] commit
    [~BRAS1-trafficpolicy-p1] quit
    [~BRAS1] traffic-policy p1 inbound
    [*BRAS1] commit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] acl ipv6 6001
    [*BRAS2-acl6-ucl-6001] rule 1 permit ipv6 source user-group group1
    [*BRAS2-acl6-ucl-6001] commit
    [~BRAS2-acl6-ucl-6001] quit
    [~BRAS2] traffic classifier c1
    [*BRAS2-classifier-c1] if-match ipv6 acl 6001
    [*BRAS2-classifier-c1] commit
    [~BRAS2-classifier-c1] quit
    [~BRAS2] traffic behavior b1
    [*BRAS2-behavior-b1] ds-lite bind instance dslite1
    [*BRAS2-behavior-b1] commit
    [~BRAS2-behavior-b1] quit
    [~BRAS2] traffic policy p1
    [*BRAS2-trafficpolicy-p1] classifier c1 behavior b1
    [*BRAS2-trafficpolicy-p1] commit
    [~BRAS2-trafficpolicy-p1] quit
    [~BRAS2] traffic-policy p1 inbound
    [*BRAS2] commit
    ```
11. Configure a DS-Lite conversion policy.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] acl ipv6 3000
    [*BRAS1-acl6-adv-3000] rule 1 permit ipv6 source 2001:db8:1:: 41
    [*BRAS1-acl6-adv-3000] commit
    [~BRAS1-acl6-ucl-6001] quit
    [~BRAS1] ds-lite instance dslite1
    [*BRAS1-ds-lite-instance-dslite1] ds-lite outbound 3000 address-group group1
    [*BRAS1-ds-lite-instance-dslite1] commit
    [~BRAS1-ds-lite-instance-dslite1] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] acl ipv6 3000
    [*BRAS2-acl6-adv-3000] rule 1 permit ipv6 source 2001:db8:1:: 41
    [*BRAS2-acl6-adv-3000] commit
    [~BRAS2-acl6-ucl-6001] quit
    [~BRAS2] ds-lite instance dslite1
    [*BRAS2-ds-lite-instance-dslite1] ds-lite outbound 3000 address-group group1
    [*BRAS2-ds-lite-instance-dslite1] commit
    [~BRAS2-ds-lite-instance-dslite1] quit
    ```
12. Configure a user-side VRRP group on the master and backup devices and configure the VRRP group to track service-location.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] bfd
    [*BRAS1-bfd] quit
    [*BRAS1] bfd ma bind peer-ip 192.168.1.1
    [*BRAS1-bfd-session-ma] commit
    [~BRAS1] quit
    [~BRAS1] interface GigabitEthernet0/1/1.2
    [~BRAS1-GigabitEthernet0/1/1.2] vlan-type dot1q 101
    [*BRAS1-GigabitEthernet0/1/1.2] ip address 192.168.1.2 255.255.0.0
    [*BRAS1-GigabitEthernet0/1/1.2] vrrp vrid 2 virtual-ip 192.168.1.10
    [*BRAS1-GigabitEthernet0/1/1.2] admin-vrrp vrid 2
    [*BRAS1-GigabitEthernet0/1/1.2] vrrp vrid 2 priority 150
    [*BRAS1-GigabitEthernet0/1/1.2] vrrp vrid 2 preempt-mode timer delay 1500
    [*BRAS1-GigabitEthernet0/1/1.2] vrrp vrid 2 track interface GigabitEthernet 0/1/2 reduced 50
    [*BRAS1-GigabitEthernet0/1/1.2] vrrp vrid 2 track service-location 21 reduced 50
    [*BRAS1-GigabitEthernet0/1/1.2] vrrp vrid 2 track bfd-session session-name ma
    [*BRAS1-GigabitEthernet0/1/1.2] commit
    [~BRAS1-GigabitEthernet0/1/1.2] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] bfd
    [*BRAS2-bfd] quit
    [*BRAS2] bfd ma bind peer-ip 192.168.1.2
    [*BRAS2-bfd-session-ma] commit
    [~BRAS2] quit
    [~BRAS2] interface GigabitEthernet0/1/1.2
    [~BRAS2-GigabitEthernet0/1/1.2] vlan-type dot1q 101
    [*BRAS2-GigabitEthernet0/1/1.2] ip address 192.168.1.1 255.255.0.0
    [*BRAS2-GigabitEthernet0/1/1.2] vrrp vrid 2 virtual-ip 192.168.1.10
    [*BRAS2-GigabitEthernet0/1/1.2] admin-vrrp vrid 2
    [*BRAS2-GigabitEthernet0/1/1.2] vrrp vrid 2 priority 150
    [*BRAS2-GigabitEthernet0/1/1.2] vrrp vrid 2 preempt-mode timer delay 1500
    [*BRAS2-GigabitEthernet0/1/1.2] vrrp vrid 2 track interface GigabitEthernet 0/1/2 reduced 50
    [*BRAS2-GigabitEthernet0/1/1.2] vrrp vrid 2 track service-location 21 reduced 50
    [*BRAS2-GigabitEthernet0/1/1.2] vrrp vrid 2 track bfd-session session-name ma
    [*BRAS2-GigabitEthernet0/1/1.2] commit
    [~BRAS2-GigabitEthernet0/1/1.2] quit
    ```
13. Configure RUI, including an RBS and an RBP, on the master and backup devices.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] remote-backup-service cgn
    [*BRAS1-rm-backup-srv-cgn] peer 10.0.0.2 source 10.0.0.1 port 7000
    [*BRAS1-rm-backup-srv-cgn] protect redirect ip-nexthop 10.0.0.2 interface GigabitEthernet0/1/3
    [*BRAS1-rm-backup-srv-cgn] ipv6-pool group1
    [*BRAS1-rm-backup-srv-cgn] commit
    [~BRAS1-rm-backup-srv-cgn] quit
    [~BRAS1] remote-backup-profile cgn
    [*BRAS1-rm-backup-prf-cgn] service-type bras
    [*BRAS1-rm-backup-prf-cgn] backup-id 10 remote-backup-service cgn
    [*BRAS1-rm-backup-prf-cgn] peer-backup hot
    [*BRAS1-rm-backup-prf-cgn] vrrp-id 2 interface GigabitEthernet0/1/1.2
    [*BRAS1-rm-backup-prf-cgn] commit
    [~BRAS1-rm-backup-prf-cgn] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] remote-backup-service cgn
    [*BRAS2-rm-backup-srv-cgn] peer 10.0.0.1 source 10.0.0.2 port 7000
    [*BRAS2-rm-backup-srv-cgn] protect redirect ip-nexthop 10.0.0.1 interface GigabitEthernet0/1/3
    [*BRAS2-rm-backup-srv-cgn] ipv6-pool group1
    [*BRAS2-rm-backup-srv-cgn] commit
    [~BRAS2-rm-backup-srv-cgn] quit
    [~BRAS2] remote-backup-profile cgn
    [*BRAS2-rm-backup-prf-cgn] service-type bras
    [*BRAS2-rm-backup-prf-cgn] backup-id 10 remote-backup-service cgn
    [*BRAS2-rm-backup-prf-cgn] peer-backup hot
    [*BRAS2-rm-backup-prf-cgn] vrrp-id 2 interface GigabitEthernet0/1/1.2
    [*BRAS2-rm-backup-prf-cgn] commit
    [~BRAS2-rm-backup-prf-cgn] quit
    ```
14. Bind the service-instance group to the RBS.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] service-instance-group 21
    [*BRAS1-service-instance-group-group1] remote-backup-service cgn
    [*BRAS1-service-instance-group-group1] commit
    [~BRAS1-service-instance-group-group1] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] service-instance-group 21
    [*BRAS2-service-instance-group-group1] remote-backup-service cgn
    [*BRAS2-service-instance-group-group1] commit
    [~BRAS2-service-instance-group-group1] quit
    ```
15. Configure a user-side interface.
    
    
    
    # Configure BRAS1.
    
    ```
    [~BRAS1] interface GigabitEthernet0/1/1
    [~BRAS1-GigabitEthernet0/1/1] ipv6 enable
    [*BRAS1-GigabitEthernet0/1/1] ipv6 address auto link-local
    [*BRAS1-GigabitEthernet0/1/1] remote-backup-profile cgn
    [*BRAS1-GigabitEthernet0/1/1] commit
    [~BRAS1-GigabitEthernet0/1/1] bas
    [~BRAS1-GigabitEthernet0/1/1-bas] access-type layer2-subscriber default-domain authentication dslite1
    [*BRAS1-GigabitEthernet0/1/1-bas] authentication-method-ipv6 bind
    [*BRAS1-GigabitEthernet0/1/1-bas] commit
    [~BRAS1-GigabitEthernet0/1/1-bas] quit
    [~BRAS1-GigabitEthernet0/1/1] quit
    ```
    
    # Configure BRAS2.
    
    ```
    [~BRAS2] interface GigabitEthernet0/1/1
    [~BRAS2-GigabitEthernet0/1/1] ipv6 enable
    [*BRAS2-GigabitEthernet0/1/1] ipv6 address auto link-local
    [*BRAS2-GigabitEthernet0/1/1] remote-backup-profile cgn
    [*BRAS2-GigabitEthernet0/1/1] commit
    [~BRAS2-GigabitEthernet0/1/1] bas
    [~BRAS2-GigabitEthernet0/1/1-bas] access-type layer2-subscriber default-domain authentication dslite1
    [*BRAS2-GigabitEthernet0/1/1-bas] authentication-method-ipv6 bind
    [*BRAS2-GigabitEthernet0/1/1-bas] commit
    [~BRAS2-GigabitEthernet0/1/1-bas] quit
    [~BRAS2-GigabitEthernet0/1/1] quit
    ```

#### Configuration Files

BRAS1 configuration file

```
#
sysname BRAS1
#
vsm on-board-mode disable
#
license
 active nat session-table size 16 slot 2 
 active ds-lite vsuf slot 2
 active nat bandwidth-enhance 40 slot 2
 active bas slot 2
#
radius-server group rd1
 radius-server authentication 192.168.7.249 1645 weight 0
 radius-server accounting 192.168.7.249 1646 weight 0
 radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
 radius-server type plus11
 radius-server traffic-unit kbyte
#
service-ha hot-backup enable
#
service-location 21
 location slot 1 
 remote-backup interface GigabitEthernet0/1/3 peer 10.0.0.2
 vrrp vrid 10 interface GigabitEthernet0/1/3
#
service-instance-group 21
 service-location 21
 remote-backup-service cgn
#
ds-lite instance dslite1 id 21
 port-range 4096
 service-instance-group 21
 ds-lite address-group group1 group-id 1 11.11.11.100 11.11.11.110 
 ds-lite outbound 3000 address-group group1
 local-ipv6 2001:db8:2::12 prefix-length 128
 remote-ipv6 2001:db8:1:: prefix-length 41
 ds-lite alg all
 ds-lite filter mode full-cone
#
bfd
#
ipv6 prefix group1 delegation
 prefix 2001:db8:1::/32
#
ipv6 pool group1 bas delegation
 prefix group1
#
user-group group1
#
remote-backup-service cgn
 peer 10.0.0.2 source 10.0.0.1 port 7000
 protect redirect ip-nexthop 10.0.0.2 interface GigabitEthernet0/1/3
 ipv6-pool group1 
#
remote-backup-profile cgn
 service-type bras
 backup-id 10 remote-backup-service cgn
 peer-backup hot
 vrrp-id 2 interface GigabitEthernet0/1/1.2
#
acl ipv6 number 3000
 rule 1 permit ipv6 source 2001:db8:1:: 41
#
acl ipv6 number 6001
 rule 1 permit ipv6 source user-group group1
#
dhcpv6 duid llt
#
traffic classifier c1 operator or
 if-match ipv6 acl 6001 precedence 1
#
traffic behavior b1
 ds-lite bind instance dslite1
#
traffic policy p1
 share-mode
 classifier c1 behavior b1 precedence 1
#
aaa
 authentication-scheme auth1
  authentication-mode radius
 accounting-scheme acct1
  accounting-mode radius
 domain dslite1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  prefix-assign-mode unshared
  ipv6-pool group1
  ppp address-release separate
  user-group group1 bind ds-lite instance dslite1
#
interface GigabitEthernet0/1/1
 undo shutdown
 ipv6 enable
 ipv6 address auto link-local
 undo dcn
 ipv6 nd autoconfig managed-address-flag
 remote-backup-profile cgn
 bas
 #
  access-type layer2-subscriber default-domain authentication dslite1
  authentication-method-ipv6 bind
 #
#
interface GigabitEthernet0/1/2
 undo shutdown
 ip address 10.4.1.1 255.255.0.0
#
interface GigabitEthernet0/1/3
 undo shutdown
 ip address 10.0.0.1 255.255.255.0
 vrrp vrid 10 virtual-ip 10.0.0.3
 admin-vrrp vrid 10 ignore-if-down
 vrrp vrid 10 priority 150
 vrrp vrid 10 preempt-mode timer delay 1500
 vrrp recover-delay 20
 vrrp vrid 10 track interface GigabitEthernet0/1/2 reduced 50
 vrrp vrid 10 track service-location 21 reduced 50
#
interface GigabitEthernet0/1/1.2
 vlan-type dot1q 101
 ip address 192.168.1.2 255.255.0.0
 vrrp vrid 2 virtual-ip 192.168.1.10
 admin-vrrp vrid 2
 vrrp vrid 2 priority 150
 vrrp vrid 2 preempt-mode timer delay 1500
 vrrp vrid 2 track interface GigabitEthernet0/1/2 reduced 50
 vrrp vrid 2 track bfd-session session-name ma
 vrrp vrid 2 track service-location 21 reduced 50
#
bfd ma bind peer-ip 192.168.1.1
#
ospf 10
 import-route unr
 opaque-capability enable
 area 0.0.0.0
  network 10.0.0.0 0.0.255.255
  network 10.4.1.0 0.0.255.255
#
traffic-policy p1 inbound
#
return
```

BRAS2 configuration file

```
#
sysname BRAS2
#
vsm on-board-mode disable
#
license
 active nat session-table size 16 slot 2 
 active ds-lite vsuf slot 2
 active nat bandwidth-enhance 40 slot 2
 active bas slot 2
#
radius-server group rd1
 radius-server authentication 192.168.7.249 1645 weight 0
 radius-server accounting 192.168.7.249 1646 weight 0
 radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
 radius-server type plus11
 radius-server traffic-unit kbyte
#
service-ha hot-backup enable
#
service-location 21
 location slot 2 
 remote-backup interface GigabitEthernet0/1/3 peer 10.0.0.1
 vrrp vrid 10 interface GigabitEthernet0/1/3
#
service-instance-group 21
 service-location 21
 remote-backup-service cgn
#
ds-lite instance dslite1 id 21
 port-range 4096
 service-instance-group 21
 ds-lite address-group group1 group-id 1 11.11.11.100 11.11.11.110 
 ds-lite outbound 3000 address-group group1
 local-ipv6 2001:db8:2::12 prefix-length 128
 remote-ipv6 2001:db8:1:: prefix-length 41
 ds-lite alg all
 ds-lite filter mode full-cone
#
bfd
#
ipv6 prefix group1 delegation
 prefix 2001:db8:1::/32
#
ipv6 pool group1 bas delegation
 prefix group1
#
user-group group2
#
remote-backup-service cgn
 peer 10.0.0.1 source 10.0.0.2 port 7000
 protect redirect ip-nexthop 10.0.0.1 interface GigabitEthernet0/1/3
 ipv6-pool group1 
#
remote-backup-profile cgn
 service-type bras
 backup-id 10 remote-backup-service cgn
 peer-backup hot
 vrrp-id 2 interface GigabitEthernet0/1/1.2
#
acl ipv6 number 3000
 rule 1 permit ipv6 source 2001:db8:1:: 41
#
acl ipv6 number 6001
 rule 1 permit ipv6 source user-group group2
#
dhcpv6 duid llt
#
traffic classifier c1 operator or
 if-match ipv6 acl 6001 precedence 1
#
traffic behavior b1
 ds-lite bind instance dslite1
#
traffic policy p1
 share-mode
 classifier c1 behavior b1 precedence 1
#
aaa
 authentication-scheme auth1
  authentication-mode radius
 accounting-scheme acct1
  accounting-mode radius
 domain dslite1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  prefix-assign-mode unshared
  ipv6-pool group1
  ppp address-release separate
  user-group group2 bind ds-lite instance dslite1
#
interface GigabitEthernet0/1/1
 undo shutdown
 ipv6 enable
 ipv6 address auto link-local
 undo dcn
 ipv6 nd autoconfig managed-address-flag
 remote-backup-profile cgn
 bas
 #
  access-type layer2-subscriber default-domain authentication dslite1
  authentication-method-ipv6 bind
 #
#
interface GigabitEthernet0/1/2
 undo shutdown
 ip address 10.5.1.1 255.255.0.0
#
interface GigabitEthernet0/1/3
 undo shutdown
 ip address 10.0.0.2 255.255.255.0
 vrrp vrid 10 virtual-ip 10.0.0.3
 admin-vrrp vrid 10
 vrrp vrid 10 priority 120
 vrrp vrid 10 track interface GigabitEthernet0/1/2 reduced 50
 vrrp vrid 10 track service-location 21 reduced 50
#
interface GigabitEthernet0/1/1.2
 vlan-type dot1q 101
 ip address 192.168.1.1 255.255.0.0
 vrrp vrid 2 virtual-ip 192.168.1.10
 admin-vrrp vrid 2
 admin-vrrp vrid 10 ignore-if-down
 vrrp vrid 2 priority 150
 vrrp vrid 2 track interface GigabitEthernet0/1/2 reduced 50
 vrrp vrid 2 track bfd-session session-name ma
 vrrp vrid 2 track service-location 21 reduced 50
#
bfd ma bind peer-ip 192.168.1.2
#
ospf 10
 import-route unr
 opaque-capability enable
 area 0.0.0.0
  network 10.0.0.0 0.0.255.255
  network 10.5.1.0 0.0.255.255
#
traffic-policy p1 inbound
#
return
```