Example for Configuring IFIT Measurement
========================================

Example for Configuring IFIT Measurement

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TOPIC_0000001563885161__fig_dc_vrp_feature_new_ipfpm_000702), users want to use the NMS to monitor network traffic in real time to quickly detect abnormal traffic and locate faults. You can configure IFIT measurement on devices so that the devices can periodically send packet loss and delay measurement information to the NMS for summary, analysis, and display.

**Figure 1** Network diagram of IFIT measurement![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001679310761.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure packet loss and delay measurement on the link between DeviceA and DeviceC to periodically collect packet loss and delay measurement data.
   * Configure the IFIT NE ID, NE role, conversion period, and aging time of measurement flows.
   * Configure an IFIT traffic classifier and a traffic behavior and bind them to an IFIT traffic policy, and then apply the policy.
2. Configure the devices to send measurement data to the NMS through telemetry.

![](public_sys-resources/note_3.0-en-us.png) 

Before performing IFIT measurement, ensure that:

* Static routes or dynamic routing protocols have been configured on the devices to ensure network connectivity between the devices.
* 1588v2 has been configured on the devices to implement clock synchronization between the devices. For details, see *1588v2 (PTP) Configuration*. (Before enabling delay measurement, you must configure 1588v2. Delay measurement is unavailable in scenarios where NTP or high-precision NTP is configured due to inaccurate timestamp information.)
* The devices have been connected to the NMS.

Only IFIT-related configurations are listed here.



#### Procedure

1. Configure packet loss and delay measurement on the link between DeviceA and DeviceC to periodically collect packet loss and delay measurement data.
   
   DeviceA and DeviceC need to be configured as both ingress and egress nodes. DeviceB retains the default role (transit node) and the IFIT traffic policy does not need to be applied. interface2 on DeviceA and interface1 on DeviceC are configured as transit ports. The following example describes the configuration of DeviceA. The configurations of other devices are similar. For details, see [Configuration Scripts](#EN-US_TOPIC_0000001563885161__section374261012444).
   
   # Configure IP addresses for interfaces.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   [~DeviceA] interface 100ge1/0/2
   [~DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.1.2.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure an ACL rule.
   
   ```
   [~DeviceA] acl number 3001
   [~DeviceA-acl4-advance-3001] rule permit tcp source 192.168.1.0 32 destination 192.168.100.0 32 source-port eq 200 
   [*DeviceA-acl4-advance-3001] quit
   [*DeviceA] commit
   ```
   # Configure IFIT measurement.
   ```
   [~DeviceA] ifit
   [*DeviceA-ifit] dcn-instance
   [*DeviceA-ifit-dcn-instance] node-id 10
   [*DeviceA-ifit-dcn-instance] role ingress-egress
   [*DeviceA-ifit-dcn-instance] transit-port interface 100ge1/0/2
   [*DeviceA-ifit-dcn-instance] interval 60
   [*DeviceA-ifit-dcn-instance] aging-time 120
   [*DeviceA-ifit-dcn-instance] traffic classifier c1
   [*DeviceA-ifit-dcn-instance-classifier-c1] if-match acl 3001
   [*DeviceA-ifit-dcn-instance-classifier-c1] quit
   [*DeviceA-ifit-dcn-instance] traffic behavior b1
   [*DeviceA-ifit-dcn-instance-behavior-b1] delay-measure per-packet enable    
   [*DeviceA-ifit-dcn-instance-behavior-b1] quit
   [*DeviceA-ifit-dcn-instance] traffic policy p1
   [*DeviceA-ifit-dcn-instance-policy-p1] classifier c1 behavior b1 precedence 1 cache-number 512 
   [*DeviceA-ifit-dcn-instance-policy-p1] quit
   [*DeviceA-ifit-dcn-instance] quit
   [*DeviceA-ifit] quit
   [*DeviceA] ifit traffic-policy p1 global 
   [*DeviceA] commit
   ```
2. Configure the devices to send measurement data to the NMS through telemetry. The following example describes the configuration of DeviceA. The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA.
   ```
   [~DeviceA] telemetry
   [*DeviceA-telemetry] destination-group ifit
   [*DeviceA-telemetry-destination-group-ifit] ipv4-address 10.10.10.10 port 10001 protocol udp
   [*DeviceA-telemetry-destination-group-ifit] quit
   [*DeviceA-telemetry] sensor-group ifit
   [*DeviceA-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic 
   [*DeviceA-telemetry-sensor-group-ipas-path] quit
   [*DeviceA-telemetry-sensor-group-ifit] sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic 
   [*DeviceA-telemetry-sensor-group-ipas-path] quit
   [*DeviceA-telemetry-sensor-group-ifit] quit
   [*DeviceA-telemetry] subscription ifit
   [*DeviceA-telemetry-subscription-ifit] sensor-group ifit
   [*DeviceA-telemetry-subscription-ifit] destination-group ifit 
   [*DeviceA-telemetry-subscription-ifit] quit
   [*DeviceA-telemetry] quit
   [*DeviceA-telemetry-subscription-ifit] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to configure devices to send data using the secure TLS encryption mode. For details, see *Telemetry Configuration*.


#### Verifying the Configuration

# Display the ACL delivery status of IFIT policies on DeviceA.

```
[~DeviceA] display ifit policy name p1 acl applied-record slot 1
Slot          : 1
TotalRecords  : 1
PolicyName    : p1
Interface     : -
----------------------------------------------------------------------------------------------
Protocol     AclNumber       AclName        RuleId     State     
----------------------------------------------------------------------------------------------
IPv4              3001       -                   5     Success   
----------------------------------------------------------------------------------------------
Fail reason:
   1 -- Insufficient resources
   2 -- Unsupported information
   3 -- Reaches the upper limit (256)
   4 -- The sub-interface configuration is incomplete
```

After the preceding configurations are complete and IFIT measurement is performed on traffic passing through DeviceA, you can view IFIT flow table information on DeviceA.

# Display detailed information about IFIT flow tables on DeviceA.

```
[~DeviceA] display ifit flow-cache slot 1
FlowID             : 1056910
StreamStatus       : Active 
PacketType         : IPv4
SrcAddress         : 192.168.1.0
DstAddress         : 192.168.100.0
Protocol           : UDP
AggretionType      : SourcePort
L4SrcPort          : -
L4DstPort          : 123
Direction          : Inbound
InterfaceName      : 100GE1/0/1
FlowStartTime      : 2021-11-13 17:39:32
FlowUpdateTime     : 2021-11-13 17:45:40
TTL                : 254
TunnelType         : Native
VNI                : 0
OuterTTL           : 253
VLAN               : 100
DQP                : -
-----------------------------------------------------------------------------------------------------------------------
Loss    PeriodID   PacketCounter   ByteCounter   TimeStamp(s)  TimeStamp(ns)  MeanDelay(ns)  MaxDelay(ns)  WarningInfo
-----------------------------------------------------------------------------------------------------------------------
   0    28213076           14109       1551880     1692895125      591623218           1024          1024  0x100000004
   1    28213077           14109       1551880     1692895145      591623218           1024          1024  0x100000004
-----------------------------------------------------------------------------------------------------------------------
```

# Display statistics in IFIT flow tables on DeviceA.

```
[~DeviceA] display ifit flow-cache statistics slot 1
-------------------------------------------------------------------------------
StreamType    Current         Aged        Created        Cleared       Exported
-------------------------------------------------------------------------------
IPv4              2              0              2              0              0
-------------------------------------------------------------------------------
IPv6              0              0              0              0              0
-------------------------------------------------------------------------------
Tunnel-IPv4       0              0              0              0              0
-------------------------------------------------------------------------------
Tunnel-IPv6       0              0              0              0              0
-------------------------------------------------------------------------------
```


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
  #
  acl number 3001
   #
    rule permit tcp source 192.168.1.0 32 destination 192.168.100.0 32 source-port eq 200
  #
  ifit
   #
   dcn-instance
    interval 60
    aging-time 120
    node-id 10
    role ingress-egress
    transit-port interface 100GE1/0/2
    #
    traffic classifier c1
     if-match acl 3001
    #
    traffic behavior b1
     delay-measure per-packet enable  
    #
    traffic policy p1
     classifier c1 behavior b1 precedence 2 cache-number 512
  #
  ifit traffic-policy p1 global
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   #
   destination-group ifit
    ipv4-address 10.10.10.10 port 10001 protocol udp
   #
   subscription ifit
    sensor-group ifit
    destination-group ifit 
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.2 255.255.255.0
  #
  ifit
   #
   dcn-instance
    interval 60
    aging-time 120
    node-id 20
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   #
   destination-group ifit
    ipv4-address 10.10.10.10 port 10001 protocol udp
   #
   subscription ifit
    sensor-group ifit
    destination-group ifit
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.3.3 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.4.3 255.255.255.0
  #
  acl number 3001
   #
    rule permit tcp source 192.168.1.0 32 destination 192.168.100.0 32 source-port eq 200
  #
  ifit
   #
   dcn-instance
    interval 60
    aging-time 120
    node-id 30
    role ingress-egress
    transit-port interface 100GE1/0/1
    #
    traffic classifier c1
     if-match acl 3001
    #
    traffic behavior b1
     delay-measure per-packet enable  
    #
    traffic policy p1
     classifier c1 behavior b1 precedence 2 cache-number 512
  #
  ifit traffic-policy p1 global
  #
  telemetry
   #
   sensor-group ifit
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-hop-statistics/flow-hop-statistic
    sensor-path huawei-ifit:ifit/huawei-ifit-statistics:flow-statistics/flow-statistic
   #
   destination-group ifit
    ipv4-address 10.10.10.10 port 10001 protocol udp
   #
   subscription ifit
    sensor-group ifit
    destination-group ifit
  ```