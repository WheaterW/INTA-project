Example for Configuring RMON
============================

When the volume of traffic on an interface exceeds a configured upper threshold, an alarm is sent to the NMS.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361439__fig_dc_vrp_rmon_cfg_001001), the subnet connected to GE 0/3/0 of the Device needs to be monitored, including:

* Collect real-time and historical statistics about various packets.
* Monitor broadcast and multicast traffic on the subnet and enable the alarm function for the total number of broadcast and multicast packets. When the total number of broadcast and multicast packets exceeds the configured threshold, the system actively reports alarm information to the NMS.

**Figure 1** Networking diagram for configuring RMON  
![](images/fig_dc_vrp_rmon_cfg_001001.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and Interface 2 in this example are GE 0/1/0 and GE 0/3/0 respectively.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Ensure that the Router and NMS are reachable.
2. Configure SNMP and community names and ensure that the Router can send trap messages to the NMS.
3. Configure the RMON statistics function and collect traffic statistics on interfaces.
4. Configure the RMON alarm function so that a trap message is sent to the NMS when the sampling value exceeds the set threshold.

#### Data Preparation

To complete the configuration, you need the following data:

* Index (1) of the RMON statistics function
* Owner (userA) for the RMON statistics function
* Sampling interval (30 seconds)
* Index (1) of the RMON alarm function
* OID ID (1.3.6.1.2.1.2.2.1.4.3) of a monitored object
* Upper threshold (1000) and lower threshold (100) for triggering an event
* Owner (userA) for the RMON alarm function

#### Procedure

1. Configure the Router and the NMS to be reachable.
2. Configure the Router to send trap messages to the NMS.
   
   
   
   # Enable SNMP to send trap messages to the NMS.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device] snmp-agent
   ```
   ```
   [*Device] snmp-agent trap enable
   ```
   
   # Configure the Router to send trap messages to the specified NMS.
   
   ```
   [*Device] snmp-agent target-host trap address udp-domain 10.1.1.1 params securityname public
   ```
   ```
   [*Device] commit
   ```
3. Configure the RMON statistics function.
   
   
   
   # Enable the RMON statistics function.
   
   ```
   [~Device] interface gigabitethernet 0/3/0
   ```
   ```
   [~Device-GigabitEthernet0/3/0] rmon-statistics enable
   ```
   ```
   [*Device-GigabitEthernet0/3/0] commit
   ```
   
   # Configure the Ethernet statistics function.
   
   ```
   [~Device-GigabitEthernet0/3/0] rmon statistics 1 owner userA
   ```
   ```
   [*Device-GigabitEthernet0/3/0] commit
   ```
   
   # Configure the historical traffic sampling function to sample the traffic on the subnet at an interval of 30 seconds and save the 10 most recent historical entries.
   
   ```
   [~Device-GigabitEthernet0/3/0] rmon history 1 buckets 10 interval 30 owner userA
   ```
   ```
   [*Device-GigabitEthernet0/3/0] commit
   ```
   ```
   [~Device-GigabitEthernet0/3/0] quit
   ```
4. Configure the RMON alarm function.
   
   
   
   # Configure the Router to send trap messages to the NMS when RMON event 1 occurs.
   
   ```
   [~Device] rmon event 1 description alarmofinterface trap public owner userA
   ```
   ```
   [*Device] commit
   ```
   
   # Set a sampling interval and thresholds for triggering event 1.
   
   ```
   [~Device] rmon alarm 1 1.3.6.1.2.1.2.2.1.4.3 5 absolute rising-threshold 1000 1 falling-threshold 100 1 owner userA
   ```
   ```
   [*Device] commit
   ```
   ```
   [~Device] quit
   ```
5. Verify the configuration.
   
   
   
   # Check data traffic information on the subnet.
   
   ```
   <Device> display rmon statistics gigabitethernet 0/3/0
   ```
   ```
   Statistics entry 1 owned by userA is valid.
     Interface : GigabitEthernet0/3/0<ifEntry.402653698>
     Received  :
     Octets              :4294966296, Packets:316091
     Broadcast packets   :311839    , Multicast packets:666
     Undersize packets   :0         , Oversize packets :0
     Fragments packets   :0         , Jabbers packets  :0
     CRC alignment errors:0         , Collisions       :0
     Dropped packets (insufficient resources):0
     Packets received according to length (octets):
     64     :0         ,  65-127  :0         ,  128-255  :0
     256-511:0         ,  512-1023:0         ,  1024-1518:0
   ```
   
   # Check historical sampling records.
   
   ```
   <Device> display rmon history gigabitethernet 0/3/0
   ```
   ```
   History control entry 1 owned by userA is valid
     Sampled interface     : GigabitEthernet0/3/0<ifEntry.402653698>
     Sampling interval     : 30(sec) with 10 buckets max
     Last Sampling time    : 0days 05h:17m:26s.30th
     Latest sampled values :
     Octets               :1000      , Packets           :100
     Broadcast packets    :100       , Multicast packets :100
     Undersize packets    :0         , Oversize packets  :0
     Fragments packets    :0         , Jabbers packets   :0
     CRC alignment errors :0         , Collisions        :0
     Dropped packet       :0         , Utilization       :0
     History record:
   
     Record No.1 (Sample time: 0days 05h:13m:56s.56th)
     Octets               :1000      , Packets           :100
     Broadcast packets    :100       , Multicast packets :100
     Undersize packets    :0         , Oversize packets  :0
     Fragments packets    :0         , Jabbers packets   :0
     CRC alignment errors :0         , Collisions        :0
     Dropped packets       :0         , Utilization       :0
   ```
   
   # Check RMON event information.
   
   ```
   <Device> display rmon event
   ```
   ```
   Event table 1 owned by userA is valid.
     Description: alarmofinterface.
     Will cause snmp-trap when triggered, last triggered at 1days 04h:00m:00s.04th
   ```
   
   # Check RMON alarm configurations.
   
   ```
   <Device> display rmon alarm 1
   ```
   ```
   Alarm table 1 owned by userA is valid.
    Samples absolute value : 1.3.6.1.2.1.2.2.1.4.3
    Sampling interval    : 5(sec)
    Rising threshold     : 1000(linked with event 1)
    Falling threshold    : 100(linked with event 1)
    When startup enables : risingOrFallingAlarm
    Latest value         : 1500
   ```

#### Configuration Files

```
#
sysname Device
#
interface GigabitEthernet0/1/0

 undo shutdown
 ip address 10.2.2.1 255.255.255.0
interface GigabitEthernet0/3/0
 undo shutdown
 ip address 10.3.3.1 255.255.255.0
 rmon-statistics enable
 rmon statistics 1 owner userA
 rmon history 1 buckets 10 interval 30 owner userA
#
ip route-static 10.1.1.0 255.255.255.0 10.2.2.2
#
snmp-agent
#
snmp-agent target-host trap address udp-domain 10.1.1.1 params securityname public
#
snmp-agent trap enable
#
rmon event 1 description alarmofinterface trap public owner userA
rmon alarm 1 1.3.6.1.2.1.2.2.1.4.3 5 absolute rising-threshold 1000 1 falling-threshold 100 1 owner userA
#
return
```