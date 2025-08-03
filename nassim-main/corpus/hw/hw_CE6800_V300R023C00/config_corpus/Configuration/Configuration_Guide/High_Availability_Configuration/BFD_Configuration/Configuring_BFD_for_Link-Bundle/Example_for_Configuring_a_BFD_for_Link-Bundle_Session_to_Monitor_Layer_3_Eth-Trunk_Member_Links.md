Example for Configuring a BFD for Link-Bundle Session to Monitor Layer 3 Eth-Trunk Member Links
===============================================================================================

Example for Configuring a BFD for Link-Bundle Session to Monitor Layer 3 Eth-Trunk Member Links

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176661889__fig_dc_vrp_bfd_cfg_011701), DeviceA and DeviceB are directly connected through Layer 3 Eth-Trunk interfaces, and BFD is required to detect faults on the Eth-Trunk link between DeviceA and DeviceB. If single-hop BFD is used, BFD randomly selects one of the Eth-Trunk member links as the detection path and monitors only this member link. Once BFD detects that the selected member link is down, it assumes that the Eth-Trunk link is down even if the other Eth-Trunk member links are up. To prevent BFD from incorrectly identifying the Eth-Trunk link status, deploy a BFD for link-bundle session instead of a single-hop BFD session.

**Figure 1** Network diagram of configuring a BFD for link-bundle session to monitor Eth-Trunk member links![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001176661919.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an Eth-Trunk interface on DeviceA and DeviceB, and add Ethernet physical interfaces to each Eth-Trunk interface.
2. Assign IP addresses to the Eth-Trunk interfaces on DeviceA and DeviceB to ensure the devices can communicate through the Layer 3 Eth-Trunk interfaces.
3. Configure a BFD for link-bundle session on DeviceA and DeviceB to monitor the Eth-Trunk member links between the devices.

#### Procedure

1. Create an Eth-Trunk interface on DeviceA and DeviceB, and add Ethernet physical interfaces to each Eth-Trunk interface.
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface Eth-Trunk 1
   [~DeviceA-Eth-Trunk1] undo portswitch
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] eth-trunk 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] eth-trunk 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176661889__context1161811745410).
2. Assign IP addresses to the Eth-Trunk interfaces on DeviceA and DeviceB to ensure the devices can communicate through the Layer 3 Eth-Trunk interfaces.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface Eth-Trunk 1
   [~DeviceA-Eth-Trunk1] undo portswitch
   [*DeviceA-Eth-Trunk1] ip address 10.1.1.1 24
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface Eth-Trunk 1
   [~DeviceB-Eth-Trunk1] undo portswitch
   [*DeviceB-Eth-Trunk1] ip address 10.1.1.2 24
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] commit
   ```
3. Configure a BFD for link-bundle session on DeviceA and DeviceB to monitor the Eth-Trunk member links between the devices.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd atob bind link-bundle peer-ip 10.1.1.2 interface Eth-Trunk 1 source-ip 10.1.1.1
   [*DeviceA-bfd-session-atob] min-rx-interval 10
   [*DeviceA-bfd-session-atob] min-tx-interval 10
   [*DeviceA-bfd-session-atob] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd
   [*DeviceB-bfd] quit
   [*DeviceB] bfd btoa bind link-bundle peer-ip 10.1.1.1 interface Eth-Trunk 1 source-ip 10.1.1.2
   [*DeviceB-bfd-session-btoa] min-rx-interval 10
   [*DeviceB-bfd-session-btoa] min-tx-interval 10
   [*DeviceB-bfd-session-btoa] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check that Eth-Trunk 1 on DeviceA and DeviceB can ping each other.

```
[~DeviceB] ping 10.1.1.1
  PING 10.1.1.1: 56  data bytes, press CTRL_C to break
    Reply from 10.1.1.1: bytes=56 Sequence=1 ttl=255 time=10 ms
    Reply from 10.1.1.1: bytes=56 Sequence=2 ttl=255 time=2 ms
    Reply from 10.1.1.1: bytes=56 Sequence=3 ttl=255 time=2 ms
    Reply from 10.1.1.1: bytes=56 Sequence=4 ttl=255 time=1 ms
    Reply from 10.1.1.1: bytes=56 Sequence=5 ttl=255 time=2 ms
  --- 10.1.1.1 ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 1/3/10 ms
```

# Run the **display bfd link-bundle session** command on DeviceA to check the BFD session status.

```
<DeviceA> display bfd link-bundle session
Total Up/Down Main Session Number : 1/0
Total Up/Down Sub Session Number : 2/0
--------------------------------------------------------------------------------
  Name                   : atob 
  State                  : Up  
  Local Discriminator    : 1048576 
  Remote Discriminator   : -                   
  Session Detect Mode    : Asynchronous Mode Without Echo Function              
  BFD Bind Type          : Interface(Eth-Trunk1)                                
  Bind Session Type      : Static_Auto(Bundle_Main | Compatible)
  Bind Peer IP Address   : 10.1.1.2                                              
  Bind Source IP Address : 10.1.1.1                                              
  FSM Board ID           : -                
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
      BFD Bind Type          : Interface(100GE1/0/1)                                
      Bind Session Type      : Dynamic(Bundle_Sub | Compatible)
      FSM Board ID           : 9                
      Min Tx Interval (ms)   : 10               
      Min Rx Interval (ms)   : 10   
      Local Detect Multi     : 3      
      Actual Tx Interval (ms): 10               
      Actual Rx Interval (ms): 10  
      Active Multi           : 3                      
      Detect Interval (ms)   : 30                    
      Destination Port       : 3784
      Last Local Diagnostic  : Control Detection Time Expired                              
--------------------------------------------------------------------------------
      Sub Session Number     : 2
      State                  : Up
      Local Discriminator    : 16386 
      Remote Discriminator   : 16386                   
      BFD Bind Type          : Interface(100GE1/0/2)                                
      Bind Session Type      : Dynamic(Bundle_Sub | Compatible)
      FSM Board ID           : 9                
      Min Tx Interval (ms)   : 10               
      Min Rx Interval (ms)   : 10   
      Local Detect Multi     : 3      
      Actual Tx Interval (ms): 10               
      Actual Rx Interval (ms): 10  
      Active Multi           : 3                      
      Detect Interval (ms)   : 30                    
      Destination Port       : 3784
      Last Local Diagnostic  : Control Detection Time Expired                                  
--------------------------------------------------------------------------------
```

The command output shows that three BFD sessions have been established on DeviceA and are in the **Up** state. The discriminators of the three BFD sessions are dynamically allocated by the system. The BFD session bound to Eth-Trunk 1 is the main session, and the other two BFD sub-sessions are bound to two Ethernet physical interfaces (100GE1/0/1 and 100GE1/0/2).

# Shut down the Ethernet physical interface 100GE1/0/1 on DeviceA.

```
[~DeviceA] interface 100ge 1/0/1
[~DeviceA-100GE1/0/1] shutdown
[*DeviceA-100GE1/0/1] quit
[*DeviceA] commit
```

# Run the **display bfd session all** command on DeviceA to check the states of the three BFD sessions.

```
<DeviceA> display bfd session all
S: Static session
D: Dynamic session
IP: IP session
IF: Single-hop session
PEER: Multi-hop session
AUTO: Automatically negotiated session
VXLAN: VXLAN session
(w): State in WTR 
(*): State is invalid
Total UP/DOWN Session Number : 2/1
--------------------------------------------------------------------------------
Local      Remote     PeerIpAddr      State     Type        InterfaceName 
--------------------------------------------------------------------------------
1048576    -          10.1.1.2       Up        S/AUTO-IF   Eth-Trunk1
16386      0          10.1.1.2       Down      D/IP-IF     100GE1/0/1
16387      16387      10.1.1.2       Up        D/IP-IF     100GE1/0/2
--------------------------------------------------------------------------------
```

The command output shows that the BFD sub-session bound to 100GE1/0/1 is in the **Down** state, but the main session bound to Eth-Trunk 1 is still in the **Up** state.

# Shut down the physical Ethernet interface 100GE1/0/2 on DeviceA.

```
[~DeviceA] interface 100ge 1/0/2
[~DeviceA-100GE1/0/2] shutdown
[*DeviceA-100GE1/0/2] quit
[*DeviceA] commit
```

# Run the **display bfd session all** command on DeviceA to check the states of the three BFD sessions.

```
<DeviceA> display bfd session all
S: Static session
D: Dynamic session
IP: IP session
IF: Single-hop session
PEER: Multi-hop session
AUTO: Automatically negotiated session
VXLAN: VXLAN session
(w): State in WTR 
(*): State is invalid
Total UP/DOWN Session Number : 0/3
--------------------------------------------------------------------------------
Local      Remote     PeerIpAddr      State     Type        InterfaceName 
--------------------------------------------------------------------------------
1048576    -          10.1.1.2       Down      S/AUTO-IF   Eth-Trunk1
16386      0          10.1.1.2       Down      D/IP-IF     100GE1/0/1
16387      0          10.1.1.2       Down      D/IP-IF     100GE1/0/2
--------------------------------------------------------------------------------
```

The command output shows that the three BFD sessions are in the **Down** state.


#### Configuration Scripts

* DeviceA
  ```
  #
   sysname DeviceA
  #
   bfd
  #
  interface Eth-Trunk1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
  #
  interface 100GE1/0/1
   eth-trunk 1
  #
  interface 100GE1/0/2
   undo portswitch
   eth-trunk 1
  #
  bfd atob bind link-bundle peer-ip 10.1.1.2 interface Eth-Trunk1 source-ip 10.1.1.1
   min-tx-interval 10
   min-rx-interval 10
  #
  return
  ```
* DeviceB
  ```
   
   sysname DeviceB
  #
   bfd
  #
  interface Eth-Trunk1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   eth-trunk 1
  #
  interface 100GE1/0/2
   undo portswitch
   eth-trunk 1
  #
  bfd btoa bind link-bundle peer-ip 10.1.1.1 interface Eth-Trunk1 source-ip 10.1.1.2
   min-tx-interval 10
   min-rx-interval 10
  #
  return
  ```