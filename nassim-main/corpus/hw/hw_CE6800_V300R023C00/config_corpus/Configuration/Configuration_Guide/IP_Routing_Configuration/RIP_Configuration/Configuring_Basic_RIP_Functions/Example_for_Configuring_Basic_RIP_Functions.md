Example for Configuring Basic RIP Functions
===========================================

Example for Configuring Basic RIP Functions

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176742627__fig_dc_vrp_rip_cfg_004801), RIP needs to be enabled on all interfaces on DeviceA, DeviceB, DeviceC, and DeviceD. These devices need to be interconnected through RIP-2.

**Figure 1** Network diagram of basic RIP function configuration![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130623198.png)

#### Precautions

When configuring basic RIP functions, consider the following factors:

* Different network segments on the same physical interface must be configured in the same RIP process.
* If a RIP process is bound to a VPN instance, interfaces in this RIP process also need to be bound to the VPN instance.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface to ensure network connectivity.
2. Configure RIP-2 packet authentication.
3. Enable RIP and configure basic RIP functions on each device.
4. Configure RIP-2 on each device and check the subnet mask.

#### Procedure

1. Assign an IP address to each interface. The configuration details are omitted.
2. Configure RIP-2 packet authentication.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA] interface 100ge1/0/1
   [*DeviceA-100GE1/0/1] rip authentication-mode hmac-sha256 cipher YsHsjx_202206 200
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of other devices are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The directly connected interfaces must be configured with the same authentication password. Otherwise, the neighbor relationship cannot be established.
3. Configure the network segments to be enabled with RIP.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] rip
   [*DeviceA-rip-1] network 192.168.1.0
   [*DeviceA-rip-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] rip
   [*DeviceB-rip-1] network 192.168.1.0
   [*DeviceB-rip-1] network 172.16.0.0
   [*DeviceB-rip-1] network 10.0.0.0
   [*DeviceB-rip-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] rip
   [*DeviceC-rip-1] network 172.16.0.0
   [*DeviceC-rip-1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] rip
   [*DeviceD-rip-1] network 10.0.0.0
   [*DeviceD-rip-1] quit
   [*DeviceD] commit
   ```
4. Configure the RIP version number.
   
   
   
   # Configure RIP-2 on DeviceA.
   
   ```
   [~DeviceA] rip
   [*DeviceA-rip-1] version 2
   [*DeviceA-rip-1] quit
   [*DeviceA] commit
   ```
   
   # Configure RIP-2 on DeviceB.
   
   ```
   [~DeviceB] rip
   [*DeviceB-rip-1] version 2
   [*DeviceB-rip-1] quit
   [*DeviceB] commit
   ```
   
   # Configure RIP-2 on DeviceC.
   
   ```
   [~DeviceC] rip
   [*DeviceC-rip-1] version 2
   [*DeviceC-rip-1] quit
   [*DeviceC] commit
   ```
   
   # Configure RIP-2 on DeviceD.
   
   ```
   [~DeviceD] rip
   [*DeviceD-rip-1] version 2
   [*DeviceD-rip-1] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# After configuring a RIP network segment, check the RIP routing table of DeviceA. The command output shows that the routes advertised by RIP-1 use natural masks.

```
[~DeviceA] display rip 1 route
 Route Flags: R - RIP, T - TRIP
              P - Permanent, A - Aging, S - Suppressed, G - Garbage-collect
-------------------------------------------------------------------------
 Peer 192.168.1.2  on 100GE1/0/1
      Destination/Mask        Nexthop     Cost   Tag     Flags   Sec
         10.0.0.0/8        192.168.1.2      1    0        RA      14
        172.16.0.0/16      192.168.1.2      1    0        RA      14
```

# After configuring a RIP version number, check the RIP routing table of DeviceA. The command output shows that the routes advertised by RIP-2 contain more accurate subnet masks.

```
[~DeviceA] display rip 1 route
Route Flags: R - RIP
          A - Aging, S - Suppressed, G - Garbage-collect 
-------------------------------------------------------------------------
 Peer 192.168.1.2  on 100GE1/0/1
      Destination/Mask        Nexthop       Cost   Tag     Flags   Sec
         10.1.1.0/24         192.168.1.2      1    0        RA      32
        172.16.1.0/24        192.168.1.2      1    0        RA      32

```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
   rip authentication-mode hmac-sha256 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%# 200
  #
  rip 1
   version 2
   network 192.168.1.0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   rip authentication-mode hmac-sha256 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%# 200
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.16.1.1 255.255.255.0
   rip authentication-mode hmac-sha256 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%# 200
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   rip authentication-mode hmac-sha256 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%# 200
  #
  rip 1
   version 2
   network 10.0.0.0
   network 172.16.0.0
   network 192.168.1.0
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.2 255.255.255.0
   rip authentication-mode hmac-sha256 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%# 200
  #
  rip 1
   version 2
   network 172.16.0.0
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   rip authentication-mode hmac-sha256 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%# 200
  #
  rip 1
   version 2
   network 10.0.0.0
  #
  return
  ```