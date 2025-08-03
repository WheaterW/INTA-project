Example for Configuring Differentiated Flow Scheduling
======================================================

Example for Configuring Differentiated Flow Scheduling

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513039958__fig19978171395514), DeviceA is directly connected to Host1 and Host2. To ensure the forwarding of mice flows is prioritized, you can configure differentiated flow scheduling on DeviceA.

**Figure 1** Network diagram for differentiated flow scheduling![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001564000213.png)

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
3. Enable differentiated flow scheduling on both the inbound and outbound interfaces.
   
   
   
   # On DeviceA, enable differentiated flow scheduling on 100GE1/0/1 and 100GE1/0/2.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] mice-elephant-flow enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] mice-elephant-flow enable
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display the configuration of differentiated flow scheduling on DeviceA.

* For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855:

```
[~DeviceA] display mice-elephant-flow configuration
Aging Time(ms): 10
Assigned Queues: 3
Mice-flow Packet Number: 200
------------------------------------
Interface      Distinguishing Status
------------------------------------
100GE1/0/1     enable
100GE1/0/2     enable
------------------------------------
```

* For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:

```
[~DeviceA] display mice-elephant-flow configuration
Assigned Queues: 3
Adjust to Queues: 4
Scheduling Mode: -
------------------------------------
Interface      Distinguishing Status
------------------------------------
100GE1/0/1     enable
100GE1/0/2     enable
------------------------------------
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
#
interface 100GE1/0/2
 mice-elephant-flow enable
#
ai-service 
 #
 mice-elephant-flow
  assign queue 3 adjust mice-flow to queue 4
#
return
```