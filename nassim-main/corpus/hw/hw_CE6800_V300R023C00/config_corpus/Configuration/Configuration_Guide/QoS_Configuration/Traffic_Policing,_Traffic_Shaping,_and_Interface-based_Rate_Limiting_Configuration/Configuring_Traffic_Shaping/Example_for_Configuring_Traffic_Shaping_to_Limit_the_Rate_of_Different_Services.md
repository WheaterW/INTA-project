Example for Configuring Traffic Shaping to Limit the Rate of Different Services
===============================================================================

Example for Configuring Traffic Shaping to Limit the Rate of Different Services

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512850234__fig_dc_cfg_qos_013101), three servers are deployed to provide voice, video, and data services, and service packets traverse DeviceA, DeviceB, and DeviceC to reach the external network. The interface connected to the voice service host joins VLAN 10; the interface connected to the video service host joins VLAN 20; the interface connected to the data service host joins VLAN 30.

**Figure 1** Network diagram for configuring traffic shaping![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001563889773.png)

Packets of voice, video, and data services are identified by 802.1p priorities 5, 3, and 2 respectively. However, jitter may occur when packets from interface 2 on DeviceB reach DeviceC. [Table 1](#EN-US_TASK_0000001512850234__table47091146357) lists the bandwidth requirements to limit jitter and ensure services.

**Table 1** Bandwidth for each service on DeviceB
| Service Type | CIR (kbit/s) | PIR (kbit/s) |
| --- | --- | --- |
| Voice | 3000 | 5000 |
| Video | 5000 | 8000 |
| Data | 2000 | 3000 |



#### Procedure

1. On DeviceB, create VLANs and add interfaces to these VLANs so that users can access the network through DeviceB.
   
   
   
   # Create VLANs 10, 20, and 30.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 10 20 30
   [*DeviceB] commit
   ```
   
   # Set the access mode of interfaces 100GE 1/0/1 and 100GE 1/0/2 to trunk, and add them to VLANs 10, 20, and 30.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] portswitch
   [~DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 10 20 30
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] portswitch
   [~DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 10 20 30
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
2. Set priorities for DeviceA's interfaces connected to the hosts to differentiate packets of different services.
   
   
   
   # On DeviceA, set the priorities of 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3 to 5, 3, and 2, respectively, and add 100GE 1/0/4 to VLANs 10, 20, and 30.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 10 20 30
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] port default vlan 10
   [*DeviceA-100GE1/0/1] port priority 5
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] portswitch
   [~DeviceA-100GE1/0/2] port default vlan 20
   [*DeviceA-100GE1/0/2] port priority 3
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/3
   [~DeviceA-100GE1/0/3] portswitch
   [~DeviceA-100GE1/0/3] port default vlan 30
   [*DeviceA-100GE1/0/3] port priority 2
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/4
   [~DeviceA-100GE1/0/4] portswitch
   [~DeviceA-100GE1/0/4] port link-type trunk
   [*DeviceA-100GE1/0/4] port trunk allow-pass vlan 10 20 30
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] commit
   ```
3. Configure queue-based traffic shaping to limit the bandwidth of voice, video, and data services.
   
   
   
   # Configure queue-based traffic shaping on DeviceB. Set the CIR values of voice, video, and data services to 3000 kbit/s, 5000 kbit/s, and 2000 kbit/s, respectively, and their PIR values to 5000 kbit/s, 8000 kbit/s, and 3000 kbit/s, respectively.
   
   ```
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] qos queue 5 shaping cir 3000 pir 5000 kbps 
   [*DeviceB-100GE1/0/2] qos queue 3 shaping cir 5000 pir 8000 kbps
   [*DeviceB-100GE1/0/2] qos queue 2 shaping cir 2000 pir 3000 kbps 
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Display statistics about queues in the outbound direction on 100GE 1/0/2.

```
[~DeviceB] display qos queue statistics interface 100ge 1/0/2
 Queue   CIR/PIR              Passed     Pass Rate             Dropped     Drop Rate  Drop Time
        (% or kbps)   (Packets/Bytes)    (pps/bps)      (Packets/Bytes)    (pps/bps)                                                
 ----------------------------------------------------------------------------------------------
     0         0                   0             0                   0             0          -
        10000000                   0             0                   0             0
 ----------------------------------------------------------------------------------------------
     1         0                   0             0                   0             0          -
        10000000                   0             0                   0             0
 ----------------------------------------------------------------------------------------------
     2      2000                  54584           0                   0             0          -
            3000                  5676736         0                   0             0
 ----------------------------------------------------------------------------------------------
     3      5000                  49648           0                   0             0          -
            8000                  5163392          0                   0             0
 ----------------------------------------------------------------------------------------------
     4         0                   0             0                   0             0          -
        10000000                   0             0                   0             0
 ----------------------------------------------------------------------------------------------
     5      3000                 49998            0                   0             0          -
            5000                 5199792            0                   0             0
 ----------------------------------------------------------------------------------------------
     6         0                   0             0                   0             0          -
        10000000                   0             0                   0             0
 ----------------------------------------------------------------------------------------------
     7         0                   0             0                   0             0          -
        10000000                   0             0                   0             0
 ----------------------------------------------------------------------------------------------

```
#### Configuration Scripts

* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 10 20 30
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 10 20 30
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 10 20 30
   qos queue 2 shaping cir 2000 kbps pir 3000 kbps
   qos queue 3 shaping cir 5000 kbps pir 8000 kbps
   qos queue 5 shaping cir 3000 kbps pir 5000 kbps
  #
  return
  ```

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 10 20 30
  #
  interface 100GE1/0/1
   port default vlan 10
   port priority 5
  #
  interface 100GE1/0/2
   port default vlan 20
   port priority 3
  #
  interface 100GE1/0/3
   port default vlan 30
   port priority 2
  #
  interface 100GE1/0/4
   port link-type trunk
   port trunk allow-pass vlan 10 20 30
  #
  return
  ```