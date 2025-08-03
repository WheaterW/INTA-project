Example for Configuring MQC-based Local Flow Mirroring (1:1)
============================================================

Example for Configuring MQC-based Local Flow Mirroring (1:1)

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001512687190__fig19616105322214), the R&D and marketing departments of an enterprise use the 192.168.1.0/24 and 192.168.2.0/24 network segments respectively to communicate with each other through DeviceA. The Server acting as a monitoring device is directly connected to DeviceA. The traffic sent from the R&D department to the marketing department needs to be monitored by the Server.

**Figure 1** Example for configuring MQC-based local flow mirroring![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1, 2, and 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001512846798.png)

#### Procedure

1. Configure 100GE1/0/2 on DeviceA as an observing port.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] observe-port 1 interface 100ge 1/0/2
   [*DeviceA] commit
   ```
2. On DeviceA, create traffic classifier **c1** and configure a rule to match packets with the source address 192.168.1.0/24 and destination address 192.168.2.0/24.
   
   
   ```
   [~DeviceA] acl number 3000
   [*DeviceA-acl4-advance-3000] rule permit ip source 192.168.1.0 24 destination 192.168.2.0 24
   [*DeviceA-acl4-advance-3000] quit
   [*DeviceA] traffic classifier c1
   [*DeviceA-classifier-c1] if-match acl 3000
   [*DeviceA-classifier-c1] quit
   [*DeviceA] commit
   ```
3. On DeviceA, create traffic behavior **b1** and configure the flow mirroring action.
   
   
   ```
   [~DeviceA] traffic behavior b1
   [*DeviceA-behavior-b1] mirroring observe-port 1
   [*DeviceA-behavior-b1] quit
   [*DeviceA] commit
   ```
4. On DeviceA, create traffic policy **p1** and bind the traffic classifier and traffic behavior to the traffic policy. Apply the traffic policy to the inbound direction of 100GE1/0/1 to monitor the packets sent from the R&D department to the marketing department.
   
   
   ```
   [~DeviceA] traffic policy p1
   [*DeviceA-trafficpolicy-p1] classifier c1 behavior b1
   [*DeviceA-trafficpolicy-p1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] traffic-policy p1 inbound
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the traffic classifier configuration.

```
[~DeviceA] display traffic classifier c1
  Traffic Classifier Information:
    Classifier: c1
      Type: OR
      Rule(s):
        if-match acl 3000
```

# Check the traffic policy configuration.

```
[~DeviceA] display traffic policy p1
  Traffic Policy Information:
    Policy: p1
      Classifier: c1
        Type: OR
      Behavior: b1
        Mirroring observe-port 1
```

# Check the mirroring configuration.

```
[~DeviceA] display port-mirroring
  Traffic mirroring:
  -----------------------------------------------------------------------------
  TrafficBehavior                        ObservePort : Interface
  -----------------------------------------------------------------------------
  b1                                               1 : 100GE1/0/2
  -----------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
observe-port 1 interface 100GE1/0/2
#
acl number 3000
 rule 5 permit ip source 192.168.1.0 0.0.0.255 destination 192.168.2.0 0.0.0.255
# 
traffic classifier c1 type or
 if-match acl 3000
#
traffic behavior b1
 mirroring observe-port 1
#
traffic policy p1
 classifier c1 behavior b1 precedence 5
#
interface 100GE1/0/1
 traffic-policy p1 inbound
#
return
```