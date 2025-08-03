Example for Configuring Basic RIPng Functions
=============================================

This section describes how to configure basic RIPng functions.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365931__fig_dc_vrp_ripng_cfg_002701), it is required that RIPng be enabled on all interfaces of DeviceA, DeviceB, DeviceC, and DeviceD and that these interfaces communicate with each other through RIPng.

**Figure 1** Network diagram of basic RIPng function configuration![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_ripng_cfg_002701.png)

#### Precautions

During the configuration, note the following:

* RIPng takes effect on an interface only after IPv6 is enabled.
* If a RIPng process is bound to a VPN instance, the interfaces running the RIPng process are also bound to the VPN instance.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface to ensure network connectivity.
2. Enable RIPng and configure basic RIPng functions on each Router.
3. Configure IPsec authentication for a RIPng process.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of the interface.

#### Procedure

1. Assign an IPv6 address to each interface. For configuration details, see configuration files in this section.
2. Configure basic RIPng functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA] ripng 1
   ```
   ```
   [*DeviceA-ripng-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ripng 1 enable
   ```
   ```
   [*DeviceA-ripng-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [*DeviceB] ripng 1
   ```
   ```
   [*DeviceB-ripng-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ripng 1 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ripng 1 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/3/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] ripng 1 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [*DeviceC] ripng 1
   ```
   ```
   [*DeviceC-ripng-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ripng 1 enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [*DeviceD] ripng 1
   ```
   ```
   [*DeviceD-ripng-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet0/3/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] ipv6 enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] ripng 1 enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceD] commit
   ```
3. Configure IPsec authentication for a RIPng process.
   
   
   
   # Create an IPSec proposal on DeviceA.
   
   ```
   [~DeviceA] ipsec proposal proposal1
   ```
   ```
   [*DeviceA-ipsec-proposal-proposal1] encapsulation-mode transport
   ```
   ```
   [*DeviceA-ipsec-proposal-proposal1] transform esp
   ```
   ```
   [*DeviceA-ipsec-proposal-proposal1] esp authentication-algorithm sha2-256
   ```
   ```
   [*DeviceA-ipsec-proposal-proposal1] commit
   ```
   ```
   [~DeviceA-ipsec-proposal-proposal1] quit
   ```
   
   # Configure an IPSec SA and apply the IPSec proposal to the SA on DeviceA.
   
   ```
   [~DeviceA] ipsec sa sa1
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] proposal proposal1
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] commit
   ```
   
   # Configure an SPI and a key in the string format on DeviceA.
   
   ```
   [~DeviceA] ipsec sa sa1
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] sa spi inbound esp 12345
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] sa spi outbound esp 12345
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] sa string-key inbound esp abcdef
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] sa string-key outbound esp abcdef
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] commit
   ```
   ```
   [~DeviceA-ipsec-sa-sa1] quit
   ```
   
   
   
   # Configure an SA in the RIPng process on DeviceA.
   
   ```
   [~DeviceA] ripng 1
   ```
   ```
   [*DeviceA-ripng-1] ipsec sa sa1
   ```
   ```
   [*DeviceA-ripng-1] commit
   ```
   
   The configurations of other devices are similar to the configuration of DeviceA. For configuration details, see configuration files.
4. Verify the configuration.
   
   
   
   # Check the neighbors of DeviceA.
   
   ```
   [~DeviceA] display ripng 1 neighbor
   ```
   ```
   Neighbor : FE80::A0A:201:1 GigabitEthernet0/1/0
   ```
   ```
   Protocol : RIPNG
   ```
   
   The command output shows that DeviceA has established neighbor relationships with other devices on the network.
   
   # Check the routing information of DeviceB.
   
   ```
   [~DeviceB] display ripng 1 route
   ```
   ```
   Route Flags: A - Aging, S - Suppressed, G - Garbage-collect
   ```
   ```
   -----------------------------------------------------------
   ```
   ```
   Peer FE80::F54C:0:9FDB:1  on GigabitEthernet0/1/0
   ```
   ```
   Dest 2001:DB8:1::1/96,
   ```
   ```
       via FE80::F54C:0:9FDB:1, cost  1, tag 0, A, 3 Sec
   ```
   ```
   Peer FE80::D472:0:3C23:1  on GigabitEthernet0/2/0
   ```
   ```
   Dest 2001:DB8:2::2/96,
   ```
   ```
       via FE80::D472:0:3C23:1, cost  1, tag 0, A, 4 Sec
   ```
   ```
   Peer FE80::D472:0:3C23:1  on GigabitEthernet0/3/0
   ```
   ```
   Dest 2001:DB8:3::2/96,
   ```
   ```
       via FE80::D472:0:3C23:1, cost  1, tag 0, A, 4 Sec
   ```
   
   The command output shows that DeviceB has learned routing information on the network.

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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1::1/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:8::1/128
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  ipsec proposal proposal1
  ```
  ```
   encapsulation-mode transport
  ```
  ```
   esp authentication-algorithm sha2-256
  ```
  ```
   esp encryption-algorithm aes 256
  ```
  ```
  #
  ```
  ```
  ipsec sa sa1 
  ```
  ```
   proposal proposal1
  ```
  ```
   sa spi inbound esp 12345
  ```
  ```
   sa string-key inbound esp %#%#<}jb{br9\zi%X+/Y@:Y>Lw(L\v#*^KsM"/8RaRe$%#%#
  ```
  ```
   sa spi outbound esp 12345
  ```
  ```
   sa string-key outbound esp %#%#<}j/@X4355SE9JZTD0>GQf"}w2@X,k6.E\Z,z\{#%#%#
  ```
  ```
  #
  ```
  ```
  ripng 1
  ```
  ```
   ipsec sa sa1
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1::2/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:2::1/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:3::1/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:9::1/128
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  ipsec proposal proposal1
  ```
  ```
   encapsulation-mode transport
  ```
  ```
   esp authentication-algorithm sha2-256
  ```
  ```
   esp encryption-algorithm aes 256
  ```
  ```
  #
  ```
  ```
  ipsec sa sa1 
  ```
  ```
   proposal proposal1
  ```
  ```
   sa spi inbound esp 12345
  ```
  ```
   sa string-key inbound esp %#%#<}jb{br9\zi%X+/Y@:Y>Lw(L\v#*^KsM"/8RaRe$%#%#
  ```
  ```
   sa spi outbound esp 12345
  ```
  ```
   sa string-key outbound esp %#%#<}j/@X4355SE9JZTD0>GQf"}w2@X,k6.E\Z,z\{#%#%#
  ```
  ```
  #
  ```
  ```
  ripng 1
  ```
  ```
   ipsec sa sa1
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
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:2::2/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:7::1/128
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  ipsec proposal proposal1
  ```
  ```
   encapsulation-mode transport
  ```
  ```
   esp authentication-algorithm sha2-256
  ```
  ```
   esp encryption-algorithm aes 256
  ```
  ```
  #
  ```
  ```
  ipsec sa sa1 
  ```
  ```
   proposal proposal1
  ```
  ```
   sa spi inbound esp 12345
  ```
  ```
   sa string-key inbound esp %#%#<}jb{br9\zi%X+/Y@:Y>Lw(L\v#*^KsM"/8RaRe$%#%#
  ```
  ```
   sa spi outbound esp 12345
  ```
  ```
   sa string-key outbound esp %#%#<}j/@X4355SE9JZTD0>GQf"}w2@X,k6.E\Z,z\{#%#%#
  ```
  ```
  #
  ```
  ```
  ripng 1
  ```
  ```
   ipsec sa sa1
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
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:3::2/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:6::1/128
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  ipsec proposal proposal1
  ```
  ```
   encapsulation-mode transport
  ```
  ```
   esp authentication-algorithm sha2-256
  ```
  ```
   esp encryption-algorithm aes 256
  ```
  ```
  #
  ```
  ```
  ipsec sa sa1 
  ```
  ```
   proposal proposal1
  ```
  ```
   sa spi inbound esp 12345
  ```
  ```
   sa string-key inbound esp %#%#<}jb{br9\zi%X+/Y@:Y>Lw(L\v#*^KsM"/8RaRe$%#%#
  ```
  ```
   sa spi outbound esp 12345
  ```
  ```
   sa string-key outbound esp %#%#<}j/@X4355SE9JZTD0>GQf"}w2@X,k6.E\Z,z\{#%#%#
  ```
  ```
  #
  ```
  ```
  ripng 1
  ```
  ```
   ipsec sa sa1
  ```
  ```
  #
  ```
  ```
  return
  ```