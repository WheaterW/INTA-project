Example for Configuring Multicast Shaping
=========================================

This section provides an example for configuring multicast shaping.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, NE40E-M2E is used.

On the network shown in [Figure 1](#EN-US_TASK_0172371645__fig_dc_ne_cfg_01386901), the Router functions as a BRAS to provide Internet access and IPTV multicast services for users in the **isp1** domain. The IGMP protocol is used on the host side and the SM mode is used on the PIM network.

The requirements on multicast shaping are as follows:

* The function of multicast shaping uses 5 Mbit/s committed bandwidth and 10 Mbit/s peak bandwidth.
* The IP address of the multicast source is 10.0.0.2, and the IP address of the multicast group is 239.0.0.1.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent GE 0/1/0 and GE 0/2/0, respectively.


**Figure 1** Configuring multicast shaping  
![](images/fig_dc_ne_cfg_01386901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces and a unicast routing protocol to implement IP connectivity.
2. Configure the BRAS service so that users can go online.
3. Configure IGMP and PIM-SM.
4. Configure multicast shaping.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of the multicast shaping list

#### Procedure

1. Configure an IP address for each interface and a unicast routing protocol.
   
   
   
   For detailed configurations, see *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Routing*.
2. Configure the access service.
   
   
   
   For detailed configurations, see *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - User Access*.
3. Configure IGMP and PIM.
   
   
   
   Enable multicast routing and IGMP on the host-side interface.
   
   # Enable multicast and configure IGMP on the host-side interface of the Router. Enable IGMPv2 on GE 0/2/0.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] multicast routing-enable
   ```
   ```
   [*HUAWEI] interface gigabitethernet 0/2/0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0] igmp enable
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0] igmp version 2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0] quit
   ```
   
   # Enable PIM-SM on GE 0/1/0 of the Router.
   
   ```
   [~HUAWEI] interface gigabitethernet 0/1/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] quit
   ```
4. Configure multicast shaping.
   
   
   
   # Configure a multicast list.
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [*HUAWEI-aaa] multicast-list list1 source-address 10.0.0.2 group-address 239.0.0.1
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
   
   # Enable multicast shaping.
   
   ```
   [~HUAWEI] multicast shaping enable
   ```
   
   # Set the parameters of multicast shaping to guarantee 5 Mbit/s committed bandwidth and 10 Mbit/s peak bandwidth.
   
   ```
   [*HUAWEI] multicast shaping
   ```
   ```
   [*HUAWEI-qos-mshaping] multicast-list name list1 cir 5000 pir 10000 
   ```
   ```
   [*HUAWEI-qos-mshaping] multicast-list name list1 cir 5000 pir 10000 car-mode
   ```
   ```
   [*HUAWEI-qos-mshaping] commit
   ```
   ```
   [~HUAWEI-qos-mshaping] quit
   ```
5. Verify the configuration.
   
   
   
   Run the **display multicast-list** command to check detailed information about the multicast list.
   
   ```
   <HUAWEI> display multicast-list list1
   ```
   ```
     -----------------------------------------------------------------------
   ```
   ```
     Multicast-list name  : list1
   ```
   ```
     Index                : 0
   ```
   ```
     Source IP/mask       : 10.0.0.2/32
   ```
   ```
     Group IP/mask        : 239.0.0.1/32
   ```
   ```
     Group vpn-instance   : --
   ```
   ```
     -----------------------------------------------------------------------   
   ```
   
   Run the **display interface** [ *interface-type* [ *interface-number* ] ] [ | { **begin** | **exclude** | **include** } *regular-expression* ] command on GE 0/1/0, and you can view that the guaranteed bandwidth for multicast traffic on GE 0/1/0 is 5 Mbit/s. Excess multicast traffic is discarded.

#### Configuration Files

* Router configuration file
  ```
  #
  ```
  ```
   sysname HUAWEI
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
   multicast shaping enable
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
   pim sm
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
   pppoe-server bind Virtual-Template 1
  ```
  ```
   igmp enable
  ```
  ```
   bas
  ```
  ```
    access-type layer2-subscriber
  ```
  ```
  #
  ```
  ```
  ip pool pool1 bas local
  ```
  ```
   gateway 192.168.1.1 255.255.255.0
  ```
  ```
   section 0 192.168.1.2 192.168.1.200
  ```
  ```
   dns-server 192.168.7.252
  ```
  ```
  #
  ```
  ```
  aaa
  ```
  ```
   multicast-list list1 index 0 source-address 10.0.0.2 group-address 239.0.0.1
  ```
  ```
   authentication-scheme auth1
  ```
  ```
   accounting-scheme acct1
  ```
  ```
   domain isp1
  ```
  ```
    authentication-scheme auth1
  ```
  ```
    accounting-scheme  acct1
  ```
  ```
    radius-server group rd1
  ```
  ```
    ip-pool pool1
  ```
  ```
  #
  ```
  ```
  multicast shaping
  ```
  ```
   multicast-list name list1 cir 5000 pir 10000 
  ```
  ```
   multicast-list name list1 cir 5000 pir 10000 car-mode
  ```
  ```
  #
  ```
  ```
  return
  ```