Example for Configuring Congestion Avoidance and Congestion Management (PQ+WDRR Scheduling and WRED Profile)
============================================================================================================

Example for Configuring Congestion Avoidance and Congestion Management (PQ+WDRR Scheduling and WRED Profile)

#### Networking Requirements

DeviceB is connected to DeviceA through interface 1. The 802.1p priorities of voice, video, and data service packets from the Internet are 6, 5, and 2, respectively. Packets of these services can reach users through DeviceA and DeviceB, as shown in [Figure 1](#EN-US_TASK_0000001608850085__fig36095521882). Because the rate of the inbound interface interface 1 on DeviceB is higher than the rates of outbound interfaces interface 2 and interface 3, congestion may occur on the two outbound interfaces.

To reduce the impact of network congestion and guarantee high-priority and latency-sensitive services, set congestion avoidance and congestion management parameters according to [Table 1](#EN-US_TASK_0000001608850085__tab_dc_cfg_qos_014701) and [Table 2](#EN-US_TASK_0000001608850085__tab_dc_cfg_qos_014702).

**Table 1** Congestion avoidance parameter settings
| Service Type | Color | Lower Threshold (%) | Upper Threshold (%) | Drop Probability |
| --- | --- | --- | --- | --- |
| Voice | Green | 80 | 100 | 10 |
| Video | Yellow | 60 | 80 | 20 |
| Data | Red | 40 | 60 | 40 |


**Table 2** Congestion management parameter settings
| Service Type | CoS Value | WDRR |
| --- | --- | --- |
| Voice | EF | 0 |
| Video | AF3 | 100 |
| Data | AF1 | 50 |


**Figure 1** Network diagram for configuring congestion avoidance and congestion management![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001634345337.png)

#### Procedure

1. Configure VLANs for each interface so that devices can communicate with each other at the link layer.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 2 5 6
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 2 5 6
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 2 5 6
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type trunk
   [*DeviceB-100GE1/0/3] port trunk allow-pass vlan 2 5 6
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
2. Configure priority mapping to map 802.1p values in voice, video, and data packets to different CoS values and colors.
   
   
   
   # Create DiffServ domain **ds1**, map 802.1p values 6, 5, and 2 to CoS values EF, AF3, and AF1, respectively, and color the packets green, yellow, and red, respectively.
   
   ```
   [~DeviceB] diffserv domain ds1
   [*DeviceB-dsdomain-ds1] 8021p-inbound 6 phb ef green
   [*DeviceB-dsdomain-ds1] 8021p-inbound 5 phb af3 yellow
   [*DeviceB-dsdomain-ds1] 8021p-inbound 2 phb af1 red
   [*DeviceB-dsdomain-ds1] quit
   ```
   
   # Bind the DiffServ domain to the inbound interface 100GE 1/0/1 of DeviceB.
   
   ```
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] trust 8021p inner
   [*DeviceB-100GE1/0/1] trust upstream ds1
   [*DeviceB-100GE1/0/1] quit
   ```
3. Configure congestion avoidance.
   
   
   
   # On DeviceB, create WRED drop profile **wred1** and set parameters for green, yellow, and red packets in the WRED drop profile.
   
   ```
   [*DeviceB] drop-profile wred1
   [*DeviceB-drop-wred1] color green low-limit 80 high-limit 100 discard-percentage 10  //Configure the WRED drop profile and set the upper and lower drop thresholds and maximum drop probability for green packets.
   [*DeviceB-drop-wred1] color yellow low-limit 60 high-limit 80 discard-percentage 20  //Configure the device to discard packets with the maximum drop probability of 20% when the percentage of the yellow packet length to the queue length reaches 60%. Configure the device to discard all newly arrived packets when the percentage of the yellow packet length to the queue length reaches 80%.
   [*DeviceB-drop-wred1] color red low-limit 40 high-limit 60 discard-percentage 40
   [*DeviceB-drop-wred1] quit
   ```
   
   # Apply WRED drop profile **wred1** to outbound interfaces 100GE 1/0/2 and 100GE 1/0/3 on DeviceB.
   
   ```
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] qos queue 5 wred wred1
   [*DeviceB-100GE1/0/2] qos queue 3 wred wred1
   [*DeviceB-100GE1/0/2] qos queue 1 wred wred1
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] qos queue 5 wred wred1
   [*DeviceB-100GE1/0/3] qos queue 3 wred wred1
   [*DeviceB-100GE1/0/3] qos queue 1 wred wred1
   [*DeviceB-100GE1/0/3] quit
   ```
4. Configure congestion management. Set scheduling parameters such as the scheduling mode and weight to implement differentiated scheduling for queues with different priorities.
   
   
   
   # Set scheduling parameters for queues with different CoS values on outbound interfaces 100GE 1/0/2 and 100GE 1/0/3 on DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] qos pq 5 to 7 drr 0 to 4  //Configure PQ scheduling for queues 5 to 7 and WDRR scheduling for queues 0 to 4.
   [*DeviceB-100GE1/0/2] qos queue 3 drr weight 100  //Set the WDRR scheduling weight of queue 3 to 100.
   [*DeviceB-100GE1/0/2] qos queue 1 drr weight 50  //Set the WDRR scheduling weight of queue 1 to 50. According to the preceding configurations, packets in queue 1 and queue 3 are scheduled based on the ratio of 1:2.
   [*DeviceB-100GE1/0/2] quit
   [~DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] qos pq 5 to 7 drr 0 to 4  //Configure PQ scheduling for queues 5 to 7 and WDRR scheduling for queues 0 to 4.
   [*DeviceB-100GE1/0/3] qos queue 3 drr weight 100  
   [*DeviceB-100GE1/0/3] qos queue 1 drr weight 50  
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   [~DeviceB] quit
   ```

#### Verifying the Configuration

# Check the configuration of DiffServ domain **ds1**.

```
<DeviceB> display diffserv domain name ds1
Diffserv domain name:ds1
 8021p-inbound 0 phb be green
 8021p-inbound 1 phb af1 green
 8021p-inbound 2 phb af1 red
 8021p-inbound 3 phb af3 green
 8021p-inbound 4 phb af4 green
 8021p-inbound 5 phb af3 yellow
 8021p-inbound 6 phb ef green
 8021p-inbound 7 phb cs7 green
 8021p-outbound be green map 0
 8021p-outbound be yellow map 0
 8021p-outbound be red map 0
 ...

```

In the DiffServ domain, 802.1p values 6, 5, and 2 are mapped to CoS values EF, AF3, and AF1, respectively, and packets are colored green, yellow, and red, respectively.

# Check the WRED drop profile configuration.

```
[DeviceB] display drop-profile name wred1
Drop-profile[7]: wred1
Color     Mode     Low-limit   High-limit  Unit  Discard(%)
-----------------------------------------------------------------
Green    Percentage    80       100         %       10
Yellow   Percentage    60        80         %       20
Red      Percentage    40        60         %       40
ECN      Percentage   100       100         %      100
-----------------------------------------------------------------

```

#### Configuration Scripts

DeviceB

```
#
sysname DeviceB
#
vlan batch 2 5 to 6
#
diffserv domain ds1
 8021p-inbound 2 phb af1 red
 8021p-inbound 5 phb af3 yellow
 8021p-inbound 6 phb ef green
#
drop-profile wred1
 color green low-limit 80 high-limit 100 discard-percentage 10
 color yellow low-limit 60 high-limit 80 discard-percentage 20
 color red low-limit 40 high-limit 60 discard-percentage 40
#
interface 100GE1/0/2
 port link-type trunk
 port trunk allow-pass vlan 2 5 to 6
 qos drr 0 to 4 
 qos queue 1 drr weight 50
 qos queue 3 drr weight 100
 qos queue 1 wred wred1
 qos queue 3 wred wred1
 qos queue 5 wred wred1
#
interface 100GE1/0/3
 port link-type trunk
 port trunk allow-pass vlan 2 5 to 6
 qos drr 0 to 4 
 qos queue 1 drr weight 50
 qos queue 3 drr weight 100
 qos queue 1 wred wred1
 qos queue 3 wred wred1
 qos queue 5 wred wred1
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 2 5 to 6
 trust upstream ds1
 trust 8021p inner
#
return
```