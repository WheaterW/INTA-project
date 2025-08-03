Example for Configuring Flow Recognition on a Media Network
===========================================================

This section provides an example for configuring flow recognition on a media network.

#### Networking Requirements

[Figure 1](#EN-US_TASK_0172373420__fig_dc_ne_cfg_flow-recognition_00002) shows a typical media network. The functions of each node are described as follows:

* Controller: delivers control instructions to the device to control, manage, and monitor the system.
* Device: provides functions such as forwarding, replication, scheduling, clean switching, and flow recognition of media traffic.
* Multimedia terminal A: functions as the transmit end of media signals and transmits traffic to the device.
* Multimedia terminal B: functions as the receive end of media signals and receives traffic from the device.

On the network:

1. Multimedia terminal A transmits video and audio streams to the device.
2. The device collects the streams on the inbound interface, and reports each stream's septuple information (source and destination MAC addresses, source and destination IP addresses, source and destination port numbers, and protocol type) and other information (such as the numbers of packets and bytes) to the controller.
3. The controller calculates the stream rate based on the information to identify audio and video streams.

**Figure 1** Typical media network![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Interface 1 in this example represents GE 0/1/1.

  
![](figure/en-us_image_0173687657.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a routing protocol for each interface so that all the nodes can communicate at the network layer.
2. Configure static telemetry subscription.
3. Configure flow recognition.
#### Data Preparation

To complete the configuration, you need the following data:

* Interface 1's IP address: 10.1.1.1
* Controller IP address: 10.1.1.2; port number: 10001
* Telemetry sampling path: huawei-flow-recognition:flowrecognition/streaminfos/streaminfo
* Proto file used for flow recognition: huawei-flow-recognition.proto


#### Procedure

1. Configure an IP address and a routing protocol for each interface so that all the nodes can communicate at the network layer. For configuration details about the device, see [Configuration Files](#EN-US_TASK_0172373420__dc_ne_recg_cfg_0001).
2. Configure static telemetry subscription. For configuration details, see [Configuration Files](#EN-US_TASK_0172373420__dc_ne_recg_cfg_0001) (Only key configurations are provided here. For details, see Telemetry Configuration).
3. Configure flow recognition.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] flow-recognition inbound
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] commit
   ```
4. Verify the configuration.
   
   
   
   # Check the flow table information of flow recognition in a specified slot.
   
   ```
   <HUAWEI> display flow-recognition cache slot 1
   ```
   ```
   Information of flow-recognition cache on slot 1
   ----------------------------------------------------------
   Interface      :  GigabitEthernet0/1/1
   Direction      :  inbound
   Protocol       :  6
   SrcMac         :  00e0-fc12-3456
   DstMac         :  00e0-fc34-5678
   SrcPort        :  10
   DstPort        :  30
   SrcAddr        :  10.10.1.3
   DstAddr        :  10.10.10.2
   FirstTimestamp :  2019-05-20 14:32:46
   LastTimestamp  :  2019-05-20 14:52:47
   PacketsCount   :  399564
   BytesCount     :  51144192
   ----------------------------------------------------------
   ```

#### Configuration Files

```
#
telemetry
 #
 sensor-group sensor1
  sensor-path huawei-flow-recognition:flow-recognition/streaminfos/streaminfo self-defined-event
 #
 destination-group destination1
  ipv4-address 10.1.1.2 port 10001 protocol grpc
 #
 subscription subscription1
  sensor-group sensor1
  destination-group destination1
#
#
interface GigabitEthernet 0/1/1
 flow-recognition inbound
#
```