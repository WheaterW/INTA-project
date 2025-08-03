Example for Configuring Single-Edge Multicast Virtual Scheduling
================================================================

This section provides an example for configuring single-edge multicast virtual scheduling in the case where a single device is used for both user access and multicast traffic forwarding.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* This is an example of normal single-edge networking. In the networking of MPLS multicast, the **multicast without-forwarding** command must be run to disable the devices from copying multicast data.
* In the networking of MPLS multicast, the IGMP and PIM protocols can be configured only on VE interfaces. For details, see "IGMP Configuration" and "PIM-SM Configuration" in *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - IP Multicast*.

As shown in [Figure 1](#EN-US_TASK_0172371639__fig_dc_ne_cfg_01386701), the family user accesses the Internet in IPoEoVLAN mode through GE 0/1/0.100 on the Router. The Router authenticates the user through a RADIUS server and allocates bandwidth for the user. The default bandwidth of the user is 2 Mbit/s. The DSLAM supports IGMP snooping.

The Router implements both user access and multicast traffic forwarding. On the basis of the existing network, the Router is configured to perform multicast virtual scheduling for the user so that the user can watch the multicast programs normally. If the user subscribes to a CCTV program with the multicast group 239.0.0.1/24 or a JSTV program with the multicast group 239.0.0.2/24, the Router adjusts the unicast bandwidth for the user according to the multicast bandwidth, with the total bandwidth of the user remaining unchanged. The minimum unicast bandwidth of the user is 1 Mbit/s.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, sub-interface 1 and interface 2 represent GE 0/1/0.100 and GE 0/2/0, respectively.


**Figure 1** Configuring single-edge multicast virtual scheduling  
![](images/fig_dc_ne_cfg_01386701.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces and a unicast routing protocol to implement IP connectivity.
2. Configure the IPoEoVLAN access type to allow the user to access the Internet.
3. Configure IGMP and PIM-SM.
4. Configure a multicast VLAN on the main user access interface so that the Router can deliver multicast data through the multicast VLAN.
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
   
   
   
   Configure the user to connect to the network in IPoEoVLAN mode through GE 0/1/0.100 of the Router. The user VLAN ID ranges from 1 to 100, and the homing domain of the user is "huawei". Configure the Router to authenticate the user through the RADIUS server. For details, see "Configuring BRAS Access" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - User Access*.
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
   
   Only the configurations related to PIM on the Device are provided here. For multicast routing related to the Internet and the PIM configurations of other devices, refer to "MBGP Configuration" and "PIM-SM Configuration" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Multicast.*
   
   # Enable multicast routing on the Router.
   
   ```
   [~HUAWEI] multicast routing-enable
   ```
   
   # Enable IGMP on the user-side GE 0/1/0.100.
   
   ```
   [~HUAWEI] interface gigabitethernet 0/1/0.100
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.100] igmp enable
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.100] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.100] quit
   ```
   
   # Enable PIM on the network-side interface GE 0/2/0.
   
   ```
   [~HUAWEI] interface gigabitethernet 0/2/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0] quit
   ```
5. Configure multicast user VLAN aggregation.
   
   
   ```
   [~HUAWEI] interface gigabitethernet 0/1/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] igmp enable
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] multicast user-aggregation vlan 1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] quit
   ```
6. Configure a multicast program list and the parameters for multicast program bandwidth.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [*HUAWEI-aaa] multicast-list cctv group-address 239.0.0.1 24
   ```
   ```
   [*HUAWEI-aaa] multicast-list jstv group-address 239.0.0.2 24
   ```
   ```
   [*HUAWEI-aaa] quit
   ```
   ```
   [*HUAWEI] multicastbandwidth
   ```
   ```
   [*HUAWEI-mbandwidth] multicast-list name cctv detect-interval 15 threshold 15
   ```
   ```
   [*HUAWEI-mbandwidth] multicast-list name jstv detect-interval 15 threshold 20
   ```
   ```
   [*HUAWEI-mbandwidth] commit
   ```
   ```
   [~HUAWEI-mbandwidth] quit
   ```
7. Configure the bandwidth reserved for unicast traffic and enable multicast virtual scheduling.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [*HUAWEI-aaa] domain huawei
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] multicast unicast-reservable-bandwidth cir 1024
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] quit
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```

#### Configuration Files

* Router configuration file
  
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