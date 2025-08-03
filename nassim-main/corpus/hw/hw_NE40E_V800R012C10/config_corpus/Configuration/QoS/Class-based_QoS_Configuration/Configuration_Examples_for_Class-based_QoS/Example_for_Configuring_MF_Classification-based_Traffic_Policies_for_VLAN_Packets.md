Example for Configuring MF Classification-based Traffic Policies for VLAN Packets
=================================================================================

This section provides an example for configuring and applying an MF classification-based traffic policy in a VLAN QoS scenario.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371309__fig_dc_ne_qos_cfg_009901), DeviceA and DeviceB connect to each other through a VLAN. When IP packets sent by DeviceA enter the VLAN, by default, the precedence of these IP packets is mapped to the 802.1p value. When these IP packets (carrying VLAN frame priority) leave the VLAN and arrive at DeviceB, the VLAN frame priority is mapped to the IP precedence according to the configuration on DeviceB. Then, these packets are forwarded according to their IP precedence.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, and interface3 in this example represent GE 0/1/0, GE 0/2/0.1, and GE 0/3/0, respectively.


**Figure 1** Networking diagram for configuring VLAN QoS  
![](images/fig_dc_ne_qos_cfg_009901.png)

#### Configuration Notes

When configuring VLAN QoS, pay attention to the following:

* The statistical function of traffic policies is disabled by default. To display the statistics about a traffic policy, you can enable statistics for the traffic policy by running the **statistics enable** command.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the VLAN and routes on DeviceA and DeviceB.
2. Configure QoS policies on DeviceB.

#### Data Preparation

To complete the configuration, you need the following data:

* Names of traffic classification, traffic behaviors, and traffic policies
* Preferences for re-marking

#### Procedure

1. Define a classifier to match packets whose 802.1p value is 2.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] traffic classifier test
   ```
   ```
   [*DeviceB-classifier-test] if-match 8021p 2
   ```
   ```
   [*DeviceB-classifier-test] commit
   ```
   ```
   [~DeviceB-classifier-test] quit
   ```
2. Define a traffic behavior to re-mark the IP precedence of packets as 4.
   
   
   ```
   [~DeviceB] traffic behavior test
   ```
   ```
   [*DeviceB-behavior-test] remark ip-precedence 4
   ```
   ```
   [*DeviceB-behavior-test] commit
   ```
   ```
   [~DeviceB-behavior-test] quit
   ```
3. Define a QoS policy to associate a configured traffic behavior with a specified traffic classifier.
   
   
   ```
   [~DeviceB] traffic policy test
   ```
   ```
   [*DeviceB-trafficpolicy-test] classifier test behavior test
   ```
   ```
   [*DeviceB-trafficpolicy-test] commit
   ```
   ```
   [~DeviceB-trafficpolicy-test] quit
   ```
4. Apply the QoS policy to the incoming traffic of GE 0/2/0.1 on DeviceB.
   
   
   ```
   [~DeviceB] interface Gigabitethernet 0/2/0.1
   ```
   ```
   [~DeviceB-Gigabitethernet0/2/0.1] traffic-policy test inbound link-layer
   ```
   ```
   [*DeviceB-Gigabitethernet0/2/0.1] commit
   ```
   ```
   [~DeviceB-Gigabitethernet0/2/0.1] quit
   ```
5. Verify the configuration.
   
   
   
   After the preceding configurations, when packets whose IP precedence is 2 are forwarded by GE 0/1/0.1 on DeviceA reach the VLAN, the IP precedence 2 is mapped to the VLAN priority 2. After these VLAN frames reach DeviceB, DeviceB forwards these VLAN frames as IP packets with the IP precedence of 4 to the network segment 10.1.2.0/24.

#### Configuration Files

DeviceB configuration file
```
#
```
```
 sysname DeviceB
```
```
#
```
```
traffic classifier test operator or
```
```
 if-match 8021p 2
```
```
#
```
```
traffic behavior test
```
```
 remark ip-precedence 4
```
```
#
```
```
traffic policy test
```
```
 classifier test behavior test precedence 1
```
```
#
```
```
interface GigabitEthernet0/2/0.1
```
```
 traffic-policy test inbound link-layer
```
```
#
```
```
return
```