Example for Configuring MQC-based Traffic Statistics Collection
===============================================================

Example for Configuring MQC-based Traffic Statistics Collection

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512688846__fig_dc_cfg_qos_006301), Host1 sends packets with the 802.1p value of 6 to DeviceA. Statistics on service packets need to be collected to properly allocate bandwidth resources.

**Figure 1** Network diagram of traffic statistics collection![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001564128069.png)

#### Procedure

1. Set the host name of the device to DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   ```
2. Configure an ACL rule.
   
   
   
   # On DeviceA, create Layer 2 ACL 4000 to match packets with the 802.1p value of 6.
   
   ```
   [~DeviceA] acl 4000
   [*DeviceA-acl-L2-4000] rule permit 8021p 6
   [*DeviceA-acl-L2-4000] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure a traffic classifier.
   
   
   
   # On DeviceA, create traffic classifier **c1** and match ACL 4000.
   
   ```
   [~DeviceA] traffic classifier c1
   [*DeviceA-classifier-c1] if-match acl 4000
   [*DeviceA-classifier-c1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
4. Configure a traffic behavior.
   
   
   
   # On DeviceA, create traffic behavior **b1** and define the traffic statistics collection action in the traffic behavior.
   
   ```
   [~DeviceA] traffic behavior b1
   [*DeviceA-behavior-b1] statistics enable
   [*DeviceA-behavior-b1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
5. Configure a traffic policy and apply it to the interface.
   
   
   
   # On DeviceA, create traffic policy **p1**, in which traffic classifier **c1** is associated with traffic behavior **b1**.
   
   ```
   [~DeviceA] traffic policy p1
   [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
   [*DeviceA-trafficpolicy-p1] quit
   ```
   
   # Apply traffic policy **p1** to the inbound direction of 100GE 1/0/1.
   
   ```
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] traffic-policy p1 inbound
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] quit
   ```

#### Verifying the Configuration

# Check the ACL configuration.

```
<DeviceA> display acl 4000
L2 ACL 4000, 1 rule
ACL's step is 5
 rule 5 permit 8021p 6 (0 times matched)
```

# Check the traffic classifier configuration.

```
<DeviceA> display traffic classifier c1
  Traffic Classifier Information:
    Classifier: c1
      Type: OR
      Rule(s):
        if-match acl 4000

```

# Check the traffic policy configuration.

```
<DeviceA> display traffic policy p1
  Traffic Policy Information:
    Policy: p1
      Classifier: c1
        Type: OR
      Behavior: b1
        Statistics: enable

```

# Check traffic statistics.

```
<DeviceA> display traffic-policy statistics interface 100ge 1/0/1 inbound
Traffic policy: p1, inbound                                                                                                         
--------------------------------------------------------------------------------
 Slot: 1                                                                        
 Item                  Packets                Bytes           pps           bps 
 -------------------------------------------------------------------------------
 Matched                212185             22067448          1600       1379215 
  Passed                212185             22067448          1600       1379215 
  Dropped                    0                    0             0             0 
   Filter                    0                    0             0             0 
   CAR                       0                    0             0             0 
 -------------------------------------------------------------------------------
```

You can view the statistics on service packets on 100GE 1/0/1.


#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
acl number 4000
 rule 5 permit 8021p 6 
#
traffic classifier c1 type or
 if-match acl 4000
#
traffic behavior b1
 statistics enable
#
traffic policy p1
 classifier c1 behavior b1 precedence 5 
#
interface 100GE1/0/1
 traffic-policy p1 inbound
#
return
```