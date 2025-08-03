Example for Configuring UDP-based Static Telemetry Subscription Using the YANG-Push Mode
========================================================================================

This section provides an example for configuring static telemetry subscription using UDP to send sampled data and adopting the YANG-Push model defined by the IETF.

#### Networking Requirements

As the network scale increases, it is required that networks be optimized or faults rectified in a timely manner based on device information. On the network shown in [Figure 1](#EN-US_TASK_0000001553632706__fig_dc_vrp_telemetry_cfg_001801), telemetry-capable DeviceA establishes a UDP connection with the collector.

**Figure 1** Configuring UDP-based static telemetry subscription![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_cfg_telemetry_00181.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a destination collector.
2. Configure a sampling path.
3. Create a subscription.

#### Data Preparation

To complete the configuration, you need the following data:

* Collector's IP address (10.20.2.1) and port number (3600) (DeviceA and the collector must be routable.)
* Name of the receiver for the sampled data (r1)
* Name of the sampling filter (f1)
* Name of the subscription (s1)
* Name of the receiver in the subscription (r2)

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
   [~DeviceA] telemetry ietf
   ```
   ```
   [~DeviceA-telemetry-ietf] receiver r1
   ```
   ```
   [*DeviceA-telemetry-ietf-receiver-r1] ipv4-address 10.20.2.1 port 3600
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the device connects to the collector using an IPv6 address, you need to run the [**ipv6-address**](cmdqueryname=ipv6-address)**ipv6-addr** **port** *port-number* command to configure an IPv6 address and a port number for the destination collector.
   
   ```
   [*DeviceA-telemetry-ietf-receiver-r1] quit
   ```
3. Configure a sampling path.
   
   
   ```
   [*DeviceA-telemetry-ietf] filter f1 type datastore
   ```
   ```
   [*DeviceA-telemetry-ietf-datastore-filter-f1] xpath /huawei-debug:debug/cpu-infos/cpu-info
   ```
   ```
   [*DeviceA-telemetry-ietf-datastore-filter-f1] quit
   ```
4. Create a subscription.
   
   
   ```
   [*DeviceA-telemetry-ietf] subscription 1
   ```
   ```
   [*DeviceA-telemetry-ietf-subs-s1] transport udp-notif
   ```
   ```
   [*DeviceA-telemetry-ietf-subs-s1] encoding json
   ```
   ```
   [*DeviceA-telemetry-ietf-subs-s1] distribute enable
   ```
   ```
   [*DeviceA-telemetry-ietf-subs-s1] update-trigger period 100
   ```
   ```
   [*DeviceA-telemetry-ietf-subs-s1] filter f1 type datastore
   ```
   ```
   [*DeviceA-telemetry-ietf-subs-s1] receiver r2
   ```
   ```
   [*DeviceA-telemetry-ietf-subs-s1-receiver-r2] bind-receiver r1 
   ```
   ```
   [*DeviceA-telemetry-ietf-subs-s1-receiver-r2] commit
   ```

#### Configuration Files

DeviceA configuration file

```
#
sysname DeviceA
#
telemetry ietf
 #
 filter f1 type datastore
  xpath /huawei-debug:debug/cpu-infos/cpu-info
 #
 receiver r1
  ipv4-address 10.20.2.1 port 3600
 #
 subscription 1
  transport udp-notif
  encoding json
  distribute enable
  update-trigger period 100
  filter f1 type datastore
  #
  receiver r2
   bind-receiver r1
#
return
```