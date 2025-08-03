Example for Configuring ECN
===========================

Example for Configuring ECN

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513154342__fig_dc_s_cfg_016401), DeviceA forwards traffic between Host1 and Host2. To prevent traffic congestion on the outbound interface of DeviceA, configure ECN on DeviceA. When network congestion occurs on the outbound interface of DeviceA, DeviceA sends an ECN-marked packet to Host2 to notify Host2 of network congestion. After receiving the ECN-marked packet, Host2 sends a CNP packet to Host1 to instruct Host1 to reduce the traffic rate.

**Figure 1** Network diagram of ECN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001563874341.png)

#### Procedure

1. Configure VLANs for interfaces so that devices can communicate with each other at the link layer.
   
   
   
   # Add 100GE 1/0/1 and 100GE 1/0/2 of DeviceA to VLAN 100.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 100
   [*DeviceA-vlan100] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 100
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 100
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
2. Create a WRED drop profile **dp1**, and set the lower drop threshold to 50%, upper drop threshold to 80%, and maximum drop probability to 30%.
   
   
   ```
   [~DeviceA] drop-profile dp1
   [*DeviceA-drop-dp1] ecn low-limit 50 high-limit 80 discard-percentage 30
   [*DeviceA-drop-dp1] quit
   [*DeviceA] commit
   ```
3. Apply the WRED drop profile to the outbound interface 100GE 1/0/2 of DeviceA and enable ECN for queue 3.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] qos queue 3 wred dp1
   [*DeviceA-100GE1/0/2] qos queue 3 ecn
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display the ECN threshold configured on the outbound interface 100GE 1/0/2 of DeviceA.

```
<DeviceA> display qos ecn threshold interface 100ge 1/0/2
* : indicates AI ECN                                                       
[]: indicates the upper ECN threshold                                           
Interface       Queue     Min     Max  Probability  Queue Size                  
                         (KB)    (KB)          (%)        (KB)                  
--------------------------------------------------------------                  
100GE1/0/2          0       0       0            0           0                  
                    1       0       0            0           0                  
                    2       0       0            0           0                  
                    3    3584    5734           30           0                  
                    4       0       0            0           0                  
                    5       0       0            0           0                  
              
```

#### Configuration Scripts

DeviceB

```
#
sysname DeviceA
#
drop-profile dp1
 ecn low-limit 50 high-limit 80 discard-percentage 30
#
vlan 100
#
interface 100GE1/0/1
 port default vlan 100
#
interface 100GE1/0/2
 port default vlan 100
 qos queue 3 wred dp1
 qos queue 3 ecn
#
return
```