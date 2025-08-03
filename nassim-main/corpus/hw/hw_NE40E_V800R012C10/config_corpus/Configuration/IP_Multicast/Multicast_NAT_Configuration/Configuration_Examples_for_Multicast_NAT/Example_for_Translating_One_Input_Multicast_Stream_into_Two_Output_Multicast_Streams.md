Example for Translating One Input Multicast Stream into Two Output Multicast Streams
====================================================================================

This section provides an example for translating one input multicast stream into two output streams, and a level-2 traffic policy is used to describe the configuration procedure.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367792__fig_dc_ne_cfg_multicastnat_000001), after passing through the router, input multicast stream 1 is translated into output multicast streams 1 and 2. The characteristics of output multicast stream 1 remain the same as those of input multicast stream 1, and those of output multicast stream 2 are translated.

The following table describes the requirements for translating input multicast stream 1.

**Table 1** Characteristics of input and output multicast streams
| Characteristics of Multicast Streams | Input Multicast Stream 1 | Output Multicast Stream 1 | Output Multicast Stream 2 |
| --- | --- | --- | --- |
| Source MAC address | 00e0-fc00-0001 | 00e0-fc00-0001 | 00e0-fc00-0002  NOTE:  By default, the post-translation MAC address is the MAC address of an outbound interface, for example, 00e0-fc00-0002. |
| Source IP address | 10.10.10.10 | 10.10.10.10 | 12.12.12.12 |
| Destination IP address | 239.0.0.1 | 239.0.0.1 | 239.1.0.2 |
| UDP destination port number | 10000 | 10000 | 10002 |



**Figure 1** Multicast stream translation![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, interface2, and interface3 in this example represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.


  
![](figure/en-us_image_0260760026.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable multicast NAT globally.
2. Create a multicast NAT instance.
3. Configure traffic policies.
4. Apply the level-1 traffic policy on the inbound interface of multicast streams.
5. Configure multicast NAT on the outbound interfaces of multicast streams.
6. Bind the output multicast streams to the multicast NAT instance

#### Data Preparation

To complete the configuration, you need the following data:

* Name of a multicast NAT instance: stream1
* Name of an ACL required for a level-1 traffic classifier: 4001
* Name of a level-1 traffic classifier: rule\_mac1
* Name of a level-1 traffic behavior: rule\_mac1
* Name of a level-1 traffic policy: match1\_mac\_list
* Name of an ACL required for a level-2 traffic classifier: 3001
* Name of a level-2 traffic classifier: rule\_ip1
* Name of a level-2 traffic behavior: rule\_ip1
* Name of a level-2 traffic policy: match1\_ip\_list1


#### Procedure

1. Enable multicast NAT on the device.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] multicast-nat enable
   ```
2. Create a multicast NAT instance named **stream1** on the device.
   
   
   ```
   [~HUAWEI] multicast-nat instance id 1 name stream1
   ```
   ```
   [*HUAWEI-multicast-nat-instance-1] commit
   ```
   ```
   [~HUAWEI-multicast-nat-instance-1] quit
   ```
3. Configure two-level traffic policies for implementing multicast NAT on the device.
   1. Configure a level-1 traffic classification rule for matching the MAC address of input multicast stream 1.
      
      
      ```
      [~HUAWEI] acl number 4001
      ```
      ```
      [*HUAWEI-acl-L2-4001] rule 1 permit source-mac 00e0-fc00-0001
      ```
      ```
      [*HUAWEI-acl-L2-4001] commit
      ```
      ```
      [~HUAWEI-acl-L2-4001] quit
      ```
   2. Configure a level-1 traffic classifier.
      
      
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
   3. Configure a level-2 traffic classification rule for matching the source IP address, destination IP address, and UDP port number of input multicast stream 1.
      
      
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
   4. Configure a level-2 traffic classifier.
      
      
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
   5. Configure a level-2 traffic behavior and bind it to the multicast NAT instance.
      
      
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
   6. Configure a level-2 traffic policy.
      
      
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
   7. Configure a level-1 traffic behavior and associate it with the level-2 traffic policy.
      
      
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
   8. Configure a level-1 traffic policy.
      
      
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
4. Apply the level-1 traffic policy on the inbound interface of multicast streams.
   
   
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
5. Configure characteristics for output multicast streams.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet0/1/1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] multicast-nat outbound id 1 name out1_1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] quit
   ```
   ```
   [~HUAWEI] interface GigabitEthernet0/1/2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] multicast-nat outbound id 2 name out1_2 src-mac auto-translate src-ip 12.12.12.12 dst-ip 239.1.0.2 dst-udp-port 10002
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2] quit
   ```
6. Bind the output multicast streams to the multicast NAT instance
   
   
   ```
   [~HUAWEI] multicast-nat bind-list
   ```
   ```
   [~HUAWEI-multicast-nat-bind-list] multicast-nat outbound id 1 name out1_1 bind instance id 1 name stream1
   ```
   ```
   [*HUAWEI-multicast-nat-bind-list] multicast-nat outbound id 2 name out1_2 bind instance id 1 name stream1
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
#
multicast-nat bind-list
 multicast-nat outbound id 1 name out1_1 bind instance id 1 name stream1
 multicast-nat outbound id 2 name out1_2 bind instance id 1 name stream1
#
diffserv domain default
#
diffserv domain 5p3d
#
acl number 3001
 rule 1 permit udp source 10.10.10.10 0 destination 239.0.0.1 0 destination-port eq 10000
#
acl number 4001
 rule 1 permit source-mac 00e0-fc00-0001
#
traffic classifier rule_ip1 operator or
 if-match acl 3001
#
traffic classifier rule_mac1 operator or
 if-match acl 4001
#
traffic behavior rule_ip1
 multicast-nat bind instance id 1 name stream1
#
traffic behavior rule_mac1
 traffic-policy match1_ip_list1 ip-layer
#
traffic policy match1_ip_list1
 share-mode
 classifier rule_ip1 behavior rule_ip1 precedence 1
#
traffic policy match1_mac_list
 share-mode
 classifier rule_mac1 behavior rule_mac1 precedence 1
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
 undo shutdown 
 multicast-nat outbound id 1 name out1_1
#
interface GigabitEthernet0/1/2
 undo shutdown
 multicast-nat outbound id 2 name out1_2 src-mac auto-translate src-ip 12.12.12.12 dst-ip 239.1.0.2 dst-udp-port 10002
#
return
```