Example for Configuring Static ARP
==================================

This example provides an example for configuring static ARP.

#### Networking Requirements

ARP is a basic link layer protocol that maps devices' IP addresses to MAC addresses. ARP is simple to use but does not have any security guarantee. Attackers may send forged ARP packets to attack networks, interrupting normal services or even breaking devices down. Therefore, carriers want to enhance backbone network security.

As shown in [Figure 1](#EN-US_TASK_0172364514__fig_dc_vrp_arp_cfg_206101), hosts connect to the backbone network through Routers. To protect the devices on the backbone network against ARP attacks and ensure stable data transmission, configure static ARP on Routers.

**Figure 1** Configuring static ARP  
![](figure/en-us_image_0000001576581913.png)

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is to configure static ARP entries on Routers. These entries will not be aged or overwritten by dynamic ARP entries so that user data can be stably transmitted.


#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses for which mapping needs to be performed
* MAC addresses for which mapping needs to be performed

#### Procedure

1. Configure static ARP entries on DeviceA. The configuration of DeviceB is similar to the configuration of DeviceA.
   
   
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
   [~DeviceA] arp static 10.1.1.1 00e0-fc41-0200
   ```
   ```
   [*DeviceA] arp static 10.1.1.2 00e0-fc41-0202
   ```
   ```
   [*DeviceA] arp static 10.1.1.3 00e0-fc41-0204
   ```
   ```
   [*DeviceA] commit
   ```
2. Verify the configuration.
   
   # Run the **display arp all** command on DeviceA to check configured ARP entries.
   ```
   <DeviceA> display arp all
   ```
   ```
   IP ADDRESS      MAC ADDRESS    EXPIRE(M) TYPE        INTERFACE   VPN-INSTANCE
                                            VLAN/CEVLAN PVC
   ------------------------------------------------------------------------------
   10.1.1.1        00e0-fc41-0200           S--
   10.1.1.2        00e0-fc41-0202           S--
   10.1.1.3        00e0-fc41-0204           S--
   ------------------------------------------------------------------------------
   Total:3         Dynamic:0       Static:3    Interface:0    Remote:0    
   Redirect:0
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
  arp static 10.1.1.1 00e0-fc41-0200
  arp static 10.1.1.2 00e0-fc41-0202
  arp static 10.1.1.3 00e0-fc41-0204
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
  arp static 10.1.2.1 00e0-fc41-0300
  arp static 10.1.2.2 00e0-fc41-0302
  arp static 10.1.2.3 00e0-fc41-0304
  ```
  ```
  #
  ```
  ```
  return
  ```