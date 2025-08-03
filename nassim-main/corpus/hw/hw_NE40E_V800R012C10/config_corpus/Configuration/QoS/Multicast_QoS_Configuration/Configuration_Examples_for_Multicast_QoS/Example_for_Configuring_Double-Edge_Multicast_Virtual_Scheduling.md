Example for Configuring Double-Edge Multicast Virtual Scheduling
================================================================

This section provides an example for configuring double-edge multicast virtual scheduling in the case where one device is used for user access and the other device is used for multicast forwarding.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371642__fig_dc_ne_cfg_01386801), the family user accesses the Internet in IPoEoVLAN mode through GE 0/1/0.100 on DeviceA. DeviceA authenticates the user through a RADIUS server and allocates bandwidth for the user. The default bandwidth of the user is 2 Mbit/s. The DSLAM supports IGMP snooping.

DeviceA implements user access, and DeviceB forwards multicast traffic. On the basis of the existing network, DeviceA is configured to perform multicast virtual scheduling for the user so that the user can watch the multicast programs normally. If the user subscribes to a CCTV program with the multicast group 239.0.0.1/24 or a JSTV program with the multicast group 239.0.0.2/24, DeviceA adjusts the unicast bandwidth for the user according to the multicast bandwidth, with the total bandwidth of the user remaining unchanged. The minimum unicast bandwidth of the user is 1 Mbit/s.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, sub-interface 1 and interface 2 represent GE 0/1/0.100 and GE 0/2/0, respectively.


**Figure 1** Configuring double-edge multicast virtual scheduling  
![](images/fig_dc_ne_cfg_01386801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces and a unicast routing protocol to implement IP connectivity.
2. Configure the IPoEoVLAN access type to allow the user to access the Internet.
3. Configure IGMP and PIM-SM.
4. Configure a multicast VLAN on the main user access interface so that DeviceA can deliver multicast data through the multicast VLAN.
5. Configure a multicast program list and the parameters for multicast program bandwidth.
6. Configure the bandwidth reserved for unicast traffic and enable multicast virtual scheduling.

#### Data Preparation

To complete the configuration, you need the following data:

* Number of the interface from which the user is connected to the network, VLAN ID on the user side, and homing domain of the user
* Multicast VLAN ID
* Addresses and bandwidth of the multicast programs
* Bandwidth reserved for unicast traffic

#### Procedure

1. Configure an IP address for each interface and a unicast routing protocol.
   
   
   
   For details, see *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Services* and *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Routing*.
2. Configure user access.
   
   
   
   Configure the user to connect to the network in IPoEoVLAN mode through GE 0/1/0.100 of DeviceA. The user VLAN ID ranges from 1 to 100, and the homing domain of the user is "huawei". Configure DeviceA to authenticate the user through the RADIUS server. For details, see "Configuring BRAS Access" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - User Access*.
3. Configure the default total bandwidth of the user.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] qos-profile huawei
   ```
   ```
   [*HUAWEI-qos-profile-huawei] user-queue cir 2000 pir 2000
   ```
   ```
   [*HUAWEI-qos-profile-huawei] quit
   ```
   ```
   [*HUAWEI] interface GigabitEthernet 0/1/0.100
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.100] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.100] user-vlan 1 100
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.100-vlan-1-100] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.100-bas] access-type layer2-subscriber
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.100-bas] authentication-method bind
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.100-bas] qos-profile huawei outbound
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.100-bas] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.100-bas] quit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.100] quit
   ```
4. Enable multicast routing and configure IGMP and PIM.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only the configurations related to PIM on DeviceA are provided here. For multicast routing related to the Internet and the PIM configurations of other devices, refer to *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Multicast.*
   
   # Enable multicast routing on DeviceA.
   
   ```
   [~DeviceA] multicast routing-enable
   ```
   
   # Enable IGMP on the user-side GE 0/1/0.100.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0.100
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.100] igmp enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.100] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.100] quit
   ```
   
   # Enable PIM on the network-side interface GE 0/2/0.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
5. Configure multicast user VLAN aggregation.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] igmp enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] multicast user-aggregation vlan 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
6. Configure a multicast program list and the parameters for multicast program bandwidth.
   
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [*DeviceA-aaa] multicast-list cctv group-address 239.0.0.1 24
   ```
   ```
   [*DeviceA-aaa] multicast-list jstv group-address 239.0.0.2 24
   ```
   ```
   [*DeviceA-aaa] quit
   ```
   ```
   [*DeviceA] multicastbandwidth
   ```
   ```
   [*DeviceA-mbandwidth] multicast-list name cctv detect-interval 15 threshold 15
   ```
   ```
   [*DeviceA-mbandwidth] multicast-list name jstv detect-interval 15 threshold 20
   ```
   ```
   [*DeviceA-mbandwidth] commit
   ```
   ```
   [~DeviceA-mbandwidth] quit
   ```
7. Configure the bandwidth reserved for unicast traffic and enable multicast virtual scheduling.
   
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [*DeviceA-aaa] domain huawei
   ```
   ```
   [*DeviceA-aaa-domain-huawei] multicast unicast-reservable-bandwidth cir 1024
   ```
   ```
   [*DeviceA-aaa-domain-huawei] commit
   ```
   ```
   [~DeviceA-aaa-domain-huawei] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
8. Disable multicast data replication and forwarding.
   
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [*DeviceA-aaa] domain huawei
   ```
   ```
   [*DeviceA-aaa-domain-huawei] multicast without-forwarding
   ```
   ```
   [*DeviceA-aaa-domain-huawei] commit
   ```
   ```
   [~DeviceA-aaa-domain-huawei] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```

#### Configuration Files

* DeviceA configuration file
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
   qos-profile huawei
  ```
  ```
     user-queue cir 2000 pir 2000
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   igmp enable
  ```
  ```
   multicast user-aggregation vlan 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0.100
  ```
  ```
   igmp enable
  ```
  ```
   user-vlan 1 100
  ```
  ```
   bas
  ```
  ```
    access-type layer2-subscriber
  ```
  ```
    authentication-method bind
  ```
  ```
    qos-profile huawei outbound identifier none
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.0.0.3 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  #  
  ```
  ```
  aaa
  ```
  ```
   multicast-list cctv group-address 239.0.0.1 24
  ```
  ```
   multicast-list jstv group-address 239.0.0.2 24
  ```
  ```
   domain huawei
  ```
  ```
    multicast unicast-reservable-bandwidth cir 1024
  ```
  ```
    multicast without-forwarding
  ```
  ```
  #
  ```
  ```
  multicastbandwidth
  ```
  ```
   multicast-list name cctv detect-interval 15 threshold 15
  ```
  ```
   multicast-list name jstv detect-interval 15 threshold 20
  ```
  ```
  #
  ```
  ```
  return
  ```