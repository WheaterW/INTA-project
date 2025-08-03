Example for Configuring the Association Between Bit Errors and IGP Routes
=========================================================================

Example_for_Configuring_the_Association_Between_Bit_Errors_and_IGP_Routes

#### Networking Requirements

When a link's BER exceeds a certain threshold, the link's interface reports link quality information. IS-IS adjusts the interface's cost value based on the link quality information, switching routes to a link with a smaller BER.

As shown in [Figure 1](#EN-US_TASK_0172362293__fig_dc_vrp_cfg_error-code_00002201):

* Four devices run IS-IS.
* Four devices are all Level-1-2 devices.
* The primary link of IS-IS is DeviceA -> DeviceC -> DeviceD (that is, link T), and its backup link is DeviceA -> DeviceB -> DeviceD. In normal circumstances, traffic between DeviceA and DeviceD travels along the primary link. Assume that DeviceA's GE0/1/0 has a high BER (that is, the primary link's quality deteriorates). To resolve this issue, configure bit-error-triggered route switching (that is, on DeviceA's GE0/1/0, enable CRC bit error detection, enable bit error detection, set BER thresholds for determining link quality, and enable IS-IS to adjust the interface's cost value based on the interface's link quality information). When the primary link's BER exceeds a certain threshold, IS-IS dynamically adjusts the cost value of the link's interface, switching traffic to the backup link.

**Figure 1** Configuring the association between bit errors and IGP routes  
![](images/fig_dc_vrp_cfg_error-code_00002201.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface0 and interface1 represent GE0/1/0 and GE0/2/0, respectively.



| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE 0/1/0 | 10.0.1.1/24 |
| GE 0/2/0 | 10.1.1.1/24 |
| DeviceB | GE 0/1/0 | 10.1.1.2/32 |
| GE 0/2/0 | 10.2.1.1/24 |
| DeviceC | GE 0/1/0 | 10.0.1.2/24 |
| GE 0/2/0 | 10.3.1.1/24 |
| DeviceD | GE 0/1/0 | 10.3.1.2/24 |
| GE 0/2/0 | 10.2.1.2/24 |
| GE 0/3/0 | 10.4.1.1/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic IS-IS functions on each device.
2. Enable BFD globally on each device.
3. Configure a large cost on DeviceA's GE0/2/0 so that traffic preferentially travels along link T.
4. On each interface of each device, enable bit error detection and set BER thresholds for determining link quality.
5. On each interface of each device, enable IS-IS to adjust the interface's cost based on the interface's link quality information.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on each device
* NET of each device
* Level of each device
* Cost of each interface on each device

#### Procedure

1. Configure an IP address for each interface. For details, see [Configuration Files](#EN-US_TASK_0172362293__section_dc_vrp_cfg_00649405).
2. Configure basic IS-IS functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] is-level level-1-2
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] is-level level-1-2
   ```
   ```
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] is-level level-1-2
   ```
   ```
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*DeviceC-isis-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] isis 1
   ```
   ```
   [*DeviceD-isis-1] is-level level-1-2
   ```
   ```
   [*DeviceD-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*DeviceD-isis-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/2/0] quit
   ```
3. Enable BFD globally.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] commit
   ```
   ```
   [~DeviceA-bfd] quit
   ```
   
   The configuration of other devices is similar to the configuration of DeviceA.
4. Set the cost of DeviceA's GE0/2/0 to 30, and check routing information.
   
   
   
   # Set the cost of DeviceA's GE0/2/0 to 30.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] isis cost 30
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   # Check information about the link from DeviceA to DeviceD. IS-IS preferentially selects link T to transmit traffic forwarded by DeviceA because link T has the smallest cost.
   
   ```
   [~DeviceA] display isis route verbose
                                                                                   
                            Route information for IS-IS(1)                          
                            -----------------------------                          
                                                                                   
                           IS-IS(1) Level-1 Forwarding Table                        
                           --------------------------------                        
                                                                                   
    IPV4 Dest  : 10.20.1.0/24       Int. Cost : 30            Ext. Cost : NULL     
    Admin Tag  : -                  Src Count : 1             Flags     : A/-/L/-/-
    Priority   : Low 
    NextHop    :                    Interface :               ExitIndex :           
       10.0.1.2                        GE0/1/0                 0x00000003         
                                                                                   
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set   
                                                                                   
                                                                                   
                           IS-IS(1) Level-2 Forwarding Table                        
                           --------------------------------                        
                                                                                   
    IPV4 Dest  : 10.20.1.0/24       Int. Cost : 30            Ext. Cost : NULL     
    Admin Tag  : -                  Src Count : 3             Flags     : -/-/-/-/-
                                                                                   
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                    U-Up/Down Bit Set   
   ```
5. On each interface of each device, enable bit error detection and set BER thresholds for determining link quality.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] link-quality low bit-error-threshold error-ratio 1 3 resume-ratio 1 6
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   The configuration of other devices is similar to the configuration of DeviceA.
6. On each interface of each device, enable IS-IS to adjust the interface's cost based on the interface's link quality information.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] isis link-quality low incr-cost max-reachable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   The configuration of other devices is similar to the configuration of DeviceA.
7. Verify the configuration.
   
   
   
   # Check detailed information about all interfaces with IS-IS enabled on DeviceA, including the interfaces' link quality information and whether costs have been adjusted based on link quality.
   
   ```
   [~DeviceA] display isis interface verbose
   ```
   ```
                          Interface information for IS-IS(1)
                          ---------------------------------
    Interface         Id      IPV4.State          IPV6.State      MTU  Type  DIS
    GE0/1/0           002         Up          Mtu:Up/Lnk:Up/IP:Up 1497 L1/L2 Yes/Yes
     Circuit MT State            : Standard  
     Description                 : 
     SNPA Address                : 00e0-fc12-7890
     IP Address                  : 10.0.1.1
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

* DeviceA configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  bfd
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-1-2
  ```
  ```
   network-entity 10.0000.0000.0001.00
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.0.1.1 255.255.255.0
  ```
  ```
   link-quality low bit-error-threshold error-ratio 1 3 resume-ratio 1 6
  ```
  ```
   isis enable 1
  ```
  ```
   isis link-quality low incr-cost max-reachable
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet 0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   link-quality low bit-error-threshold error-ratio 1 3 resume-ratio 1 6
  ```
  ```
   isis enable 1
  ```
  ```
   isis cost 30
  ```
  ```
   isis link-quality low incr-cost max-reachable
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
  #
  bfd
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-1-2
  ```
  ```
   network-entity 10.0000.0000.0002.00
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   
  ```
  ```
   link-quality low bit-error-threshold error-ratio 1 3 resume-ratio 1 6
  ```
  ```
   isis enable 1
  ```
  ```
   isis link-quality low incr-cost max-reachable
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet 0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.1 255.255.255.0
  ```
  ```
   link-quality low bit-error-threshold error-ratio 1 3 resume-ratio 1 6
  ```
  ```
   isis enable 1
  ```
  ```
   isis link-quality low incr-cost max-reachable
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  bfd
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-1-2
  ```
  ```
   network-entity 10.0000.0000.0003.00
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.0.1.2 255.255.255.0
  ```
  ```
   
  ```
  ```
   link-quality low bit-error-threshold error-ratio 1 3 resume-ratio 1 6
  ```
  ```
   isis enable 1
  ```
  ```
   isis link-quality low incr-cost max-reachable
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet 0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.1 255.255.255.0
  ```
  ```
   link-quality low bit-error-threshold error-ratio 1 3 resume-ratio 1 6
  ```
  ```
   isis enable 1
  ```
  ```
   isis link-quality low incr-cost max-reachable
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  bfd
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-1-2
  ```
  ```
   network-entity 10.0000.0000.0004.00
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.2 255.255.255.0
  ```
  ```
   link-quality low bit-error-threshold error-ratio 1 3 resume-ratio 1 6
  ```
  ```
   isis enable 1
  ```
  ```
   isis link-quality low incr-cost max-reachable
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet 0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.2 255.255.255.0
  ```
  ```
   link-quality low bit-error-threshold error-ratio 1 3 resume-ratio 1 6
  ```
  ```
   isis enable 1
  ```
  ```
   isis link-quality low incr-cost max-reachable
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet 0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.4.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```