Example for Configuring Centralized DS-Lite Providing Backup for Centralized DS-Lite
====================================================================================

This section provides an example for configuring centralized DS-Lite providing backup for centralized DS-Lite.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172374749__fig_dc_ne_cfg_nat_0012), DS-Lite device A is connected to device B that backs up device A. If no fault occurs, device A performs NAT for user traffic. If all available service boards' CPUs fail or the number of failed CPUs on device A reaches the value of down-number, user traffic is switched to device B for NAT.

The configuration requirements are as follows:

* PCs on the private network segment of 10.110.10.1/24 can access the Internet.

**Figure 1** Centralized DS-Lite providing backup for centralized DS-Lite![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configurations in this example are mainly performed on Device A and Device B.

Interfaces 1 and 2 in this example represent GE 0/2/1 and GE 0/2/2, respectively.


  
![](images/fig_dc_ne_ds-lite_cfg_0094.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure device A:
   1. Configure basic DS-Lite functions and enable centralized DS-Lite providing backup for centralized DS-Lite.
   2. Configure a DS-Lite traffic diversion policy.
   3. Advertise the local IP route to the IPv6 network.
   4. Configure a DS-Lite translation policy.
2. Configure device B:
   1. Configure basic DS-Lite functions.
   2. Configure a DS-Lite traffic diversion policy.
   3. Configure a DS-Lite translation policy.
   4. Configure static routes.

#### Data Preparation

To complete the configuration, you need the following data:

* DS-Lite instance name (ds-lite1)
* Slot ID (1) of the DS-Lite board to which a DS-Lite instance is bound
* Local IP address (2001:DB8::1) and remote IP address (2001:DB8:2::1) of a DS-Lite tunnel
* DS-Lite address pool number (1) and group name (group1)
* Centralized DS-Lite providing backup for centralized DS-Lite in a DS-Lite instance
* Configure ACL6 rules for DS-Lite traffic classification and policy-based traffic diversion
* Configure a DS-Lite translation policy.


#### Procedure

1. Configure basic DS-Lite functions on the master device (device A).
   1. Configure basic license functions.
      
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceA
      [*HUAWEI] commit
      [~DeviceA] vsm on-board-mode disable
      [*DeviceA] commit
      [~DeviceA] license
      [~DeviceA-license] active ds-lite vsuf slot 1
      [*DeviceA-license] active nat session-table size 16 slot 1 
      [*DeviceA-license] active nat bandwidth-enhance 40 slot 1
      [*DeviceA-license] commit
      [~DeviceA-license] quit
      ```
   2. Configure a DS-Lite instance and bind it to a DS-Lite board.
      
      
      ```
      [~DeviceA] service-location 1
      [*DeviceA-service-location-1] location slot 1 
      [*DeviceA-service-location-1] commit
      [~DeviceA-service-location-1] quit
      [~DeviceA] service-instance-group 1
      [*DeviceA-instance-group-1] service-location 1
      [*DeviceA-instance-group-1] commit
      [~DeviceA-instance-group-1] quit
      [~DeviceA] ds-lite instance ds-lite1 id 1
      [*DeviceA-ds-lite-instance-ds-lite1] service-instance-group 1
      [*DeviceA-ds-lite-instance-ds-lite1] quit
      [~DeviceA-ds-lite-instance-ds-lite1] commit
      ```
   3. Configure a local IPv6 address and a remote IPv6 address for a DS-Lite tunnel.
      
      
      ```
      [~DeviceA] ds-lite instance ds-lite1
      [~DeviceA-ds-lite-instance-ds-lite1] local-ipv6 2001:DB8::1 prefix-length 128
      [*DeviceA-ds-lite-instance-ds-lite1] remote-ipv6 2001:DB8:2::1 prefix-length 64
      [*DeviceA-ds-lite-instance-ds-lite1] commit
      [~DeviceA-ds-lite-instance-ds-lite1] quit
      ```
   4. Configure a DS-Lite address pool. Set the address pool with a range of **10.38.160.100** through **10.38.160.110**.
      
      
      ```
      [~DeviceA] ds-lite instance ds-lite1
      [*DeviceA-ds-lite-instance-ds-lite1] ds-lite address-group group1 group-id 1 10.38.160.100 10.38.160.110
      [*DeviceA-ds-lite-instance-ds-lite1] commit
      [~DeviceA-ds-lite-instance-ds-lite1] quit
      ```
   5. Enable centralized DS-Lite providing backup for centralized DS-Lite.
      
      
      ```
      [~DeviceA] ds-lite instance ds-lite1
      [*DeviceA-ds-lite-instance-ds-lite1] ds-lite centralized-backup enable 
      [*DeviceA-ds-lite-instance-ds-lite1] commit
      [~DeviceA-ds-lite-instance-ds-lite1] quit
      ```
2. Configure a DS-Lite traffic diversion policy on the master device.
   1. Configure IPv6 ACL-based traffic classification rules.
      
      
      ```
      [~DeviceA] acl ipv6 3500
      [*DeviceA-acl6-basic-3500] rule permit ipv6 source 2001:DB8:2::1 64 destination 2001:DB8::1 128
      [*DeviceA-acl6-basic-3500] commit
      [~DeviceA-acl6-basic-3500] quit
      ```
   2. Configure a traffic classifier.
      
      
      ```
      [~DeviceA] traffic classifier c1
      [*DeviceA-classifier-c1] if-match ipv6 acl 3500
      [*DeviceA-classifier-c1] commit
      [~DeviceA-classifier-c1] quit
      ```
   3. Configure a traffic behavior and bind the traffic behavior to the DS-Lite instance named **ds-lite1**.
      
      
      ```
      [~DeviceA] traffic behavior b1 
      [*DeviceA-behavior-b1] ds-lite bind instance ds-lite1
      [*DeviceA-behavior-b1] commit
      [~DeviceA-behavior-b1] quit
      ```
   4. Configure a DS-Lite traffic diversion policy and associate the IPv6 ACL-based traffic classification rule with the traffic behavior.
      
      
      ```
      [~DeviceA] traffic policy p1
      [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
      [*DeviceA-trafficpolicy-p1] commit
      [~DeviceA-trafficpolicy-p1] quit
      ```
   5. Apply the policy to GE 0/2/1.
      
      
      ```
      [~DeviceA] interface GigabitEthernet 0/2/1
      [~DeviceA-GigabitEthernet0/2/1] traffic-policy p1 inbound
      [*DeviceA-GigabitEthernet0/2/1] commit
      [~DeviceA-GigabitEthernet0/2/1] quit
      ```
3. Configure interfaces and a routing protocol.
   1. Configure IS-IS.
      
      
      ```
      [~DeviceA] isis 1000
      [*DeviceA-isis-1000] is-level level-1 
      [*DeviceA-isis-1000] network-entity 10.1000.1000.1002.00
      [*DeviceA-isis-1000] ipv6 enable topology ipv6
      [*DeviceA-isis-1000] commit
      [~DeviceA-isis-1000] quit
      ```
   2. Configure the DS-Lite device's interface connected to the IPv6 network.
      
      
      ```
      [~DeviceA] interface GigabitEthernet 0/2/1
      [~DeviceA-GigabitEthernet0/2/1] ipv6 enable
      [*DeviceA-GigabitEthernet0/2/1] ipv6 address 2001:DB8:2::2:1 64
      [*DeviceA-GigabitEthernet0/2/1] isis ipv6 enable 1000
      [*DeviceA-GigabitEthernet0/2/1] commit
      [~DeviceA-GigabitEthernet0/2/1] quit
      ```
4. Configure the device to import the local IP route to the IS-IS routing table so that the route is advertised to the IPv6 network. In this example, UNRs are used as the local IP route and address pool route.
   
   
   ```
   [~DeviceA] isis 1000
   [~DeviceA-isis-1000] ipv6 import-route unr
   [*DeviceA-isis-1000] commit
   [~DeviceA-isis-1000] quit
   ```
5. Configure a DS-Lite translation policy.
   
   
   ```
   [~DeviceA] ds-lite instance ds-lite1
   [*DeviceA-ds-lite-instance-ds-lite1] ds-lite outbound 3500 address-group group1 
   [*DeviceA-ds-lite-instance-ds-lite1] commit
   [~DeviceA-ds-lite-instance-ds-lite1] quit
   ```
6. After the configuration is complete, the DS-Lite device can establish connections with other devices. In addition, the CPE is routable to the local IP address and the addresses in the address pool.
   
   
   ```
   [~DeviceA] display ipv6 routing-table 2001:DB8::1
   Routing Table : _Public_
   Summary Count : 1
    Destination  : 2001:DB8::1                         PrefixLength : 128
    NextHop      : FE80::218:82FF:FE84:CCF             Preference   : 15
    Cost         : 10                                  Protocol     : Unr
    RelayNextHop : ::                                  TunnelID     : 0x0
    Interface    : InLoopBack0                         Flags        : D 
   ```
7. Configure basic DS-Lite functions on the backup device (device B).
   1. Configure basic license functions.
      
      
      ```
      <HUAWEI> system-view  
      [~DeviceB] sysname DeviceB  
      [*DeviceB] commit  
      [~DeviceB] vsm on-board-mode disable
      [*DeviceB] commit
      [~DeviceB] license  
      [*DeviceB-license] active ds-lite vsuf slot 1 
      [*DeviceB-license] active nat session-table size 16 slot 1 
      [*DeviceB-license] commit  
      [~DeviceB-license] quit
      ```
   2. Configure a DS-Lite instance and bind it to a DS-Lite board.
      
      
      ```
      [~DeviceB] service-location 1  
      [*DeviceB-service-location-1] location slot 1  
      [*DeviceB-service-location-1] commit  
      [~DeviceB-service-location-1] quit  
      [~DeviceB] service-instance-group 1  
      [*DeviceB-instance-group-1] service-location 1  
      [*DeviceB-instance-group-1] commit  
      [~DeviceB-instance-group-1] quit  
      [~DeviceB] ds-lite instance ds-lite1 id 1  
      [*DeviceB-ds-lite-instance-ds-lite1] service-instance-group 1  
      [*DeviceB-ds-lite-instance-ds-lite1] quit  
      [~DeviceB-ds-lite-instance-ds-lite1] commit
      ```
   3. Configure a local IPv6 address and a remote IPv6 address for a DS-Lite tunnel.
      
      
      ```
      [~DeviceB] ds-lite instance ds-lite1  
      [~DeviceB-ds-lite-instance-ds-lite1] local-ipv6 2001:DB8::1 prefix-length 128  
      [*DeviceB-ds-lite-instance-ds-lite1] remote-ipv6 2001:DB8:2::1 prefix-length 64  
      [*DeviceB-ds-lite-instance-ds-lite1] commit  
      [~DeviceB-ds-lite-instance-ds-lite1] quit
      ```
   4. Configure a DS-Lite address pool and a NAT translation policy. Set the address pool with a range of 10.38.160.10 through 10.38.160.20.
      
      
      ```
      [~DeviceB] ds-lite instance ds-lite1  
      [*DeviceB-ds-lite-instance-ds-lite1] ds-lite address-group group1 group-id 1 10.38.160.10 10.38.160.20  
      [*DeviceB-ds-lite-instance-ds-lite1] commit  
      [~DeviceB-ds-lite-instance-ds-lite1] quit
      ```
8. Configure a DS-Lite traffic diversion policy on the backup device.
   1. Configure IPv6 ACL-based traffic classification rules.
      
      
      ```
      [~DeviceB] acl ipv6 3500  
      [*DeviceB-acl6-basic-3500] rule permit ipv6 source 2001:DB8:2::1 64 destination 2001:DB8::1 128  
      [*DeviceB-acl6-basic-3500] commit  
      [~DeviceB-acl6-basic-3500] quit
      ```
   2. Configure a traffic classifier.
      
      
      ```
      [~DeviceB] traffic classifier c1  
      [*DeviceB-classifier-c1] if-match ipv6 acl 3500  
      [*DeviceB-classifier-c1] commit  
      [~DeviceB-classifier-c1] quit
      ```
   3. Configure a traffic behavior and bind the traffic behavior to the DS-Lite instance named **ds-lite1**.
      
      
      ```
      [~DeviceB] traffic behavior b1   
      [*DeviceB-behavior-b1] ds-lite bind instance ds-lite1  
      [*DeviceB-behavior-b1] commit  
      [~DeviceB-behavior-b1] quit
      ```
   4. Configure a DS-Lite traffic diversion policy and associate the IPv6 ACL-based traffic classification rule with the traffic behavior.
      
      
      ```
      [~DeviceB] traffic policy p1  
      [*DeviceB-trafficpolicy-p1] classifier c1 behavior b1  
      [*DeviceB-trafficpolicy-p1] commit  
      [~DeviceB-trafficpolicy-p1] quit
      ```
   5. Apply the policy to GE 0/2/2.
      
      
      ```
      [~DeviceB] interface GigabitEthernet 0/2/2  
      [~DeviceB-GigabitEthernet0/2/2] traffic-policy p1 inbound  
      [*DeviceB-GigabitEthernet0/2/2] commit  
      [~DeviceB-GigabitEthernet0/2/2] quit
      ```
9. Configure basic DS-Lite functions and a traffic diversion policy on the backup device.
   
   
   ```
   [~DeviceB] ds-lite instance ds-lite1 
   [*DeviceB-ds-lite-instance-ds-lite1] ds-lite outbound 3500 address-group group1
   [*DeviceB-ds-lite-instance-ds-lite1] commit
   [~DeviceB-ds-lite-instance-ds-lite1] quit
   ```
10. Configure a static route on the backup device.
    
    
    ```
    [~DeviceB] ipv6 route-static 2001:DB8:2:: 64 2001:DB8:1::2:2 
    [*DeviceB] commit
    ```
11. Configure a static route to the local IPv6 address segment of the DS-Lite tunnel on the master device so that user traffic can be switched to the backup device if the service board on the master device fails.
    
    
    ```
    [~DeviceA] ipv6 route-static 2001:DB8::1 128 2001:DB8:1::2:1 
    [*DeviceA] commit
    ```

#### Configuration Files

* Master DS-Lite device configuration file
  
  ```
  #  
  sysname DeviceA 
  #
  vsm on-board-mode disable
  #  
  license  
   active ds-lite vsuf slot 1 
   active nat session-table size 16 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #  
  acl ipv6 number 3500 
   rule permit ipv6 source 2001:DB8:2::1 64 destination 2001:DB8::1 128 
  #  
  service-location 1  
   location slot 1  
  #  
  service-instance-group 1  
   service-location 1  
  #  
  ds-lite instance ds-lite1 id 1 
   service-instance-group 1  
   local-ipv6 2001:DB8::1 prefix-length 128 
   remote-ipv6 2001:DB8:2::1 prefix-length 64 
   ds-lite address-group group1 group-id 1 10.38.160.100 10.38.160.110 
   ds-lite outbound 3500 address-group group1 
   ds-lite centralized-backup enable 
  #  
  traffic classifier c1 operator or
   if-match acl 3500 precedence 1
  #  
  traffic behavior b1  
   ds-lite bind instance ds-lite1 
  #  
  traffic policy p1  
   classifier c1 behavior b1 precedence 1  
  #  
  isis 1000 
   is-level level-1 
   network-entity 10.1000.1000.1002.00 
   ipv6 enable topology ipv6 
   ipv6 import-route unr
  #
  interface gigabitEthernet 0/2/1  
   undo shutdown  
   ipv6 enable 
   ipv6 address 2001:DB8:2::2:1 64 
   traffic-policy p1 inbound  
   isis ipv6 enable 1000
  #
  interface gigabitEthernet 0/2/2  
   undo shutdown  
   ipv6 enable 
   ipv6 address 2001:DB8:1::2:2 64   
  #
  ipv6 route-static 2001:DB8::1 128 2001:DB8:1::2:1
  #  
   return
  ```
* Backup DS-Lite device configuration file
  
  ```
  #  
  sysname DeviceB 
  #
  vsm on-board-mode disable
  #  
  license  
   active ds-lite vsuf slot 1 
   active nat session-table size 16 slot 1 
   active nat bandwidth-enhance 40 slot 1
  #  
  acl ipv6 number 3500 
   rule permit ipv6 source 2001:DB8:2::1 64 destination 2001:DB8::1 128
  #  
  service-location 1  
   location slot 1   
  #  
  service-instance-group 1  
   service-location 1  
  #  
  ds-lite instance ds-lite1 id 1 
   service-instance-group 1  
   local-ipv6 2001:DB8::1 prefix-length 128 
   remote-ipv6 2001:DB8:2::1 prefix-length 64 
   ds-lite address-group group1 group-id 1 10.38.160.10 10.38.160.20 
   ds-lite outbound 3500 address-group group1 
   ds-lite centralized-backup enable 
  #  
  traffic classifier c1 operator or
   if-match acl 3500 precedence 1
  #  
  traffic behavior b1  
   ds-lite bind instance ds-lite1 
  #  
  traffic policy p1  
   classifier c1 behavior b1 precedence 1  
  #  
  isis 1000 
   is-level level-1 
   network-entity 10.1000.1000.1002.00 
   ipv6 enable topology ipv6 
   ipv6 import-route unr
  #
  interface gigabitEthernet 0/2/2  
   undo shutdown  
   ipv6 enable 
   ipv6 address 2001:DB8:1::2:1 64 
   traffic-policy p1 inbound  
   isis ipv6 enable 1000
  # 
  ipv6 route-static 2001:DB8:2:: 64 2001:DB8:1::2:2
  #
   return
  ```