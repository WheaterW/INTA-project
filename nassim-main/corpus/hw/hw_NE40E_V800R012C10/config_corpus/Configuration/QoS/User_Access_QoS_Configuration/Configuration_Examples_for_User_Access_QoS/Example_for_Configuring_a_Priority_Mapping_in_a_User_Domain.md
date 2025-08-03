Example for Configuring a Priority Mapping in a User Domain
===========================================================

This section provides an example for configuring a priority mapping based on BA classification in a user domain.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001232554952__fig_dc_ne_cfg_01380101), subscriber1 accesses the Internet through PPPoEoVLAN. The networking requirements are as follows:

* The user belongs to the domain **isp1** and accesses the Internet through GE 0/2/0.1 of Device in PPPoEoVLAN mode. The device connected to Device supports the dial-up function.
* RADIUS authentication and accounting are used.
* The IP address of the RADIUS server is 192.168.7.249. The authentication and accounting port numbers are 1645 and 1646, respectively. RADIUS+1.1 is used, with the key **itellin**.
* The IP address of the DNS server is 192.168.7.252.
* The priority of the online user in the domain **isp1** is 3.

To change the 802.1p value of subscriber1's VLAN packets, configure a priority mapping on Device.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 and Interface2.1 in this example represent GE 0/1/0 and GE 0/2/0.1, respectively.


**Figure 1** Networking diagram of configuring a priority mapping in a user domain  
![](figure/en-us_image_0000001277154565.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the BRAS service function on Device for users to go online.
2. Configure a priority mapping in the user domain on Device.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of the domain to which users belong
* User priority to be mapped
* Service class and color of packets

#### Procedure

1. Configure the BRAS service function on Device for users to go online.
   
   
   
   For detailed configurations, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - User Access*.
2. Configure a priority mapping in the user domain.
   
   
   
   # Configure the priority of online users.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device
   [*HUAWEI] commit
   [~Device] aaa
   [~Device-aaa] domain isp1
   [*Device-aaa] commit
   [~Device-aaa-domain-isp1] user-priority upstream 3
   [*Device-aaa-domain-isp1] commit
   [~Device-aaa-domain-isp1] quit
   [~Device-aaa] quit
   ```
   
   # Configure a priority mapping.
   
   ```
   [~Device] diffserv domain isp1
   [*Device-dsdomain-isp1] user-priority 3 phb af4 yellow 
   [*Device-dsdomain-isp1] commit
   [~Device-dsdomain-isp1] quit
   ```
   
   # Enable BA classification in the domain.
   
   ```
   [~Device] aaa
   [~Device-aaa] domain isp1
   [*Device-aaa-domain-isp1] trust upstream isp1
   [*Device-aaa-domain-isp1] commit
   [~Device-aaa-domain-isp1] return
   ```
   
   After the preceding configuration is complete, the priorities of the packets of the users who go online through the domain **isp1** are all 3, and the service class and color mapped inside Device are AF4 and yellow, respectively.
3. Verify the configuration.
   
   
   
   Run the **display port-queue statistics interface gigabitethernet 0/1/0 outbound** command on Device. Because BA classification is enabled for all online users with priority 3 in the domain **isp1**, traffic enters the AF4 queue and the 802.1p value carried in packets on the outbound interface is 4.
   
   ```
   <Device> display port-queue statistics gigabitethernet 0/1/0 outbound
   ```
   ```
   GigabitEthernet0/1/0 outbound traffic statistics:
    [be]
    Current usage percentage of queue: 0
     Total pass:
                          1,003,905,621 packets,             90,351,505,260 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [af1]
    Current usage percentage of queue: 0
     Total pass:
                                      0 packets,                          0 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [af2]
    Current usage percentage of queue: 0
     Total pass:
                                      0 packets,                          0 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [af3]
    Current usage percentage of queue: 0
     Total pass:
                                      0 packets,                          0 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [af4]
    Current usage percentage of queue: 0
     Total pass:
                              1,748,941 packets,                157,404,690 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                 26,117 pps,                     18,804,240 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [ef]
    Current usage percentage of queue: 0
     Total pass:
                                      0 packets,                          0 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [cs6]
    Current usage percentage of queue: 0
     Total pass:
                                    335 packets,                     25,502 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
    [cs7]
    Current usage percentage of queue: 0
     Total pass:
                                      0 packets,                          0 bytes
     Total discard:
                                      0 packets,                          0 bytes
       Drop tail discard:
                                      0 packets,                          0 bytes
       Wred discard:
                                      0 packets,                          0 bytes
     Last 30 seconds pass rate:
                                      0 pps,                              0 bps
     Last 30 seconds discard rate:
                                      0 pps,                              0 bps
       Drop tail discard rate:
                                      0 pps,                              0 bps
       Wred discard rate:
                                      0 pps,                              0 bps
     buffer size:                    10 kbytes
     used buffer size:                0 kbytes
     Peak rate:
                             0000-00-00 00:00:00                          0 bps
   ```

#### Configuration Files

Device configuration file
```
#
sysname Device
# 
diffserv domain default
diffserv domain 5p3d
diffserv domain isp1 
 user-priority 3 phb af4 yellow
diffserv domain qinq
#
radius-server group rd1
 radius-server shared-key-cipher %^%#clY:%[]x='-RMNJus[s/VJ:3YBq3<..|.{'xgbp+%^%
 radius-server authentication 192.168.7.249 1645 weight 0
 radius-server accounting 192.168.7.249 1646 weight 0
 radius-server type plus11
 radius-server traffic-unit kbyte
#
ip pool pool1 bas local
 gateway 10.82.0.1 255.255.255.0
 section 0 10.82.0.2 10.82.0.200 
 dns-server 192.168.7.252
#
aaa
 authentication-scheme auth1
 accounting-scheme acct1
#
domain default0
domain default1
domain default_admin
domain isp1
 authentication-scheme auth1
 accounting-scheme acct1
 radius-server group rd1
 ip-pool pool1
 trust upstream isp1
 user-priority upstream 3
  #
interface Virtual-Template1
#
interface GigabitEthernet0/2/0
 undo shutdown
#
interface GigabitEthernet0/2/0.1
 user-vlan 1
 pppoe-server bind Virtual-Template 1
 bas
  access-type layer2-subscriber default-domain authentication isp1
#
interface GigabitEthernet0/1/0
 undo shutdown
 ip address 192.168.7.1 255.255.255.0
#
return
```