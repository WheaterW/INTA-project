Example for Configuring Clean Switching of Multicast Streams in Multicast Groups
================================================================================

This section provides an example for configuring clean switching of multiple multicast streams in two input multicast groups.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367797__fig272515160215), four multicast streams are input from source 1 and source 2 to switch 1 and switch 2, respectively. Switch 1 and switch 2 aggregate the multicast streams into input multicast groups 1 and 2, respectively. Each input multicast group contains four multicast streams. After the two multicast groups enter the router, the router outputs only the four multicast streams in multicast group 1 at the beginning. Output multicast group 1 retains the characteristics of the multicast streams. If clean switching is required, the controller delivers a switching instruction to the router so that the router outputs the content of multicast group 2.

Configuration requirements: Input multicast streams 1 to 4 form input multicast group 1, and input multicast streams 5 to 8 form input multicast group 2. Before receiving a switching instruction from the controller, the router outputs the content of multicast group 1. After receiving a switching instruction from the controller, the router outputs the content of multicast group 2, ensuring that images are smooth and clear.

**Table 1** Characteristics of input multicast streams
| Multicast Stream Characteristics | Input Multicast Stream 1 | Input Multicast Stream 2 | Input Multicast Stream 3 | Input Multicast Stream 4 | Input Multicast Stream 5 | Input Multicast Stream 6 | Input Multicast Stream 7 | Input Multicast Stream 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Source MAC address | 00e0-fc12-3456 | 00e0-fc12-3456 | 00e0-fc12-3456 | 00e0-fc12-3456 | 00e0-fc22-3456 | 00e0-fc22-3456 | 00e0-fc22-3456 | 00e0-fc22-3456 |
| Source IP address | 10.10.10.10 | 10.10.10.10 | 10.10.10.10 | 10.10.10.10 | 12.12.12.12 | 12.12.12.12 | 12.12.12.12 | 12.12.12.12 |
| Destination IP address | 225.0.0.1 | 225.0.0.2 | 225.0.0.3 | 225.0.0.4 | 225.0.0.1 | 225.0.0.2 | 225.0.0.3 | 225.0.0.4 |
| Destination UDP port number | 10000 | 10001 | 10002 | 10003 | 10000 | 10001 | 10002 | 10003 |




#### Configuration Roadmap

**Figure 1** Multicast stream translation![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, and interface3 in this example represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.


  
![](figure/en-us_image_0000001197301500.png "Click to enlarge")

The configuration roadmap is as follows:

1. Enable multicast NAT globally.
2. Create multicast NAT instances.
3. Create a multicast NAT instance group and add the multicast NAT instances to the group.
4. Configure traffic policies.
5. Enable multicast stream translation on an outbound interface and configure multicast stream translation parameters.
6. Configure a multicast NAT outbound group and add the specified output multicast streams to the multicast NAT outbound group.
7. Bind the multicast NAT outbound group to the multicast NAT instance group.
8. Configure clean switching of multicast streams in multicast groups.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast NAT instance names: streamin1, streamin2, streamin3, streamin4, streamin5, streamin6, streamin7, and streamin8
* ACL names required for level-1 traffic classifiers: 4001 and 4002
* Level-1 traffic classifier names: rule\_mac1 and rule\_mac2
* Level-1 traffic behavior names: rule\_mac1 and rule\_mac2
* Level-1 traffic policy names: match1\_mac\_list and match2\_mac\_list2
* ACL names required for level-2 traffic classifiers: 3001, 3002, 3003, 3004, 3005, 3006, 3007, and 3008
* Level-2 traffic classifier names: rule\_ip1, rule\_ip2, rule\_ip3, rule\_ip4, rule\_ip5, rule\_ip6, rule\_ip7, and rule\_ip8
* Level-2 traffic behavior names: rule\_ip1, rule\_ip2, rule\_ip3, rule\_ip4, rule\_ip5, rule\_ip6, rule\_ip7, and rule\_ip8
* Level-2 traffic policy names: match1\_ip\_list1 and match1\_ip\_list2


#### Procedure

1. Enable multicast NAT on the device.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] multicast-nat enable
   ```
2. Create multicast NAT instances named **streamin1**, **streamin2**, **streamin3**, **streamin4**, **streamin5**, **streamin6**, **streamin7**, and **streamin8** on the device.
   
   
   ```
   [~HUAWEI] multicast-nat instance id 1 name streamin1
   ```
   ```
   [*HUAWEI-multicast-nat-instance-1] multicast-nat instance id 2 name streamin2
   ```
   ```
   [*HUAWEI-multicast-nat-instance-2] multicast-nat instance id 3 name streamin3
   ```
   ```
   [*HUAWEI-multicast-nat-instance-3] multicast-nat instance id 4 name streamin4
   ```
   ```
   [*HUAWEI-multicast-nat-instance-4] multicast-nat instance id 5 name streamin5
   ```
   ```
   [*HUAWEI-multicast-nat-instance-5] multicast-nat instance id 6 name streamin6
   ```
   ```
   [*HUAWEI-multicast-nat-instance-6] multicast-nat instance id 7 name streamin7
   ```
   ```
   [*HUAWEI-multicast-nat-instance-7] multicast-nat instance id 8 name streamin8
   ```
   ```
   [*HUAWEI-multicast-nat-instance-8] commit
   ```
   ```
   [~HUAWEI-multicast-nat-instance-8] quit
   ```
3. Create multicast NAT instance groups named **streamingroup1** and **streamingroup2** on the device, and add multicast NAT instances to **streamingroup1** and **streamingroup2**.
   
   
   ```
   [~HUAWEI] multicast-nat instance-group id 1 name streamingroup1
   ```
   ```
   [*HUAWEI-multicast-nat-instance-group-1] assign instance id 1 part 1
   ```
   ```
   [*HUAWEI-multicast-nat-instance-group-1] assign instance id 2 part 2
   ```
   ```
   [*HUAWEI-multicast-nat-instance-group-1] assign instance id 3 part 3
   ```
   ```
   [*HUAWEI-multicast-nat-instance-group-1] assign instance id 4 part 4
   ```
   ```
   [*HUAWEI-multicast-nat-instance-group-1] commit
   ```
   ```
   [~HUAWEI-multicast-nat-instance-group-1] quit
   ```
   ```
   [~HUAWEI] multicast-nat instance-group id 2 name streamingroup2
   ```
   ```
   [*HUAWEI-multicast-nat-instance-group-2] assign instance id 5 part 1
   ```
   ```
   [*HUAWEI-multicast-nat-instance-group-2] assign instance id 6 part 2
   ```
   ```
   [*HUAWEI-multicast-nat-instance-group-2] assign instance id 7 part 3
   ```
   ```
   [*HUAWEI-multicast-nat-instance-group-2] assign instance id 8 part 4
   ```
   ```
   [*HUAWEI-multicast-nat-instance-group-2] commit
   ```
   ```
   [~HUAWEI-multicast-nat-instance-group-2] quit
   ```
4. Configure two-level traffic policies for implementing multicast NAT on the device.
   1. Configure level-1 traffic classification rules for matching the MAC addresses of input multicast groups 1 and 2 to allow the four multicast streams contained in each of the groups to pass through.
      
      
      ```
      [~HUAWEI] acl number 4001
      ```
      ```
      [*HUAWEI-acl-L2-4001] rule 1 permit source-mac 00e0-fc12-3456
      ```
      ```
      [*HUAWEI-acl-L2-4001] commit
      ```
      ```
      [~HUAWEI-acl-L2-4001] quit
      ```
      ```
      [~HUAWEI] acl number 4002
      ```
      ```
      [*HUAWEI-acl-L2-4002] rule 1 permit source-mac 00e0-fc22-3456
      ```
      ```
      [*HUAWEI-acl-L2-4002] commit
      ```
      ```
      [~HUAWEI-acl-L2-4002] quit
      ```
   2. Configure level-1 traffic classifiers.
      
      
      ```
      [~HUAWEI] traffic classifier rule_mac1
      ```
      ```
      [*HUAWEI-classifier-rule_mac1] if-match acl 4001
      ```
      ```
      [*HUAWEI-classifier-rule_mac1] commit
      ```
      ```
      [~HUAWEI-classifier-rule_mac1] quit
      ```
      ```
      [~HUAWEI] traffic classifier rule_mac2
      ```
      ```
      [*HUAWEI-classifier-rule_mac2] if-match acl 4002
      ```
      ```
      [*HUAWEI-classifier-rule_mac2] commit
      ```
      ```
      [~HUAWEI-classifier-rule_mac2] quit
      ```
   3. Configure level-2 traffic classification rules for matching the source IP addresses, destination IP addresses, and UDP port numbers of the four input multicast streams in each of the input multicast groups 1 and 2.
      
      
      ```
      [~HUAWEI] acl number 3001
      ```
      ```
      [*HUAWEI-acl4-advance-3001] rule 1 permit udp source 10.10.10.10 0 destination 225.0.0.1 0 destination-port eq 10000
      ```
      ```
      [*HUAWEI-acl4-advance-3001] commit
      ```
      ```
      [~HUAWEI-acl4-advance-3001] quit
      ```
      ```
      [~HUAWEI] acl number 3002
      ```
      ```
      [*HUAWEI-acl4-advance-3002] rule 1 permit udp source 10.10.10.10 0 destination 225.0.0.2 0 destination-port eq 10001
      ```
      ```
      [*HUAWEI-acl4-advance-3002] commit
      ```
      ```
      [~HUAWEI-acl4-advance-3002] quit
      ```
      ```
      [~HUAWEI] acl number 3003
      ```
      ```
      [*HUAWEI-acl4-advance-3003] rule 1 permit udp source 10.10.10.10 0 destination 225.0.0.3 0 destination-port eq 10002
      ```
      ```
      [*HUAWEI-acl4-advance-3003] commit
      ```
      ```
      [~HUAWEI-acl4-advance-3003] quit
      ```
      ```
      [~HUAWEI] acl number 3004
      ```
      ```
      [*HUAWEI-acl4-advance-3004] rule 1 permit udp source 10.10.10.10 0 destination 225.0.0.4 0 destination-port eq 10003
      ```
      ```
      [*HUAWEI-acl4-advance-3004] commit
      ```
      ```
      [~HUAWEI-acl4-advance-3004] quit
      ```
      ```
      [~HUAWEI] acl number 3005
      ```
      ```
      [*HUAWEI-acl4-advance-3005] rule 1 permit udp source 12.12.12.12 0 destination 225.0.0.1 0 destination-port eq 10000
      ```
      ```
      [*HUAWEI-acl4-advance-3005] commit
      ```
      ```
      [~HUAWEI-acl4-advance-3005] quit
      ```
      ```
      [~HUAWEI] acl number 3006
      ```
      ```
      [*HUAWEI-acl4-advance-3006] rule 1 permit udp source 12.12.12.12 0 destination 225.0.0.2 0 destination-port eq 10001
      ```
      ```
      [*HUAWEI-acl4-advance-3006] commit
      ```
      ```
      [~HUAWEI-acl4-advance-3006] quit
      ```
      ```
      [~HUAWEI] acl number 3007
      ```
      ```
      [*HUAWEI-acl4-advance-3007] rule 1 permit udp source 12.12.12.12 0 destination 225.0.0.3 0 destination-port eq 10002
      ```
      ```
      [*HUAWEI-acl4-advance-3007] commit
      ```
      ```
      [~HUAWEI-acl4-advance-3007] quit
      ```
      ```
      [~HUAWEI] acl number 3008
      ```
      ```
      [*HUAWEI-acl4-advance-3008] rule 1 permit udp source 12.12.12.12 0 destination 225.0.0.4 0 destination-port eq 10003
      ```
      ```
      [*HUAWEI-acl4-advance-3008] commit
      ```
      ```
      [~HUAWEI-acl4-advance-3008] quit
      ```
   4. Configure level-2 traffic classifiers.
      
      
      ```
      [~HUAWEI] traffic classifier rule_ip1
      ```
      ```
      [*HUAWEI-classifier-rule_ip1] if-match acl 3001
      ```
      ```
      [*HUAWEI-classifier-rule_ip1] commit
      ```
      ```
      [~HUAWEI-classifier-rule_ip1] quit
      ```
      ```
      [~HUAWEI] traffic classifier rule_ip2
      ```
      ```
      [*HUAWEI-classifier-rule_ip2] if-match acl 3002
      ```
      ```
      [*HUAWEI-classifier-rule_ip2] commit
      ```
      ```
      [~HUAWEI-classifier-rule_ip2] quit
      ```
      ```
      [~HUAWEI] traffic classifier rule_ip3
      ```
      ```
      [*HUAWEI-classifier-rule_ip3] if-match acl 3003
      ```
      ```
      [*HUAWEI-classifier-rule_ip3] commit
      ```
      ```
      [~HUAWEI-classifier-rule_ip3] quit
      ```
      ```
      [~HUAWEI] traffic classifier rule_ip4
      ```
      ```
      [*HUAWEI-classifier-rule_ip4] if-match acl 3004
      ```
      ```
      [*HUAWEI-classifier-rule_ip4] commit
      ```
      ```
      [~HUAWEI-classifier-rule_ip4] quit
      ```
      ```
      [~HUAWEI] traffic classifier rule_ip5
      ```
      ```
      [*HUAWEI-classifier-rule_ip5] if-match acl 3005
      ```
      ```
      [*HUAWEI-classifier-rule_ip5] commit
      ```
      ```
      [~HUAWEI-classifier-rule_ip5] quit
      ```
      ```
      [~HUAWEI] traffic classifier rule_ip6
      ```
      ```
      [*HUAWEI-classifier-rule_ip6] if-match acl 3006
      ```
      ```
      [*HUAWEI-classifier-rule_ip6] commit
      ```
      ```
      [~HUAWEI-classifier-rule_ip6] quit
      ```
      ```
      [~HUAWEI] traffic classifier rule_ip7
      ```
      ```
      [*HUAWEI-classifier-rule_ip7] if-match acl 3007
      ```
      ```
      [*HUAWEI-classifier-rule_ip7] commit
      ```
      ```
      [~HUAWEI-classifier-rule_ip7] quit
      ```
      ```
      [~HUAWEI] traffic classifier rule_ip8
      ```
      ```
      [*HUAWEI-classifier-rule_ip8] if-match acl 3008
      ```
      ```
      [*HUAWEI-classifier-rule_ip8] commit
      ```
      ```
      [~HUAWEI-classifier-rule_ip8] quit
      ```
   5. Configure level-2 traffic behaviors and bind them to the multicast NAT instances.
      
      
      ```
      [~HUAWEI] traffic behavior rule_ip1
      ```
      ```
      [*HUAWEI-behavior-rule_ip1] multicast-nat bind instance id 1 name streamin1
      ```
      ```
      [*HUAWEI-behavior-rule_ip1] commit
      ```
      ```
      [~HUAWEI-behavior-rule_ip1] quit
      ```
      ```
      [~HUAWEI] traffic behavior rule_ip2
      ```
      ```
      [*HUAWEI-behavior-rule_ip2] multicast-nat bind instance id 2 name streamin2
      ```
      ```
      [*HUAWEI-behavior-rule_ip2] commit
      ```
      ```
      [~HUAWEI-behavior-rule_ip2] quit
      ```
      ```
      [~HUAWEI] traffic behavior rule_ip3
      ```
      ```
      [*HUAWEI-behavior-rule_ip3] multicast-nat bind instance id 3 name streamin3
      ```
      ```
      [*HUAWEI-behavior-rule_ip3] commit
      ```
      ```
      [~HUAWEI-behavior-rule_ip3] quit
      ```
      ```
      [~HUAWEI] traffic behavior rule_ip4
      ```
      ```
      [*HUAWEI-behavior-rule_ip4] multicast-nat bind instance id 4 name streamin4
      ```
      ```
      [*HUAWEI-behavior-rule_ip4] commit
      ```
      ```
      [~HUAWEI-behavior-rule_ip4] quit
      ```
      ```
      [~HUAWEI] traffic behavior rule_ip5
      ```
      ```
      [*HUAWEI-behavior-rule_ip5] multicast-nat bind instance id 5 name streamin5
      ```
      ```
      [*HUAWEI-behavior-rule_ip5] commit
      ```
      ```
      [~HUAWEI-behavior-rule_ip5] quit
      ```
      ```
      [~HUAWEI] traffic behavior rule_ip6
      ```
      ```
      [*HUAWEI-behavior-rule_ip6] multicast-nat bind instance id 6 name streamin6
      ```
      ```
      [*HUAWEI-behavior-rule_ip6] commit
      ```
      ```
      [~HUAWEI-behavior-rule_ip6] quit
      ```
      ```
      [~HUAWEI] traffic behavior rule_ip7
      ```
      ```
      [*HUAWEI-behavior-rule_ip7] multicast-nat bind instance id 7 name streamin7
      ```
      ```
      [*HUAWEI-behavior-rule_ip7] commit
      ```
      ```
      [~HUAWEI-behavior-rule_ip7] quit
      ```
      ```
      [~HUAWEI] traffic behavior rule_ip8
      ```
      ```
      [*HUAWEI-behavior-rule_ip8] multicast-nat bind instance id 8 name streamin8
      ```
      ```
      [*HUAWEI-behavior-rule_ip8] commit
      ```
      ```
      [~HUAWEI-behavior-rule_ip8] quit
      ```
   6. Configure level-2 traffic policies.
      
      
      ```
      [~HUAWEI] traffic policy match1_ip_list1
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list1] classifier rule_ip1 behavior rule_ip1 
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list1] classifier rule_ip2 behavior rule_ip2 
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list1] classifier rule_ip3 behavior rule_ip3 
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list1] classifier rule_ip4 behavior rule_ip4 
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list1] commit
      ```
      ```
      [~HUAWEI-trafficpolicy-match1_ip_list1] quit
      ```
      ```
      [~HUAWEI] traffic policy match1_ip_list2
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list2] classifier rule_ip5 behavior rule_ip5
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list2] classifier rule_ip6 behavior rule_ip6
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list2] classifier rule_ip7 behavior rule_ip7
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list2] classifier rule_ip8 behavior rule_ip8
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list2] commit
      ```
      ```
      [~HUAWEI-trafficpolicy-match1_ip_list2] quit
      ```
   7. Configure level-1 traffic behaviors and associate them with the level-2 traffic policies.
      
      
      ```
      [~HUAWEI] traffic behavior rule_mac1
      ```
      ```
      [*HUAWEI-behavior-rule_mac1] traffic-policy match1_ip_list1 ip-layer
      ```
      ```
      [*HUAWEI-behavior-rule_mac1] commit
      ```
      ```
      [~HUAWEI-behavior-rule_mac1] quit
      ```
      ```
      [~HUAWEI] traffic behavior rule_mac2
      ```
      ```
      [*HUAWEI-behavior-rule_mac2] traffic-policy match1_ip_list2 ip-layer
      ```
      ```
      [*HUAWEI-behavior-rule_mac2] commit
      ```
      ```
      [~HUAWEI-behavior-rule_mac2] quit
      ```
   8. Configure level-1 traffic policies.
      
      
      ```
      [~HUAWEI] traffic policy match1_mac_list
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_mac_list] classifier rule_mac1 behavior rule_mac1
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_mac_list] commit
      ```
      ```
      [~HUAWEI-trafficpolicy-match1_mac_list] quit
      ```
      ```
      [~HUAWEI] traffic policy match2_mac_list2
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_mac_list] classifier rule_mac2 behavior rule_mac2
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_mac_list] commit
      ```
      ```
      [~HUAWEI-trafficpolicy-match1_mac_list] quit
      ```
5. Apply the level-1 traffic policies on the inbound interfaces of multicast streams.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet0/1/0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] traffic-policy match1_mac_list inbound link-layer
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] multicast-nat inbound enable
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] quit
   ```
   ```
   [~HUAWEI] interface GigabitEthernet0/1/1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] traffic-policy match2_mac_list2 inbound link-layer
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] multicast-nat inbound enable
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] quit
   ```
6. Enable multicast stream translation on an outbound interface and configure multicast stream translation parameters.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet0/1/2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] multicast-nat outbound id 1 name out1_1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] multicast-nat outbound id 2 name out1_2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] multicast-nat outbound id 3 name out1_3
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] multicast-nat outbound id 4 name out1_4
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2] quit
   ```
7. Configure a multicast NAT outbound group and add the specified output multicast streams to the multicast NAT outbound group.
   
   
   ```
   [~HUAWEI] multicast-nat outbound-group id 1 name streamoutgroup1
   ```
   ```
   [*HUAWEI-multicast-nat-outbound-group-1] assign outbound id 1 part 1
   ```
   ```
   [*HUAWEI-multicast-nat-outbound-group-1] assign outbound id 2 part 2
   ```
   ```
   [*HUAWEI-multicast-nat-outbound-group-1] assign outbound id 3 part 3
   ```
   ```
   [*HUAWEI-multicast-nat-outbound-group-1] assign outbound id 4 part 4
   ```
   ```
   [*HUAWEI-multicast-nat-outbound-group-1t] commit
   ```
   ```
   [~HUAWEI-multicast-nat-outbound-group-1] quit
   ```
8. Bind the multicast NAT outbound group to the multicast NAT instance group.
   
   
   ```
   [~HUAWEI] multicast-nat bind-list
   ```
   ```
   [~HUAWEI-multicast-nat-bind-list] multicast-nat outbound-group id 1 name streamoutgroup1 bind instance-group id 1 name streamingroup1
   ```
   ```
   [*HUAWEI-multicast-nat-bind-list] commit
   ```
   ```
   [~HUAWEI-multicast-nat-bind-list] quit
   ```
9. Configure clean switching to switch output multicast group 1 to output multicast group 2.
   
   
   ```
   [~HUAWEI] multicast-nat bind-list
   ```
   ```
   [~HUAWEI-multicast-nat-bind-list] multicast-nat outbound-group id 1 name streamoutgroup1 bind instance-group id 2 name streamingroup2 switch-mode clean-switch
   ```
   ```
   [*HUAWEI-multicast-nat-bind-list] commit
   ```
   ```
   [~HUAWEI-multicast-nat-bind-list] quit
   ```

#### Configuration Files

```
#
sysname HUAWEI
#
multicast-nat enable
#
multicast-nat instance id 1 name streamin1
multicast-nat instance id 2 name streamin2
multicast-nat instance id 3 name streamin3
multicast-nat instance id 4 name streamin4
multicast-nat instance id 5 name streamin5
multicast-nat instance id 6 name streamin6
multicast-nat instance id 7 name streamin7
multicast-nat instance id 8 name streamin8
#
multicast-nat bind-list
 multicast-nat outbound-group id 1 name streamoutgroup1 bind instance-group id 2 name streamingroup2 switch-mode clean-switch
#
multicast-nat instance-group id 1 name streamingroup1
 assign instance id 1 part 1
 assign instance id 2 part 2
 assign instance id 3 part 3
 assign instance id 4 part 4
#
multicast-nat instance-group id 2 name streamingroup2
 assign instance id 5 part 1
 assign instance id 6 part 2
 assign instance id 7 part 3
 assign instance id 8 part 4
#
multicast-nat outbound-group id 1 name streamoutgroup1
 assign outbound id 1 part 1
 assign outbound id 2 part 2
 assign outbound id 3 part 3
 assign outbound id 4 part 4
#
diffserv domain default
#
diffserv domain 5p3d
#
acl number 3001
 rule 1 permit udp source 10.10.10.10 0 destination 225.0.0.1 0 destination-port eq 10000
acl number 3002
 rule 1 permit udp source 10.10.10.10 0 destination 225.0.0.2 0 destination-port eq 10001
acl number 3003
 rule 1 permit udp source 10.10.10.10 0 destination 225.0.0.3 0 destination-port eq 10002
acl number 3004
 rule 1 permit udp source 10.10.10.10 0 destination 225.0.0.4 0 destination-port eq 10003
acl number 3005
 rule 1 permit udp source 12.12.12.12 0 destination 225.0.0.1 0 destination-port eq 10000
acl number 3006
 rule 1 permit udp source 12.12.12.12 0 destination 225.0.0.2 0 destination-port eq 10001
acl number 3007
 rule 1 permit udp source 12.12.12.12 0 destination 225.0.0.3 0 destination-port eq 10002
acl number 3008
 rule 1 permit udp source 12.12.12.12 0 destination 225.0.0.4 0 destination-port eq 10003
#
acl number 4001
 rule 1 permit source-mac 00e0-fc12-3456
acl number 4002
 rule 1 permit source-mac 00e0-fc22-3456
#
traffic classifier rule_ip1 operator or
 if-match acl 3001
traffic classifier rule_ip2 operator or
 if-match acl 3002
traffic classifier rule_ip3 operator or
 if-match acl 3003
traffic classifier rule_ip4 operator or
 if-match acl 3004
traffic classifier rule_ip5 operator or
 if-match acl 3005
traffic classifier rule_ip6 operator or
 if-match acl 3006
traffic classifier rule_ip7 operator or
 if-match acl 3007
traffic classifier rule_ip8 operator or
 if-match acl 3008
#
traffic classifier rule_mac1 operator or
 if-match acl 4001
traffic classifier rule_mac2 operator or
 if-match acl 4002
#
traffic behavior rule_ip1
 multicast-nat bind instance id 1 name streamin1
traffic behavior rule_ip2
 multicast-nat bind instance id 2 name streamin2
traffic behavior rule_ip3
 multicast-nat bind instance id 3 name streamin3
traffic behavior rule_ip4
 multicast-nat bind instance id 4 name streamin4
traffic behavior rule_ip5
 multicast-nat bind instance id 5 name streamin5
traffic behavior rule_ip6
 multicast-nat bind instance id 6 name streamin6
traffic behavior rule_ip7
 multicast-nat bind instance id 7 name streamin7
traffic behavior rule_ip8
 multicast-nat bind instance id 8 name streamin8
#
traffic behavior rule_mac1
 traffic-policy match1_ip_list1 ip-layer
traffic behavior rule_mac2
 traffic-policy match1_ip_list2 ip-layer
#
traffic policy match1_ip_list1
 share-mode
 classifier rule_ip1 behavior rule_ip1 precedence 1
 classifier rule_ip2 behavior rule_ip2 precedence 2
 classifier rule_ip3 behavior rule_ip3 precedence 3
 classifier rule_ip4 behavior rule_ip4 precedence 4
traffic policy match1_ip_list2
 share-mode
 classifier rule_ip5 behavior rule_ip5 precedence 1
 classifier rule_ip6 behavior rule_ip6 precedence 2
 classifier rule_ip7 behavior rule_ip7 precedence 3
 classifier rule_ip8 behavior rule_ip8 precedence 4
#
traffic policy match1_mac_list
 share-mode
 classifier rule_mac1 behavior rule_mac1 precedence 1
 classifier rule_mac2 behavior rule_mac2 precedence 2
#
traffic policy match2_mac_list2
 share-mode
 classifier rule_mac2 behavior rule_mac2 precedence 2
#
interface GigabitEthernet0/1/0
 undo negotiation auto
 undo shutdown
 multicast-nat inbound enable
 traffic-policy match1_mac_list inbound link-layer
#
interface GigabitEthernet0/1/1
 undo negotiation auto
 undo shutdown
 multicast-nat inbound enable
 traffic-policy match2_mac_list2 inbound link-layer
#
interface GigabitEthernet0/1/2
 undo shutdown
 multicast-nat outbound id 1 name out1_1
 multicast-nat outbound id 2 name out1_2
 multicast-nat outbound id 3 name out1_3
 multicast-nat outbound id 4 name out1_4
#
return
```