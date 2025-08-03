Example for Configuring Inter-Chassis Cold Backup to Be Associated with CGN Service Boards
==========================================================================================

This section provides an example for configuring inter-chassis cold backup to be associated with CGN service boards for improved NAT device reliability.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.

On the centralized NAT network shown in [Figure 1](#EN-US_TASK_0000001092838008__en-us_task_0172374615_fig_dc_ne_cfg_nat_009801), a NAT service board is equipped in slot 1 on CGN1 and slot 1 on CGN2. CGN1 and CGN2 are standalone CGN devices attached to CRs on the MAN.

If a CGN service board fails, BGP does not withdraw the default route advertised to a downstream device. As a result, traffic attempts to reach the CGN device over the static route but is interrupted. To prevent the traffic interruption, inter-chassis cold backup can be associated with CGN service boards. A ServiceIf interface is associated with a HA service status monitoring group to monitor the CGN board status in real time. Once the ServiceIf interface detects the abnormal CGN service board status, a master/backup CGN device switchover is triggered so that traffic switches to the backup CGN device.

**Figure 1** Network diagram of NAT inter-chassis cold backup![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/2/0.


  
![](images/fig_dc_ne_cfg_nat_009801.png)

#### Context

The configuration roadmap is as follows:

1. Configure basic NAT functions.
2. Create an HA service status monitoring group and associate it with a service-location group.
3. Configure a ServiceIf interface and bind it to the HA service status monitoring group.
4. Configure a NAT traffic diversion policy and NAT traffic conversion policy.


#### Data Preparation

To complete the configuration, you need the following data:

| No. | Data |
| --- | --- |
| 1 | Service-location group index |
| 2 | Slot ID and CPU ID of the master CPU on CGN1's service board (CPU 0 in slot 1 is used in this scenario) |
| 3 | Slot ID and CPU ID of the backup CPU on CGN2's service board (CPU 0 in slot 1 is used in this scenario) |
| 4 | Service-instance group name |
| 5 | Name and index of a NAT instance |
| 6 | Name of an HA service status monitoring group |
| 7 | ServiceIf interface number |




#### Procedure

1. Set the maximum number of sessions that can be created on the NAT service board in slot 1 to 6M on master and backup devices.
   
   # Configure master CGN1.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CGN1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CGN1] vsm on-board-mode disable
   ```
   ```
   [*CGN1] commit
   ```
   ```
   [~CGN1] license
   ```
   ```
   [~CGN1-license] active nat session-table size 6 slot 1
   ```
   ```
   [~CGN1-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [~CGN1-license] quit
   ```
   
   # Configure backup CGN2.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CGN2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CGN2] vsm on-board-mode disable
   ```
   ```
   [*CGN2] commit
   ```
   ```
   [~CGN2] license
   ```
   ```
   [~CGN2-license] active nat session-table size 6 slot 1 
   ```
   ```
   [~CGN2-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [~CGN2-license] quit
   ```
2. Create a service-location group on each CGN device.
   
   
   
   # On CGN1, create a service-location group **1** and configure CPU with ID **0** in slot 1 as a member in inter-chassis service-location backup.
   
   ```
   [~CGN1] service-location 1
   ```
   ```
   [*CGN1-service-location-1] location slot 1
   ```
   ```
   [*CGN1-service-location-1] commit
   ```
   ```
   [~CGN1-service-location-1] quit
   ```
   
   # On CGN2, create a service-location group **1** and configure CPU with ID **0** in slot 1 as a member in HA inter-chassis service-location backup.
   
   ```
   [~CGN2] service-location 1
   ```
   ```
   [*CGN2-service-location-1] location slot 1
   ```
   ```
   [*CGN2-service-location-1] commit
   ```
   ```
   [~CGN2-service-location-1] quit
   ```
3. Create a service-instance group and bind it to the service-location group on each CGN device.
   
   
   
   # On CGN1, create a service-instance group named **group 1** and bind it to service-location group **1**.
   
   ```
   [~CGN1] service-instance-group group1
   ```
   ```
   [*CGN1-service-instance-group-group1] service-location 1
   ```
   ```
   [*CGN1-service-instance-group-group1] commit
   ```
   ```
   [~CGN1-service-instance-group-group1] quit
   ```
   
   # On CGN2, create a service-instance group named **group 1** and bind it to service-location group **1**.
   
   ```
   [~CGN2] service-instance-group group1
   ```
   ```
   [*CGN2-service-instance-group-group1] service-location 1
   ```
   ```
   [*CGN2-service-instance-group-group1] commit
   ```
   ```
   [~CGN2-service-instance-group-group1] quit
   ```
4. Create a service status monitoring group and bind it to the service-location group on each CGN device.
   
   
   
   # On CGN1, create a service status monitoring group named **group1** and bind it to service-location group **1**.
   
   ```
   [~CGN1] monitor-location-group group1
   ```
   ```
   [*CGN1-monitor-location-group-group1] service-location 1
   ```
   ```
   [*CGN1-monitor-location-group-group1] commit
   ```
   ```
   [~CGN1-monitor-location-group-group1] quit
   ```
   
   # On CGN2, create a service status monitoring group named **group1** and bind it to service-location group **1**.
   
   ```
   [~CGN2] monitor-location-group group1
   ```
   ```
   [*CGN2-monitor-location-group-group1] service-location 1
   ```
   ```
   [*CGN2-monitor-location-group-group1] commit
   ```
   ```
   [~CGN2-monitor-location-group-group1] quit
   ```
5. Create a loopback interface on each CGN device and enable a BGP route between CGN1 and CGN2.
   
   
   
   # Create **loopBack0** on CGN1 and establish a BGP route between CGN1 and CGN2.
   
   ```
   [~CGN1] interface LoopBack0
   ```
   ```
   [*CGN1-LoopBack0] ip address 1.1.1.1 255.255.255.255
   ```
   ```
   [*CGN1-LoopBack0] commit
   ```
   ```
   [~CGN1-LoopBack0] quit
   ```
   ```
   [~CGN1] bgp 100
   ```
   ```
   [*CGN1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*CGN1-bgp] peer 3.3.3.3 connect-interface LoopBack0
   ```
   ```
   [*CGN1-bgp] commit
   ```
   ```
   [~CGN1-bgp] quit
   ```
   
   
   
   # Create **loopBack0** on CGN2 and establish a BGP route between CGN1 and CGN2.
   
   
   
   ```
   [~CGN2] interface LoopBack0
   ```
   ```
   [*CGN2-LoopBack0] ip address 2.2.2.2 255.255.255.255
   ```
   ```
   [*CGN2-LoopBack0] commit
   ```
   ```
   [~CGN2-LoopBack0] quit
   ```
   ```
   [~CGN2] bgp 100
   ```
   ```
   [*CGN2-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*CGN2-bgp] peer 3.3.3.3 connect-interface LoopBack0
   ```
   ```
   [*CGN2-bgp] commit
   ```
   ```
   [~CGN2-bgp] quit
   ```
6. Create a ServiceIf interface and bind it to the HA service status monitoring group on each CGN device.
   
   
   
   # On CGN1, create a ServiceIf interface named **serviceIf 1** and bind it to the service status monitoring group named **group1**.
   
   ```
   [~CGN1] interface serviceif 1
   ```
   ```
   [*CGN1-ServiceIf1] ip address unnumbered interface LoopBack0
   ```
   ```
   [*CGN1-ServiceIf1] track monitor-location-group group1
   ```
   ```
   [*CGN1-ServiceIf1] commit
   ```
   ```
   [~CGN1-ServiceIf1] quit
   ```
   
   # On CGN2, create a ServiceIf interface named **serviceIf 1** and bind it to the service status monitoring group named **group1**.
   
   ```
   [~CGN2] interface serviceif 1
   ```
   ```
   [*CGN2-ServiceIf1] ip address unnumbered interface LoopBack0
   ```
   ```
   [*CGN2-ServiceIf1] track monitor-location-group group1
   ```
   ```
   [*CGN2-ServiceIf1] commit
   ```
   ```
   [~CGN2-ServiceIf1] quit
   ```
7. Configure a static route with the outbound interface set to the ServiceIf interface on each CGN device. Use a routing protocol to advertise the static route on each CGN device to the downstream BRAS to form the primary and backup routes.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Configure a default route with the outbound interface set to serviceIf 1 on the master CGN device, use BGP to advertise the route to downstream devices, and set route cost 1. Configure the same route on the backup CGN device and set route cost 2 that is greater than route cost 1. Traffic is preferentially sent over the route advertised by the master device based on cost values.
   
   
   
   # On CGN1, configure a static route with the outbound interface set to **serviceIf 1**.
   
   ```
   [~CGN1] ip route-static 0.0.0.0 0.0.0.0 serviceif 1
   ```
   ```
   [*CGN1] commit
   ```
   ```
   [~CGN1] quit
   ```
   
   # On CGN2, configure a static route with the outbound interface set to **serviceIf 1**.
   
   ```
   [~CGN2] ip route-static 0.0.0.0 0.0.0.0 serviceif 1
   ```
   ```
   [*CGN2] commit
   ```
   ```
   [~CGN2] quit
   ```
   
   
   
   # Import the route to BGP on CGN1.
   
   
   
   ```
   [~CGN1] bgp 100
   ```
   ```
   [*CGN1] ipv4-family unicast
   ```
   ```
   [*CGN1-bgp-af-ipv4] import-route static med 10
   ```
   ```
   [*CGN1-bgp-af-ipv4] commit
   ```
   ```
   [~CGN1-bgp-af-ipv4] quit
   ```
   # Import the route to BGP on CGN2.
   ```
   [~CGN2] bgp 100
   ```
   ```
   [*CGN2] ipv4-family unicast
   ```
   ```
   [*CGN2-bgp-af-ipv4] import-route static med 20
   ```
   ```
   [*CGN2-bgp-af-ipv4] commit
   ```
   ```
   [~CGN2-bgp-af-ipv4] quit
   ```
8. Create a NAT instance on each CGN device and bind it to the service-instance group.
   
   
   
   # On CGN1, create a NAT instance named **nat** and bind it to a service instance group named **group 1**.
   
   ```
   [~CGN1] nat instance nat id 1
   ```
   ```
   [*CGN1-nat-instance-nat] service-instance-group group1
   ```
   ```
   [*CGN1-nat-instance-nat] nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105
   ```
   ```
   [*CGN1-nat-instance-nat] commit
   ```
   ```
   [~CGN1-nat-instance-nat] quit
   ```
   
   # On CGN2, create a NAT instance named **nat** and bind it to a service instance group named **group 1**.
   
   ```
   [~CGN2] nat instance nat id 1
   ```
   ```
   [*CGN2-nat-instance-nat] service-instance-group group1
   ```
   ```
   [*CGN2-nat-instance-nat] nat address-group address-group1 group-id 1 11.11.11.106 11.11.11.110
   ```
   ```
   [*CGN2-nat-instance-nat] commit
   ```
   ```
   [~CGN2-nat-instance-nat] quit
   ```
9. Configure a NAT traffic diversion policy and a NAT conversion policy on the master and backup devices. For details, see [Example for Configuring Centralized NAT](dc_ne_nat_cfg_0057_1.html) in IPv6 Transition Technology > NAT Configuration.
   
   
   
   # Configure a NAT traffic diversion policy and a NAT traffic conversion policy on CGN1.
   
   1. Configure a NAT traffic diversion policy.
      
      1. Configure an ACL numbered **3001** and an ACL rule numbered **1** to allow hosts only within the network segment 192.168.10.0/24 to access the Internet.
         ```
         [~CGN1] acl 3001
         ```
         ```
         [*CGN1-acl4-advance-3001] rule 1 permit ip source 192.168.10.0 0.0.0.255
         ```
         ```
         [*CGN1-acl4-advance-3001] commit
         ```
         ```
         [~CGN1-acl4-advance-3001] quit
         ```
      2. Configure a traffic classifier.
         ```
         [~CGN1] traffic classifier classifier1
         ```
         ```
         [*CGN1-classifier-classifier1] if-match acl 3001
         ```
         ```
         [*CGN1-classifier-classifier1] commit
         ```
         ```
         [~CGN1-classifier-classifier1] quit
         ```
      3. Configure a traffic behavior named **behavior1**, which binds traffic to the NAT instance named **nat**.
         ```
         [~CGN1] traffic behavior behavior1
         ```
         ```
         [*CGN1-behavior-behavior1] nat bind instance nat
         ```
         ```
         [*CGN1-behavior-behavior1] commit
         ```
         ```
         [~CGN1-behavior-behavior1] quit
         ```
      4. Configure a NAT traffic policy named **policy1** to associate the ACL rule with the traffic behavior.
         ```
         [~CGN1] traffic policy policy1
         ```
         ```
         [*CGN1-policy-policy1] classifier classifier1 behavior behavior1
         ```
         ```
         [*CGN1-policy-policy1] commit
         ```
         ```
         [~CGN1-policy-policy1] quit
         ```
      5. Apply the NAT traffic diversion policy in the view of GE 0/2/0.
         ```
         [~CGN1] interface gigabitEthernet 0/2/0
         ```
         ```
         [~CGN1-GigabitEthernet0/2/0] ip address 192.168.10.1 255.255.255.0
         ```
         ```
         [*CGN1-GigabitEthernet0/2/0] traffic-policy policy1 inbound
         ```
         ```
         [*CGN1-GigabitEthernet0/2/0] commit
         ```
         ```
         [~CGN1-GigabitEthernet0/2/0] quit
         ```
   2. Configure a NAT conversion policy.
      
      ```
      [~CGN1] nat instance nat
      ```
      ```
      [~CGN1-nat-instance-nat] nat outbound 3001 address-group address-group1
      ```
      ```
      [*CGN1-nat-instance-nat] commit
      ```
      ```
      [~CGN1-nat-instance-nat] quit
      ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of CGN2 is similar to that of CGN1. For configuration details, see [CGN2 configuration file](#EN-US_TASK_0000001092838008__en-us_task_0172374615_config_02) in this section.
   
   # Run the [**display nat instance nat**](cmdqueryname=display+nat+instance+nat) command on each CGN device to verify NAT configurations.
   
   ```
   [~CGN1] display nat instance nat
   ```
   ```
   nat instance nat id 1      
    service-instance-group group1     
    nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105   
    nat outbound 3001 address-group address-group1
   ```
   ```
   [~CGN2] display nat instance nat
   ```
   ```
   nat instance nat id 1         
    service-instance-group group1    
    nat address-group address-group1 group-id 1 11.11.11.106 11.11.11.110   
    nat outbound 3001 address-group address-group1
   ```

#### Configuration Files

* CGN1 configuration file
  
  ```
  #
  sysname CGN1
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 6 slot 1
   active nat bandwidth-enhance 40 slot 1
  #
  acl number 3001
   rule 1 permit ip source 192.168.10.0 0.0.0.255
  #
  traffic classifier classifier1 operator or
   if-match acl 3001 precedence 1
  #
  traffic behavior behavior1
   nat bind instance nat
  #
  traffic policy policy1
   classifier classifier1 behavior behavior1 precedence 1
  #
  service-location 1
   location slot 1 
  #
  service-instance-group group1
   service-location 1
  #
  monitor-location-group group1
   service-location 1
  #
  bgp 100
   private-4-byte-as enable
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable 
    import-route static med 10
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.3 enable 
   #
   ipv4-family vpn-instance vpn1
    default-route imported
    import-route direct
    import-route static med 10
  #
  nat instance nat id 1
   service-instance-group group1     
   nat address-group address-group1 group-id 1 11.11.11.100 11.11.11.105   
   nat outbound 3001 address-group address-group1
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
   traffic-policy policy1 inbound
  #
  interface serviceif 1
   ip address unnumbered interface LoopBack0
   track monitor-location-group group1
  #
  ip route-static 0.0.0.0 0.0.0.0 serviceif 1
  #
  return
  ```
* CGN2 configuration file
  
  ```
  #
  sysname CGN2
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 6 slot 1
   active nat bandwidth-enhance 40 slot 1
  #
  acl number 3001
   rule 1 permit ip source 192.168.10.0 0.0.0.255
  #
  traffic classifier classifier1 operator or
   if-match acl 3001 precedence 1
  #
  traffic behavior behavior1
   nat bind instance nat
  #
  traffic policy policy1
   classifier classifier1 behavior behavior1 precedence 1
  #
  service-location 1
   location slot 1
  #
  service-instance-group group1
   service-location 1
  #
  monitor-location-group group1
   service-location 1
  #
  bgp 100
   private-4-byte-as enable
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable 
    import-route static med 20
  #
  nat instance nat id 1
   service-instance-group group1      
   nat address-group address-group1 group-id 1 11.11.11.106 11.11.11.110  
   nat outbound 3001 address-group address-group1
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  interface GigabitEthernet 0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
   traffic-policy policy1 inbound
  #
  interface serviceif 1
   ip address unnumbered interface LoopBack0
   track monitor-location-group group1
  #
  ip route-static 0.0.0.0 0.0.0.0 serviceif 1
  #
  return
  ```