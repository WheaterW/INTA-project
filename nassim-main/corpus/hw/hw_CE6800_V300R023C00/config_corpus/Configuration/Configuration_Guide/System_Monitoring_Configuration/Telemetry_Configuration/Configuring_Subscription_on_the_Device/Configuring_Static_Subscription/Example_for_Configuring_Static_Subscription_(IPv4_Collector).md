Example for Configuring Static Subscription (IPv4 Collector)
============================================================

Example for Configuring Static Subscription (IPv4 Collector)

#### Networking Requirements

As the network scale increases, you need to optimize networks and rectify faults based on device information. For example, if the CPU usage of a device exceeds a specified threshold, the device reports data to a collector so that network traffic can be monitored and optimized in a timely manner.

As shown in [Figure 1](#EN-US_TASK_0000001563994425__en-us_task_0275777943_fig117736513266), DeviceA supports telemetry and establishes a gRPC connection with the collector. When the CPU usage of DeviceA exceeds 40%, data needs to be sent to the collector. When the system memory usage of DeviceA exceeds 50%, data needs to be sent to the collector.

**Figure 1** Network diagram of configuring gRPC-based static subscription  
![](figure/en-us_image_0000001513034246.png)

#### Procedure

1. Configure a destination collector for receiving sampled data.
   
   
   
   # On DeviceA, create the destination group **destination1** to which a destination collector belongs, set the IP address and port number of the destination collector to 10.20.2.1 and 10001, respectively, and set the gRPC encryption mode to TLS.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] telemetry
   [~DeviceA-telemetry] destination-group destination1
   [*DeviceA-telemetry-destination-group-destination1] ipv4-address 10.20.2.1 port 10001 protocol gRPC
   [*DeviceA-telemetry-destination-group-destination1] quit
   [*DeviceA-telemetry] commit
   ```
2. Configure the sampling path and filter criteria.
   
   
   
   # Configure the sampling sensor group **sensor1**.
   
   ```
   [~DeviceA-telemetry] sensor-group sensor1
   [*DeviceA-telemetry] commit
   ```
   
   # Configure a sampling path and customized event for sampling CPU usage data. In this example, the sampling path is **huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info**, the filtering field is **system-cpu-usage**, and the filter criterion is that the CPU usage is greater than 40%.
   
   ```
   [~DeviceA-telemetry-sensor-group-sensor1] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info self-defined-event 
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path] filter cpuinfo
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path-filter-cpuinfo] op-field system-cpu-usage op-type gt op-value 40
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path-filter-cpuinfo] quit
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path] quit
   [*DeviceA-telemetry-sensor-group-sensor1] commit
   ```
   
   # Configure a sampling path and customized event for sampling system memory usage data. In this example, the sampling path is **huawei-cpu-memory:cpu-memory/board-memory-infos/board-memory-info**, the filtering field is **os-memory-usage**, and the filter criterion is that the system memory usage is greater than 50%.
   
   ```
   [~DeviceA-telemetry-sensor-group-sensor1] sensor-path huawei-cpu-memory:cpu-memory/board-memory-infos/board-memory-info self-defined-event
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path] filter meminfo
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path-filter-meminfo] op-field os-memory-usage op-type gt op-value 50
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path-filter-meminfo] quit
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path] quit
   [*DeviceA-telemetry-sensor-group-sensor1] quit
   [*DeviceA-telemetry] commit
   ```
3. Create a static subscription.
   
   
   
   # On DeviceA, create a subscription named **subscription1** and associate it with the sampling sensor group **sensor1** and destination group **destination1**.
   
   ```
   [~DeviceA-telemetry] subscription subscription1
   [*DeviceA-telemetry-subscription-subscription1] sensor-group sensor1 sample-interval 60000
   [*DeviceA-telemetry-subscription-subscription1] destination-group destination1
   [*DeviceA-telemetry-subscription-subscription1] commit
   ```

#### Verifying the Configuration

Check static subscription information after the configuration is complete.

# Display static subscription information.

```
[~DeviceA] display telemetry subscription subscription1
---------------------------------------------------------------------------     
Sub-name           : subscription1                                              
Source Address     : 10.1.1.1                                                          
Dscp               : 0                                                          
Protocol           : GRPC                                                       
Encoding           : GPB                                                        
Send bytes         : -                                                          
Send packets       : -                                                          
Total send delay   : -                                                         
Total send error   : -                                                          
Total send  drop   : -                                                          
Total other error  : -                                                          
Last send-time     : -                                       
Sensor group:                                                                   
---------------------------------------------------------------------------     
Sensor-name  Sample-interval(ms) Heartbeat-interval(s) Suppression State        
---------------------------------------------------------------------------     
sensor1      60000               -                     NO          RESOLVED     
---------------------------------------------------------------------------     
Destination group:                                                              
---------------------------------------------------------------------------     
Dest-name    Dest-IP          Dest-port  State        Vpn-name      Protocol    Compression 
---------------------------------------------------------------------------     
destination1 10.20.2.1        10001      RESOLVED     -             GRPC        None
---------------------------------------------------------------------------     
Sub-state          : PASSIVE                                                    
---------------------------------------------------------------------------     

Total subscription number is :  1        
```
#### Configuration Scripts

DeviceA
```
#
sysname DeviceA
#
telemetry
 #
 sensor-group sensor1
  sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info self-defined-event              
   filter cpuinfo                                                               
    op-field system-cpu-usage op-type gt op-value 40  
  sensor-path huawei-cpu-memory:cpu-memory/board-memory-infos/board-memory-info self-defined-event 
    filter meminfo
     op-field os-memory-usage op-type gt op-value 50
 #
 destination-group destination1
  ipv4-address 10.20.2.1 port 10001 protocol gRPC
 #
 subscription subscription1
  sensor-group sensor1 sample-interval 60000
  destination-group destination1
#
return
```