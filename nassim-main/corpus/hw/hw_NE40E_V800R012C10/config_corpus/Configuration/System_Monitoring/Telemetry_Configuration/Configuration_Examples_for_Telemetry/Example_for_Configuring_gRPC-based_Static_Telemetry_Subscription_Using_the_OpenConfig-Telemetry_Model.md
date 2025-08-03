Example for Configuring gRPC-based Static Telemetry Subscription Using the OpenConfig-Telemetry Model
=====================================================================================================

This section provides an example for configuring static telemetry subscription using gRPC to send sampled data Based on the OpenConfig-Telemetry model.

#### Networking Requirements

As the network scale increases, users need to optimize networks and rectify faults based on device information. For example, if the CPU usage of a device exceeds a specified threshold, the device reports data to a collector so that network traffic can be monitored and optimized in a timely manner.

On the network shown in [Figure 1](#EN-US_TASK_0139427983__fig_dc_vrp_telemetry_cfg_001801), DeviceA supports telemetry and establishes a gRPC connection with the collector. When the CPU usage of DeviceA exceeds 40%, data needs to be sent to the collector. When the system memory usage of DeviceA exceeds 50%, a customized event needs to be sent to the collector.

**Figure 1** Configuring gRPC-based static telemetry subscription![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_cfg_telemetry_00181.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a destination collector.
2. Configure the data to be sampled and a customized event.
3. Create a subscription.

#### Data Preparation

To complete the configuration, you need the following data:

* Collector's IP address 10.20.2.1 and port number 10001 (DeviceA and the collector must be routable.)
* Destination group name **destination1**
* Sampling sensor group name **sensor1**
* Subscription name **subscription1**

#### Procedure

1. Configure an IP address and a routing protocol for each interface so that all devices can communicate at the network layer. For details, see configuration files.
2. Configure a destination collector.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] telemetry
   ```
   ```
   [~DeviceA-telemetry] destination-group destination1
   ```
   ```
   [*DeviceA-telemetry-destination-group-destination1] ipv4-address 10.20.2.1 port 10001 protocol grpc
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If the device connects to the destination collector using an IPv6 address, you must run the [**ipv6-address**](cmdqueryname=ipv6-address) *ip-address-ipv6* **port** *port* [ **vpn-instance** *vpn-instance* ] [ **protocol** **grpc** [ **no-tls** ] ] command to configure the IPv6 address and port number of the destination collector.
   * For details about how to configure TLS encryption for gRPC, see Configuration Files.
   ```
   [*DeviceA-telemetry-destination-group-destination1] quit
   ```
3. Configure the data to be sampled and a customized event. When the value of os-memory-usage in the sampling path **huawei-debug:debug/memory-infos/memory-info** is greater than 50, a customized event is reported.
   
   
   ```
   [*DeviceA-telemetry] sensor-group sensor1
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1] sensor-path huawei-debug:debug/cpu-infos/cpu-info 
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1-path] filter cpuinfo
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1-path-filter-cpuinfo] op-field system-cpu-usage op-type gt op-value 40
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1-path-filter-cpuinfo] quit
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1-path] quit
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1] sensor-path huawei-debug:debug/memory-infos/memory-info self-defined-event
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path] filter meminfo
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path-filter-meminfo] op-field os-memory-usage op-type gt op-value 50
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path-filter-meminfo] quit
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1-self-defined-event-path] quit
   ```
   ```
   [*DeviceA-telemetry-sensor-group-sensor1] quit
   ```
4. Create a subscription.
   
   
   ```
   [*DeviceA-telemetry] subscription subscription1
   ```
   ```
   [*DeviceA-telemetry-subscription-subscription1] sensor-group sensor1
   ```
   ```
   [*DeviceA-telemetry-subscription-subscription1] destination-group destination1
   ```
   ```
   [*DeviceA-telemetry-subscription-subscription1] commit
   ```

#### Configuration Files

DeviceA configuration file

```
#
sysname DeviceA
#
ssl policy policy1
 pki-domain domain1
#
grpc
 #
 grpc client 
  ssl-policy policy1
  ssl-verify peer
#
telemetry
 #
 sensor-group sensor1
  sensor-path huawei-debug:debug/cpu-infos/cpu-info 
   filter cpuinfo
     op-field system-cpu-usage op-type gt op-value 40
  sensor-path huawei-debug:debug/memory-infos/memory-info self-defined-event 
    filter meminfo
     op-field os-memory-usage op-type gt op-value 50
 #
 destination-group destination1
  ipv4-address 10.20.2.1 port 10001 protocol grpc
 #
 subscription subscription1
  sensor-group sensor1
  destination-group destination1
#
pki domain domain1
#
return
```