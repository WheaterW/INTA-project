Example for Configuring a UCL-based Traffic Policy
==================================================

This section provides an example for configuring a UCL-based traffic policy for BA classification.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001232714856__fig_dc_ne_cfg_01280001), user access is provided through the DSLAM in PPPoE mode. Device is required to mark the priorities of users and distinguish them as gold or silver users. It must also guarantee bandwidth and limit the rate of user-to-network traffic based on the priorities.

**Figure 1** Networking diagram of a UCL-based traffic policy  
![](figure/en-us_image_0000001276994801.png "Click to enlarge")  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the BRAS service function for users to go online.
2. Configure a user group.
3. Configure a UCL rule.
4. Configure a traffic classifier, traffic behavior, and traffic policy.
5. Apply the UCL-based traffic policy.
6. Specify the domain to which users belong.

#### Data Preparation

To complete the configuration, you need the following data:

* User group name
* UCL number
* Traffic classifier, traffic behavior, and traffic policy names
* CIR: 15 Mbit/s; CBS: 300000 bytes; PIR: 20 Mbit/s; PBS: 500000 bytes
* Name of the domain to which users belong

#### Procedure

1. Configure the BRAS service function on Device for users to go online.
   
   
   
   For detailed configurations, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - User Access*.
2. Configure a user group.
   
   
   ```
   <~HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*Device] commit
   ```
   ```
   [~Device] user-group group1
   ```
   ```
   [*Device] commit
   ```
3. Configure a UCL rule.
   
   
   ```
   [~Device] acl 6001
   ```
   ```
   [*Device-acl-ucl-6001] rule 1 permit ip source user-group group1 destination any
   ```
   ```
   [*Device-acl-ucl-6001] commit
   ```
   ```
   [*Device-acl-ucl-6001] quit
   ```
4. Configure a traffic classifier and define an ACL-based matching rule.
   
   
   ```
   [~Device] traffic classifier c1  
   ```
   ```
   [*Device-classifier-c1] if-match acl 6001 
   ```
   ```
   [*Device-classifier-c1] commit
   ```
   ```
   [*Device-classifier-c1] quit
   ```
5. Configure a traffic behavior.
   
   
   ```
   [~Device] traffic behavior b1 
   ```
   ```
   [*Device-behavior-b1] car cir 15000 pir 20000 cbs 300000 pbs 500000    
   ```
   ```
   [*Device-behavior-b1] commit
   ```
   ```
   [*Device-behavior-b1] quit
   ```
6. Define a traffic policy to associate the traffic classifier with the traffic behavior.
   
   
   ```
   [~Device] traffic policy p1
   ```
   ```
   [*Device-trafficpolicy-p1] classifier c1 behavior b1
   ```
   ```
   [*Device-trafficpolicy-p1] statistics enable
   ```
   ```
   [*Device-trafficpolicy-p1]commit
   ```
   ```
   [*Device-trafficpolicy-p1] quit
   ```
7. Apply the UCL-based traffic policy. In VS mode, the [**traffic-policy**](cmdqueryname=traffic-policy) command is supported only by the admin VS.
   
   
   ```
   [~Device] traffic-policy p1 inbound 
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the UCL-based traffic policy is applied in the system view, the traffic of all online users is classified based on the corresponding UCL rule.
8. Specify the domain to which users belong.
   
   
   ```
   [~Device] aaa
   ```
   ```
   [*Device-aaa] domain isp1 
   ```
   ```
   [*Device-aaa-domain-isp1] user-group group1 
   ```
   ```
   [*Device-aaa-domain-isp1] commit
   ```
   ```
   [*Device-aaa-domain-isp1] quit
   ```
9. Verify the configuration.
   
   After completing the preceding configuration, run the **display traffic policy** command to check information about the configured traffic policy, traffic classifier, and traffic behavior.
   ```
   <Device> display traffic policy user-defined p1
   User Defined Traffic Policy Information:
       Policy: p1
         Total: 5120  Used: 2  Free: 5118
         Description: 
         Step: 1
         Statistic Enable
         Share-mode
         Classifier: c1 Precedence: 1
           Behavior: b1
           Committed Access Rate:
             CIR 15000 (Kbps), PIR 20000 (Kbps), CBS 300000 (byte), PBS 500000 (byte), ADJUST 0
               Conform Action: pass  Yellow Action: pass  Exceed Action: discard  Color-aware: no
   
         Classifier: default-class Precedence: 65535
           Behavior: be
           -none-
   
   ```
   
   Run the **display traffic policy statistics ucl** [ **slot** *slot-id* ] { **inbound** | **outbound** } command to check statistics about the UCL-based traffic policy. In VS mode, this command is supported only by the admin VS.
   ```
   <Device> display traffic policy statistics ucl slot 1 inbound
   ```
   ```
   Traffic policy inbound: p1
   
   Slot: 1
   Traffic policy applied at 2022-10-19 10:15:57
   Statistics enabled at 2022-10-18 19:17:37
   Statistics last cleared: Never
   Rule number: 2 IPv4, 0 IPv6
   Current status: OK!
   Item                             Packets                      Bytes
   -------------------------------------------------------------------
   Matched                       20,935,529              2,009,808,208
     +--Passed                      543,363                 52,178,560
     +--Dropped                  20,392,166              1,957,629,648 
   Missed                                 0                          0
   
   Last 30 seconds rate
   Item                                 pps                        bps
   -------------------------------------------------------------------
   Matched                        1,007,607                773,842,816  
     +--Passed                       26,326                 20,225,840
     +--Dropped                     981,281                753,616,976
   Missed                                 0                          0
   ```

#### Configuration Files

Device configuration file
```
# 
sysname Device
```
```
#
```
```
radius-server group rd1
```
```
 radius-server authentication 192.168.7.249 1645 weight 0
```
```
 radius-server accounting 192.168.7.249 1646 weight 0
```
```
 radius-server shared-key-cipher %^%#clY:%[]x='-RMNJus[s/VJ:3YBq3&lt;..|.{'xgbp+%^%
```
```
 radius-server type plus11
```
```
 radius-server traffic-unit kbyte
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
interface GigabitEthernet0/2/0
```
```
 undo shutdown
```
```
#
```
```
interface GigabitEthernet0/2/0.1
```
```
 pppoe-server bind Virtual-Template 1
```
```
 user-vlan 1
```
```
 bas
```
```
  access-type layer2-subscriber default-domain authentication isp1
```
```
  authentication-method ppp
```
```
#
```
```
ip pool pool1 bas local
```
```
 gateway 192.168.0.1 255.255.255.0
```
```
 section 0 192.168.0.2 192.168.0.200
```
```
 dns-server  192.168.7.252
```
```
#
```
```
acl number 6001
 rule 1 permit ip source user-group group1
#
traffic classifier c1 operator or
 if-match acl 6001
#
traffic behavior b1
 car cir 15000 pir 20000 cbs 300000 pbs 500000 green pass yellow pass red discard
#
traffic policy p1
 share-mode
 statistics enable
 classifier c1 behavior b1
#
traffic-policy p1 inbound
#  
user-group group1
#
aaa
 authentication-scheme auth1
 accounting-scheme acct1
#
domain isp1
 authentication-scheme auth1
 accounting-scheme acct1
 radius-server group rd1
 ip-pool pool1
 user-group group1
#
 return
```