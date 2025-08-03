Example for Configuring Dynamic BFD for IS-IS
=============================================

Example for Configuring Dynamic BFD for IS-IS

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130784126__fig_dc_vrp_isis_cfg_008701), IS-IS runs on DeviceA, DeviceB, and DeviceC. BFD for IS-IS is enabled on DeviceA, DeviceB, and DeviceC. Service traffic is transmitted over the primary link DeviceA -> DeviceB. The link DeviceA -> DeviceC -> DeviceB serves as the backup link. BFD is configured for the interfaces on the link between DeviceA and DeviceB. If the link fails, BFD can fast detect the failure and notify IS-IS of the failure so that service traffic can be transmitted through the backup link.

**Figure 1** Network diagram of dynamic BFD for IS-IS![](public_sys-resources/note_3.0-en-us.png) 

Interface 1, interface 2, and interface 3 in this example represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130784172.png)

#### Configuration Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see Configuring IS-IS Authentication. IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic IS-IS functions on each device for interworking.
2. Configure an IS-IS cost for each interface on each device (except the switch).
3. Enable BFD globally.
4. Enable BFD for IS-IS on DeviceA, DeviceB, and DeviceC.
5. Enable BFD for the interfaces on DeviceA and DeviceB.

#### Procedure

1. Configure IPv4 addresses for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.1.3.1 255.255.255.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784126__postreq24192593172748).
2. Configure basic IS-IS functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis
   [*DeviceA-isis-1] is-level level-2
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] isis enable 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784126__postreq24192593172748).
   
   # Run the [**display isis peer**](cmdqueryname=display+isis+peer) command. The command output shows that an IS-IS neighbor relationship has been established between DeviceA and DeviceB, and between DeviceA and DeviceC. DeviceA is used as an example.
   
   ```
   [~DeviceA] display isis peer
   Peer information for ISIS(1)
   ----------------------------------------------------------------------------------
                                                                   
   System ID        Interface        Circuit ID          State HoldTime Type      PR
   ----------------------------------------------------------------------------------
   0000.0000.0002  100GE1/0/2            0000.0000.0002.01 Up   9s       L2       64
   0000.0000.0003  100GE1/0/1            0000.0000.0001.02 Up   21s      L2       64
   Total Peer(s): 2
   ```
   
   # Devices have learned routes from each other. The following example uses the command output on Device A.
   
   ```
   [~DeviceA] display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: _public_
            Destinations : 8        Routes : 9
   Destination/Mask      Proto   Pre  Cost     Flags NextHop          Interface
           10.1.1.0/24    Direct  0    0           D  10.1.1.1        100GE1/0/1
           10.1.1.1/32    Direct  0    0           D  127.0.0.1       InLoopBack0
           10.1.2.0/24    ISIS    15   20          D  10.1.1.2         100GE1/0/1
           10.1.3.0/24    Direct  0    0           D  10.1.3.1         100GE1/0/2
           10.1.3.1/32    Direct  0    0           D  127.0.0.1       InLoopBack0
           127.0.0.0/8    Direct  0    0           D  127.0.0.1       InLoopBack0
         127.0.0.1/32     Direct  0    0           D  127.0.0.1       InLoopBack0
         172.16.1.0/24  ISIS   15   20          D  10.1.3.2        100GE1/0/2
   ```
   
   According to the preceding command output, the next hop address of the route to 172.16.1.0/24 is 10.1.3.2, and traffic is transmitted on the primary link DeviceA -> DeviceB.
3. Configure an IS-IS cost for each interface on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] isis cost 5
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784126__postreq24192593172748).
4. Enable BFD for IS-IS.
   
   
   
   # Enable BFD for IS-IS on DeviceA.
   
   ```
   [~DeviceA] bfd
   [*DeviceA-bfd] quit
   [*DeviceA] isis
   [*DeviceA-isis-1] bfd all-interfaces enable
   [*DeviceA-isis-1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784126__postreq24192593172748).
   
   # Run the [**display isis bfd**](cmdqueryname=display+isis+bfd) **session** **all** command on DeviceA, DeviceB, or DeviceC. The command output shows that the BFD session is up. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display isis bfd session all
   BFD session information for ISIS(1)                    
   -----------------------------------------------------------------
   Peer System ID : 0000.0000.0002        Interface : 100GE1/0/2
   TX : 10            BFD State : up      Peer IP Address : 10.1.3.2
   RX : 10            LocDis : 16385      Local IP Address: 10.1.3.1
   Multiplier : 3     RemDis : 16388      Type : L2
   Diag : No diagnostic information
   
   Peer System ID : 0000.0000.0003        Interface : 100GE1/0/1
   TX : 10            BFD State : up      Peer IP Address : 10.1.1.2
   RX : 10            LocDis : 16386      Local IP Address: 10.1.1.1
   Multiplier : 3     RemDis : 16387      Type : L2
   Diag : No diagnostic information
   Total BFD session(s): 2                       
   ```
   
   According to the preceding command output, the BFD sessions between DeviceA and DeviceB and between DeviceA and DeviceC are up.
5. Configure BFD for interfaces.
   
   
   
   # Configure BFD on 100GE 1/0/2 of DeviceA, set the minimum interval at which BFD packets are sent to 100 ms, the minimum interval at which BFD packets are received to 100 ms, and the local detection multiplier to 4.
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] isis bfd enable
   [*DeviceA-100GE1/0/2] isis bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure BFD on 100GE 1/0/2 of DeviceB, set the minimum interval at which BFD packets are sent to 100 ms, the minimum interval at which BFD packets are received to 100 ms, and the local detection multiplier to 4.
   
   ```
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] isis bfd enable
   [*DeviceB-100GE1/0/2] isis bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Run the [**display isis bfd**](cmdqueryname=display+isis+bfd) **session** **all** command on DeviceB. The command output shows that BFD parameters have taken effect.

```
[~DeviceB] display isis bfd session all
BFD session information for ISIS(1)                    
-----------------------------------------------------------------
Peer System ID : 0000.0000.0001        Interface : 100GE1/0/2
TX : 100           BFD State : up      Peer IP Address : 10.1.3.1
RX : 100           LocDis : 16385      Local IP Address: 10.1.3.2
Multiplier : 4     RemDis : 16385      Type : L2
Diag : No diagnostic information

Peer System ID : 0000.0000.0003        Interface : 100GE1/0/1
TX : 10            BFD State : up      Peer IP Address : 10.1.2.1
RX : 10            LocDis : 16385      Local IP Address: 10.1.2.2
Multiplier : 4     RemDis : 16385      Type : L2
Diag : No diagnostic information
Total BFD session (s):2                    
```

# Run the [**shutdown**](cmdqueryname=shutdown) command on 100GE 1/0/2 of DeviceB to simulate a failure of the primary link.

```
[~DeviceB] interface 100ge 1/0/2
[~DeviceB-100GE1/0/2] shutdown
[*DeviceB] commit
```

# Check the IP routing table of DeviceA.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 9        Routes : 9

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

        10.1.1.0/24  Direct 0    0             D  10.1.1.1        100GE1/0/1
        10.1.1.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
      10.1.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
        10.1.2.0/24  ISIS  15   20             D  10.1.1.2        100GE1/0/1
      127.0.0.0/8    Direct 0    0             D  127.0.0.1       InLoopBack0
      127.0.0.1/32   Direct 0    0             D  127.0.0.1       InLoopBack0
127.255.255.255/32   Direct 0    0             D  127.0.0.1       InLoopBack0
  172.16.1.0/24   ISIS  15   30           D  10.1.1.2      100GE1/0/1
255.255.255.255/32   Direct 0    0             D  127.0.0.1       InLoopBack0   
```

According to the preceding command output, the backup link DeviceA -> DeviceC -> DeviceB takes effect, and the next hop address of the route to 172.16.1.0/24 becomes 10.1.1.2.

# Run the [**display isis bfd**](cmdqueryname=display+isis+bfd) **session** **all** command on DeviceA. The command output shows that only the BFD session between DeviceA and DeviceC is up.

```
[~DeviceA] display isis bfd session all
BFD session information for ISIS(1)                    
-----------------------------------------------------------------
Peer System ID : 0000.0000.0003        Interface : 100GE1/0/1
TX : 10            BFD State : up      Peer IP Address : 10.1.1.2
RX : 10            LocDis : 16385      Local IP Address: 10.1.1.1
Multiplier : 3     RemDis : 16388      Type : L2
Diag : No diagnostic information
Total BFD session (s):1                       
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  isis 1
   is-level level-2
   bfd all-interfaces enable
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
   isis enable 1
   isis cost 5
   isis bfd enable
   isis bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  bfd
  #
  isis 1
   is-level level-2
   bfd all-interfaces enable
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.2 255.255.255.0
   isis enable 1
   isis cost 5
   isis bfd enable
   isis bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
   isis enable 1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  bfd
  #
  isis 1
   is-level level-2
   bfd all-interfaces enable
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
  #
  return
  ```