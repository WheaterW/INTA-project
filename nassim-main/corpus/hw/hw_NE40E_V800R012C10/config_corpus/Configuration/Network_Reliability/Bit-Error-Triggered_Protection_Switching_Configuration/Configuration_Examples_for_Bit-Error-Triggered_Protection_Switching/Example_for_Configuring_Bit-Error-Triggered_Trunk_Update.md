Example for Configuring Bit-Error-Triggered Trunk Update
========================================================

This section provides an example for configuring bit-error-triggered trunk update.

#### Networking Requirements

To improve link reliability and balance traffic, you can bundle multiple physical interfaces into a logical aggregation group, that is, a trunk interface. To minimize the impact of bit errors on services transmitted through a trunk interface, configure bit-error-triggered update for the trunk interface. In this example, trunk-bit-error-triggered IGP route switching (recommended) is configured.

On the network shown in [Figure 1](#EN-US_TASK_0172362296__fig_dc_vrp_cfg_error-code_00001501), PE1 and PE2 communicate over an Eth-Trunk interface. The Eth-Trunk interfaces on PE1 and PE2 both consist of GE 0/1/0 and GE 0/1/1. If bit errors occur on a GE interface, for example, GE 0/1/0 on PE1, traffic forwarded through the GE interface experiences packet loss or errors. To resolve this issue, configure bit-error-triggered trunk update for each Eth-Trunk interface. If bit errors occur on an Eth-Trunk member interface (GE 0/1/0), the Eth-Trunk interface disables this member interface from forwarding traffic.

If bit errors occur on both GE 0/1/0 and GE 0/1/1 of PE1, the Eth-Trunk interface ignores the bit errors on the member interfaces and remains up. However, the link quality level of the Eth-Trunk interface becomes LOW, triggering IS-IS to increase the cost of the Eth-Trunk interface's link. IS-IS routes then do not preferentially select the link.

**Figure 1** Bit-error-triggered trunk update![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_cfg_error-code_00001501.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an Eth-Trunk interface on PE1 and PE2 and add the corresponding GE interfaces to the Eth-Trunk interfaces.
2. Configure basic IS-IS functions on PE1 and PE2.
3. Enable BFD globally on PE1 and PE2.
4. Enable link-quality bit error detection on each GE interface.
5. Enable bit-error-triggered update for the Eth-Trunk interfaces.
6. Enable IS-IS to automatically adjust the link cost based on link quality of the Eth-Trunk interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Eth-Trunk interface IDs on PE1 and PE2: 1
* Eth-Trunk interface IP address on PE1: 10.1.1.1/24; Eth-Trunk interface IP address on PE2: 10.1.1.2/24
* Bit error alarm threshold on each GE interface: 3 x 10-4; alarm clear threshold: 2 x 10-5

#### Procedure

1. Create Eth-Trunk interfaces.
   
   # Configure PE1.
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] interface eth-trunk 1
   ```
   ```
   [*PE1-Eth-Trunk1] ip address 10.1.1.1 24
   ```
   ```
   [*PE1-Eth-Trunk1] commit
   ```
   ```
   [~PE1-Eth-Trunk1] quit
   ```
   
   # Configure PE2.
   ```
   <PE2> system-view
   ```
   ```
   [~PE2] interface eth-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk1] ip address 10.1.1.2 24
   ```
   ```
   [*PE2-Eth-Trunk1] commit
   ```
   ```
   [~PE2-Eth-Trunk1] quit
   ```
2. Add GE interfaces to the Eth-Trunk interfaces.
   
   # Configure PE1.
   ```
   [~PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] eth-trunk 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] eth-trunk 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] quit
   ```
   
   # Configure PE2.
   ```
   [~PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] eth-trunk 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE2-GigabitEthernet0/1/1] eth-trunk 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/1] quit
   ```
3. Configure basic IS-IS functions.
   
   # Configure PE1.
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-1-2
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface eth-trunk 1
   ```
   ```
   [*PE1-Eth-Trunk1] isis enable 1
   ```
   ```
   [*PE1-Eth-Trunk1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-1-2
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface eth-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk1] isis enable 1
   ```
   ```
   [*PE2-Eth-Trunk1] quit
   ```
   ```
   [*PE2] commit
   ```
4. Enable BFD globally.
   
   # Configure PE1.
   ```
   [~PE1] bfd
   ```
   ```
   [*PE1-bfd] commit
   ```
   ```
   [~PE1-bfd] quit
   ```
   
   # Configure PE2.
   ```
   [~PE2] bfd
   ```
   ```
   [*PE2-bfd] commit
   ```
   ```
   [~PE2-bfd] quit
   ```
5. Enable bit error detection on the GE interfaces.
   
   # Configure PE1.
   ```
   [~PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] link-quality low bit-error-threshold error-ratio 3 4 resume-ratio 2 5
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] link-quality low bit-error-threshold error-ratio 3 4 resume-ratio 2 5
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] quit
   ```
   
   # Configure PE2.
   ```
   [~PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] link-quality low bit-error-threshold error-ratio 3 4 resume-ratio 2 5
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE2-GigabitEthernet0/1/1] link-quality low bit-error-threshold error-ratio 3 4 resume-ratio 2 5
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/1] quit
   ```
6. Enable bit error detection on each Eth-Trunk interface.
   
   # Configure PE1.
   ```
   [~PE1] interface eth-trunk 1
   ```
   ```
   [~PE1-Eth-Trunk1] bit-error-detection
   ```
   ```
   [*PE1-Eth-Trunk1] commit
   ```
   ```
   [~PE1-Eth-Trunk1] quit
   ```
   
   # Configure PE2.
   ```
   [~PE2] interface eth-trunk 1
   ```
   ```
   [~PE2-Eth-Trunk1] bit-error-detection
   ```
   ```
   [*PE2-Eth-Trunk1] commit
   ```
   ```
   [~PE2-Eth-Trunk1] quit
   ```
7. Enable IS-IS to automatically adjust the link cost based on link quality of the Eth-Trunk interfaces.
   
   # Configure PE1.
   ```
   [~PE1] interface eth-trunk 1
   ```
   ```
   [~PE1-Eth-Trunk1] isis link-quality low incr-cost max-reachable
   ```
   ```
   [*PE1-Eth-Trunk1] commit
   ```
   ```
   [~PE1-Eth-Trunk1] quit
   ```
   
   # Configure PE2.
   ```
   [~PE2] interface eth-trunk 1
   ```
   ```
   [~PE2-Eth-Trunk1] isis link-quality low incr-cost max-reachable
   ```
   ```
   [*PE2-Eth-Trunk1] commit
   ```
   ```
   [~PE2-Eth-Trunk1] quit
   ```
8. Verify the configuration.
   
   
   
   If bit errors occur on PE1's GE 0/1/0, run the [**display interface eth-trunk 1**](cmdqueryname=display+interface+eth-trunk+1) command on PE1. The command output shows that GE 0/1/0 is in the **Down** state. That means that traffic cannot be forwarded through GE 0/1/0.
   
   ```
   [~PE1] display interface eth-trunk 1
   ```
   ```
   Eth-Trunk1 current state : UP (ifindex: 28)  
   Line protocol current state : UP 
   Last line protocol up time : 2013-01-24 03:37:55
   Description: 
   Route Port,Hash arithmetic : According to flow, Maximal BW: 200Mbps, Current BW: 100Mbps, The Maximum Transmit Unit is 1500
   Internet Address is 10.1.1.1/24
   IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 00e0-fc12-7880
   Current system time: 2013-01-24 03:55:47
   Physical is ETH_TRUNK
       Last 300 seconds input rate 0 bits/sec, 0 packets/sec
       Last 300 seconds output rate 0 bits/sec, 0 packets/sec
       Input: 210700 packets,0 bytes
              72716 unicast,130423 broadcast,7561 multicast
              0 errors,0 drops
       Output:244570 packets,0 bytes
              108213 unicast,130430 broadcast,5927 multicast
              0 errors,0 drops
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
   ----------------------------------------------------------
   PortName                      Status              Weight   
   ----------------------------------------------------------
   GigabitEthernet0/1/0           DOWN             1    
   GigabitEthernet0/1/1                UP                  1        
   ----------------------------------------------------------
   The Number of Ports in Trunk : 2
   The Number of UP Ports in Trunk : 1
   ```
   
   If bit errors occur on both GE 0/1/0 and GE 0/1/1 of PE1, run the [**display isis interface verbose**](cmdqueryname=display+isis+interface+verbose) command on PE1. The command output shows that the link quality level of the IS-IS interface is **LOW** and the cost is adjusted based on link quality.
   
   ```
   [~PE1] display isis interface verbose
   ```
   ```
                          Interface information for ISIS(1)
                          ---------------------------------
    Interface         Id      IPV4.State          IPV6.State      MTU  Type  DIS
    Eth-Trunk 1       001         Up          Mtu:Up/Lnk:Up/IP:Up 1497 L1/L2 Yes/Yes
     Circuit MT State            : Standard  
     Description                 : PE1, Eth-Trunk 1 Interface
     SNPA Address                : 00e0-fc12-7890
     IP Address                  : 192.168.10.1
     IPV6 Link Local Address     : 
     IPV6 Global Address(es)     : 
     Csnp Timer Value            :  L1    10  L2    10
     Hello Timer Value           :  L1    10  L2    10
     DIS Hello Timer Value       :  L1     3  L2     3
     Hello Multiplier Value      :  L1     3  L2     3
     LSP-Throttle Timer          :  L12    50 <50ms>
     Cost                        :  L1    10  L2    10
     Ipv6 Cost                   :  L1     0  L2     0
     Priority                    :  L1    64  L2    64
     Retransmit Timer Value      :  L1     5  L2     5
     Bandwidth-Value             :  Low  100000000  High          0
     Static Bfd                  :  NO
     Dynamic Bfd                 :  YES
     Static IPv6 Bfd             :  NO
     Dynamic IPv6 Bfd            :  NO
     Suppress Base               :  NO
     IPv6 Suppress Base          :  NO
     Extended-Circuit-Id Value   :  0000000000
     Circuit State               :  OSI:UP   / IP:UP   / MTU:UP   / IPBorrow:UP   /
                                    BandWidth:UP   / IsEnable:UP   / Interface:UP  
     Circuit Ipv6 State          :  OSI:UP   / IP:UP   / MTU:UP   / IPBorrow:UP   /
                                    BandWidth:UP   / IsEnable:DOWN / Interface:UP
     BFD Incr-Cost State         :  MT0 L1 : NO / MT0 L2 : NO / MT2 L1 : NO / MT2 L2 : NO
     Link quality adjust cost    :  YES
     Link quality                :  0x4(LOW)
     
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #                                                                               
  sysname PE1                                                                     
  #                                                                               
  bfd                                                                             
  #                                                                               
  isis 1
   is-level level-1-2
   network-entity 10.0000.0000.0001.00
  #
  interface Eth-Trunk1
   ip address 10.1.1.1 255.255.255.0
   bit-error-detection                                                            
   isis enable 1
   isis link-quality low incr-cost max-reachable
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown  
   eth-trunk 1    
   link-quality low bit-error-threshold error-ratio 3 4 resume-ratio 2 5
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown  
   eth-trunk 1    
   link-quality low bit-error-threshold error-ratio 3 4 resume-ratio 2 5
  #                                                                               
  return
  ```
* PE2 configuration file
  
  ```
  #                                                                               
  sysname PE2                                                                     
  #                                                                               
  bfd                                                                   
  #                                                                               
  isis 1
   is-level level-1-2
   network-entity 10.0000.0000.0002.00
  #
  interface Eth-Trunk1
   ip address 10.1.1.2 255.255.255.0
   bit-error-detection                                                             
   isis enable 1
   isis link-quality low incr-cost max-reachable
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown  
   eth-trunk 1    
   link-quality low bit-error-threshold error-ratio 3 4 resume-ratio 2 5
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown  
   eth-trunk 1    
   link-quality low bit-error-threshold error-ratio 3 4 resume-ratio 2 5
  #
  return
  ```