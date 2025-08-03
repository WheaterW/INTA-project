Example for Configuring MPAC
============================

This section provides an example for configuring an MPAC policy and applying it globally and on a specific interface.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372612__fig_dc_vrp_mpac_cfg_001101), deploy an MPAC policy on DeviceA to prevent it from being attacked by various TCP/IP attack packets.

**Figure 1** MPAC network diagram![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE0/1/0.


  
![](images/fig_dc_vrp_mpac_cfg_001101.png)

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface addresses and routes to ensure network connectivity.
2. Configure an IPv4 MPAC policy named test on DeviceA.
3. Apply the IPv4 MPAC policy named test on GE0/1/0.
4. Apply the IPv4 MPAC policy named test on DeviceA globally.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IP addresses and routes
* Policy for restricting the sending of packets to the CPU
* IPv4 MPAC policy to be applied globally
* IPv4 MPAC policy to be applied on a specific interface

#### Procedure

1. Configure interface IP addresses and routes to ensure network connectivity. For configuration details, see [Configuration Files](#EN-US_TASK_0172372612__p1) in this section.
2. Configure an IPv4 MPAC policy named test on DeviceA.
   
   
   ```
   <~DeviceA> system-view
   ```
   ```
   [~DeviceA] service-security policy ipv4 test
   ```
   ```
   [*DeviceA-service-sec-test] rule 10 deny protocol ip source-ip 10.10.1.1 0
   ```
   ```
   [*DeviceA-service-sec-test] step 10
   ```
   ```
   [*DeviceA-service-sec-test] description rule 10 is deny ip packet which from 10.10.1.1
   ```
   ```
   [*DeviceA-service-sec-test] commit
   ```
   ```
   [~DeviceA-service-sec-test] quit
   ```
3. Apply the IPv4 MPAC policy named test on DeviceA globally.
   
   
   ```
   [~DeviceA] service-security global-binding ipv4 test
   ```
   ```
   [*DeviceA] commit
   ```
4. Apply the IPv4 MPAC policy named test on GE0/1/0 of DeviceA.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] service-security binding ipv4 test
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
5. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display service-security statistics** command to check information about the rules in the IPv4 MPAC policy.
   
   ```
   [~DeviceA] display service-security statistics ipv4 test
   ```
   ```
   Policy Name : test
   Description : rule 10 is deny ip packet which from 10.10.1.1
   Step        : 10
    rule 10 deny protocol ip source-ip 10.10.1.1 0 (10 times matched)
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  service-security global-binding ipv4 test
  #
  service-security policy ipv4 test
   description rule 10 is deny ip packet which from 10.10.1.1
   step 10
   rule 10 deny protocol ip source-ip 10.10.1.1 0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
   service-security binding ipv4 test
  #
  ```