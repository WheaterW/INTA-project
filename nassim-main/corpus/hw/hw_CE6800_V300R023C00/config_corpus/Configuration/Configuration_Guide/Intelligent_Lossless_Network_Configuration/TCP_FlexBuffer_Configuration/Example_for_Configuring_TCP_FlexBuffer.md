Example for Configuring TCP FlexBuffer
======================================

Example for Configuring TCP FlexBuffer

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512843902__fig19978171395514), DeviceA is directly connected to Host1 and Host2. To ensure the forwarding of mice flows is prioritized, you can configure differentiated flow scheduling on DeviceA.

**Figure 1** Network diagram for differentiated flow scheduling![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001513163454.png)

#### Procedure

1. Set the system resource mode to **balance**. (This configuration is required only for the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.)
   
   
   
   # On DeviceA, set the system resource mode to **balance** and restart DeviceA to make the configuration take effect.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] system resource balance
   [*DeviceA] commit
   [~DeviceA] quit
   <DeviceA> save
   Warning: The current configuration will be written to the device. Continue? [Y/N]:Y
   Now saving the current configuration to the slot 1 ......... 
   Info: Save the configuration successfully. 
   <DeviceA> reboot 
   Warning: The system will reboot. Continue? [Y/N]:Y
   ```
2. Configure global parameters for differentiated flow scheduling.
   
   
   * For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:
   
   
   
   # On DeviceA, enable differentiated flow scheduling for queue 3 and set the number of packets in a mice flow to 200.
   
   ```
   [~DeviceA] ai-service
   [*DeviceA-ai-service] mice-elephant-flow
   [*DeviceA-ai-service-mice-elephant-flow] assign queue 3
   [*DeviceA-ai-service-mice-elephant-flow] mice-flow packet-number 200
   [*DeviceA-ai-service-mice-elephant-flow] quit
   [*DeviceA-ai-service] quit
   [*DeviceA] commit
   ```
   
   
   * For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
   
   # On DeviceA, specify the elephant-flow queue for which differentiated flow scheduling is to be enabled to queue 3 and the mice-flow queue after the adjustment to queue 4.
   
   
   
   ```
   [~DeviceA] ai-service
   [*DeviceA-ai-service] mice-elephant-flow
   [*DeviceA-ai-service-mice-elephant-flow] assign queue 3 adjust mice-flow to queue 4
   [*DeviceA-ai-service-mice-elephant-flow] quit
   [*DeviceA-ai-service] quit
   [*DeviceA] commit
   ```
3. Enable differentiated flow scheduling on both the inbound and outbound interfaces. You need to set the size of the dynamic queue-level service buffer in the outbound direction to 9 only for the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.
   
   
   
   # On DeviceA, enable differentiated flow scheduling on 100GE1/0/1 and 100GE1/0/2.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] mice-elephant-flow enable
   [*DeviceA-100GE1/0/1] qos buffer queue 3 shared-threshold dynamic 9
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] mice-elephant-flow enable
   [*DeviceA-100GE1/0/2] qos buffer queue 3 shared-threshold dynamic 9
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
4. Enable TCP FlexBuffer.
   
   
   
   # On DeviceA, enable TCP FlexBuffer.
   
   ```
   [~DeviceA] ai-service
   [*DeviceA-ai-service] mice-elephant-flow
   [*DeviceA-ai-service-mice-elephant-flow] flex-buffer enable
   [*DeviceA-ai-service-mice-elephant-flow] quit
   [*DeviceA-ai-service] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display the configuration of differentiated flow scheduling on DeviceA.

* For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:

```
[~DeviceA] display flex-buffer state
Low-Limit: Lower threshold of packets of all colors. The unit is Bytes.
High-Limit: Upper threshold of packets of all colors. The unit is Bytes.
Discard-Percentage: Drop probability of packets of all colors. The unit is %.
Dynamic: Dynamic queue-level queue service buffer size of a mice-flow queue.
---------------------------------------------------------------------------------------------------
Current Mice-flow Packet Number: 200
Interface       Queue   Low-Limit   High-Limit   Discard-Percentage   Dynamic      Last Adjust Time
---------------------------------------------------------------------------------------------------
100GE1/0/1          3      153600       512000                    1         6   2021-11-24 15:48:02
---------------------------------------------------------------------------------------------------
100GE1/0/2          3           -            -                    -         5                     -
---------------------------------------------------------------------------------------------------
```

* For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:

```
[~DeviceA] display flex-buffer state
Low-Limit: Lower threshold of packets of all colors. The unit is Bytes.
High-Limit: Upper threshold of packets of all colors. The unit is Bytes.
Discard-Percentage: Drop probability of packets of all colors. The unit is %.
-----------------------------------------------------------------------------------------
Interface       Queue   Low-Limit   High-Limit   Discard-Percentage      Last Adjust Time
-----------------------------------------------------------------------------------------
100GE1/0/1          3      153600       512000                    1   2021-11-24 15:48:02
-----------------------------------------------------------------------------------------
100GE1/0/2          3           -            -                    -                     -
----------------------------------------------------------------------------------------- 
```

#### Configuration Scripts

DeviceA

* For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:

```
#
sysname DeviceA
#
interface 100GE1/0/1 
 mice-elephant-flow enable
#
interface 100GE1/0/2
 mice-elephant-flow enable
#
ai-service 
 #
 mice-elephant-flow
  assign queue 3
  mice-flow packet-number 200
  flex-buffer enable
#
return
```

* For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:

```
#
sysname DeviceA
#
system resource balance
#
interface 100GE1/0/1 
 mice-elephant-flow enable
 qos buffer queue 3 shared-threshold dynamic 9
#
interface 100GE1/0/2
 mice-elephant-flow enable
 qos buffer queue 3 shared-threshold dynamic 9
#
ai-service 
 #
 mice-elephant-flow
  assign queue 3 adjust mice-flow to queue 4
  flex-buffer enable
#
return
```