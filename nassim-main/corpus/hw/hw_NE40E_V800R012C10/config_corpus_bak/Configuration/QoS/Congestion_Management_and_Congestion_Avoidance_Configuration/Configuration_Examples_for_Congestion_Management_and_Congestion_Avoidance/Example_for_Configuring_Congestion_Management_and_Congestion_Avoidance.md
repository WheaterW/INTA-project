Example for Configuring Congestion Management and Congestion Avoidance
======================================================================

This section provides an example for configuring congestion management and congestion avoidance in a typical application scenario.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371204__fig_dc_ne_qos_cfg_205201), Server sends mission-critical data, Telephone sends voice data, and PC1 and PC2 send non-mission-critical data to the network through DeviceA. On DeviceA, the rate of the inbound interface interface1 is greater than that of the outbound interface interface2. Therefore, congestion may occur on interface2 and may be intensifying.

In the case of network congestion, the service data from the server and the telephone must be preferentially sent. In addition, the telephone requires 5 Mbit/s bandwidth, and the server requires 4 Mbit/s bandwidth. As PC1 and PC2 are VIP users, bandwidth must be assured for the data that PC1 and PC2 send. The delay must be as low as possible. If congestion intensifies on the network, packets are dropped according to priority.

In this scenario, WRED needs to be configured on DeviceA to work with WFQ for scheduling and discarding.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.


**Figure 1** Networking diagram for configuring congestion management and congestion avoidance  
![](images/fig_dc_ne_qos_cfg_205201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Mark the service priorities of different flows on the inbound interface interface1 of DeviceA.
2. Configure a WRED profile and set the lower drop threshold, upper drop threshold, and drop probability for packets.
3. On the outbound interface interface2 of DeviceA, configure a different scheduling policy for port queues of each CoS and apply a configured WRED object to the scheduling policy.

#### Data Preparation

To complete the configuration, you need the following data:

* ACL numbers, traffic classifier names, traffic behavior names, re-marked service priorities, and traffic policy names
* WRED profile name, lower and upper drop thresholds, drop probability, and packet color in each queue
* Interfaces and port queues to which WRED profiles are applied

#### Procedure

1. Configure ACL rules for packets from Server, Telephone, PC1, and PC2.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] acl number 2001
   ```
   ```
   [*DeviceA-acl4-basic-2001] rule permit source 10.1.1.3 0.0.0.0
   ```
   ```
   [*DeviceA-acl4-basic-2001] commit
   ```
   ```
   [~DeviceA-acl4-basic-2001] quit
   ```
   ```
   [~DeviceA] acl number 2002
   ```
   ```
   [*DeviceA-acl4-basic-2002] rule permit source 10.1.1.2 0.0.0.0
   ```
   ```
   [*DeviceA-acl4-basic-2002] commit
   ```
   ```
   [~DeviceA-acl4-basic-2002] quit
   ```
   ```
   [~DeviceA] acl number 2003
   ```
   ```
   [*DeviceA-acl4-basic-2003] rule permit source 10.1.1.4 0.0.0.0
   ```
   ```
   [*DeviceA-acl4-basic-2003] commit
   ```
   ```
   [~DeviceA-acl4-basic-2003] quit
   ```
   ```
   [~DeviceA] acl number 2004
   ```
   ```
   [*DeviceA-acl4-basic-2004] rule permit source 10.1.1.5 0.0.0.0
   ```
   ```
   [*DeviceA-acl4-basic-2004] commit
   ```
   ```
   [~DeviceA-acl4-basic-2004] return
   ```
2. On DeviceA's GE 0/1/0, configure MF classification and mark the service priority of each flow.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] traffic classifier aa
   ```
   ```
   [*DeviceA-classifier-aa] if-match acl 2001
   ```
   ```
   [*DeviceA-classifier-aa] commit
   ```
   ```
   [~DeviceA-classifier-aa] quit
   ```
   ```
   [~DeviceA] traffic classifier bb
   ```
   ```
   [*DeviceA-classifier-bb] if-match acl 2002
   ```
   ```
   [*DeviceA-classifier-bb] commit
   ```
   ```
   [~DeviceA-classifier-bb] quit
   ```
   ```
   [~DeviceA] traffic classifier cc
   ```
   ```
   [*DeviceA-classifier-cc] if-match acl 2003
   ```
   ```
   [*DeviceA-classifier-cc] commit
   ```
   ```
   [~DeviceA-classifier-cc] quit
   ```
   ```
   [~DeviceA] traffic classifier dd
   ```
   ```
   [*DeviceA-classifier-dd] if-match acl 2004
   ```
   ```
   [*DeviceA-classifier-dd] commit
   ```
   ```
   [~DeviceA-classifier-dd] quit
   ```
   ```
   [~DeviceA] traffic behavior aa
   ```
   ```
   [*DeviceA-behavior-aa] remark ip-precedence 5
   ```
   ```
   [*DeviceA-behavior-aa] car cir 5000
   ```
   ```
   [*DeviceA-behavior-aa] commit
   ```
   ```
   [~DeviceA-behavior-aa] quit
   ```
   ```
   [~DeviceA] traffic behavior bb
   ```
   ```
   [*DeviceA-behavior-bb] remark ip-precedence 4
   ```
   ```
   [*DeviceA-behavior-bb] car cir 4000
   ```
   ```
   [*DeviceA-behavior-bb] commit
   ```
   ```
   [~DeviceA-behavior-bb] quit
   ```
   ```
   [~DeviceA] traffic behavior cc
   ```
   ```
   [*DeviceA-behavior-cc] remark ip-precedence 3
   ```
   ```
   [*DeviceA-behavior-cc] commit
   ```
   ```
   [~DeviceA-behavior-cc] quit
   ```
   ```
   [~DeviceA] traffic behavior dd
   ```
   ```
   [*DeviceA-behavior-dd] remark ip-precedence 2
   ```
   ```
   [*DeviceA-behavior-dd] commit
   ```
   ```
   [~DeviceA-behavior-dd] quit
   ```
   ```
   [~DeviceA] traffic policy ee
   ```
   ```
   [*DeviceA-trafficpolicy-ee] classifier aa behavior aa
   ```
   ```
   [*DeviceA-trafficpolicy-ee] classifier bb behavior bb
   ```
   ```
   [*DeviceA-trafficpolicy-ee] classifier cc behavior cc
   ```
   ```
   [*DeviceA-trafficpolicy-ee] classifier dd behavior dd
   ```
   ```
   [*DeviceA-trafficpolicy-ee] commit
   ```
   ```
   [~DeviceA-trafficpolicy-ee] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] traffic-policy ee inbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] return
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For details about the mapping between the IP precedence and service class, see [Default Mapping Between IP Precedence/MPLS EXP/802.1p and Service Class](feature_0021577558.html#EN-US_CONCEPT_0172356827__qos_fea_img_01) in the *HUAWEI NE40E-M2 series Feature Description - QoS Priority Mapping*.
   
   The priorities of queues with specific service classes are calculated based on scheduling algorithms.
   * If PQ scheduling is configured for all queues with the eight service classes, the priorities of the queues are placed in descending order as follows: CS7 > CS6 > EF > AF4 > AF3 > AF2 > AF1 > BE.
   * If PQ scheduling is configured for the BE queue (not applied in most cases) and WFQ scheduling is configured for the queues with the other service classes, the priority of the BE queue is higher than that of the other queues.
   * If WFQ scheduling is configured for all queues with the eight service classes, all the queues have the same priority.
3. Configure a WRED profile on DeviceA.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] port-wred pw
   ```
   ```
   [*DeviceA-port-wred-pw] color green low-limit 70 high-limit 100 discard-percentage 100
   ```
   ```
   [*DeviceA-port-wred-pw] color yellow low-limit 60 high-limit 90 discard-percentage 100
   ```
   ```
   [*DeviceA-port-wred-pw] color red low-limit 50 high-limit 80 discard-percentage 100
   ```
   ```
   [*DeviceA-port-wred-pw] commit
   ```
   ```
   [~DeviceA-port-wred-pw] quit
   ```
   
   After the preceding configuration is complete, run the **display port-wred configuration verbose** command to check the WRED profile parameters.
   
   ```
   <DeviceA> display port-wred configuration verbose
   ```
   ```
   Port wred name : pw
   ---------------------------------------------------
   Color    Low-limit    High-limit    Discard-percent
   ---------------------------------------------------
   green    70           100           100
   yellow   60           90            100
   red      50           80            100
   Queue Depth : 8000
   Reference relationships : NULL 
   ```
4. On DeviceA's GE 0/2/0, configure port queues and apply the configured WRED object **pw** to the port queues.
   
   
   ```
   [~DeviceA] interface gigabitethernet0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] port-queue ef pq port-wred pw outbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] port-queue af4 wfq weight 15 shaping 100 port-wred pw outbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] port-queue af3 wfq weight 10 shaping 50 port-wred pw outbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] port-queue af2 wfq weight 10 shaping 50 port-wred pw outbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] return
   ```
   
   After the preceding configuration is complete, run the **display port-queue configuration interface** command to check the detailed configuration of port queues.
   
   ```
   <DeviceA> display port-queue configuration interface gigabitethernet 0/2/0 outbound
   ```
   ```
   GigabitEthernet0/2/0 outbound current port-queue configuration:  
    be : arithmetic: wfq                weight: 10         tm weight: 3                       
          fact weight: 10.00             shaping(kbps): NA                                   
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  12800 - 12800                                                            
            yellow(low-high limit) (kbytes)                  12800 - 12800                                                             
            red   (low-high limit) (kbytes)                  12800 - 12800                                                             
          current queue-length     (kbytes)                  12800                                                                     
          cir:123                        cir-percentage:NA
          cir-arithmetic:pq              cir-weight:NA
          pir:123                        pir-percentage:NA
          pir-arithmetic:lpq             pir-weight:NA      
    af1: arithmetic: wfq                weight: 10         tm weight: 3                                                               
          fact weight: 10.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  12800 - 12800                                                             
            yellow(low-high limit) (kbytes)                  12800 - 12800                                                             
            red   (low-high limit) (kbytes)                  12800 - 12800                                                             
          current queue-length     (kbytes)                  12800                                                                     
          cir:NA                         cir-percentage:10
          cir-arithmetic:pq              cir-weight:NA
          pir:NA                         pir-percentage:20
          pir-arithmetic:wfq             pir-weight:15    
    af2: arithmetic: wfq                weight: 10         tm weight: 3                                                               
          fact weight: 10.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  12800 - 12800                                                             
            yellow(low-high limit) (kbytes)                  12800 - 12800                                                             
            red   (low-high limit) (kbytes)                  12800 - 12800                                                             
          current queue-length     (kbytes)                  12800                                                                     
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA 
    af3: arithmetic: wfq                weight: 15         tm weight: 2                                                               
          fact weight: 15.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  12800 - 12800                                                             
            yellow(low-high limit) (kbytes)                  12800 - 12800                                                             
            red   (low-high limit) (kbytes)                  12800 - 12800                                                            
          current queue-length     (kbytes)                  12800                                                                     
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA 
    af4: arithmetic: wfq                weight: 15         tm weight: 2                                                               
          fact weight: 15.00             shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  12800 - 12800                                                             
            yellow(low-high limit) (kbytes)                  12800 - 12800                                                             
            red   (low-high limit) (kbytes)                  12800 - 12800                                                             
          current queue-length     (kbytes)                  12800                                                                     
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA 
    ef : arithmetic: pq                 weight: NA         tm weight: 0                                                               
          fact weight: 0.00              shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  1280 - 1280                                                               
            yellow(low-high limit) (kbytes)                  1280 - 1280                                                               
            red   (low-high limit) (kbytes)                  1280 - 1280                                                               
          current queue-length     (kbytes)                  1280                                                                      
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA 
    cs6: arithmetic: pq                 weight: NA         tm weight: 0                                                               
          fact weight: 0.00              shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  1280 - 1280                                                               
            yellow(low-high limit) (kbytes)                  1280 - 1280                                                               
            red   (low-high limit) (kbytes)                  1280 - 1280                                                               
          current queue-length     (kbytes)                  1280                                                                      
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA 
    cs7: arithmetic: pq                 weight: NA         tm weight: 0                                                               
          fact weight: 0.00              shaping(kbps): NA                                                                             
          port-wred: NA                                                                                                                
            green (low-high limit) (kbytes)                  1280 - 1280                                                               
            yellow(low-high limit) (kbytes)                  1280 - 1280                                                               
            red   (low-high limit) (kbytes)                  1280 - 1280                                                               
          current queue-length     (kbytes)                  1280                                                                      
          cir:NA                         cir-percentage:NA
          cir-arithmetic:NA              cir-weight:NA
          pir:NA                         pir-percentage:NA
          pir-arithmetic:NA              pir-weight:NA
   ```
5. Verify the configuration.
   
   
   
   When the network has traffic, run the [**display port-queue statistics**](cmdqueryname=display+port-queue+statistics) [ **slot** *slot-id* | **interface** { *interface-type* *interface-number* | *interface-name* } ] [ *cos-value* ] **outbound** command on DeviceA. The command output shows that the traffic volumes of various CoSs increase rapidly. With the rapid increase in traffic volumes, the volume of discarded traffic also increases rapidly according to the configured WRED drop parameters.

#### Configuration Files

DeviceA configuration file
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
acl number 2001
```
```
 rule permit source 10.1.1.3 0
```
```
#
```
```
acl number 2002
```
```
 rule permit source 10.1.1.2 0
```
```
#
```
```
acl number 2003
```
```
 rule permit source 10.1.1.4 0
```
```
#
```
```
acl number 2004
```
```
 rule permit source 10.1.1.5 0 
```
```
#
```
```
traffic classifier aa operator or
```
```
 if-match acl 2001
```
```
traffic classifier bb operator or
```
```
 if-match acl 2002
```
```
traffic classifier cc operator or
```
```
 if-match acl 2003
```
```
traffic classifier dd operator or
```
```
 if-match acl 2004
```
```
#
```
```
traffic behavior aa
```
```
 remark ip-precedence 5
```
```
 car cir 5000
```
```
traffic behavior bb
```
```
 car cir 4000
```
```
 remark ip-precedence 4
```
```
traffic behavior cc
```
```
 remark ip-precedence 3
```
```
traffic behavior dd
```
```
 remark ip-precedence 2
```
```
#
```
```
traffic policy ee
```
```
 classifier aa behavior aa
```
```
 classifier bb behavior bb
```
```
 classifier cc behavior cc
```
```
 classifier dd behavior dd
```
```
#
```
```
port-wred pw
```
```
 color green low-limit 70 high-limit 100 discard-percentage 100
```
```
 color yellow low-limit 60 high-limit 90 discard-percentage 100
```
```
 color red low-limit 50 high-limit 80 discard-percentage 100
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
 ip address 10.1.1.1 255.255.255.0
```
```
 traffic-policy ee inbound
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
 ip address 10.10.1.1 255.255.255.0
```
```
 port-queue af2 wfq weight 10 shaping 50 port-wred pw outbound
```
```
 port-queue af3 wfq weight 10 shaping 50 port-wred pw outbound
```
```
 port-queue af4 wfq weight 15 shaping 100 port-wred pw outbound
```
```
 port-queue ef pq port-wred pw outbound
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
  network 10.1.1.0 0.0.0.255
```
```
  network 10.10.1.0 0.0.0.255
```
```
#
```
```
return
```