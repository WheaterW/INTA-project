Example for Configuring Basic RIP Functions
===========================================

This section describes how to configure basic RIP functions, including how to enable RIP and configure a RIP version number on each device.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365881__fig73601147124514), it is required that RIP be enabled on all interfaces of DeviceA, DeviceB, DeviceC, and DeviceD and that these interfaces communicate with each other through RIP-2.

**Figure 1** Configuring basic RIP functions![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_rip_cfg_004801.png)

#### Precautions

During the configuration, note the following:

* Different network segments on the same physical interface cannot be enabled in different RIP processes.
* If a RIP process is bound to a VPN instance, interfaces in this RIP process also need to be bound to the VPN instance.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface to ensure network connectivity.
2. Configure RIP-2 packet authentication.
3. Enable RIP and configure basic RIP functions on each Router.
4. Configure RIP-2 on each Router and check the subnet mask.

#### Data Preparation

To complete the configuration, you need the following data:

* RIP-enabled network segment 192.168.1.0 on DeviceA
* RIP-enabled network segments 192.168.1.0, 172.16.0.0, and 10.0.0.0 on DeviceB
* RIP-enabled network segment 172.16.0.0 on DeviceC
* RIP-enabled network segment 10.0.0.0 on DeviceD
* RIP-2 on DeviceA, DeviceB, DeviceC, and DeviceD

#### Procedure

1. Assign an IP address to each interface. For configuration details, see configuration files in this section.
2. Configure RIP-2 packet authentication.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] rip authentication-mode hmac-sha256 cipher YsHsjx_202206 200
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA] quit
   ```
   
   The configurations of other devices are similar to the configuration of DeviceA. For configuration details, see configuration files.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The directly connected interfaces must be configured with the same authentication password. Otherwise, the neighbor relationship cannot be established.
3. Configure the network segments to be enabled with RIP.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] rip
   ```
   ```
   [*DeviceA-rip-1] network 192.168.1.0
   ```
   ```
   [*DeviceA-rip-1] commit
   ```
   ```
   [~DeviceA-rip-1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] rip
   ```
   ```
   [*DeviceB-rip-1] network 192.168.1.0
   ```
   ```
   [*DeviceB-rip-1] network 172.16.0.0
   ```
   ```
   [*DeviceB-rip-1] network 10.0.0.0
   ```
   ```
   [*DeviceB-rip-1] commit
   ```
   ```
   [~DeviceB-rip-1] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] rip
   ```
   ```
   [*DeviceC-rip-1] network 172.16.0.0
   ```
   ```
   [*DeviceC-rip-1] commit
   ```
   ```
   [~DeviceC-rip-1] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] rip
   ```
   ```
   [*DeviceD-rip-1] network 10.0.0.0
   ```
   ```
   [*DeviceD-rip-1] commit
   ```
   ```
   [~DeviceD-rip-1] quit
   ```
   
   # Check the RIP routing table of DeviceA.
   
   ```
   [~DeviceA] display rip 1 route
   ```
   ```
    Route Flags: R - RIP
   ```
   ```
                 A - Aging, S - Suppressed, G - Garbage-collect
   ```
   ```
   -------------------------------------------------------------------------
   ```
   ```
    Peer 192.168.1.2  on GigabitEthernet0/1/0
   ```
   ```
         Destination/Mask        Nexthop     Cost   Tag     Flags   Sec
   ```
   ```
            10.0.0.0/8        192.168.1.2      1    0        RA      14
   ```
   ```
            172.16.0.0/16     192.168.1.2      1    0        RA      14
   ```
   
   The command output shows that the routes advertised by RIP-1 use natural masks.
4. Configure the RIP version number.
   
   
   
   # Configure RIP-2 on DeviceA.
   
   ```
   [~DeviceA] rip
   ```
   ```
   [~DeviceA-rip-1] version 2
   ```
   ```
   [*DeviceA-rip-1] commit
   ```
   ```
   [~DeviceA-rip-1] quit
   ```
   
   # Configure RIP-2 on DeviceB.
   
   ```
   [~DeviceB] rip
   ```
   ```
   [~DeviceB-rip-1] version 2
   ```
   ```
   [*DeviceB-rip-1] commit
   ```
   ```
   [~DeviceB-rip-1] quit
   ```
   
   # Configure RIP-2 on DeviceC.
   
   ```
   [~DeviceC] rip
   ```
   ```
   [~DeviceC-rip-1] version 2
   ```
   ```
   [*DeviceC-rip-1] commit
   ```
   ```
   [~DeviceC-rip-1] quit
   ```
   
   # Configure RIP-2 on DeviceD.
   
   ```
   [~DeviceD] rip
   ```
   ```
   [~DeviceD-rip-1] version 2
   ```
   ```
   [*DeviceD-rip-1] commit
   ```
   ```
   [~DeviceD-rip-1] quit
   ```
5. Verify the configuration.
   
   
   
   # Check the RIP routing table of DeviceA.
   
   ```
   [~DeviceA] display rip 1 route
   ```
   ```
   Route Flags: R - RIP
   ```
   ```
                A - Aging, S - Suppressed, G - Garbage-collect 
   ```
   ```
   -------------------------------------------------------------------------
   ```
   ```
    Peer 192.168.1.2  on GigabitEthernet0/1/0
   ```
   ```
         Destination/Mask        Nexthop       Cost   Tag     Flags   Sec
   ```
   ```
            10.1.1.0/24         192.168.1.2      1    0        RA      32
   ```
   ```
            172.16.1.0/24       192.168.1.2      1    0        RA      32
   ```
   
   The command output shows that the routes advertised by RIP-2 contain more accurate subnet masks.

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
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
   rip authentication-mode hmac-sha256 cipher %^%#c;\wJ4Qi8I1FMGM}KmIK9rha/.D.!$"~0(Ep66z~%^%# 200
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 1.1.1.1 255.255.255.255 
  ```
  ```
   rip enable 1
  ```
  ```
  #
  ```
  ```
  rip 1
  ```
  ```
   version 2
  ```
  ```
   network 192.168.1.0
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
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
   rip authentication-mode hmac-sha256 cipher %^%#*&/]"$OoC.u#h5%iA0Q.3,$mP{]0;Ivk-,Gyy/w4%^%# 200
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
   ip address 172.16.1.1 255.255.255.0
  ```
  ```
   rip authentication-mode hmac-sha256 cipher %^%#BVZr*tW;4"],!H~L\*XPyb.Y!BVdHE`D,uM~1q"<%^%# 200
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
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   rip authentication-mode hmac-sha256 cipher %^%#D[hPG}hUbHNR-EJM.%=P&OR}NU]W&L>GAd84)-7,%^%# 200
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 2.2.2.2 255.255.255.255 
  ```
  ```
   rip enable 1
  ```
  ```
  #
  ```
  ```
  rip 1
  ```
  ```
   version 2
  ```
  ```
   network 10.0.0.0
  ```
  ```
   network 172.16.0.0
  ```
  ```
   network 192.168.1.0
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
   ip address 172.16.1.2 255.255.255.0
  ```
  ```
   rip authentication-mode hmac-sha256 cipher %^%#ogrEOF0J;)8umQDUcfm8uc92G2xV@By=^#;<~2zF%^%# 200
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 3.3.3.3 255.255.255.255 
  ```
  ```
   rip enable 1
  ```
  ```
  #
  ```
  ```
  rip 1
  ```
  ```
   version 2
  ```
  ```
   network 172.16.0.0
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
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   rip authentication-mode hmac-sha256 cipher %^%#+40P:fm"RB,[>}'<6O1B"!K[Go_=u4Q]Yp$Hh:wJ%^%# 200
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 4.4.4.4 255.255.255.255 
  ```
  ```
   rip enable 1
  ```
  ```
  #
  ```
  ```
  rip 1
  ```
  ```
   version 2
  ```
  ```
   network 10.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```