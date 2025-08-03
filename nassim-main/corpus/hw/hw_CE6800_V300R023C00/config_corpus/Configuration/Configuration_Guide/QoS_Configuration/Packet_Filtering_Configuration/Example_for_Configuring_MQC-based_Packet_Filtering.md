Example for Configuring MQC-based Packet Filtering
==================================================

Example for Configuring MQC-based Packet Filtering

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512833270__fig_dc_cfg_qos_036101), Host1, Host2, and Host3 communicate with each other through DeviceA. For specific reasons, Host1 is allowed to receive traffic from Host2 through DeviceA but is not allowed to receive traffic from Host3.

**Figure 1** Network diagram of packet filtering![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001563872793.png)

#### Procedure

1. Configure an ACL rule.
   
   
   
   # On DeviceA, create ACL 3001 to match the traffic with source IP address 192.168.3.1 and destination IP address 192.168.1.1 (traffic from Host3 to Host1).
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] acl 3001
   [*DeviceA-acl4-advance-3001] rule permit ip source 192.168.3.1 0 destination 192.168.1.1 0
   [*DeviceA-acl4-advance-3001] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Configure a traffic classifier.
   
   
   
   # On DeviceA, create traffic classifier **c1** and reference ACL 3001 in the traffic classifier.
   
   ```
   [~DeviceA] traffic classifier c1
   [*DeviceA-classifier-c1] if-match acl 3001
   [*DeviceA-classifier-c1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure a traffic behavior.
   
   
   
   # On DeviceA, create traffic behavior **b1** and define the deny action in the traffic behavior.
   
   ```
   [~DeviceA] traffic behavior b1
   [*DeviceA-behavior-b1] deny
   [*DeviceA-behavior-b1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
4. Configure a traffic policy and apply it to the outbound direction of 100GE 1/0/1.
   
   
   
   # On DeviceA, create a traffic policy **p1** and bind a traffic classifier to a traffic behavior in the traffic policy.
   
   ```
   [~DeviceA] traffic policy p1
   [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
   [*DeviceA-trafficpolicy-p1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Apply traffic policy **p1** to the outbound direction of 100GE 1/0/1.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] traffic-policy p1 outbound
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

# Check the ACL configuration.

```
<DeviceA> display acl 3001
Advanced ACL 3001, 1 rule                                                                                                           
ACL's step is 5                                                                                                                     
 rule 5 permit ip source 192.168.3.0 0 destination 192.168.1.0 0
 (0 times matched)                                 
```

# Check the traffic classifier configuration.

```
<DeviceA> display traffic classifier c1
  Traffic Classifier Information:
    Classifier: c1
      Type: OR
      Rule(s):
        if-match acl 3001
```

# Check the traffic policy configuration.

```
<DeviceA> display traffic policy p1
  Traffic Policy Information:
    Policy: p1
      Classifier: c1
        Type: OR
      Behavior: b1
        Deny
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
acl number 3001
 rule 5 permit ip source 192.168.3.0 0.0.0.255 destination 192.168.1.0 0.0.0.255
# 
traffic classifier c1 type or
 if-match acl 3001
#
traffic behavior b1
 deny
#
traffic policy p1
 classifier c1 behavior b1 precedence 5 
#
interface 100GE1/0/1
 traffic-policy p1 outbound
#
return
```