Example for Collecting Statistics About IPv4 Original Flows
===========================================================

This section provides an example for configuring NetStream traffic statistics collection, helping you rapidly analyze the type and location of abnormal traffic.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172373022__fig_dc_vrp_ns_cfg_003101), NetStream is configured to collect statistics about the source IP address, destination IP address, port, and protocol information of network packets on the user side. Such statistics help analyze users' behaviors and detect virus-infected terminals, source and destination of denial of service (DoS) and distributed denial of service (DDoS) attacks, source of spams, and unauthorized websites. Based on other characteristics of NetStream data flows, other network devices can filter out and restrict the spread of virus-infected traffic.

**Figure 1** Network diagram of NetStream traffic statistics collection![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.

  
![](images/fig_dc_vrp_ns_cfg_003101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the PE and CE to communicate.
2. Configure NetStream to collect statistics about incoming and outgoing packets on the user-side interface of the PE.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of the user-side interface of the PE
* Version for outputting NetStream packets
* Destination address, destination port number, and source address of the output NetStream flows
* ID of the slot in which the NetStream service processing board resides (In this example, the NetStream service processing board is in slot 3.)

#### Procedure

1. Configure the PE and CE to communicate.
   
   
   
   Assign an IP address and a mask to each interface according to [Figure 1](#EN-US_TASK_0172373022__fig_dc_vrp_ns_cfg_003101). The configuration details are not provided.
2. Enable NetStream statistics collection on GE 0/1/0 of the PE.
   
   
   
   # Configure the board to process NetStream services in distributed mode.
   
   ```
   [*PE] slot 3
   ```
   ```
   [*PE-slot-3] ip netstream sampler to slot self
   ```
   ```
   [*PE-slot-3] quit
   ```
   
   # Collect statistics about TCP flags in original flows.
   
   ```
   [*PE] ip netstream tcp-flag enable
   ```
   
   # Set the version for outputting NetStream flows to V5, and specify the source and destination addresses and destination port number for the output flows.
   
   ```
   [*PE] ip netstream export host 192.168.2.2 9001
   ```
   ```
   [*PE] ip netstream export source 192.168.2.1
   ```
   
   # Enable NetStream sampling and configure the fixed packet sampling mode.
   
   ```
   [*PE] ip netstream sampler fix-packets 10000 inbound
   ```
   ```
   [*PE] ip netstream sampler fix-packets 10000 outbound
   ```
   ```
   [*PE] commit
   ```
   
   # Configure NetStream to collect statistics about incoming and outgoing flows on GigabitEthernet 0/1/0 of the PE.
   
   ```
   [*PE] interface GigabitEthernet 0/1/0
   ```
   ```
   [*PE-GigabitEthernet0/1/0] undo shutdown 
   ```
   ```
   [*PE-GigabitEthernet0/1/0] ip netstream inbound
   ```
   ```
   [*PE-GigabitEthernet0/1/0] ip netstream outbound
   ```
   ```
   [*PE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream enabled on a main interface cannot collect traffic statistics about its sub-interface.
3. Verify the configuration.
   
   
   
   # Run the [**display ip netstream cache origin slot**](cmdqueryname=display+ip+netstream+cache+origin+slot) **3** command after completing the configuration. The command output shows information about various original flows in the NetStream flow buffer.
   
   ```
   [~PE] display ip netstream cache origin slot 3
   
   
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
    0                             24            253            0
    0                             24            0              60
    3                                                          384       
    192.168.2.1                                                in
    192.168.1.3                                                0         
    192.168.1.4                                                0         
    0.0.0.0                                                    UNKNOWN             
    0                             0            0         
    0                             0            0         
    0                             0            0         
    0.0.0.0                                    0               0        
    2018-05-09 11:38:07           2018-05-09 11:40:30          --
    --                            -:-
    66(Forwarded Not Fragmented)
   ```

#### Configuration Files

* CE configuration file
  
  ```
  #
  ```
  ```
  sysname CE
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/0
  ```
  ```
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
  # 
  ```
  ```
  return 
  ```
* PE configuration file
  
  ```
  # 
  ```
  ```
  slot 3
  ```
  ```
   ip netstream sampler to slot self
  ```
  ```
  #
  ```
  ```
  sysname PE
  ```
  ```
  #
  ```
  ```
  ip netstream tcp-flag enable
  ```
  ```
  ip netstream sampler fix-packets 10000 inbound 
  ```
  ```
  ip netstream sampler fix-packets 10000 outbound
  ```
  ```
  ip netstream export source 192.168.2.1
  ```
  ```
  ip netstream export host 192.168.2.2 9001
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet 0/2/0
  ```
  ```
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/0
  ```
  ```
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
   ip netstream inbound
  ```
  ```
   ip netstream outbound
  ```
  ```
  # 
  ```
  ```
  return
  ```