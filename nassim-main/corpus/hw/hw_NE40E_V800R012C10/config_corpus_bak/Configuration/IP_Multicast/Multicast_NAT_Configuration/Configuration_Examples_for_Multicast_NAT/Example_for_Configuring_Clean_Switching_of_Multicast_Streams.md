Example for Configuring Clean Switching of Multicast Streams
============================================================

This section provides an example for configuring clean switching for two input multicast streams.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367794__fig167874358200), multicast streams 1 and 2 are input from sources 1 and 2 to the router, respectively. The router outputs only multicast stream 1, and the characteristics of multicast stream 1 remain unchanged. If clean switching is required, the controller delivers a clean switching instruction to the router so that the router outputs multicast stream 2 rather than stream 1. The characteristics of multicast stream 2 remain unchanged.

After clean switching is configured, input multicast stream 1 is translated according to the following table.

**Table 1** Characteristics of input and output multicast streams
| Multicast Stream Characteristics | Input Multicast Stream 1 | Input Multicast Stream 2 | Output Multicast Stream 1 | Output Multicast Stream 2 |
| --- | --- | --- | --- | --- |
| Source MAC address | 00e0-fc12-3456 | 00e0-fc22-3456 | 00e0-fc12-3456 | 00e0-fc22-3456 |
| Source IP address | 10.10.10.10 | 12.12.12.12 | 10.10.10.10 | 12.12.12.12 |
| Destination IP address | 239.0.0.1 | 239.1.0.2 | 239.0.0.1 | 239.1.0.2 |
| Destination UDP port number | 10000 | 10002 | 10000 | 10002 |




#### Configuration Roadmap

**Figure 1** Multicast stream translation![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, and interface3 in this example represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.


  
![](figure/en-us_image_0000001197141496.png "Click to enlarge")

The configuration roadmap is as follows:

1. Enable multicast NAT globally.
2. Create multicast NAT instances.
3. Configure traffic policies.
4. Apply the level-1 traffic policies on the inbound interfaces of multicast streams.
5. Configure multicast NAT on the outbound interface of multicast streams.
6. Bind output multicast streams to multicast NAT instances.
7. Configure clean switching of multicast streams.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast NAT instance names: stream1 and stream2
* ACL names required for level-1 traffic classifiers: 4001 and 4002
* Level-1 traffic classifier names: rule\_mac1 and rule\_mac2
* Level-1 traffic behavior names: rule\_mac1 and rule\_mac2
* Level-1 traffic policy names: match1\_mac\_list and match2\_mac\_list
* ACL names required for level-2 traffic classifiers: 3001 and 3002
* Level-2 traffic classifier names: rule\_ip1 and rule\_ip2
* Level-2 traffic behavior names: rule\_ip1 and rule\_ip2
* Level-2 traffic policy names: match1\_ip\_list1 and match1\_ip\_list2


#### Procedure

1. Enable multicast NAT on the device.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] multicast-nat enable
   ```
2. Create multicast NAT instances named stream1 and stream2 on the device.
   
   
   ```
   [~HUAWEI] multicast-nat instance id 1 name stream1
   ```
   ```
   [*HUAWEI] multicast-nat instance id 2 name stream2
   ```
   ```
   [*HUAWEI-multicast-nat-instance-1] commit
   ```
   ```
   [~HUAWEI-multicast-nat-instance-1] quit
   ```
3. Configure two-level traffic policies for implementing multicast NAT on the device.
   1. Configure level-1 traffic classification rules for matching the MAC addresses of input multicast streams 1 and 2.
      
      
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
   3. Configure level-2 traffic classification rules for matching the source IP addresses, destination IP addresses, and UDP port numbers of input multicast streams 1 and 2.
      
      
      ```
      [~HUAWEI] acl number 3001
      ```
      ```
      [*HUAWEI-acl4-advance-3001] rule 1 permit udp source 10.10.10.10 0 destination 239.0.0.1 0 destination-port eq 10000
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
      [*HUAWEI-acl4-advance-3002] rule 1 permit udp source 12.12.12.12 0 destination 239.1.0.2 0 destination-port eq 10002
      ```
      ```
      [*HUAWEI-acl4-advance-3002] commit
      ```
      ```
      [~HUAWEI-acl4-advance-3002] quit
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
   5. Configure level-2 traffic behaviors and bind them to the multicast NAT instances.
      
      
      ```
      [~HUAWEI] traffic behavior rule_ip1
      ```
      ```
      [*HUAWEI-behavior-rule_ip1] multicast-nat bind instance id 1 name stream1
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
      [*HUAWEI-behavior-rule_ip2] multicast-nat bind instance id 2 name stream2
      ```
      ```
      [*HUAWEI-behavior-rule_ip2] commit
      ```
      ```
      [~HUAWEI-behavior-rule_ip2] quit
      ```
   6. Configure level-2 traffic policies.
      
      
      ```
      [~HUAWEI] traffic policy match1_ip_list1
      ```
      ```
      [*HUAWEI-trafficpolicy-match1_ip_list1] classifier rule_ip1 behavior rule_ip1 
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
      [*HUAWEI-trafficpolicy-match1_ip_list2] classifier rule_ip2 behavior rule_ip2
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
      [~HUAWEI] traffic policy match2_mac_list
      ```
      ```
      [*HUAWEI-trafficpolicy-match2_mac_list] classifier rule_mac2 behavior rule_mac2
      ```
      ```
      [*HUAWEI-trafficpolicy-match2_mac_list] commit
      ```
      ```
      [~HUAWEI-trafficpolicy-match2_mac_list] quit
      ```
4. Apply the level-1 traffic policies on the inbound interfaces of multicast streams.
   
   
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
   [*HUAWEI-GigabitEthernet0/1/1] traffic-policy match2_mac_list inbound link-layer
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
5. Configure characteristics for output multicast streams.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet0/1/2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] multicast-nat outbound id 1 name out1_1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2] quit
   ```
6. Bind an output multicast stream to the multicast instance to output multicast stream 1.
   
   
   ```
   [~HUAWEI] multicast-nat bind-list
   ```
   ```
   [~HUAWEI-multicast-nat-bind-list] multicast-nat outbound id 1 name out1_1 bind instance id 1 name stream1
   ```
   ```
   [*HUAWEI-multicast-nat-bind-list] commit
   ```
   ```
   [~HUAWEI-multicast-nat-bind-list] quit
   ```
7. Configure clean switching to switch output multicast stream 1 to output multicast stream 2.
   
   
   ```
   [~HUAWEI] multicast-nat bind-list
   ```
   ```
   [~HUAWEI-multicast-nat-bind-list] multicast-nat outbound id 1 name out1_1 bind instance id 2 name stream2 switch-mode clean-switch
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
multicast-nat instance id 1 name stream1
multicast-nat instance id 2 name stream2
#
multicast-nat bind-list
 multicast-nat outbound id 1 name out1_1 bind instance id 2 name stream2 switch-mode clean-switch
#
diffserv domain default
#
diffserv domain 5p3d
#
acl number 3001
 rule 1 permit udp source 10.10.10.10 0 destination 239.0.0.1 0 destination-port eq 10000
acl number 3002
 rule 1 permit udp source 12.12.12.12 0 destination 239.1.0.2 0 destination-port eq 10002
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
#
traffic classifier rule_mac1 operator or
 if-match acl 4001
traffic classifier rule_mac2 operator or
 if-match acl 4002
#
traffic behavior rule_ip1
 multicast-nat bind instance id 1 name stream1
traffic behavior rule_ip2
 multicast-nat bind instance id 2 name stream2
#
traffic behavior rule_mac1
 traffic-policy match1_ip_list1 ip-layer
traffic behavior rule_mac2
 traffic-policy match1_ip_list2 ip-layer
#
traffic policy match1_ip_list1
 share-mode
 classifier rule_ip1 behavior rule_ip1 precedence 1
traffic policy match1_ip_list2
 share-mode
 classifier rule_ip2 behavior rule_ip2 precedence 1
#
traffic policy match1_mac_list
 share-mode
 classifier rule_mac1 behavior rule_mac1 precedence 1
traffic policy match2_mac_list
 share-mode
 classifier rule_mac2 behavior rule_mac2 precedence 1
#
license
#
interface GigabitEthernet0/1/0
 undo negotiation auto
 undo shutdown
 traffic-policy match1_mac_list inbound link-layer
 multicast-nat inbound enable
#
interface GigabitEthernet0/1/1
 undo negotiation auto
 undo shutdown
 traffic-policy match2_mac_list inbound link-layer
 multicast-nat inbound enable
#
interface GigabitEthernet0/1/2
 undo shutdown
 multicast-nat outbound id 1 name out1_1
#
return
```