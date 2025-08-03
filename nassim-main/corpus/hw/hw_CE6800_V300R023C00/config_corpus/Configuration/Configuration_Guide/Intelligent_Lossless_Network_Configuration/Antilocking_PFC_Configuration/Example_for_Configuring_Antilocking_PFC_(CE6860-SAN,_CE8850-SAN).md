Example for Configuring Antilocking PFC (CE6860-SAN, CE8850-SAN)
================================================================

Example for Configuring Antilocking PFC (CE6860-SAN, CE8850-SAN)

#### Networking Requirements

In the following figure, a lossless service is deployed on data center servers in a DCI scenario. The physical distance between DeviceA and DeviceB (ingress devices for DCI) is 90 km (a relatively long distance), which may cause packet loss in the lossless service. To provide sufficient buffer space for queues that carry the lossless service and make full use of the buffer space, you can set the plane buffer optimization mode to enhanced long-distance mode, enable distance-based headroom buffer check, and enable antilocking PFC on DeviceA and DeviceB.

**Figure 1** Network diagram of antilocking PFC in a DCI scenario![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001564125381.png)

#### Procedure

1. Configure the long-distance plane buffer optimization function.
   
   
   
   # Set the plane buffer optimization mode to enhanced long-distance mode on DeviceA. The configuration takes effect after DeviceA is restarted. The configurations on DeviceB are similar to those on DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] ai-service
   [*DeviceA-ai-service] buffer optimization mode enhanced-long-distance
   [*DeviceA-ai-service] quit
   [*DeviceA] commit
   [~DeviceA] quit
   <DeviceA> reboot 
   The system will reboot. Continue? [Y/N]:Y
   ```
2. Configure the distance-based headroom buffer check function.
   
   
   
   # Configure DeviceA. Because the distance between DeviceA and DeviceB is 90 km, set the long-distance mode of the interface on DeviceA to **level-100** and enable the distance-based headroom buffer check function.
   
   ```
   <DeviceA> system-view
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] long-distance mode level-100
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB. Specifically, set the long-distance mode of the interface on DeviceB to **level-100** and enable the distance-based headroom buffer check function.
   
   ```
   <DeviceB> system-view
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] long-distance mode level-100
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # When the distance-based headroom buffer check function is enabled on DeviceA but not enabled on DeviceB, the detection fails. In this case, you need to trigger the interface on DeviceA to send a detection packet.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] start long-distance detect
   [~DeviceA-100GE1/0/1] quit
   ```
3. Configure antilocking PFC.
   
   
   
   # In this example, queue 3 is used to carry the lossless service, so enable antilocking PFC for queue 3 on the interface of DeviceA. The configurations on DeviceB are similar to those on DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] dcb abs-pfc queue 3 enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display the configuration and status of antilocking PFC on DeviceA.

```
[~DeviceA] display abs-pfc status interface 100ge 1/0/1
Current buffer optimization mode: Enhanced-long-distance
-----------------------------------------------------------------------------------------------
Interface         Queue         Status         RTT(us)        Threshold(KB)         Speed(Gbps)
-----------------------------------------------------------------------------------------------
100GE1/0/1            3         Enable             397                    0                 100
-----------------------------------------------------------------------------------------------
```

# Display the statistics about antilocking PFC on DeviceA.

```
[~DeviceA] display abs-pfc interface 100ge 1/0/1 
-----------------------------------------------------------------------------------------
Interface         Queue         Received(Frames)        ReceivedRate(pps)     DeadlockNum
                             Transmitted(Frames)     TransmittedRate(pps)     RecoveryNum
-----------------------------------------------------------------------------------------
100GE1/0/1            3                118789880                    43517               0
                                               0                        0               0
-----------------------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
interface 100GE1/0/1
 long-distance mode level-100
 dcb abs-pfc queue 3 enable threshold 0
#
ai-service
 #
 buffer optimization mode enhanced-long-distance
#
return
```

DeviceB

```
#
sysname DeviceA
#
interface 100GE1/0/1
 long-distance mode level-100
 dcb abs-pfc queue 3 enable threshold 0
#
ai-service
 #
 buffer optimization mode enhanced-long-distance
#
return
```