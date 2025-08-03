Example for Configuring IP-based MF Classification on an MPLS Interface
=======================================================================

This section provides an example for configuring IP-based MF classification on an MPLS interface.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371297__fig_dc_ne_qos_cfg_006901), PE1, the P, and PE2 are routers on the MPLS backbone network, and CE1, CE2, CE3, and CE4 are access routers on the edge of the backbone network. Use PE1 as an example. You can configure IP-based MF classification on the public network interface (Interface3) of PE1 to implement traffic control on the public network side and verify the packet sending and receiving through traffic statistics.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1, Interface2, and Interface3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/1/3, respectively.


**Figure 1** Configuring IP-based MF classification on an MPLS interface  
![](images/fig_dc_ne_qos_cfg_007401.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic MPLS functions.
2. Configure MF classification based on IP layer information for incoming/outgoing packets on the public network.
3. Configure ACL rules.
4. Configure a traffic classifier.
5. Configure a traffic behavior.
6. Configure a traffic policy.
7. Apply the traffic policy.

#### Data Preparation

To complete the configuration, you need the following data:

* ACL number
* Names of the traffic classifier, traffic behavior, and traffic policy, and number of the interface to which the traffic policy is applied

#### Procedure

1. Configure basic MPLS functions. The configuration details are not mentioned here.
   
   
   
   For details about how to configure basic MPLS functions, see [Example for Configuring BGP/MPLS IP VPN](../vrp/dc_vrp_mpls-l3vpn-v4_cfg_0102.html) in *HUAWEI NE40E-M2 series* *Configuration Guide - VPN - BGP/MPLS IP VPN Configuration*.
2. Configure MF classification based on IP layer information for incoming/outgoing packets on the public network.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] slot 1
   ```
   ```
   [~PE1-slot-1] traffic-policy match-ip-layer mpls-pop
   ```
   ```
   [*PE1-slot-1] traffic-policy match-ip-layer mpls-push
   ```
   ```
   [*PE1-slot-1] commit
   ```
   ```
   [~PE1-slot-1] quit
   ```
3. Configure ACL rules.
   
   
   ```
   [~PE1] acl number 3333
   ```
   ```
   [*PE1-acl-advance-3333] rule 5 permit ip source 11.11.11.11 0 destination 33.33.33.33 0
   ```
   ```
   [*PE1-acl-advance-3333] rule 10 permit ip source 33.33.33.33 0 destination 11.11.11.11 0
   ```
   ```
   [*PE1-acl-advance-3333] commit
   ```
   ```
   [~PE1-acl-advance-3333] quit
   ```
4. Configure a traffic classifier.
   
   
   ```
   [~PE1] traffic classifier c1
   ```
   ```
   [*PE1-classifier-c1] if-match acl 3333
   ```
   ```
   [*PE1-classifier-c1] commit
   ```
   ```
   [~PE1-classifier-c1] quit
   ```
5. Configure a traffic behavior.
   
   
   ```
   [~PE1] traffic behavior b1
   ```
   ```
   [*PE1-behavior-b1] permit
   ```
   ```
   [*PE1-behavior-b1] commit
   ```
   ```
   [~PE1-behavior-b1] quit
   ```
6. Configure a traffic policy.
   
   
   ```
   [~PE1] traffic policy p1
   ```
   ```
   [*PE1-trafficpolicy-p1] classifier c1 behavior b1
   ```
   ```
   [*PE1-trafficpolicy-p1] share-mode
   ```
   ```
   [*PE1-trafficpolicy-p1] statistic enable
   ```
   ```
   [*PE1-trafficpolicy-p1] commit
   ```
   ```
   [~PE1-trafficpolicy-p1] quit
   ```
7. Apply the traffic policy.
   
   
   ```
   [~PE1] interface gigabitethernet 0/1/3
   ```
   ```
   [~PE1-GigabitEthernet0/1/3] traffic-policy p1 inbound
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] traffic-policy p1 outbound
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/3] quit
   ```
8. Verify the configuration.
   
   
   
   After completing the configuration, run the [**ping 33.33.33.33**](cmdqueryname=ping+33.33.33.33) command on CE1 to ping CE3, and run the [**display traffic policy statistics**](cmdqueryname=display+traffic+policy+statistics) command on PE1 to view statistics about traffic exchanged between CE3 and CE1.
   
   ```
   [~PE1] display traffic policy statistics interface gigabitethernet 0/1/3 inbound
   ```
   ```
   Info: The statistics is shared because the policy is shared.
   Interface: GigabitEthernet0/1/3
   Traffic policy inbound: p1
   Traffic policy applied at 2017-08-30 18:30:20 
   Statistics enabled at 2017-08-30 18:30:20
   Statistics last cleared: Never
   Rule number: 1 IPv4, 0 IPv6 
   Current status: OK!
   Item                             Packets                      Bytes
   -------------------------------------------------------------------
   Matched                                5                       500
     +--Passed                            4                       400
     +--Dropped                           1                       100
   Missed                                 0                         0 
   Last 30 seconds rate
   Item                                 pps                        bps
   -------------------------------------------------------------------
   Matched                                5                       500
     +--Passed                            4                       400
     +--Dropped                           1                       100
   Missed                                 0                         0
   ```

#### Configuration Files

PE1 configuration file

```
#
sysname PE1
#
slot 1 
 traffic-policy match-ip-layer mpls-pop mpls-push

#
acl number 3333
 rule 5 permit ip source 11.11.11.11 0 destination 33.33.33.33 0
 rule 10 permit ip source 33.33.33.33 0 destination 11.11.11.11 0
#
traffic classifier c1 operator or
 if-match acl 3333
#
traffic behavior b1
#        
traffic policy p1
 share-mode
 statistic enable
 classifier c1 behavior b1 precedence 1
#
interface GigabitEthernet0/1/3
 undo shutdown
 traffic-policy p1 inbound
 traffic-policy p1 outbound
# 
return
```