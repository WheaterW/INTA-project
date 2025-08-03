Example for Configuring MF Classification for IP Packets
========================================================

This section provides an example for configuring MF classification for IP packets.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371294__fig_dc_ne_qos_cfg_006901), MF classification is configured on DeviceC to implement access control between DeviceA and DeviceB. In addition, traffic statistics can be collected to verify packet sending and receiving.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 and Interface2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


**Figure 1** Configuring a traffic policy based on MF classification  
![](images/fig_dc_ne_qos_cfg_007301.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure ACL rules.
2. Configure a traffic classifier.
3. Configure a traffic behavior.
4. Configure a traffic policy.
5. Apply the traffic policy.

#### Data Preparation

To complete the configuration, you need the following data:

* ACL number
* Names of the traffic classifier, traffic behavior, and traffic policy, and number of the interface to which the traffic policy is applied

#### Procedure

1. Configure ACL rules.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceC] acl number 3333
   ```
   ```
   [*DeviceC-acl-advance-3333] rule 5 permit ip source 1.1.1.1 0 destination 2.2.2.2 0
   ```
   ```
   [*DeviceC-acl-advance-3333] rule 10 permit ip source 2.2.2.2 0 destination 1.1.1.1 0
   ```
   ```
   [*DeviceC-acl-advance-3333] commit
   ```
   ```
   [~DeviceC-acl-advance-3333] quit
   ```
2. Configure a traffic classifier.
   
   
   ```
   [~DeviceC] traffic classifier c1
   ```
   ```
   [*DeviceC-classifier-c1] if-match acl 3333
   ```
   ```
   [*DeviceC-classifier-c1] commit
   ```
   ```
   [~DeviceC-classifier-c1] quit
   ```
3. Configure a traffic behavior.
   
   
   ```
   [~DeviceC] traffic behavior b1
   ```
   ```
   [*DeviceC-behavior-b1] permit
   ```
   ```
   [*DeviceC-behavior-b1] commit
   ```
   ```
   [~DeviceC-behavior-b1] quit
   ```
4. Configure a traffic policy.
   
   
   ```
   [~DeviceC] traffic policy p1
   ```
   ```
   [*DeviceC-trafficpolicy-p1] classifier c1 behavior b1
   ```
   ```
   [*DeviceC-trafficpolicy-p1] share-mode
   ```
   ```
   [*DeviceC-trafficpolicy-p1] statistics enable
   ```
   ```
   [*DeviceC-trafficpolicy-p1] commit
   ```
   ```
   [~DeviceC-trafficpolicy-p1] quit
   ```
5. Apply the traffic policy.
   
   
   ```
   [~DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] traffic-policy p1 inbound
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] traffic-policy p1 outbound
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] quit
   ```
   
   
   ```
   [~DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] traffic-policy p1 inbound
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] traffic-policy p1 outbound
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
6. Verify the configuration.
   
   
   
   After completing the configuration, run the [**ping 2.2.2.2**](cmdqueryname=ping+2.2.2.2) command on DeviceA to ping DeviceB, and run the [**display traffic policy statistics**](cmdqueryname=display+traffic+policy+statistics) command on DeviceC to check statistics about traffic exchanged between DeviceA and DeviceB.
   
   ```
   [~DeviceC] display traffic policy statistics interface gigabitethernet 0/1/0 inbound
   ```
   ```
   Info: The statistics is shared because the policy is shared.
   Interface: GigabitEthernet0/1/0 
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

DeviceC configuration file

```
#
sysname DeviceC
#
acl number 3333
 rule 5 permit ip source 1.1.1.1 0 destination 2.2.2.2 0
 rule 10 permit ip source 2.2.2.2 0 destination 1.1.1.1 0
#
traffic classifier c1 operator or
 if-match acl 3333
#
traffic behavior b1 
#        
traffic policy p1
 share-mode
 statistics enable
 classifier c1 behavior b1 precedence 1
#
interface GigabitEthernet0/1/0
 undo shutdown
 traffic-policy p1 inbound
 traffic-policy p1 outbound
#
interface GigabitEthernet0/2/0
 undo shutdown
 traffic-policy p1 inbound
 traffic-policy p1 outbound
# 
return
```