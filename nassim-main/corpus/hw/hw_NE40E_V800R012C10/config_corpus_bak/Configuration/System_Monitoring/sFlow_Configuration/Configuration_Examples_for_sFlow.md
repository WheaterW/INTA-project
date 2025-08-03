Configuration Examples for sFlow
================================

This section provides sFlow configuration examples.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172373334__fig_dc_ne_sflow_cfg_000601), traffic between network 1 and network 2 is exchanged through device A. Maintenance personnel need to monitor the traffic on interface 2 and devices to identify traffic anomalies and ensure normal operation on network 1.

**Figure 1** sFlow network diagram  
![](images/fig_dc_ne_sflow_cfg_000601.png)![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example:

* Interface 1 is GE 0/1/1.
* Interface 2 is GE 0/1/2.
* Interface 3 is GE 0/1/3.



#### Configuration Roadmap

To configure sFlow, configure device A as an sFlow agent and enable Flow sampling on interface 2 so that the agent collects traffic statistics. The agent encapsulates traffic statistics into sFlow packets and sends the sFlow packets from interface 1 to the sFlow collector. The collector displays the traffic statistics based on information in the received sFlow packets.

The configuration roadmap is as follows:

1. Assign an IP address to each interface.
2. Configure sFlow agent and collector information on the device.
3. Configure flow sampling on interface 2.

#### Procedure

1. Assign an IP address to each interface of device A.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ip address 10.1.10.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/1/2
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] ip address 10.1.20.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/1/3
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/3] ip address 10.1.30.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/3] quit
   ```
2. Configure sFlow agent and collector information.
   
   
   
   # Configure an IP address for an sFlow agent.
   
   ```
   [~DeviceA] sflow
   ```
   ```
   [~DeviceA-sflow] sflow agent ip 10.1.10.1
   ```
   ```
   [*DeviceA-sflow] commit
   ```
   
   # Configure sFlow collector information.
   
   ```
   [~DeviceA-sflow] sflow collector 2
   ```
   ```
   [*DeviceA-sflow-collector-2] commit
   ```
   ```
   [~DeviceA-sflow-collector-2] sflow server ip 10.1.10.2
   ```
   ```
   [*DeviceA-sflow-collector-2] commit
   ```
   ```
   [~DeviceA-sflow-collector-2] quit
   ```
   ```
   [~DeviceA-sflow] quit
   ```
3. Enable sFlow on a specified board.
   
   
   ```
   [~DeviceA] slot 3
   ```
   ```
   [~DeviceA-slot-3] sflow enable
   ```
   ```
   [*DeviceA-slot-3] commit
   ```
   ```
   [*DeviceA-slot-3] quit
   ```
4. Configure flow sampling.
   
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/2
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] sflow flow-sampling collector 2 inbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] sflow flow-sampling rate 4000 inbound
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
5. Verify the configuration.
   
   
   ```
   [~DeviceA] display sflow configuration
   sflow
    sflow agent ip 10.1.10.1
    sflow collector 2
     sflow server ip 10.1.10.2
   slot 3
    sflow enable
   interface GigabitEthernet0/1/2
    sflow flow-sampling collector 2 inbound
    sflow flow-sampling rate 4000 inbound
   ```

#### Configuration Files

Device A configuration file

```
#
```
```
sysname DeviceA
```
```
#
```
```
interface GigabitEthernet0/1/1
```
```
ip address 10.1.10.1 255.255.255.0
```
```
#
```
```
interface GigabitEthernet0/1/2
```
```
ip address 10.1.20.1 255.255.255.0
```
```
#
```
```
interface GigabitEthernet0/1/3
```
```
ip address 10.1.30.1 255.255.255.0
```
```
#
```
```
sflow
```
```
sflow agent ip 10.1.10.1
```
```
sflow collector 2
```
```
sflow server ip 10.1.10.2
```
```
slot 3
```
```
sflow enable
```
```
#
```
```
interface GigabitEthernet0/1/2
```
```
sflow flow-sampling collector 2 inbound
```
```
sflow flow-sampling rate 4000 inbound
```
```
#
```
```
return 
```