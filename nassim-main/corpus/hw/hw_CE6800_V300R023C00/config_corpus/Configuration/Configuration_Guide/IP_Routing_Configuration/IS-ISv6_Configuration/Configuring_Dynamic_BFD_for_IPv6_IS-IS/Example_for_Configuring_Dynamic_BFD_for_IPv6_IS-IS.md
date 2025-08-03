Example for Configuring Dynamic BFD for IPv6 IS-IS
==================================================

Example for Configuring Dynamic BFD for IPv6 IS-IS

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176662149__en-us_task_0275864047_fig454265411232), two links exist between DeviceS and DeviceD. In normal cases, traffic is transmitted along the primary link. It is required that BFD for IPv6 IS-IS be configured to rapidly switch traffic to the backup link if the primary link or the switch fails.

**Figure 1** Network diagram of dynamic BFD for IPv6 IS-IS![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001229880979.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface.
2. Configure basic IPv6 IS-IS functions on each device (except the switch) to ensure IPv6 connectivity.
3. Configure an IS-IS cost for each interface on each device (except the switch) to ensure that the primary link takes precedence over the backup link.
4. Enable BFD globally on each device (except the switch).
5. Enable BFD for IPv6 IS-IS in the IS-IS view on each device (except the switch).

#### Procedure

1. Assign an IPv6 address to each interface.
   
   
   
   # Configure DeviceS. The configurations of other devices are similar to the configuration of DeviceS. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176662149__en-us_task_0275864047_postreq24192593172748).
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceS
   [*HUAWEI] commit
   [~DeviceS] interface 100ge 1/0/1
   [~DeviceS-100GE1/0/1] undo portswitch
   [*DeviceS-100GE1/0/1] ipv6 enable
   [*DeviceS-100GE1/0/1] ipv6 address 2001:db8:1::1/64
   [*DeviceS-100GE1/0/1] quit
   [*DeviceS] commit
   ```
2. Configure basic IPv6 IS-IS functions.
   
   
   
   # Configure DeviceS.
   
   ```
   [~DeviceS] isis 10
   [*DeviceS-isis-10] is-level level-2
   [*DeviceS-isis-10] network-entity 10.0000.0000.0001.00
   [*DeviceS-isis-10] ipv6 enable
   [*DeviceS-isis-10] quit
   [*DeviceS] interface 100ge 1/0/1
   [*DeviceS-100GE1/0/1] isis ipv6 enable 10
   [*DeviceS-100GE1/0/1] quit
   [*DeviceS] interface 100ge 1/0/2
   [*DeviceS-100GE1/0/2] isis ipv6 enable 10
   [*DeviceS-100GE1/0/2] quit
   [*DeviceS] commit
   ```
   
   # Configure DeviceN.
   
   ```
   [~DeviceN] isis 10
   [*DeviceN-isis-10] is-level level-2
   [*DeviceN-isis-10] network-entity 10.0000.0000.0002.00
   [*DeviceN-isis-10] ipv6 enable
   [*DeviceN-isis-10] quit
   [*DeviceN] interface 100ge 1/0/1
   [*DeviceN-100GE1/0/1] isis ipv6 enable 10
   [*DeviceN-100GE1/0/1] quit
   [*DeviceN] interface 100ge 1/0/2
   [*DeviceN-100GE1/0/2] isis ipv6 enable 10
   [*DeviceN-100GE1/0/2] quit
   [*DeviceN] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] isis 10
   [*DeviceD-isis-10] is-level level-2
   [*DeviceD-isis-10] network-entity 10.0000.0000.0003.00
   [*DeviceD-isis-10] ipv6 enable
   [*DeviceD-isis-10] quit
   [*DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] isis ipv6 enable 10
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] isis ipv6 enable 10
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] interface 100ge 1/0/3
   [*DeviceD-100GE1/0/3] isis ipv6 enable 10
   [*DeviceD-100GE1/0/3] quit
   [*DeviceD] commit
   ```
   
   Run the **display ipv6 routing-table** command. The output shows that the devices (except the switch) have learned IPv6 routes from each other.
3. Configure an IS-IS cost for each interface.
   
   
   
   # Configure DeviceS.
   
   ```
   [~DeviceS] interface 100ge 1/0/1
   [~DeviceS-100GE1/0/1] isis ipv6 cost 1 level-2
   [*DeviceS-100GE1/0/1] quit
   [*DeviceS] interface 100ge 1/0/2
   [*DeviceS-100GE1/0/2] isis ipv6 cost 10 level-2
   [*DeviceS-100GE1/0/2] quit
   [*DeviceS] commit
   ```
   
   # Configure DeviceN.
   
   ```
   [~DeviceN] interface 100ge 1/0/1
   [~DeviceN-100GE1/0/1] isis ipv6 cost 10 level-2
   [*DeviceN-100GE1/0/1] quit
   [*DeviceN] interface 100ge 1/0/2
   [*DeviceN-100GE1/0/2] isis ipv6 cost 10 level-2
   [*DeviceN-100GE1/0/2] quit
   [*DeviceN] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] interface 100ge 1/0/1
   [~DeviceD-100GE1/0/1] isis ipv6 cost 1 level-2
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] isis ipv6 cost 10 level-2
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```
4. Enable BFD for IPv6 IS-IS.
   
   
   
   # Configure DeviceS.
   
   ```
   [~DeviceS] bfd
   [*DeviceS-bfd] quit
   [*DeviceS] isis 10
   [*DeviceS-isis-10] ipv6 bfd all-interfaces enable
   [*DeviceS-isis-10] ipv6 bfd all-interfaces min-tx-interval 150 min-rx-interval 150
   [*DeviceS-isis-10] quit
   [*DeviceS] commit
   ```
   
   # Configure DeviceN.
   
   ```
   [~DeviceN] bfd
   [*DeviceN-bfd] quit
   [*DeviceN] isis 10
   [*DeviceN-isis-10] ipv6 bfd all-interfaces enable
   [*DeviceN-isis-10] ipv6 bfd all-interfaces min-tx-interval 150 min-rx-interval 150
   [*DeviceN-isis-10] quit
   [*DeviceN] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bfd
   [*DeviceD-bfd] quit
   [*DeviceD] isis 10
   [*DeviceD-isis-10] ipv6 bfd all-interfaces enable
   [*DeviceD-isis-10] ipv6 bfd all-interfaces min-tx-interval 150 min-rx-interval 150
   [*DeviceD-isis-10] quit
   [*DeviceD] commit
   ```
   
   # After the configurations are complete, run the **display isis ipv6 bfd session all** command on DeviceS or DeviceD. The command output shows that the BFD parameters have taken effect. The following uses the command output on DeviceS as an example.
   
   ```
   [~DeviceS] display isis ipv6 bfd session all
   
   Peer System ID : 0000.0000.0003        Type : L2
   Interface : 100GE1/0/1           
   IPv6 BFD State : up      TX : 150            RX : 150            Multiplier : 3     
   LocDis : 16386      Local IPv6 Address: FE80::E0:2F47:B103:1
   RemDis : 16386      Peer IPv6 Address : FE80::E0:2F47:B107:1
   Diag : No diagnostic information
   
   Peer System ID : 0000.0000.0002        Type : L2
   Interface : 100GE1/0/2           
   IPv6 BFD State : up      TX : 150            RX : 150            Multiplier : 3     
   LocDis : 16386      Local IPv6 Address: FE80::C964:0:B203:1
   RemDis : 16386      Peer IPv6 Address : FE80::C964:0:B8B6:1
   Diag : No diagnostic information
   
    Total BFD session(s): 2
   ```

#### Verifying the Configuration

# Run the **display ipv6 routing-table 2001:db8:4::1 64** command on DeviceS to check the IPv6 routing table. The command output shows that the next hop address and outbound interface of the route are FE80::E0:2F47:B107:1 and 100GE1/0/1, respectively.

```
[~DeviceS] display ipv6 routing-table 2001:db8:4::1 64
Routing Table : public
Summary Count : 1

Destination  : 2001:db8:4::                            PrefixLength : 64
NextHop      : FE80::E0:2F47:B107:1                    Preference   : 15
Cost         : 11                                      Protocol     : ISIS
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/1                    Flags        : D   
```

# Run the [**shutdown**](cmdqueryname=shutdown) command on 100GE 1/0/1 of DeviceD to simulate a fault on the primary link.

```
[~DeviceD] interface 100ge 1/0/1
[~DeviceD-100GE1/0/1] shutdown
[*DeviceD] commit
```

# Run the **display ipv6 routing-table 2001:db8:4::1 64** command on DeviceS to check the IPv6 routing table.

```
[~DeviceS] display ipv6 routing-table 2001:db8:4::1 64
Routing Table : public
Summary Count : 1

Destination  : 2001:db8:4::                            PrefixLength : 64
NextHop      : FE80::C964:0:B8B6:1                     Preference   : 15
Cost         : 20                                      Protocol     : ISIS
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    :100GE1/0/2                    Flags        : D   
```

According to the preceding command output, the backup link takes effect after the primary link fails. The next hop address of the route to 2001:db8:4::/64 becomes FE80::C964:0:B8B6:1, the outbound interface becomes 100GE 1/0/2, and the route cost changes.

# Run the **display isis ipv6 bfd session all** command on DeviceS. The command output shows that only one BFD session exists between DeviceS and DeviceN and is up.

```
[~DeviceS] display isis ipv6 bfd 10 session all
Peer System ID : 0000.0000.0002        Type : L2
Interface : 100GE1/0/2           
IPv6 BFD State : up      TX : 150            RX : 150            Multiplier : 3
LocDis : 16386      Local IPv6 Address: FE80::C964:0:B203:1
RemDis : 16386      Peer IPv6 Address : FE80::C964:0:B8B6:1
Diag : No diagnostic information

 Total BFD session(s): 1
```

#### Configuration Scripts

* DeviceS
  
  ```
  #
  sysname DeviceS
  #
  bfd
  #
  isis 10
   is-level level-2
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology standard
   ipv6 bfd all-interfaces enable
   ipv6 bfd all-interfaces min-tx-interval 150 min-rx-interval 150
   #
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   isis ipv6 enable 10
   isis ipv6 cost 1 level-2
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   isis ipv6 enable 10
   isis ipv6 cost 10 level-2
   #
  return
  ```
* DeviceN
  
  ```
  #
  sysname DeviceN
  #
  bfd
  #
  isis 10
   is-level level-2
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology standard
   ipv6 bfd all-interfaces enable
   ipv6 bfd all-interfaces min-tx-interval 150 min-rx-interval 150
   #
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   isis ipv6 enable 10
   isis ipv6 cost 10 level-2
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   isis ipv6 enable 10
   isis ipv6 cost 10 level-2
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  bfd
  #
  isis 10
   is-level level-2
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology standard
   ipv6 bfd all-interfaces enable
   ipv6 bfd all-interfaces min-tx-interval 150 min-rx-interval 150
   #
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   isis ipv6 enable 10
   isis ipv6 cost 1 level-2
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
   isis ipv6 enable 10
   isis ipv6 cost 10 level-2
   #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   isis ipv6 enable 10
   #
  return
  ```