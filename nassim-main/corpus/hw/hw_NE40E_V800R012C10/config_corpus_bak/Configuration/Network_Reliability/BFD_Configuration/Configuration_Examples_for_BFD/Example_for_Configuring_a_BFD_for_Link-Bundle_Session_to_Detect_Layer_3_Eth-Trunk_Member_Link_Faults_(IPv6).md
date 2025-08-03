Example for Configuring a BFD for Link-Bundle Session to Detect Layer 3 Eth-Trunk Member Link Faults (IPv6)
===========================================================================================================

This section provides an example for configuring a BFD for link-bundle session to monitor Layer 3 Eth-Trunk member links and rapidly detect link faults in an IPv6 scenario.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0227428934__fig_dc_vrp_bfd_cfg_011701), DeviceA and DeviceB are directly connected through Layer 3 Eth-Trunk interfaces. BFD sessions can be bound to Eth-Trunk interfaces to monitor the connectivity of the Eth-Trunk between DeviceA and DeviceB. If single-hop BFD sessions are used, BFD selects one of the Eth-Trunk member links to monitor the state of the Eth-Trunk. Once BFD detects that the selected member link is down, it assumes that the Eth-Trunk is down even if the other member links of the Eth-Trunk are up. To prevent BFD from incorrectly reporting the Eth-Trunk state, deploy BFD for link-bundle sessions instead of single-hop BFD sessions.

**Figure 1** Configuring a BFD for link-bundle session to detect Eth-Trunk member link faults (IPv6)![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/3/0 and GE0/3/1, respectively.


  
![](figure/en-us_image_0227428936.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an Eth-Trunk interface on DeviceA and DeviceB, and then add Ethernet physical interfaces to each Eth-Trunk interface.
2. Assign IPv6 addresses to the Eth-Trunk interfaces on DeviceA and DeviceB to enable the devices to interwork with each other through the Eth-Trunk interfaces.
3. Configure a BFD for link-bundle session on DeviceA and DeviceB to monitor the Eth-Trunk member links between them.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The IPv6 addresses configured for Eth-Trunk interfaces can be global or link-local addresses. If global addresses are used, BFD for link-bundle cannot share a session with BFD for IGP. However, if link-local addresses are used, BFD for link-bundle can share a session with BFD for IGP. In this example, global addresses are used.

#### Data Preparation

To complete the configuration, you need the following data:

* IDs of the physical interfaces connecting DeviceA and DeviceB
* IPv6 addresses of the Eth-Trunk interfaces
* Minimum interval at which BFD for link-bundle session packets are received

#### Procedure

1. Create an Eth-Trunk interface on DeviceA and DeviceB, and then add Ethernet physical interfaces to each Eth-Trunk interface.
   
   
   
   # Configure DeviceA. The configuration of DeviceB is similar to the configuration of DeviceA. For configuration details, see Configuration Files in this section.
   
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
   [~DeviceA] interface Eth-Trunk 1
   ```
   ```
   [*DeviceA-Eth-Trunk1] commit
   ```
   ```
   [~DeviceA-Eth-Trunk1] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet0/3/0
   ```
   ```
   [~DeviceA-Gigabitethernet0/3/0] undo shutdown
   ```
   ```
   [*DeviceA-Gigabitethernet0/3/0] eth-trunk 1
   ```
   ```
   [*DeviceA-Gigabitethernet0/3/0] commit
   ```
   ```
   [~DeviceA-Gigabitethernet0/3/0] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet0/3/1
   ```
   ```
   [~DeviceA-Gigabitethernet0/3/1] undo shutdown
   ```
   ```
   [*DeviceA-Gigabitethernet0/3/1] eth-trunk 1
   ```
   ```
   [*DeviceA-Gigabitethernet0/3/1] commit
   ```
   ```
   [~DeviceA-Gigabitethernet0/3/1] quit
   ```
2. Assign IPv6 addresses to the Eth-Trunk interfaces on DeviceA and DeviceB to enable the devices to interwork with each other through the Eth-Trunk interfaces.
   
   
   
   # Configure DeviceA. The configuration of DeviceB is similar to the configuration of DeviceA. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceA] interface Eth-Trunk 1
   ```
   ```
   [~DeviceA-Eth-Trunk1] ipv6 enable
   ```
   ```
   [~DeviceA-Eth-Trunk1] ipv6 address 2001:DB8:1::1 64
   ```
   ```
   [*DeviceA-Eth-Trunk1] commit
   ```
   ```
   [~DeviceA-Eth-Trunk1] quit
   ```
   
   After the configuration is complete, Eth-Trunk 1 on DeviceA and DeviceB can ping each other.
   
   The following example uses the command output on DeviceB.
   
   ```
   [~DeviceB] ping ipv6 2001:DB8:1::1 
   ```
   ```
     PING 2001:DB8:1::1 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 2001:DB8:1::1: bytes=56 Sequence=1 ttl=255 time=10 ms
   ```
   ```
       Reply from 2001:DB8:1::1: bytes=56 Sequence=2 ttl=255 time=2 ms
   ```
   ```
       Reply from 2001:DB8:1::1: bytes=56 Sequence=3 ttl=255 time=2 ms
   ```
   ```
       Reply from 2001:DB8:1::1: bytes=56 Sequence=4 ttl=255 time=1 ms
   ```
   ```
       Reply from 2001:DB8:1::1: bytes=56 Sequence=5 ttl=255 time=2 ms
   ```
   ```
     --- 2001:DB8:1::1 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 1/3/10 ms
   ```
3. Configure a BFD for link-bundle session on DeviceA and DeviceB to monitor the Eth-Trunk member links between them.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd atob bind link-bundle peer-ipv6 2001:DB8:1::2 interface Eth-Trunk 1 source-ipv6 2001:DB8:1::1
   ```
   ```
   [*DeviceA-bfd-session-atob] min-rx-interval 10
   ```
   ```
   [*DeviceA-bfd-session-atob] min-tx-interval 10
   ```
   ```
   [*DeviceA-bfd-session-atob] commit
   ```
   ```
   [~DeviceA-bfd-session-atob] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd btoa bind link-bundle peer-ipv6 2001:DB8:1::1 interface Eth-Trunk 1 source-ipv6 2001:DB8:1::2
   ```
   ```
   [*DeviceB-bfd-session-btoa] min-rx-interval 10
   ```
   ```
   [*DeviceB-bfd-session-btoa] min-tx-interval 10
   ```
   ```
   [*DeviceB-bfd-session-btoa] commit
   ```
   ```
   [~DeviceB-bfd-session-btoa] quit
   ```
4. Verify the configuration.
   
   
   
   # After completing the configuration, run the **display bfd link-bundle session** command on DeviceA. The command output shows that three BFD sessions have been established and are in the **Up** state. The discriminators of the three BFD sessions are dynamically allocated by the system. The BFD session bound to Eth-Trunk 1 is the main session, and the other two are BFD sub-sessions bound to GE0/3/0 and GE0/3/1, respectively.
   
   ```
   [DeviceA] display bfd link-bundle session
   ```
   ```
   Total Up/Down Main Session Number : 1/0
   Total Up/Down Sub Session Number : 2/0
   --------------------------------------------------------------------------------
     Name                   : atob 
     State                  : Up  
     Local Discriminator    : 1048576 
     Remote Discriminator   : -                   
     Session Detect Mode    : Asynchronous Mode Without Echo Function              
     BFD Bind Type          : Interface(Eth-Trunk1)                                
     Bind Session Type      : Static_Auto(Bundle_Main)
     Bind Peer IP Address   : 2001:DB8:1::2                                              
     Bind Source IP Address : 2001:DB8:1::1                                              
     FSM Board Id           : -                
     TOS-EXP                : 7          
     Min Tx Interval (ms)   : 10               
     Min Rx Interval (ms)   : 10   
     Local Detect Multi     : 3      
     WTR Interval (ms)      : -                                                                    
     Last Local Diagnostic  : Control Detection Time Expired                                        
     Bind Application       : AUTO 
     Sub Session Count      : 2
   --------------------------------------------------------------------------------
         Sub Session Number     : 1
         State                  : Up
         Local Discriminator    : 16385 
         Remote Discriminator   : 16385                   
         BFD Bind Type          : Interface(GigabitEthernet0/3/0)                                
         Bind Session Type      : Dynamic(Bundle_Sub)
         FSM Board Id           : 9                
         Min Tx Interval (ms)   : 10               
         Min Rx Interval (ms)   : 10   
         Local Detect Multi     : 3      
         Actual Tx Interval (ms): 10               
         Actual Rx Interval (ms): 10  
         Active Multi           : 3                      
         Detect Interval (ms)   : 30                    
         Destination Port       : 6784
         Last Local Diagnostic  : Control Detection Time Expired                              
   --------------------------------------------------------------------------------
         Sub Session Number     : 2
         State                  : Up
         Local Discriminator    : 16386 
         Remote Discriminator   : 16386                   
         BFD Bind Type          : Interface(GigabitEthernet0/3/1)                                
         Bind Session Type      : Dynamic(Bundle_Sub)
         FSM Board Id           : 9                
         Min Tx Interval (ms)   : 10               
         Min Rx Interval (ms)   : 10   
         Local Detect Multi     : 3      
         Actual Tx Interval (ms): 10               
         Actual Rx Interval (ms): 10  
         Active Multi           : 3                      
         Detect Interval (ms)   : 30                    
         Destination Port       : 6784
         Last Local Diagnostic  : Control Detection Time Expired                                  
   --------------------------------------------------------------------------------
   ```
   
   # Shut down GE0/3/0 on DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet0/3/0
   ```
   ```
   [~DeviceA-Gigabitethernet0/3/0] shutdown
   ```
   ```
   [*DeviceA-Gigabitethernet0/3/0] commit
   ```
   ```
   [~DeviceA-Gigabitethernet0/3/0] quit
   ```
   
   # Run the **display bfd session all** command on DeviceA to view the states of the BFD sessions. The command output shows that the BFD sub-session bound to GE0/3/0 is in the **Down** state and the BFD main session bound to Eth-Trunk 1 is still in the **Up** state.
   
   ```
   [DeviceA] display bfd session all
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local      Remote     PeerIpAddr      State     Type        InterfaceName 
   --------------------------------------------------------------------------------
   1048576    -          10.1.1.2       Up        S/AUTO-IF   Eth-Trunk1
   16386      0          10.1.1.2       Down      D/IP-IF     Gigabitethernet0/3/0
   16387      16387      10.1.1.2       Up        D/IP-IF     Gigabitethernet0/3/1
   --------------------------------------------------------------------------------
   Total UP/DOWN Session Number : 2/1
   ```
   
   # Shut down GE0/3/1, and run the **display bfd session all** command on DeviceA. The command output shows that all three BFD sessions are in the **Down** state.
   
   ```
   [DeviceA] display bfd session all
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local      Remote     PeerIpAddr      State     Type        InterfaceName 
   --------------------------------------------------------------------------------
   1048576    -          10.1.1.2       Down        S/AUTO-IF   Eth-Trunk1
   16386      0          10.1.1.2       Down      D/IP-IF     Gigabitethernet0/3/0
   16387      16387      10.1.1.2       Down        D/IP-IF     Gigabitethernet0/3/1
   --------------------------------------------------------------------------------
   Total UP/DOWN Session Number : 0/3
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
  ```
  ```
  interface Eth-Trunk1
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:1::1 64
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/3/1
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  bfd
  ```
  ```
  #
  ```
  ```
  bfd atob bind link-bundle peer-ipv6 2001:DB8:1::2 interface Eth-Trunk1 source-ipv6 2001:DB8:1::1
  ```
  ```
   min-tx-interval 10
  ```
  ```
   min-rx-interval 10
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
  ```
  ```
  interface Eth-Trunk1
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:DB8:1::2 64
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/3/1
  ```
  ```
   undo shutdown
  ```
  ```
   eth-trunk 1
  ```
  ```
  #
  ```
  ```
  bfd
  ```
  ```
  #
  ```
  ```
  bfd btoa bind link-bundle peer-ipv6 2001:DB8:1::1 interface Eth-Trunk1 source-ipv6 2001:DB8:1::2
  ```
  ```
   min-tx-interval 10
  ```
  ```
   min-rx-interval 10
  ```
  ```
  #
  ```
  ```
  return
  ```