Example for Collecting Statistics About IPv6 Original Flows
===========================================================

This section provides an example for deploying NetStream to collect statistics about original flows. This example uses the configurations on an IPv6 network.

#### Networking Requirements

As the Internet continues to develop rapidly, carrier networks support higher bandwidth and predictable QoS parameters. As such, carriers need to provide finer-grained management and accounting services. To implement classified monitoring over networks more effectively, you can configure NetStream monitoring services to output traffic statistics collected on specified interfaces to specified NSCs and NDAs for analysis. This enables collected statistics to be output to multiple addresses.

As shown in [Figure 1](#EN-US_TASK_0172373034__fig_dc_vrp_ns_cfg_005101), GE0/1/0 and GE0/2/0 on DeviceC are connected to two IPv6 networks through DeviceA and DeviceB, respectively. DeviceC collects traffic statistics, aggregates the statistics, and sends them to NMS1 and NMS2.

To collect flow-specific statistics, configure NetStream monitoring services in the inbound direction of GE 0/1/0 and GE 0/2/0 on DeviceC. Traffic statistics collected on GE 0/1/0 are sent to NMS1 with an IPv4 address and traffic statistics collected on GE 0/2/0 are sent to NMS2 with an IPv6 address.

**Figure 1** Network diagram of NetStream traffic statistics collection![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.

  
![](images/fig_dc_vrp_ns_cfg_005101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface on each Router.
2. Enable NetStream statistics collection on RouterC.
3. Configure NetStream monitoring services on RouterC.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on each Router
* Version for outputting NetStream flows
* Source and destination addresses, destination port number, and monitoring view name of the output NetStream flows
* ID of the slot in which the NetStream service processing board resides (In this example, the NetStream service processing board is in slot 3.)

#### Procedure

1. Configure IP addresses for each Router. The configuration details are not provided here.
2. Enable NetStream statistics collection on DeviceC.
   
   
   
   # Configure the board to process NetStream services in distributed mode.
   
   ```
   [*DeviceC] slot 3 
   ```
   ```
   [*DeviceC-slot-3] ipv6 netstream sampler to slot self
   ```
   ```
   [*DeviceC-slot-3] quit 
   ```
   
   # Collect statistics about TCP flags in original flows.
   
   ```
   [*DeviceC] ipv6 netstream tcp-flag enable
   ```
   
   # Enable NetStream sampling and configure the fixed packet sampling mode.
   
   ```
   [*DeviceC] ipv6 netstream sampler fix-packets 10000 inbound
   ```
   
   # Set the version number and source address of the output packets carrying original flow statistics.
   
   ```
   [*DeviceC] ipv6 netstream export version 9
   ```
   ```
   [*DeviceC] ipv6 netstream export source ipv6 2001:db8:100::1
   ```
   
   # Configure NetStream to collect statistics about incoming flows on GE 0/1/0 and GE 0/2/0.
   
   ```
   [*DeviceC] interface GigabitEthernet0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] undo shutdown 
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ipv6 netstream inbound
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] undo shutdown 
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 netstream inbound
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream enabled on a main interface cannot collect traffic statistics about its sub-interface.
3. Configure NetStream monitoring services.
   
   
   ```
   [*DeviceC] ipv6 netstream monitor monitor1
   ```
   ```
   [*DeviceC-monitor-monitor1] ipv6 netstream export host 192.168.0.2 6000
   ```
   ```
   [*DeviceC-monitor-monitor1] quit
   ```
   ```
   [*DeviceC] ipv6 netstream monitor monitor2
   ```
   ```
   [*DeviceC-monitor-monitor2] ipv6 netstream export host ipv6 2001:db8:100::1 6000
   ```
   ```
   [*DeviceC-monitor-monitor2] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ipv6 netstream monitor monitor1 inbound
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 netstream monitor monitor2 inbound
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] commit 
   ```
4. Verify the configuration.
   
   
   
   Run the [**display ipv6 netstream monitor all**](cmdqueryname=display+ipv6+netstream+monitor+all) command to check information about all NetStream monitoring services.
   
   ```
   [~DeviceC] display ipv6 netstream monitor all
   ```
   ```
   Monitor monitor1
    ID        : 1
    AppCount  : 1
   
    Address                                   Port            
    192.168.0.2                               6000            
   ------------------------------------------------------------
   Monitor monitor2
    ID        : 2
    AppCount  : 1
   
    Address                                   Port            
    2001:DB8:100::1                           6000            
   ------------------------------------------------------------
   ```
   
   # Run the **display ipv6 netstream cache origin slot 3** command to check information about various original flows in the NetStream flow buffer.
   
   ```
   [~DeviceC] display ipv6 netstream cache origin slot 3
   ```
   ```
   
   
    DstIf                         
    SrcIf                           
    DstP                          Msk          Pro            Tos 
    SrcP                          Msk          Flags          Ttl
    Packets                                                   Bytes
    NextHop                                                   Direction
    DstIP                                                     DstAs
    SrcIP                                                     SrcAs
    BGP: BGP NextHop                                          TopLabelType
    Label1                        Exp1         Bottom1
    Label2                        Exp2         Bottom2
    Label3                        Exp3         Bottom3
    TopLabelIpAddress                          VlanId         VniId
    CreateFlowTime                LastRefreshTime             VPN(direct)
    FlowLabel                     Rdvalue
    ForwardStatus
    --------------------------------------------------------------------------
   
    GigabitEthernet0/2/0                                                        
    GigabitEthernet0/1/0                                          
    0                             0            59             0  
    0                             0            0              100
    443426                                                    56758528  
    ::                                                        in
    2001:DB8:20::1                                            0         
    2001:DB8:80::1                                            0         
    ::                                                        UNKNOWN             
    0                             0            0         
    0                             0            0         
    0                             0            0         
    0.0.0.0                                    0              0
    2018-05-09 11:38:07           2018-05-09 11:40:30         --
    112706                        -:-
    64(Forwarded Unknown)
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  # 
  sysname DeviceA
  # 
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:200::2/96
  #
  return
  ```
* DeviceB configuration file
  
  ```
  # 
  sysname DeviceB
  # 
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:300::2/96
  #
  return
  ```
* DeviceC configuration file
  
  ```
  # 
  sysname DeviceC
   # 
  ipv6 netstream tcp-flag enable
  ipv6 netstream sampler fix-packets 10000 inbound 
  ipv6 netstream export version 9
  ipv6 netstream export source ipv6 2001:DB8:100::1
   # 
  ipv6 netstream monitor monitor1
   ipv6 netstream export host 192.168.0.2 6000
  #
  ipv6 netstream monitor monitor2
   ipv6 netstream export host ipv6 2001:DB8:100::1 6000
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:200::1/96
   ipv6 netstream inbound
   ipv6 netstream monitor monitor1 inbound
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:300::1/96
   ipv6 netstream inbound
   ipv6 netstream monitor monitor2 inbound
  #
  slot 3
   ipv6 netstream sampler to slot self
  #      
  return
  ```