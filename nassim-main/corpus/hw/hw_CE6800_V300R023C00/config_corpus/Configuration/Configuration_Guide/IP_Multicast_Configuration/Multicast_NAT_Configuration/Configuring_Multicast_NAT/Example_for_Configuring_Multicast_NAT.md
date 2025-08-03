Example for Configuring Multicast NAT
=====================================

Example for Configuring Multicast NAT

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001193989747__fig_dc_vrp_multicast_cfg_007301), after passing through the Device, the input multicast stream is converted into output multicast streams 1 and 2. For output multicast stream 1, only the source MAC address is translated; for output multicast stream 2, all multicast stream characteristics are translated.

The following table describes the translation requirements for the input multicast streams.

**Table 1** Characteristics of input and output multicast streams
| Multicast Stream Characteristics | Input Multicast Stream | Output Multicast Stream 1 | Output Multicast Stream 2 |
| --- | --- | --- | --- |
| Source MAC address | 00e0-fc00-0001 | 00e0-fc00-0002  NOTE:  By default, the post-translation MAC address (00e0-fc00-0002 in this example) is the MAC address of an outbound interface (interface2 in this example). | 00e0-fc00-0003  NOTE:  By default, the post-translation MAC address (00e0-fc00-0003 in this example) is the MAC address of an outbound interface (interface3 in this example). |
| Source IP address | 10.10.1.1 | 10.10.1.1 | 10.10.2.2 |
| Destination IP address | 239.0.0.1 | 239.0.0.1 | 239.1.0.2 |
| Destination UDP port | 10000 | 10000 | 10002 |



**Figure 1** Multicast stream translation networking![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001382515782.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable multicast NAT globally.
2. Create a multicast NAT instance.
3. Configure a traffic policy.
4. Apply the traffic policy on the inbound interface of multicast streams.
5. Configure multicast NAT on the outbound interfaces of multicast streams.
6. Bind output multicast streams to the multicast instance.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of a multicast NAT instance: stream
* Name of an ACL required for a traffic classifier: 3001
* Name of an ACL required for a traffic classifier: 4001
* Name of a traffic classifier: rule
* Name of a traffic behavior: rule
* Name of a traffic policy: match\_list


#### Procedure

1. Enable multicast NAT on the device.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device
   [*HUAWEI] commit
   [~Device] multicast-nat enable
   [*Device] commit
   ```
2. Create a multicast NAT instance named **stream** on the device.
   
   
   ```
   [~Device] multicast-nat instance id 1 name stream
   [*Device-multicast-nat-instance-1] commit
   [~Device-multicast-nat-instance-1] quit
   ```
3. Configure a traffic policy for implementing multicast NAT on the device.
   
   
   
   # Configure an advanced ACL 4001 on the Device to match the MAC addresses of input multicast streams.
   
   ```
   [~Device] acl number 4001
   [*Device-acl-L2-4001] rule 1 permit source-mac 00e0-fc00-0001
   [*Device-acl-L2-4001] commit
   [~Device-acl-L2-4001] quit
   ```
   
   # Configure an advanced ACL 3001 on the Device to match the source IP address, destination IP address, and UDP port number of input multicast streams.
   
   ```
   [~Device] acl number 3001
   [*Device-acl-advance-3001] rule 1 permit udp source 10.10.1.1 0 destination 239.0.0.1 0 destination-port eq 10000
   [*Device-acl-advance-3001] commit
   [~Device-acl-advance-3001] quit
   ```
   
   # Configure a traffic classifier on the Device.
   
   ```
   [~Device] traffic classifier rule type and
   [*Device-classifier-rule] if-match acl 3001
   [*Device-classifier-rule] if-match acl 4001
   [*Device-classifier-rule] commit
   [~Device-classifier-rule] quit
   ```
   
   # Configure a traffic behavior on the Device.
   
   ```
   [~Device] traffic behavior rule
   [*Device-behavior-rule] multicast-nat bind instance id 1 name stream
   [*Device-behavior-rule] commit
   [~Device-behavior-rule] quit
   ```
   
   # Configure a traffic policy on the Device and bind the traffic classifier and traffic behavior in the traffic policy.
   
   ```
   [~Device] traffic policy match_list
   [*Device-trafficpolicy-match_list] classifier rule behavior rule
   [*Device-trafficpolicy-match_list] commit
   [~Device-trafficpolicy-match_list] quit
   ```
4. Apply the traffic policy on the inbound interface of multicast streams.
   
   
   ```
   [~Device] interface 100ge 1/0/1
   [*Device-100GE1/0/1] undo portswitch
   [*Device-100GE1/0/1] traffic-policy match_list inbound
   [*Device-100GE1/0/1] multicast-nat inbound enable
   [*Device-100GE1/0/1] commit
   [~Device-100GE1/0/1] quit
   ```
5. Configure characteristics for output multicast streams.
   
   
   ```
   [~Device] interface 100ge 1/0/2
   [*Device-100GE1/0/2] undo portswitch
   [*Device-100GE1/0/2] multicast-nat outbound id 1 name out1_1
   [*Device-100GE1/0/2] commit
   [~Device-100GE1/0/2] quit
   [~Device] interface 100ge 1/0/3
   [*Device-100GE1/0/3] undo portswitch
   [*Device-100GE1/0/3] multicast-nat outbound id 2 name out1_2 src-ip 10.10.2.2 dst-ip 239.1.0.2 dst-udp-port 10002
   [*Device-100GE1/0/3] commit
   [~Device-100GE1/0/3] quit
   ```
6. Bind output multicast streams to the multicast instance.
   
   
   ```
   [~Device] multicast-nat bind-list
   [*Device-multicast-nat-bind-list] multicast-nat outbound id 1 name out1_1 bind instance id 1 name stream
   [*Device-multicast-nat-bind-list] multicast-nat outbound id 2 name out1_2 bind instance id 1 name stream
   [*Device-multicast-nat-bind-list] commit
   [~Device-multicast-nat-bind-list] quit
   ```

#### Configuration Scripts

* Device
  
  ```
  #
  sysname Device
  #
  multicast-nat enable
  #
  multicast-nat instance id 1 name stream
  #
  acl number 3001
   rule 1 permit udp source 10.10.1.1 0 destination 239.0.0.1 0 destination-port eq 10000
  #
  acl number 4001
   rule 1 permit source-mac 00e0-fc00-0001
  #
  traffic classifier rule type and
   if-match acl 3001
   if-match acl 4001
   if-match source-mac 00e0-fc00-0001 
  #
  traffic behavior rule
   multicast-nat bind instance id 1 name stream
  #
  traffic policy match_list
   classifier rule behavior rule
  #
  interface 100GE1/0/1
   undo portswitch
   multicast-nat inbound enable
   traffic-policy match_list inbound 
  #
  interface 100GE1/0/2
   undo portswitch
   multicast-nat outbound id 1 name out1_1
  #
  interface 100GE1/0/3
   undo portswitch
   multicast-nat outbound id 2 name out1_2 src-ip 10.10.2.2 dst-ip 239.1.0.2 dst-udp-port 10002
  #
  multicast-nat bind-list
   multicast-nat outbound id 1 name out1_1 bind instance id 1 name stream
   multicast-nat outbound id 2 name out1_2 bind instance id 1 name stream
  #
  return
  ```