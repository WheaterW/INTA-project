Example for Configuring the Multicast MAC Encapsulation Mode for G.8275.1 Packets to Implement Network-wide Time Synchronization
================================================================================================================================

Example_for_Configuring_the_Multicast_MAC_Encapsulation_Mode_for_G.8275.1_Packets_to_Implement_Network-wide_Time_Synchronization

#### Networking Requirements

G.8275.1 can be used as a time synchronization protocol to transmit time signals of the BITS server on the entire network so that network-wide time synchronization can be achieved for base stations.

On the network shown in [Example for Configuring the Multicast MAC Encapsulation Mode for G.8275.1 Packets to Implement Network-wide Time Synchronization](dc_ne_g82751_cfg_9008.html), the transport network carries the wireless services between gNodeBs, and all transport network nodes support G.8275.1. To ensure time synchronization between G.8275.1-capable base stations and transport network devices, you can configure G.8275.1 and time can be configured use network-wide T-BCs to transmit time information.

**Figure 1** Configuring the multicast MAC encapsulation mode for G.8275.1 packets to implement network-wide time synchronization![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1, Interface2, and Interface3 represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.

![](figure/en-us_image_0000001779081406.png "Click to enlarge")


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Connect PE1 and PE2 to BITS servers.
2. Configure PE1, PE2, Device1, and Device2 as T-BCs to implement network-wide time synchronization.
3. Configure synchronous Ethernet to implement frequency synchronization for a higher synchronization precision.
4. Enable performance monitoring on the passive interfaces of Device1 and Device2.
5. To prevent reverse synchronization of clock signals, disable Interface 1 on PE1 and PE2 and Interface 2 on Device1 and Device2 from working in the slave state.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Configure devices to use the default multicast MAC encapsulation mode to transmit G.8275.1 packets.



#### Procedure

1. Configure PE1 and PE2 to import BITS clock signals through their clock interfaces. The configuration details are not provided here.
2. Configure PE1, PE2, Device1, and Device2 as T-BCs.
   1. Configure PE1.
      
      
      ```
      [~PE1] ptp enable
      [*PE1] ptp profile g-8275-1 enable
      [*PE1] ptp device-type t-bc
      [*PE1] commit
      [~PE1] interface gigabitethernet 0/1/0
      [~PE1-GigabitEthernet0/1/0] ptp enable
      [*PE1-GigabitEthernet0/1/0] clock synchronization enable
      [*PE1-GigabitEthernet0/1/0] commit
      [~PE1-GigabitEthernet0/1/0] quit
      ```
   2. Configure PE2.
      
      
      ```
      [~PE2] ptp enable
      [*PE2] ptp profile g-8275-1 enable
      [*PE2] ptp device-type t-bc
      [*PE2] commit
      [~PE2] interface gigabitethernet 0/1/0
      [~PE2-GigabitEthernet0/1/0] ptp enable
      [*PE2-GigabitEthernet0/1/0] clock synchronization enable
      [*PE2-GigabitEthernet0/1/0] commit
      [~PE2-GigabitEthernet0/1/0] quit
      ```
   3. Configure Device1.
      
      
      ```
      [~Device1] ptp enable
      [*Device1] ptp profile g-8275-1 enable
      [*Device1] ptp device-type t-bc
      [*Device1] ptp passive-measure enable
      [*Device1] commit
      [~Device1] interface gigabitethernet 0/1/0
      [~Device1-GigabitEthernet0/1/0] ptp enable
      [*Device1-GigabitEthernet0/1/0] ptp notslave disable
      [*Device1-GigabitEthernet0/1/0] clock synchronization enable
      [*Device1-GigabitEthernet0/1/0] clock priority 10
      [*Device1-GigabitEthernet0/1/0] commit
      [~Device1-GigabitEthernet0/1/0] quit
      [~Device1] interface gigabitethernet 0/1/1
      [~Device1-GigabitEthernet0/1/1] ptp enable
      [*Device1-GigabitEthernet0/1/1] clock synchronization enable
      [*Device1-GigabitEthernet0/1/1] commit
      [~Device1-GigabitEthernet0/1/1] quit
      [~Device1] interface gigabitethernet 0/1/2
      [~Device1-GigabitEthernet0/1/2] ptp enable
      [*Device1-GigabitEthernet0/1/2] ptp notslave disable
      [*Device1-GigabitEthernet0/1/2] clock synchronization enable
      [*Device1-GigabitEthernet0/1/2] clock priority 20
      [*Device1-GigabitEthernet0/1/2] commit
      [~Device1-GigabitEthernet0/1/2] quit
      ```
   4. Configure Device2.
      
      
      ```
      [~Device2] ptp enable
      [*Device2] ptp profile g-8275-1 enable
      [*Device2] ptp device-type t-bc
      [*Device2] ptp passive-measure enable
      [*Device2] commit
      [~Device2] interface gigabitethernet 0/1/0
      [~Device2-GigabitEthernet0/1/0] ptp enable
      [*Device2-GigabitEthernet0/1/0] ptp notslave disable
      [*Device2-GigabitEthernet0/1/0] clock synchronization enable
      [*Device2-GigabitEthernet0/1/0] clock priority 10
      [*Device2-GigabitEthernet0/1/0] commit
      [~Device2-GigabitEthernet0/1/0] quit
      [~Device2] interface gigabitethernet 0/1/1
      [~Device2-GigabitEthernet0/1/1] ptp enable
      [*Device2-GigabitEthernet0/1/1] clock synchronization enable
      [*Device2-GigabitEthernet0/1/1] commit
      [~Device2-GigabitEthernet0/1/1] quit
      [~Device2] interface gigabitethernet 0/1/2
      [~Device2-GigabitEthernet0/1/2] ptp enable
      [*Device2-GigabitEthernet0/1/2] ptp notslave disable
      [*Device2-GigabitEthernet0/1/2] clock synchronization enable
      [*Device2-GigabitEthernet0/1/2] clock priority 20
      [*Device2-GigabitEthernet0/1/2] commit
      [~Device2-GigabitEthernet0/1/2] quit
      ```
3. Configure base stations to receive G.8275.1 packets from Device1 and Device2. The configuration details are not provided here.
4. Verify the configuration.
   
   
   
   After completing the configurations, run the **display ptp all** command to check the running status of G.8275.1. The following example uses the command output on Device1. The command output shows that the G.8275.1 interface GE 0/1/0 on Device1 is working in the Slave state, the grandmaster clock ID is 0a05d7fffe341500, and the parent clock ID is 0a05d7fffe341500. Device1 has synchronized with the master clock source.
   
   ```
   [~Device1] display ptp all
   Device config info
     ------------------------------------------------------------------------------
     PTP state         :enabled              Domain  value      :24
     Slave only        :-                    Device type        :T-BC
     Set port state    :-                    Local clock ID     :0aa1c6fffe699700
     Acl               :no                   Virtual clock ID   :no
     Acr               :-                    Time lock success  :yes
     Asymmetry measure :disable              Passive measure    :enable
     PTP profile       :G.8275.1 V2.0
     Send GM WTR       :no
    
     BMC run info
     ------------------------------------------------------------------------------
     Grand clock ID    :0a05d7fffe341500               
     Receive number    :GigabitEthernet0/1/0                                                                                           
     Parent clock ID   :0a05d7fffe341500               
     Parent portnumber :35585                          
     Priority1         :128                 Priority2           :128               
     Step removed      :0                   Clock accuracy      :0xfe                                                                
     Clock class       :6                   Time Source         :0xa0                                                                  
     UTC Offset        :35                  UTC Offset Valid    :True                                                                 
     Timescale         :PTP                 Time traceable      :True                                                                 
     Leap              :None                Frequency traceable :True                                                                 
     Offset scaled     :0xffff              Sync uncertain      :True
                                                                                                                                       
     Port info                                                                                                                         
     Name                        State        Delay-mech Ann-timeout Type   Domain                                                     
     ------------------------------------------------------------------------------                                                    
     GigabitEthernet0/1/0        slave       delay      3           T-BC   24      
    
     Time Performance Statistics(ns): Slot X  Card X  Port X 
     ------------------------------------------------------------------------------
     Realtime(T2-T1)   :1104                    Pathdelay     :0 
     Max(T2-T1)        :1110
     Min(T2-T1)        :1100
     Realtime(T4-T3)   :998 
     Max(T4-T3)        :428 
     Min(T4-T3)        :-715
   
     Offset from master:-281
    
     Clock source info
     Clock     Pri  Pri2 Accuracy Class TimeSrc  Signal Switch Direction In-Status
     ------------------------------------------------------------------------------
     local     128  128  0xFE     248   0xa0     -      -      -         -
     bits1/11  128  128  0x20     6     0x20     1pps   off    in/-      normal
     bits1/12  128  128  0x20     6     0x20     1pps   off    in/-      normal
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ptp enable
  ptp profile g-8275-1 enable
  ptp device-type t-bc
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   clock synchronization enable 
   ptp enable
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ptp enable
  ptp profile g-8275-1 enable
  ptp device-type t-bc
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   clock synchronization enable 
   ptp enable
  #
  return
  ```
* Device1 configuration file
  
  ```
  #
  sysname Device1
  #
  ptp enable
  ptp profile g-8275-1 enable
  ptp device-type t-bc
  ptp passive-measure enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ptp notslave disable
   clock synchronization enable
   clock priority 10
   ptp enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   clock synchronization enable
   ptp enable
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ptp notslave disable
   clock synchronization enable
   clock priority 20
   ptp enable
  #
  return
  ```
* Device2 configuration file
  
  ```
  #
  sysname Device2
  #
  ptp enable
  ptp profile g-8275-1 enable
  ptp device-type t-bc
  ptp passive-measure enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ptp notslave disable
   clock synchronization enable
   clock priority 10
   ptp enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   clock synchronization enable
   ptp enable
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ptp notslave disable
   clock synchronization enable
   clock priority 20
   ptp enable
  #
  return
  ```