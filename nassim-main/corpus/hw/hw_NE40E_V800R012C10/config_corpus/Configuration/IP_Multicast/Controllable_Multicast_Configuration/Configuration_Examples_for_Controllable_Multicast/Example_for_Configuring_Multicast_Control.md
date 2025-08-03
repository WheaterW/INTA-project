Example for Configuring Multicast Control
=========================================

This section provides several examples to illustrate how to configure controllable multicast based on a typical controllable multicast networking.

#### Networking Requirement

Multicast control is required to control the multicast rights of users in different domains.

As shown in [Figure 1](#EN-US_TASK_0172367746__fig_dc_ne_mcontrol_cfg_001501), three multicast sources, S1, S2, and S3, in the PIM-SM domain send packets with addresses 225.1.1.1, 226.1.1.1, and 227.1.1.1. Users access the multicast network through the Router. The requirements are as follows: Users in domain isp1 can join multicast groups 225.1.1.1 and 226.1.1.1 only; users in domain isp2 can join multicast groups 226.1.1.1 and 227.1.1.1 only.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This example describes how to configure multicast control on an IPv4 network. Configurations on an IPv6 network are the same, and are not mentioned here.


**Figure 1** Networking diagram of multicast control  
![](images/fig_dc_ne_mcontrol_cfg_001501.png)  

The BRAS uses GE 0/1/0 to communicate with the access network and uses GE 0/1/1, GE 0/1/2, and GE 0/1/3 to communicate with PIM-SM devices.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the IP addresses of the interfaces and the unicast routing protocol to implement IP connectivity.
2. Configure the access service so that users can go online.
3. Configure IGMP and PIM-SM to implement uncontrollable multicast.
4. Configure the controllable multicast feature and enable controllable multicast on interfaces.
5. Verify the configuration.

#### Data Preparation

To complete the configuration, you need the following data:

* Maximum number of multicast programs that a user is allowed to access at a time (the value is 2)


#### Procedure

1. Configure the IP address of the interface and the unicast routing protocol.
   
   
   
   For details, refer to the *HUAWEI NE40E-M2 seriesUniversal Service RouterConfiguration Guide - IP Services* and the *HUAWEI NE40E-M2 seriesUniversal Service RouterConfiguration Guide - IP Routing*.
2. Configure the access service.
   
   
   
   For details, refer to the *HUAWEI NE40E-M2 seriesUniversal Service RouterConfiguration Guide - User Access*.
3. Configure IGMP and PIM.
   
   
   
   For details, see "Configuring PIM-SM" in *IGMP Configuration* and *PIM Configuration*.
4. Configure controllable multicast.
   
   
   
   # Configure the multicast program list.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS] aaa
   ```
   ```
   [~BRAS-aaa] multicast-list list1 group-address 225.1.1.1
   ```
   ```
   [~BRAS-aaa] multicast-list list2 group-address 226.1.1.1
   ```
   ```
   [~BRAS-aaa] multicast-list list3 group-address 227.1.1.1
   ```
   
   # Configure the multicast profile.
   
   ```
   [~BRAS-aaa] multicast-profile profile1
   ```
   ```
   [~BRAS-aaa-mprofile-profile1] multicast-list name list1
   ```
   ```
   [~BRAS-aaa-mprofile-profile1] multicast-list name list2
   ```
   ```
   [~BRAS-aaa-mprofile-profile1] quit
   ```
   ```
   [~BRAS-aaa] multicast-profile profile2
   ```
   ```
   [~BRAS-aaa-mprofile-profile2] multicast-list name list2
   ```
   ```
   [~BRAS-aaa-mprofile-profile2] multicast-list name list3
   ```
   ```
   [~BRAS-aaa-mprofile-profile2] quit
   ```
   
   # Apply the multicast profile to the domain.
   
   ```
   [~BRAS-aaa] domain isp1
   ```
   ```
   [*BRAS-aaa-domain-isp1] commit
   ```
   ```
   [~BRAS-aaa-domain-isp1] multicast-profile profile1
   ```
   ```
   [*BRAS-aaa-domain-isp1] commit
   ```
   ```
   [~BRAS-aaa-domain-isp1] quit
   ```
   ```
   [~BRAS-aaa] domain isp2
   ```
   ```
   [*BRAS-aaa-domain-isp2] commit
   ```
   ```
   [~BRAS-aaa-domain-isp2] multicast-profile profile2
   ```
   ```
   [*BRAS-aaa-domain-isp2] commit
   ```
   ```
   [~BRAS-aaa-domain-isp2] quit
   ```
   ```
   [~BRAS-aaa] quit
   ```
   
   # Enable the controllable multicast feature on the interface.
   
   ```
   [~BRAS] interface gigabitethernet0/1/0
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0] igmp enable
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0] bas
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0-bas] quit
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0] multicast authorization-enable
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] quit
   ```
   ```
   [*BRAS] commit
   ```
5. Verify the configuration.
   
   
   
   # Use the **display access-user** command to view the multicast control rights of the user after the user goes online. For example, you can view the rights of users user1@isp1 and user1@isp2.
   
   ```
   [~BRAS] display access-user username user1@isp1
   ```
   ```
     --------------------------------------------------------------------------
   ```
   ```
     UserID     Username               Interface      IP address       MAC
   ```
   ```
     --------------------------------------------------------------------------
   ```
   ```
     1          user1@isp1             GE0/1/0        172.22.0.3       00-e0-fc-12-34-56
   ```
   ```
     --------------------------------------------------------------------------
   ```
   ```
     Total 1
   ```
   ```
   [~BRAS] display access-user user-id 1
   ```
   ```
     User access index             : 1
   ```
   ```
     User name                     : user1@isp1
   ```
   ```
     ......
   ```
   ```
     Multicast-profile             : profile1
   ```
   ```
     ......
   ```
   ```
   [~BRAS] display access-user username user1@isp2
   ```
   ```
     --------------------------------------------------------------------------
   ```
   ```
     UserID    Username               Interface      IP address       MAC
   ```
   ```
     --------------------------------------------------------------------------
   ```
   ```
     2         user1@isp2             GE0/1/0        172.22.0.5       00-e0-fc-12-34-56
   ```
   ```
     --------------------------------------------------------------------------
   ```
   ```
     Total 1
   ```
   ```
   [~BRAS] display access-user user-id 2
   ```
   ```
     User access index             : 2
   ```
   ```
     User name                     : user1@isp2
   ```
   ```
     ......
   ```
   ```
     Multicast-profile             : profile2
   ```
   ```
     ......
   ```

#### Configuration Files

```
#
```
```
 sysname BRAS
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
interface Virtual-Template1
```
```
#
```
```
interface GigabitEthernet0/1/1
```
```
 undo shutdown
```
```
 ip address 192.168.3.2 255.255.255.0
```
```
 pim sm
```
```
#
```
```
interface GigabitEthernet0/1/2
```
```
 undo shutdown
```
```
 ip address 192.168.2.2 255.255.255.0
```
```
 pim sm
```
```
#
```
```
interface GigabitEthernet0/1/3
```
```
 undo shutdown
```
```
 ip address 192.168.9.2 255.255.255.0
```
```
 pim sm
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
#
```
```
interface GigabitEthernet0/1/0
```
```
 igmp enable
```
```
 pim sm
```
```
 bas
```
```
#
```
```
  access-type layer2-subscriber
```
```
 multicast authorization-enable
```
```
#
```
```
ip pool pool1 bas local
```
```
 gateway 172.22.0.1 255.255.255.0
```
```
 section 0 172.22.0.2 172.22.0.254
```
```
 dns-server  192.168.7.252
```
```
#
```
```
aaa
```
```
 multicast-list list1 group-address 225.1.1.1
```
```
 multicast-list list2 group-address 226.1.1.1
```
```
 multicast-list list3 group-address 227.1.1.1
```
```
 multicast-profile profile1
```
```
  multicast-list name list1
```
```
  multicast-list name list2
```
```
 multicast-profile profile2
```
```
  multicast-list name list2
```
```
  multicast-list name list3
```
```
 authentication-scheme auth1
```
```
 authentication-scheme auth2
```
```
 accounting-scheme acct1
```
```
 accounting-scheme acct2
```
```
 domain isp1
```
```
  authentication-scheme auth1
```
```
  accounting-scheme acct1
```
```
  radius-server group rd1
```
```
  ip-pool pool1
```
```
  multicast-profile profile1
```
```
 domain isp2
```
```
  authentication-scheme auth2
```
```
  accounting-scheme acct2
```
```
  radius-server group rd1
```
```
  ip-pool pool1
```
```
  multicast-profile profile2
```
```
#
```
```
ospf 1
```
```
 area 0.0.0.0
```
```
  network 192.168.3.0 0.0.0.255
```
```
  network 192.168.2.0 0.0.0.255
```
```
  network 192.168.9.0 0.0.0.255
```
```
#
```
```
return
```