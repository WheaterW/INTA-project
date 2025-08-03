Example for Configuring a BFD for Perlink Session to Detect Eth-Trunk Member Link Faults on a VLAN
==================================================================================================

Example for Configuring a BFD for Perlink Session to Detect Eth-Trunk Member Link Faults on a VLAN

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130782130__fig_dc_vrp_bfd_cfg_011401), DeviceA and DeviceB are directly connected through Eth-Trunk interfaces. The Eth-Trunk interfaces on the two devices are added to VLAN 100. BFD is required to detect faults on the link between DeviceA and DeviceB. If a single-hop BFD session is bound to the VLANIF interface to detect Eth-Trunk link faults, BFD selects one of the Eth-Trunk member links as the detection path and monitors only this member link. Once BFD detects that the selected member link is down, it assumes that the Eth-Trunk link is down even if the other Eth-Trunk member links are up. To prevent BFD from incorrectly reporting link faults, deploy BFD for Perlink sessions instead of single-hop BFD sessions.

**Figure 1** Network diagram of configuring a BFD for Perlink session to detect Eth-Trunk member link faults on a VLAN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001130782160.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an Eth-Trunk interface on DeviceA and DeviceB, and add Ethernet physical interfaces to each Eth-Trunk interface.
2. Create a VLAN on DeviceA and DeviceB, add the Eth-Trunk interface to the VLAN, and create a VLANIF interface to implement Layer 3 interworking between the two devices through the VLANIF interface.
3. Configure a BFD for Perlink session on DeviceA and DeviceB to monitor the Eth-Trunk member links between the devices.

#### Procedure

1. Create an Eth-Trunk interface on DeviceA and DeviceB, and add Ethernet physical interfaces to each Eth-Trunk interface.
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface Eth-Trunk 1
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
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130782130__context197516915919).
2. Create a VLAN on DeviceA and DeviceB, add the Eth-Trunk interface to the VLAN, and create a VLANIF interface to implement Layer 3 interworking between the two devices through the VLANIF interface.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] vlan 100
   [~DeviceA-vlan100] quit
   [*DeviceA] commit
   [~DeviceA] interface Eth-Trunk 1
   [~DeviceA-Eth-Trunk1] portswitch
   [~DeviceA-Eth-Trunk1] port link-type access
   [*DeviceA-Eth-Trunk1] port default vlan 100
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   [~DeviceA] interface Vlanif 100
   [*DeviceA-Vlanif100] ip address 10.1.1.1 24
   [*DeviceA-Vlanif100] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] vlan 100
   [~DeviceB-vlan100] quit
   [*DeviceB] commit
   [~DeviceB] interface Eth-Trunk 1
   [~DeviceB-Eth-Trunk1] portswitch
   [~DeviceB-Eth-Trunk1] port link-type access
   [*DeviceB-Eth-Trunk1] port default vlan 100
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] commit
   [~DeviceB] interface Vlanif 100
   [*DeviceB-Vlanif100] ip address 10.1.1.2 24
   [*DeviceB-Vlanif100] quit
   [*DeviceB] commit
   ```
3. Configure a BFD for Perlink session on DeviceA and DeviceB to monitor the Eth-Trunk member links between the devices.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] bfd atob bind peer-ip 10.1.1.2 interface Vlanif 100 source-ip 10.1.1.1 per-link one-arm-echo
   [*DeviceA-bfd-session-atob] min-rx-interval 10
   [*DeviceA-bfd-session-atob] min-tx-interval 10
   [*DeviceA-bfd-session-atob] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check that the VLANIF interfaces on DeviceA and DeviceB can ping each other.

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

# Run the **display bfd session all verbose** command on DeviceA to check the BFD session status.

```
[~DeviceA] display bfd session all verbose
(w): State in WTR 
(*): State is invalid
Total UP/DOWN Session Number : 3/0
--------------------------------------------------------------------------------
  Name : atob                  (Single Hops)   State : Up
--------------------------------------------------------------------------------
  Local Discriminator    : 1048576            Remote Discriminator   : 1048576
  Session Detect Mode    : Asynchronous Mode With Echo Function
  BFD Bind Type          : Interface(Vlanif100)  
  Bind Session Type      : Static_Auto(Bundle_Main) 
  Bind Peer IP Address   : 10.1.1.2        
  Bind Interface         : Vlanif100                                         
  Bind Source IP Address : 10.1.1.1   
  FSM Board ID           : -                ToS-EXP                : 7
  Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
  Actual Tx Interval (ms): -                Actual Rx Interval (ms): - 
  WTR Interval (ms)      : -                Detect Interval (ms)   : - 
  Local Detect Multi     : 3                Active Multi           : -  
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 3784             TTL                    : 255
  Proc Interface Status  : Disable          Process PST            : Disable
  Config PST             : Disable
  Last Local Diagnostic  : Control Detection Time Expired
  Bind Application       : AUTO   
  Session Description    : - 
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
  Name : dyn_16386             (Single Hops)   State : Up
--------------------------------------------------------------------------------
  Local Discriminator    : 16386            Remote Discriminator   : 16386
  Session Detect Mode    : Asynchronous Mode With Echo Function
  BFD Bind Type          : Interface(100GE1/0/1)  
  Bind Session Type      : Dynamic(Bundle_Sub) 
  Bind Peer IP Address   : 10.1.1.2        
  Bind Interface         : 100GE1/0/1                                     
  Bind Source IP Address : 10.1.1.1   
  FSM Board ID           : 3                ToS-EXP                : 7
  Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
  Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10 
  WTR Interval (ms)      : -                Detect Interval (ms)   : 30 
  Local Detect Multi     : 3                Active Multi           : 3 
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 3784             TTL                    : 255
  Proc Interface Status  : Disable          Process PST            : Disable
  Config PST             : Disable
  Last Local Diagnostic  : Control Detection Time Expired
  Bind Application       : BFD   
  Session Description    : - 
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
  Name : dyn_16387             (Single Hops)   State : Up
--------------------------------------------------------------------------------
  Local Discriminator    : 16387            Remote Discriminator   : 16387
  Session Detect Mode    : Asynchronous Mode With Echo Function
  BFD Bind Type          : Interface(100GE1/0/2)  
  Bind Session Type      : Dynamic(Bundle_Sub) 
  Bind Peer IP Address   : 10.1.1.2        
  Bind Interface         : 100GE1/0/2                                     
  Bind Source IP Address : 10.1.1.1   
  FSM Board ID           : 3                ToS-EXP                : 7
  Min Tx Interval (ms)   : 10               Min Rx Interval (ms)   : 10
  Actual Tx Interval (ms): 10               Actual Rx Interval (ms): 10 
  WTR Interval (ms)      : -                Detect Interval (ms)   : 30 
  Local Detect Multi     : 3                Active Multi           : 3 
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 3784             TTL                    : 255
  Proc Interface Status  : Disable          Process PST            : Disable
  Config PST             : Disable
  Last Local Diagnostic  : Control Detection Time Expired
  Bind Application       : BFD   
  Session Description    : - 
--------------------------------------------------------------------------------
```

The command output shows that three BFD sessions have been established on DeviceA and are in the **Up** state. The discriminators of the three BFD sessions are dynamically allocated. The BFD session bound to VLANIF 100 is a management session, and the other two BFD sessions are sub-sessions. The BFD sub-sessions are bound to Ethernet physical interfaces 100GE1/0/1 and 100GE1/0/2, respectively.

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
(w): State in WTR 
(*): State is invalid
Total UP/DOWN Session Number : 2/1
--------------------------------------------------------------------------------
Local      Remote     PeerIpAddr      State     Type        InterfaceName 
--------------------------------------------------------------------------------
16385      16385      10.1.1.2       Up        S/AUTO-IF   Vlanif100
16386      16386      10.1.1.2       Down      D/IP-IF     100GE1/0/1
16387      16387      10.1.1.2       Up        D/IP-IF     100GE1/0/2
--------------------------------------------------------------------------------
```

The command output shows that the BFD sub-session bound to 100GE1/0/1 is in the **Down** state, but the BFD management session bound to VLANIF 100 remains in the **Up** state.

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
(w): State in WTR 
(*): State is invalid
Total UP/DOWN Session Number : 0/3
--------------------------------------------------------------------------------
Local      Remote     PeerIpAddr      State     Type        InterfaceName 
--------------------------------------------------------------------------------
16385      16385      10.1.1.2       Down      S/AUTO-IF   Vlanif100
16386      16386      10.1.1.2       Down      D/IP-IF     100GE1/0/1
16387      16387      10.1.1.2       Down      D/IP-IF     100GE1/0/2
--------------------------------------------------------------------------------
```

The command output shows that the three BFD sessions are in the **Down** state.


#### Configuration Scripts

* DeviceA
  ```
  #
   sysname DeviceA
  #
   vlan 100
  #
   bfd
  #
  interface Vlanif100
   ip address 10.1.1.1 255.255.255.0
  #
  interface Eth-Trunk1
   port default vlan 100
  #
  interface 100GE1/0/1
   eth-trunk 1
  #
  interface 100GE1/0/2
   eth-trunk 1
  #
  bfd atob bind peer-ip 10.1.1.2 interface Vlanif100 source-ip 10.1.1.1 per-link one-arm-echo
   min-tx-interval 10
   min-rx-interval 10
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  vlan batch 100
  #
  interface Vlanif100
   ip address 10.1.1.2 255.255.255.0
  #
  interface Eth-Trunk1
   port default vlan 100
  #
  interface 100GE1/0/1
   eth-trunk 1
  #
  interface 100GE1/0/2
   eth-trunk 1
  #
  return
  ```