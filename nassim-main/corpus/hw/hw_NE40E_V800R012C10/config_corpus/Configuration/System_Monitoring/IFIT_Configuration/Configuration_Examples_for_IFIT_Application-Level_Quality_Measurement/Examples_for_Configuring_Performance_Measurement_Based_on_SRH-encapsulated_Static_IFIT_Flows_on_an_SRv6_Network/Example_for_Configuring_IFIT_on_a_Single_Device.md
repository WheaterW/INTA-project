Example for Configuring IFIT on a Single Device
===============================================

This section provides an example for configuring IFIT to measure packet loss and delay on a single device in a native IP scenario.

#### Networking Requirements

When IFIT is deployed on a network, it is possible that only a single device supports IFIT and upstream and downstream devices do not support IFIT. In this case, IFIT can provide performance measurement for a single device. The native IP scenario is used as an example. On the network shown in [Figure 1](#EN-US_TASK_0000001274688542__fig3691666259), DeviceA is a standalone IFIT-capable device.

**Figure 1** Configuring IFIT on a single device![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents GE 0/1/0.


  
![](figure/en-us_image_0000001340224481.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a routing protocol for each involved interface so that all devices can communicate at the network layer.
2. Create a static IFIT flow on DeviceA.
3. Configure single-device measurement on DeviceA to periodically collect statistics on the packet loss rate and transmission delay on the bearer network.
4. Configure the device to send statistics to the NMS through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface as listed in [Figure 1](#EN-US_TASK_0000001274688542__fig3691666259)
* IFIT instance ID (1) and measurement interval (30s)
* Target flow's source IP address (10.1.1.1) and destination IP address (10.2.1.1)
* NMS's IPv4 address (192.168.100.100) and port number (10001), and reachable routes between the NMS and devices


#### Procedure

1. Configure an IP address and a routing protocol for each involved interface so that all devices can communicate at the network layer. The configuration details are not provided here.
2. Create a static IFIT flow on DeviceA.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] ifit
   ```
   ```
   [*DeviceA-ifit] node-id 1
   ```
   ```
   [*DeviceA-ifit] instance 1
   ```
   ```
   [*DeviceA-ifit-instance-1] flow unidirectional source 10.1.1.1 destination 10.2.1.1 dscp 63
   ```
   ```
   [*DeviceA-ifit-instance-1] binding interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-ifit-instance-1] commit
   ```
3. Configure single-device measurement on DeviceA.
   
   
   ```
   [~DeviceA-ifit-instance-1] single-device-measure enable
   ```
   ```
   [*DeviceA-ifit-instance-1] commit
   ```
   ```
   [~DeviceA-ifit-instance-1] quit
   ```
   ```
   [~DeviceA-ifit] quit
   ```
   # Run the [**display ifit static**](cmdqueryname=display+ifit+static) command to check the configuration and status of DeviceA.
   ```
   [~DeviceA] display ifit static instance 1
   ```
   ```
   -------------------------------------------------------------------------
   Flow Classification                     : static
   Instance Id                             : 1
   Instance Name                           : 1
   Instance Type                           : instance 
   Flow Id                                 : 1835009
   Flow Monitor Id                         : 786433
   Flow Node Id                            : 1
   Flow Type                               : unidirectional
   Source IP Address/Mask Length           : 10.1.1.1/32
   Destination IP Address/Mask Length      : 10.2.1.1/32
   Protocol                                : any
   Source Port                             : any
   Destination Port                        : any
   Gtp                                     : disable
   Gtp TeId                                : --
   Dscp                                    : 63
   Interface                               : GigabitEthernet0/1/0
   vpn-instance                            : --
   Measure State                           : enable
   Loss Measure                            : enable
   Delay Measure                           : enable
   Delay Per packet Measure                : disable
   Disorder Measure                        : disable
   Gtpu Sequence Measure                   : disable
   Single Device Measure                   : enable
   Measure Mode                            : e2e
   Interval                                : 30(s)
   Tunnel Type                             : --
   Flow Match Priority                     : 0
   Flow InstType Priority                  : 9
   ```
4. Configure the device to send statistics to the NMS through telemetry.
   
   
   ```
   [~DeviceA] telemetry
   ```
   ```
   [~DeviceA-telemetry] destination-group ifit
   ```
   ```
   [*DeviceA-telemetry-destination-group-ifit] ipv4-address 192.168.100.100 port 10001 protocol grpc
   ```
   ```
   [*DeviceA-telemetry-destination-group-ifit] quit
   ```
   ```
   [*DeviceA-telemetry] sensor-group ifit
   ```
   ```
   [*DeviceA-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   ```
   ```
   [*DeviceA-telemetry-sensor-group-ifit-path] quit
   ```
   ```
   [*DeviceA-telemetry-sensor-group-ifit] quit
   ```
   ```
   [*DeviceA-telemetry] subscription ifit
   ```
   ```
   [*DeviceA-telemetry-subscription-ifit] sensor-group ifit sample-interval 0
   ```
   ```
   [*DeviceA-telemetry-subscription-ifit] destination-group ifit
   ```
   ```
   [*DeviceA-telemetry-subscription-ifit] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to configure devices to send data using a secure TLS encryption mode. For details, see *Telemetry Configuration*.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 192.168.2.1 255.255.255.0
  #
  ifit
   node-id 1
   instance 1
    flow unidirectional source 10.1.1.1 destination 10.2.1.1 dscp 63
    binding interface Gigabitethernet0/1/0
    single-device-measure enable
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   #
   destination-group ifit
    ipv4-address 192.168.100.100 port 10001 protocol grpc
   #
   subscription ifit
    sensor-group ifit sample-interval 0
    destination-group ifit
  #               
  return 
  ```