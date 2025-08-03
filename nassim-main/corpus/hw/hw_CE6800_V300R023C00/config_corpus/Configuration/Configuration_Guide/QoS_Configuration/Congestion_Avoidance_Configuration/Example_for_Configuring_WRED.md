Example for Configuring WRED
============================

Example for Configuring WRED

#### Networking Requirements

Host1 and Host2 provide voice, video, and data services, for which traffic is transmitted through DeviceB and then DeviceA. To reduce the impact of network congestion and guarantee high-priority, latency-sensitive services, set congestion avoidance parameters according to [Table 1](#EN-US_TASK_0000001512675202__tb_01).

**Table 1** Congestion avoidance parameters
| Service Type | Color | Lower Drop Threshold (%) | Upper Drop Threshold (%) | Drop Probability (%) | CoS |
| --- | --- | --- | --- | --- | --- |
| Voice | Green | 80 | 100 | 10 | EF |
| Video | Yellow | 60 | 80 | 20 | AF3 |
| Data | Red | 40 | 60 | 40 | AF1 |


**Figure 1** Network diagram of congestion avoidance![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001513034382.png)

#### Procedure

1. Configure VLANs for interfaces so that devices can communicate with each other at the link layer.
   
   
   
   # Configure 100GE 1/0/3 on DeviceB as a trunk interface. Add 100GE 1/0/1 to VLAN 100, 100GE 1/0/2 to VLAN 200, and 100GE 1/0/3 to VLAN 100 and VLAN 200.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 100 200
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port default vlan 100
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port default vlan 200
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type trunk
   [*DeviceB-100GE1/0/3] port trunk allow-pass vlan 100 200
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
2. Configure priority mapping to map 802.1p values in voice, data, and video packets to different CoS values and colors.
   
   
   
   # Create the DiffServ domain **ds1**, map 802.1p values 6, 5, and 2 to CoS values EF, AF3, and AF1, respectively, and color packets green, yellow, and red.
   
   ```
   [~DeviceB] diffserv domain ds1
   [*DeviceB-dsdomain-ds1] 8021p-inbound 6 phb ef green
   [*DeviceB-dsdomain-ds1] 8021p-inbound 5 phb af3 yellow
   [*DeviceB-dsdomain-ds1] 8021p-inbound 2 phb af1 red
   [*DeviceB-dsdomain-ds1] quit
   [*DeviceB] commit
   ```
   
   # Bind the DiffServ domain to the inbound interfaces 100GE 1/0/1 and 100GE 1/0/2 on DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] trust upstream ds1
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] trust upstream ds1
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
3. Configure a WRED drop profile to mitigate or eliminate congestion.
   
   
   
   # Create WRED drop profile **wred1** on DeviceB and set WRED parameters for green, yellow, and red packets in this drop profile.
   
   ```
   [~DeviceB] drop-profile wred1
   [*DeviceB-drop-wred1] color green low-limit 80 high-limit 100 discard-percentage 10
   [*DeviceB-drop-wred1] color yellow low-limit 60 high-limit 80 discard-percentage 20
   [*DeviceB-drop-wred1] color red low-limit 40 high-limit 60 discard-percentage 40
   [*DeviceB-drop-wred1] quit
   [*DeviceB] commit
   ```
   
   # Apply the WRED drop profile **wred1** to queues on the outbound interface of DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/3
   [~DeviceB-100GE1/0/3] qos queue 5 wred wred1
   [*DeviceB-100GE1/0/3] qos queue 3 wred wred1
   [*DeviceB-100GE1/0/3] qos queue 1 wred wred1
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the configuration of the DiffServ domain **ds1**. You can see that 802.1p values 6, 5, and 2 are mapped to CoS values EF, AF3, and AF1 and to colors green, yellow, and red, respectively.

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

# Check the configuration of the WRED drop profile **wred1**. You can see WRED parameter settings of green, yellow, and red packets in this profile.

```
<DeviceB> display drop-profile name wred1
Drop-profile[1]: wred1
Color    Mode         Low-limit   High-limit  Unit     Discard(%)
-----------------------------------------------------------------
Green    Percentage   80          100         %        10                       
Yellow   Percentage   60          80          %        20                       
Red      Percentage   40          60          %        40                       
ECN      Percentage   100         100         %        100  
-----------------------------------------------------------------

```
# Check the configuration of 100GE 1/0/3. You can see the scheduling parameters of queues with different CoS values.
```
<DeviceB> display qos configuration interface 100GE 1/0/3
 interface 100GE1/0/3
 --------------------------------------------------------------------------                                                         
 trust flag        : outer 8021p                                                                                                      
 diffserv domain   : default                                                                                                          
 dei enable        : disable
 port priority     : 0                                                                                                                
 phb marking 8021p : enable                                                                                                           
 phb marking dscp  : disable
 phb marking exp : -                                                                                                          
 port wred         : -                                                                                                                
 port lr           : cir = -, cbs = -                                                                                       
 port car inbound  : - 
 port car outbound : - 
 schedule profile : -                                                                                                                
 --------------------------------------------------------------------------                                                         
 queue          shaping       schedule     wred                                                                                     
             cir       pir                                                                                                          
             cbs       pbs                                                                                                          
 --------------------------------------------------------------------------                                                         
 0             -         -    pq          -                               
               -         -     

 1             -         -    pq          wred1                           
               -         -    

 2             -         -    pq          -                               
               -         -     

 3             -         -    pq          wred1                           
               -         -     

 4             -         -    pq          -                               
               -         -    

 5             -         -    pq           wred1                           
               -         -     

 6             -         -    pq          -                               
               -         -     

 7             -         -    pq          -                               
               -         -     

 --------------------------------------------------------------------------

```


#### Configuration Scripts

DeviceB

```
#
sysname DeviceB
#
drop-profile wred1
 color green low-limit 80 high-limit 100 discard-percentage 10
 color yellow low-limit 60 high-limit 80 discard-percentage 20
 color red low-limit 40 high-limit 60 discard-percentage 40
#
vlan batch 100 200
#
diffserv domain ds1
 8021p-inbound 2 phb af1 red
 8021p-inbound 5 phb af3 yellow
 8021p-inbound 6 phb ef green
#
interface 100GE1/0/1
 port default vlan 100
 trust upstream ds1
#
interface 100GE1/0/2
 port default vlan 200
 trust upstream ds1
#
interface 100GE1/0/3
 port link-type trunk
 port trunk allow-pass vlan 100 200
 qos queue 1 wred wred1
 qos queue 3 wred wred1
 qos queue 5 wred wred1
#
return
```