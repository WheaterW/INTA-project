Example for Configuring UDP-based Static Telemetry Subscription Using the OpenConfig-Telemetry Model
====================================================================================================

This section provides an example for configuring static telemetry subscription using UDP to send sampled data based on the OpenConfig-Telemetry model.

#### Networking Requirements

As the network scale increases, users need to optimize networks and rectify faults based on device information. For example, if the CPU usage of a device exceeds a specified threshold, the device reports data to a collector so that network traffic can be monitored and optimized in a timely manner.

As shown in [Figure 1](#EN-US_TASK_0139427989__fig_dc_vrp_telemetry_cfg_001801), telemetry-capable DeviceA establishes a UDP connection with the collector. It is required that data be sent to the collector when DeviceA's CPU usage exceeds 40% and a customized event be sent to the collector when DeviceA's system memory usage exceeds 50%.

**Figure 1** Network diagram of configuring UDP-based static telemetry subscription![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.

  
![](figure/en-us_image_0000001203094248.png)  



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a destination collector.
2. Configure the data to be sampled and a customized event.
3. Create a subscription.

#### Data Preparation

To complete the configuration, you need the following data:

* Collector's IP address (10.20.2.1) and port number (10001); IP address of DeviceA's interface1 (192.168.1.1) and port number (11111)
* Destination group name **destination1**
* Sampling sensor group name **sensor1**
* Subscription name **subscription1**

#### Procedure

1. Configure an IP address and a routing protocol for each interface so that all devices can communicate at the network layer.
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
   [*DeviceA-telemetry-destination-group-destination1] ipv4-address 10.20.2.1 port 10001 protocol udp
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the device connects to the destination collector using an IPv6 address, you need to run the [**ipv6-address**](cmdqueryname=ipv6-address) *ip-address* **port** *port* [ **vpn-instance** *vpn-instance* ] [ **protocol** **udp** ] command to configure an IPv6 address and port number for the destination collector.
   
   ```
   [*DeviceA-telemetry-destination-group-destination1] quit
   ```
3. Configure the data to be sampled and a customized event.
   
   
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
   [*DeviceA-telemetry-subscription-subscription1] local-source-address ipv4 192.168.1.1 port 11111
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the device connects to the destination collector using an IPv6 address, you need to run the **[**local-source-address ipv6**](cmdqueryname=local-source-address+ipv6)** *ip-address* **port** *port* command to configure a source IPv6 address and a source port number.
   
   ```
   [*DeviceA-telemetry-subscription-subscription1] commit
   ```

#### Configuration Files

DeviceA configuration file

```
#
sysname DeviceA
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
  ipv4-address 10.20.2.1 port 10001 protocol udp
 #
 subscription subscription1
  sensor-group sensor1
  destination-group destination1
  local-source-address ipv4 192.168.1.1 port 11111
#
return
```