Example for Configuring eMDI Detection for a Common Layer 3 Multicast Service
=============================================================================

This section provides an example for configuring eMDI detection for common Layer 3 multicast services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0174518879__fig_dc_vrp_multicast_cfg_227201), IPTV programs are provided for host users in multicast mode. eMDI detection is deployed on Device A, Device B, Device C, and Device D to monitor the quality of IPTV service packets. Network O&M personnel can check the detection results reported by the devices through telemetry in real time on the monitor platform, quickly demarcating and locating faults.

In this example, PIM-DM is deployed on the network.

**Figure 1** Configuring basic PIM-DM functions![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0174640639.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IP addresses to interfaces and configure a unicast routing protocol.
2. Configure PIM-DM.
3. Configure eMDI detection.
   1. Configure eMDI to monitor a channel group.
   2. Configure eMDI to monitor a board group.
   3. Bind the channel group to the board group.
4. Configure telemetry.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group G address: 225.1.1.1/24
* Multicast source S address: 10.1.4.100/24
* Version number of IGMP running between the Router and user hosts: 2
* Name of the channel group monitored by eMDI: IPTV-channel
* Name of the board group monitored by eMDI: IPTV-lpu

#### Procedure

1. Assign IP addresses to Router interfaces and configure a unicast routing protocol. For configuration details, see [Configuration Files](#EN-US_TASK_0174518879__example_dc_vrp_multicast_cfg_227201) in this section.
2. Configure PIM-DM.
   
   
   * Enable multicast on each device and PIM-DM on each interface.
     
     # Configure Device A.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] sysname DeviceA
     ```
     ```
     [*HUAWEI] commit
     ```
     ```
     [~DeviceA] multicast routing-enable
     ```
     ```
     [*DeviceA] interface gigabitethernet 0/1/0
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/0] pim dm
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/0] quit
     ```
     ```
     [*DeviceA] interface gigabitethernet 0/1/1
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/1] pim dm
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/1] quit
     ```
     ```
     [*DeviceA] commit
     ```
     
     The configurations of Device B, Device C, and Device D are similar to the configuration of Device A. For configuration details, see [Configuration Files](#EN-US_TASK_0174518879__example_dc_vrp_multicast_cfg_227201).
   * Configure IGMP on the Router interfaces connected to the user hosts.
     
     # Configure Device C.
     
     ```
     [~DeviceC] interface gigabitethernet 0/1/0
     ```
     ```
     [~DeviceC-GigabitEthernet0/1/0] igmp enable
     ```
     ```
     [*DeviceC-GigabitEthernet0/1/0] igmp static-group 225.1.1.1
     ```
     ```
     [*DeviceC-GigabitEthernet0/1/0] quit
     ```
     ```
     [*DeviceC] commit
     ```
     
     # Configure Device D.
     
     ```
     [~DeviceD] interface gigabitethernet 0/1/1
     ```
     ```
     [~DeviceD-GigabitEthernet0/1/1] igmp enable
     ```
     ```
     [*DeviceD-GigabitEthernet0/1/1] igmp static-group 225.1.1.1
     ```
     ```
     [*DeviceD-GigabitEthernet0/1/1] quit
     ```
     ```
     [*DeviceD] commit
     ```
   
   After completing the configuration, run the following commands to check whether the multicast service is configured successfully.
   
   * Run the **display pim interface** command to check the PIM-DM configuration and status of each Router interface. The following example uses the command output on Device B.
     ```
     <DeviceB> display pim interface
     ```
     ```
      VPN-Instance: public net
      Interface           State NbrCnt HelloInt     DR-Pri     DR-Address      
      GE0/1/0             up         1       30          1     10.1.1.2 (local) 
      GE0/1/1             up         1       30          1     10.1.2.2         
      GE0/1/2             up         1       30          1     10.1.3.2 
     ```
   * Run the **display pim neighbor** command to check the PIM-DM neighbor relationship between Routers. The following example uses the command output on Device B.
     ```
     <DeviceB> display pim neighbor
     ```
     ```
     VPN-Instance: public net
      Total Number of Neighbors = 3 
     
             Neighbor           Interface   Uptime  Expires  Dr-Priority BFD-Session 
             10.1.1.1            GE0/1/0  04:34:59 00:01:18            1           N
             10.1.2.2            GE0/1/1  04:29:56 00:01:23            1           N
             10.1.3.2            GE0/1/2  04:24:22 00:01:28            1           N
     ```
   * Run the **display pim routing-table** command to check the PIM routing table of each Router. Assume that both user A and user B need to receive information about multicast group G (225.1.1.1/24). When multicast source S (10.1.4.100/24) sends multicast data to multicast group G, a multicast distribution tree (MDT) is generated through flooding. Each Router on the MDT path has (S, G) entries. When user A and user B join multicast group G, Device C and Device D generate (\*, G) entries. The command output on each Router is as follows:
     ```
     <DeviceA> display pim routing-table
     ```
     ```
      VPN-Instance: public net
      Total 0 (*, G) entry; 1 (S, G) entry
     
      (10.1.4.100, 225.1.1.1)
          Protocol: pim-dm, Flag: LOC ACT 
          UpTime: 00:08:18     
          Upstream interface: GigabitEthernet0/1/1
              Upstream neighbor: NULL
              RPF prime neighbor: NULL
          Downstream interface(s) information:
          Total number of downstreams: 1
             1: GigabitEthernet0/1/0
                  Protocol: pim-dm, UpTime: 00:08:18, Expires: never
     ```
     ```
     <DeviceB> display pim routing-table
     ```
     ```
      VPN-Instance: public net
      Total 0 (*, G) entry; 1 (S, G) entry
     
      (10.1.4.100, 225.1.1.1)
          Protocol: pim-dm, Flag: ACT 
          UpTime: 00:10:25     
          Upstream interface: GigabitEthernet0/1/0
              Upstream neighbor: 10.1.1.1
              RPF prime neighbor: 10.1.1.1
          Downstream interface(s) information:
          Total number of downstreams: 2
             1: GigabitEthernet0/1/1
                  Protocol: pim-dm, UpTime: 00:06:48, Expires: never 
             2: GigabitEthernet0/1/2
                  Protocol: pim-dm, UpTime: 00:05:53, Expires: never 
     ```
     ```
     <DeviceC> display pim routing-table
     ```
     ```
      VPN-Instance: public net
      Total 1 (*, G) entry; 1 (S, G) entry
     
      (*, 225.1.1.1)
          Protocol: pim-dm, Flag: WC 
          UpTime: 00:11:47     
          Upstream interface: NULL
              Upstream neighbor: NULL
              RPF prime neighbor: NULL
          Downstream interface(s) information:
          Total number of downstreams: 1
             1: GigabitEthernet0/1/0
                  Protocol: static, UpTime: 00:11:47, Expires: never 
     
      (10.1.4.100, 225.1.1.1)
          Protocol: pim-dm, Flag: ACT 
          UpTime: 00:17:13     
          Upstream interface: GigabitEthernet0/1/1
              Upstream neighbor: 10.1.2.1
              RPF prime neighbor: 10.1.2.1
          Downstream interface(s) information:
          Total number of downstreams: 1
             1: GigabitEthernet0/1/0
                  Protocol: pim-dm, UpTime: 00:11:47, Expires: -
     ```
     ```
     <DeviceD> display pim routing-table
     ```
     ```
      VPN-Instance: public net
      Total 1 (*, G) entry; 1 (S, G) entry
     
      (*, 225.1.1.1)
          Protocol: pim-dm, Flag: WC 
          UpTime: 00:05:26     
          Upstream interface: NULL
              Upstream neighbor: NULL
              RPF prime neighbor: NULL
          Downstream interface(s) information:
          Total number of downstreams: 1
             1: GigabitEthernet0/1/1
                  Protocol: static, UpTime: 00:05:26, Expires: never 
     
      (10.1.4.100, 225.1.1.1)
          Protocol: pim-dm, Flag: ACT 
          UpTime: 00:09:58     
          Upstream interface: GigabitEthernet0/1/2
              Upstream neighbor: 10.1.3.1
              RPF prime neighbor: 10.1.3.1
          Downstream interface(s) information:
          Total number of downstreams: 1
             1: GigabitEthernet0/1/1
                  Protocol: pim-dm, UpTime: 00:05:26, Expires: - 
     ```
3. Configure eMDI detection.
   
   
   
   The following uses the configuration of Device A as an example. The configurations of Device B, Device C, and Device D are similar to the configuration of Device A. For configuration details, see [Configuration Files](#EN-US_TASK_0174518879__example_dc_vrp_multicast_cfg_227201).
   
   # Configure eMDI to monitor a channel group.
   
   ```
   [~DeviceA] emdi
   ```
   ```
   [~DeviceA-emdi] emdi channel-group IPTV-channel
   ```
   ```
   [*DeviceA-emdi-channel-group-IPTV-channel] emdi channel 1 source 10.1.4.100 group 225.1.1.1 pt 33 clock-rate 90kHz
   ```
   ```
   [*DeviceA-emdi-channel-group-IPTV-channel] quit
   ```
   ```
   [*DeviceA-emdi] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure eMDI to monitor a board group.
   
   ```
   [~DeviceA] emdi
   ```
   ```
   [~DeviceA-emdi] emdi lpu-group IPTV-lpu
   ```
   ```
   [*DeviceA-emdi-lpu-group-IPTV-lpu] emdi bind slot all
   ```
   ```
   [*DeviceA-emdi-lpu-group-IPTV-lpu] quit
   ```
   ```
   [*DeviceA-emdi] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Bind the channel group to the board group.
   
   ```
   [~DeviceA] emdi
   ```
   ```
   [~DeviceA-emdi] emdi bind channel-group IPTV-channel lpu-group IPTV-lpu
   ```
   ```
   [~DeviceA-emdi] emdi bind channel-group IPTV-channel lpu-group IPTV-lpu outbound
   ```
   ```
   [*DeviceA-emdi] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   After completing the configuration, run the [**display emdi statistics history**](cmdqueryname=display+emdi+statistics+history) command to check the detection result when multicast traffic passes through DeviceA.
   
   * Check the detection result in the inbound direction.
     ```
     <DeviceA> display emdi statistics history channel 1 start 3 end 5
     ```
     ```
     Channel Name   : 1 
     Total Records  : 3         Latest Rate(pps) : 0                   Latest Detect Time : 2021-02-18 21:22:40
     ---------------------------------------------------------------------------------------------------------------------------------------------------------
      Record          Record        Monitor     Monitor    Received      Ra
     te         Rate         RTP-LC       RTP-SE       RTP-LR       RTP-SER        RTP   
      Index           Time         Period(s)    Status     Packets       pps          bps                                   (1/100000)   (1/100000)    Jitter(ms)
     ---------------------------------------------------------------------------------------------------------------------------------------------------------
      3        2019-02-02:08-33-00     60      Normal      4393232      439323     4871215641       6700          6633         152           151           0         
      4        2019-02-02:08-32-00     60      Normal      4388533      438853     4866005390       6700          6633         152           151           0         
      5        2019-02-02:08-31-00     60      Normal      4388218      438821     4865656118       6700          6633         152           151           0         
     ---------------------------------------------------------------------------------------------------------------------------------------------------------
     ```
   * Check the detection result in the outbound direction.
     ```
     <DeviceA> display emdi statistics history outbound channel 1 start 3 end 5 slot 1
     ```
     ```
     Channel Name   : 1 
     Total Records  : 3         Latest Rate(pps) : 0                   Latest Detect Time : 2021-02-18 21:22:40
     ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      Record          Record        Monitor     Monitor    Received      Rate         Rate         RTP-LC       RTP-SE       RTP-LR       RTP-SER        RTP             Interface
      Index           Time         Period(s)    Status     Packets       pps          bps                                   (1/100000)   (1/100000)    Jitter(ms)
     ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      3        2019-02-02:08-33-00     60      Normal      4393232      439323     4871215641       6700          6633         152           151           0       GigabitEthernet0/1/0 
      4        2019-02-02:08-32-00     60      Normal      4388533      438853     4866005390       6700          6633         152           151           0       GigabitEthernet0/1/0 
      5        2019-02-02:08-31-00     60      Normal      4388218      438821     4865656118       6700          6633         152           151           0       GigabitEthernet0/1/0 
     ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     ```
4. Configure telemetry.
   
   
   
   The following uses the configuration of Device A as an example. The configurations of Device B, Device C, and Device D are similar to the configuration of Device A. For configuration details, see [Configuration Files](#EN-US_TASK_0174518879__example_dc_vrp_multicast_cfg_227201) (Only key configurations are provided here. For details, see Telemetry Configuration).
   
   # Configure a destination collector.
   
   ```
   [~DeviceA] telemetry
   ```
   ```
   [~DeviceA-telemetry] destination-group Monitor
   ```
   ```
   [*DeviceA-telemetry-destination-group-Monitor] ipv4-address 10.1.7.2 port 10001 protocol grpc
   ```
   ```
   [*DeviceA-telemetry-destination-group-Monitor] commit
   ```
   ```
   [*DeviceA-telemetry-destination-group-Monitor] quit
   ```
   
   # Configure a sampling path.
   
   ```
   [~DeviceA-telemetry] sensor-group emdimonitor
   ```
   ```
   [*DeviceA-telemetry-sensor-group-emdimonitor] sensor-path huawei-emdi:emdi/emdi-telem-reps/emdi-telem-rep
   ```
   ```
   [*DeviceA-telemetry-sensor-group-emdimonitor] sensor-path huawei-emdi:emdi/emdi-telem-rtps/emdi-telem-rtp
   ```
   ```
   [*DeviceA-telemetry-sensor-group-emdimonitor] sensor-path huawei-emdi:emdi/out-telem-reps/out-telem-rep
   ```
   ```
   [*DeviceA-telemetry-sensor-group-emdimonitor] commit
   ```
   ```
   [*DeviceA-telemetry-sensor-group-emdimonitor] quit
   ```
   
   # Create a static subscription.
   
   ```
   [~DeviceA-telemetry] subscription EMDI
   ```
   ```
   [*DeviceA-telemetry-subscription-EMDI] sensor-group emdimonitor
   ```
   ```
   [*DeviceA-telemetry-subscription-EMDI] destination-group Monitor
   ```
   ```
   [*DeviceA-telemetry-subscription-EMDI] commit
   ```
   
   After completing the configuration, check the real-time detection result reported through telemetry on the monitor platform.

#### Configuration Files

* Device A configuration file
  
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
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   pim dm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.4.1 255.255.255.0
  ```
  ```
   pim dm
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.1.4.0 0.0.0.255
  ```
  ```
  #
  emdi
   emdi channel-group IPTV-channel
    emdi channel 1 source 10.1.4.100 group 225.1.1.1 pt 33 clock-rate 90kHz
   emdi lpu-group _default_
    emdi bind slot all
   emdi lpu-group IPTV-lpu
    emdi bind slot all
   emdi bind channel-group IPTV-channel lpu-group IPTV-lpu
   emdi bind channel-group IPTV-channel lpu-group IPTV-lpu outbound
  #
  telemetry
   #
   sensor-group emdimonitor
    sensor-path huawei-emdi:emdi/emdi-telem-reps/emdi-telem-rep
    sensor-path huawei-emdi:emdi/emdi-telem-rtps/emdi-telem-rtp
    sensor-path huawei-emdi:emdi/out-telem-reps/out-telem-rep
  #
   destination-group Monitor
    ipv4-address 10.1.7.2 port 10001 protocol grpc
   #
   subscription EMDI
    sensor-group emdimonitor
    destination-group Monitor
  #
  ```
  ```
  return
  ```
* Device B configuration file
  
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
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   pim dm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.1 255.255.255.0
  ```
  ```
   pim dm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.3.1 255.255.255.0
  ```
  ```
   pim dm
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.1.2.0 0.0.0.255
  ```
  ```
    network 10.1.3.0 0.0.0.255
  ```
  ```
  #
  emdi
   emdi channel-group IPTV-channel
    emdi channel 1 source 10.1.4.100 group 225.1.1.1 pt 33 clock-rate 90kHz
   emdi lpu-group _default_
    emdi bind slot all
   emdi lpu-group IPTV-lpu
    emdi bind slot all
   emdi bind channel-group IPTV-channel lpu-group IPTV-lpu
   emdi bind channel-group IPTV-channel lpu-group IPTV-lpu outbound
  #
  telemetry
   #
   sensor-group emdimonitor
    sensor-path huawei-emdi:emdi/emdi-telem-reps/emdi-telem-rep
    sensor-path huawei-emdi:emdi/emdi-telem-rtps/emdi-telem-rtp
  #
   destination-group Monitor
    ipv4-address 10.1.7.2 port 10001 protocol grpc
   #
   subscription EMDI
    sensor-group emdimonitor
    destination-group Monitor
  #
  ```
  ```
  return
  ```
* Device C configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.5.1 255.255.255.0
  ```
  ```
   pim dm
  ```
  ```
   igmp enable
  ```
  ```
   igmp static-group 225.1.1.1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.2 255.255.255.0
  ```
  ```
   pim dm
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.2.0 0.0.0.255
  ```
  ```
    network 10.1.5.0 0.0.0.255
  ```
  ```
  #
  emdi
   emdi channel-group IPTV-channel
    emdi channel 1 source 10.1.4.100 group 225.1.1.1 pt 33 clock-rate 90kHz
   emdi lpu-group _default_
    emdi bind slot all
   emdi lpu-group IPTV-lpu
    emdi bind slot all
   emdi bind channel-group IPTV-channel lpu-group IPTV-lpu
   emdi bind channel-group IPTV-channel lpu-group IPTV-lpu outbound
  #
  telemetry
   #
   sensor-group emdimonitor
    sensor-path huawei-emdi:emdi/emdi-telem-reps/emdi-telem-rep
    sensor-path huawei-emdi:emdi/emdi-telem-rtps/emdi-telem-rtp
  #
   destination-group Monitor
    ipv4-address 10.1.7.2 port 10001 protocol grpc
   #
   subscription EMDI
    sensor-group emdimonitor
    destination-group Monitor
  #
  ```
  ```
  return
  ```
* Device D configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.6.1 255.255.255.0
  ```
  ```
   pim dm
  ```
  ```
   igmp enable
  ```
  ```
   igmp static-group 225.1.1.1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.3.2 255.255.255.0
  ```
  ```
   pim dm
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.3.0 0.0.0.255
  ```
  ```
    network 10.1.6.0 0.0.0.255
  ```
  ```
  #
  emdi
   emdi channel-group IPTV-channel
    emdi channel 1 source 10.1.4.100 group 225.1.1.1 pt 33 clock-rate 90kHz
   emdi lpu-group _default_
    emdi bind slot all
   emdi lpu-group IPTV-lpu
    emdi bind slot all
   emdi bind channel-group IPTV-channel lpu-group IPTV-lpu
   emdi bind channel-group IPTV-channel lpu-group IPTV-lpu outbound
  #
  telemetry
   #
   sensor-group emdimonitor
    sensor-path huawei-emdi:emdi/emdi-telem-reps/emdi-telem-rep
    sensor-path huawei-emdi:emdi/emdi-telem-rtps/emdi-telem-rtp
  #
   destination-group Monitor
    ipv4-address 10.1.7.2 port 10001 protocol grpc
   #
   subscription EMDI
    sensor-group emdimonitor
    destination-group Monitor
  #
  ```
  ```
  return
  ```