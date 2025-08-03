Example for Managing Interfaces
===============================

This section uses an example to describe how to configure interface parameters, such as the interface description, maximum transmission unit (MTU), and interval at which traffic statistics are collected.

#### Networking Requirements

To ensure smooth communication between devices on a network, you need to configure both physical and logical interfaces properly and set the following parameters:

* Interface description
* MTU
* Trap threshold for the outbound and inbound bandwidth usage on a specified interface
* Interval at which traffic statistics are collected
* Whether the device sends a trap message to the network management system (NMS) when the interface status changes
* Whether the control-flap function is enabled


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a description for an interface.
2. Set an MTU for the interface to ensure successful packet transmission over the interface.
3. Set the interval at which traffic statistics (including the traffic volumes and rates) are collected globally.
4. Create a sub-interface and set an MTU for the sub-interface so that packets can reach the receiver.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface name
* Interface description
* Interface MTU
* Interval at which traffic statistics are collected globally
* Sub-interface MTU

#### Procedure

1. Configure a description for an interface.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface gigabitethernet 0/2/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0] description for IFM
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0] commit
   ```
2. Set an MTU for the interface.
   
   
   ```
   [~HUAWEI-GigabitEthernet0/2/0] mtu 1000
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/2/0] quit
   ```
3. Set the interval at which traffic statistics are collected globally.
   
   
   ```
   [~HUAWEI] set flow-stat interval 100
   ```
   ```
   [*HUAWEI] commit
   ```
4. Create a sub-interface and set the MTU of the sub-interface.
   
   
   ```
   [~HUAWEI] interface gigabitethernet 0/2/0.1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0.1] mtu 800
   ```
   ```
   [*HUAWEI-GigabitEthernet0/2/0.1] commit
   ```

#### Configuration Files

```
#
```
```
set flow-stat interval 100
```
```
#
```
```
interface Gigabitethernet0/2/0
```
```
 description for IFM
```
```
 mtu 1000
```
```
#
```
```
interface Gigabitethernet0/2/0.1
```
```
 mtu 800
```
```
#
```
```
return
```