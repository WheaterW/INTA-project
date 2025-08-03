Example for Configuring ECN Overlay
===================================

Example for Configuring ECN Overlay

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513170018__fig19978171395514), the hybrid overlay is deployed on a VXLAN network, and a VXLAN tunnel is established between DeviceA and the vSwitch of Server2, enabling Server1 and Server2 to communicate with each other. Queue 3 is configured to carry services with heavy traffic, and static ECN needs to be deployed for this queue to prevent congestion. Because the network is a VXLAN network, you also need to configure the ECN Overlay function on all devices to apply the ECN function.

**Figure 1** Network diagram of ECN Overlay![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001512690890.png "Click to enlarge")

#### Procedure

1. Configure the static ECN function.
   
   
   
   # Configure the static ECN function for queue 3 on DeviceA, and set the lower drop threshold to 30, upper drop threshold to 50, and maximum drop probability to 20. (These values are presented in the form of percentage.) The configurations of DeviceB and DeviceC are similar to that of DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] drop-profile dp1
   [*DeviceA-drop-dp1] ecn low-limit 30 high-limit 50 discard-percentage 20
   [*DeviceA-drop-dp1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] qos queue 3 wred dp1
   [*DeviceA-100GE1/0/1] qos queue 3 ecn
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] qos queue 3 wred dp1
   [*DeviceA-100GE1/0/2] qos queue 3 ecn
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
2. Configure the ECN Overlay function.
   
   
   
   # Configure the ECN Overlay function on DeviceA to ensure the inner ECN mark of VXLAN packets is the same as the outer ECN mark. The configurations of DeviceB and DeviceC are similar to that of DeviceA.
   
   ```
   [~DeviceA] assign forward nvo3 egress mark-ecn enable
   [*DeviceA] assign forward nvo3 transit mark inner-ecn enable
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the ECN thresholds on DeviceA.

```
[~DeviceA] display qos ecn threshold interface 100ge 1/0/1                                         
* : indicates AI ECN                                           
[]: indicates the upper ECN threshold                          
Interface       Queue     Min     Max  Probability  Queue Size 
                         (KB)    (KB)          (%)        (KB) 
-------------------------------------------------------------- 
100GE1/0/1          0       0       0            0           0 
                    1       0       0            0           0 
                    2       0       0            0           0 
                    3    2150    3584           20           0 
                    4       0       0            0           0 
                    5       0       0            0           0 
```
# Check whether the ECN Overlay function is enabled on DeviceA.
```
[~DeviceA] display nvo3 ecn configuration
---------------------------------------------------------------------------------------
 Slot                   Mark inner ECN                      Copy outer ECN
---------------------------------------------------------------------------------------
  1                         Enable                              Enable
---------------------------------------------------------------------------------------

```


#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
drop-profile dp1
 ecn low-limit 30 high-limit 50 discard-percentage 20
# 
assign forward nvo3 egress mark-ecn enable 
assign forward nvo3 transit mark inner-ecn enable
#
interface 100GE1/0/1
 qos queue 3 wred dp1
 qos queue 3 ecn
#
interface 100GE1/0/2
 qos queue 3 wred dp1
 qos queue 3 ecn
#
return

```

DeviceB

```
#
sysname DeviceB
#
drop-profile dp1
 ecn low-limit 30 high-limit 50 discard-percentage 20
# 
assign forward nvo3 egress mark-ecn enable 
assign forward nvo3 transit mark inner-ecn enable
#
interface 100GE1/0/1
 qos queue 3 wred dp1
 qos queue 3 ecn
#
interface 100GE1/0/2
 qos queue 3 wred dp1
 qos queue 3 ecn
#
return

```

DeviceC

```
#
sysname DeviceC
#
drop-profile dp1
 ecn low-limit 30 high-limit 50 discard-percentage 20
# 
assign forward nvo3 egress mark-ecn enable 
assign forward nvo3 transit mark inner-ecn enable
#
interface 100GE1/0/1
 qos queue 3 wred dp1
 qos queue 3 ecn
#
interface 100GE1/0/2
 qos queue 3 wred dp1
 qos queue 3 ecn
#
return

```