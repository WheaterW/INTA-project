Example for Configuring the Buffer Optimization Function
========================================================

Example for Configuring the Buffer Optimization Function

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513160398__fig19978171395514), a lossless service is deployed on both Host1 and Host2. The physical distance between DeviceA and DeviceB is 90 km (a relatively long distance), which may cause packet loss in the lossless service. To ensure sufficient buffer space for queues carrying the lossless service, you can configure long-distance plane buffer optimization and distance-based headroom buffer check on DeviceA and DeviceB.

**Figure 1** Network diagram of the buffer optimization function![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001563880409.png)

#### Precautions

The parameter settings in this example are for reference only. You need to configure each device based on the traffic model on your network.

Only the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM support the plane buffer optimization function.


#### Procedure

1. Configure PFC.
   
   
   
   # In this example, queue 4 carries the lossless service as planned, so enable PFC for queue 4 on the interface of DeviceA. The configurations on DeviceB are similar to those on DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
   [*DeviceA] dcb pfc
   [*DeviceA-dcb-pfc-default] priority 4
   [*DeviceA-dcb-pfc-default] quit
   [*DeviceA] port-group all_using   
   [*DeviceA-port-group-all_using] group-member 100ge 1/0/1 to 100ge 1/0/2
   [*DeviceA-port-group-all_using] dcb pfc enable mode manual
   [*DeviceA-port-group-all_using] quit
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After PFC is configured, queue 4 is a lossless queue and requires the headroom buffer. For details about other PFC configurations, see [PFC](galaxy_dcb_cfg_0004.html).
2. Configure the long-distance plane buffer optimization function.
   
   
   
   # Set the plane buffer optimization mode to long-distance mode on DeviceA. The configuration takes effect after DeviceA is restarted. The configurations on DeviceB are similar to those on DeviceA.
   
   ```
   [~DeviceA] ai-service
   [*DeviceA-ai-service] buffer optimization mode long-distance
   [*DeviceA-ai-service] quit
   [*DeviceA] commit
   [~DeviceA] quit
   <DeviceA> reboot 
   The system will reboot. Continue? [Y/N]:Y
   ```
3. Configure the distance-based headroom buffer check function.
   
   
   
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
   
   # When the distance-based headroom buffer check function is enabled on DeviceA but not enabled on DeviceB, the detection fails. You need to trigger the interface on DeviceA to send a detection packet.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] start long-distance detect
   [~DeviceA-100GE1/0/1] quit
   ```

#### Verifying the Configuration

# Display buffer optimization information.

```
[~DeviceA] display buffer optimization configuration slot 1  
-----------------------------------------------------------------------------------------------------------------------
Buffer unit: KB
Configure buffer optimization mode: Long-distance
Current buffer optimization mode: Long-distance
Interface that can be enabled with both PFC and long-distance mode:                                                    
100GE1/0/1       100GE1/0/2      

-----------------------------------------------------------------------------------------------------------------------
Pipe                       Buffer
-----------------------------------------------------------------------------------------------------------------------
   0                        20480
   1                         3072  
   2                        20480
   3                         3072
   4                         3072
   5                         3072

-----------------------------------------------------------------------------------------------------------------------
Interface        Port        Chip        Pipe       PFC          Mode         DetectHdrmResult     RequiredHdrm
-----------------------------------------------------------------------------------------------------------------------
100GE1/0/1          16           0           0       Enable       level-100               12496            12500
-----------------------------------------------------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
dcb pfc
 priority 4
#
qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
#
interface 100GE1/0/1
 long-distance mode level-100
 dcb pfc enable mode manual
#
interface 100GE1/0/2
 dcb pfc enable mode manual
#
ai-service 
 #
 buffer optimization mode long-distance
#
port-group all_using        
 group-member 100GE1/0/1   
 group-member 100GE1/0/2 
#
return

```

DeviceB

```
#
sysname DeviceB
#
dcb pfc
 priority 4
#
qos buffer headroom-pool size 4 mbytes slot 1      //This command is required only on the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.
#
interface 100GE1/0/1
 long-distance mode level-100
 dcb pfc enable mode manual
#
interface 100GE1/0/2
 dcb pfc enable mode manual
#
ai-service 
 #
 buffer optimization mode long-distance
#
port-group all_using        
 group-member 100GE1/0/1  
 group-member 100GE1/0/2 
#
return

```