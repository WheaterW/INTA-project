Example for Configuring DNS-based SSM Mapping
=============================================

If a multicast device has many IGMPv1 and IGMPv2 users and there are many SSM mappings, you can configure the DNS-based SSM mapping function to simplify mapping configuration and maintenance.

#### Networking Requirements

On the multicast network shown in [Figure 1](#EN-US_TASK_0172366774__fig_dc_vrp_multicast_cfg_229101), PIM-SM is run, and the SSM mode is configured to provide multicast services. IGMPv3 runs on the Router interfaces connecting to user hosts Receivers. Receivers run IGMPv2, and the IGMP protocol cannot be upgraded to IGMPv3.

The SSM group address range on the network is 232.1.1.0/24. Source1, Source2, Source3, and Source4 send multicast traffic to the multicast groups in this range. It is required that Receiver1 receive multicast traffic only from Source1 and Source3 while Receiver2 receive multicast traffic only from Source2 and Source4.

**Figure 1** Networking diagram for configuring DNS-based SSM mapping![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, 3, and 4 in this example represent GE 0/1/1, GE 0/1/2, GE 0/1/3, and GE 0/1/4, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_229101.png)  

| Device | Interface Name | Interface IP Address |
| --- | --- | --- |
| DeviceA | GE0/1/1 | 10.0.1.1/24 |
| GE0/1/2 | 192.168.1.1/24 |
| DeviceB | GE0/1/1 | 10.0.3.1/24 |
| GE0/1/2 | 192.168.3.1/24 |
| DeviceC | GE0/1/1 | 192.168.1.2/24 |
| GE0/1/2 | 192.168.3.2/24 |
| GE0/1/3 | 192.168.2.1/24 |
| DeviceD | GE0/1/1 | 10.0.11.1/24 |
| GE0/1/2 | 10.0.10.1/24 |
| GE0/1/3 | 192.168.2.2/24 |
| GE0/1/4 | 10.0.12.1/24 |



#### Precautions

When configuring DNS-based SSM mapping, note the following:

* PIM-SM and IGMP need to be enabled in succession on the interfaces connecting to the hosts.
* The ranges of SSM group addresses configured on all Routers in a PIM-SM domain must be the same.
* Before configuring DNS-based SSM mapping, configure basic IGMP functions. For details, see [Example for Configuring Basic IGMP Functions](dc_vrp_multicast_cfg_2068.html).
* The configured SSM source-group address mappings take effect only after the SSM mapping function is enabled on the interfaces.

#### Configuration Roadmap

1. Assign IP addresses to Router interfaces and configure a unicast routing protocol.
2. Enable multicast routing on all Routers that provide multicast services.
3. Enable PIM-SM on all interfaces of each multicast Router.
4. Enable the IGMP and SSM mapping functions on the interfaces connecting to user hosts.
5. Configure the SSM group address range on all Routers in the PIM-SM domain.
6. Configure DNS-based static SSM mapping on the Router connecting to the user hosts.

#### Data Preparation

To complete the configuration, you need the following data:

* SSM group address range
* IP addresses of Source1, Source2, Source3, and Source4
* DNS server's IP address 10.0.10.5

#### Procedure

1. Assign IP addresses to Router interfaces and configure a unicast routing protocol. For configuration details, see **Configuration Files** in this section.
2. Enable multicast on each Router and PIM-SM on each interface of the Routers.
   
   
   
   # The configurations on DeviceA, DeviceB, and DeviceC are similar to the configuration of DeviceD. For configuration details, see **Configuration Files** in this section.
   
   ```
   [~DeviceD] multicast routing-enable
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/4
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/4] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/4] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/4] quit
   ```
3. Enable the IGMP and SSM mapping functions on the interfaces connecting to user hosts.
   
   
   
   # Enable the IGMP and SSM mapping functions on GE0/1/1 and GE0/1/4 of DeviceD.
   
   ```
   [~DeviceD] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/1] igmp enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] igmp version 3
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] igmp ssm-mapping enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/4
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/4] igmp enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/4] igmp version 3
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/4] igmp ssm-mapping enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/4] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/4] quit
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/4] quit
   ```
4. Set SSM group address ranges.
   
   
   
   # Set the SSM group address range to 232.1.1.0/24 on all Routers. The configurations for DeviceB, DeviceC, and DeviceD are similar to those on DeviceA. For configuration details, see **Configuration Files** in this section.
   
   ```
   [~DeviceA] acl number 2000
   ```
   ```
   [*DeviceA-acl4-basic-2000] rule permit source 232.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-acl4-basic-2000] quit
   ```
   ```
   [*DeviceA] pim
   ```
   ```
   [*DeviceA-pim] ssm-policy 2000
   ```
   ```
   [*DeviceA-pim] commit
   ```
   ```
   [~DeviceA-pim] quit
   ```
5. Configure DNS-based static SSM mapping on the Router connecting to the user hosts.
   
   
   
   # On DeviceD, set the domain name suffix used by multicast groups 232.1.1.5 and 232.1.1.10 to **huawei.com**.
   
   ```
   [~DeviceD] igmp
   ```
   ```
   [*DeviceD-igmp] ssm-mapping query dns
   ```
   ```
   [*DeviceD-igmp] ssm-mapping domain huawei.com
   ```
   ```
   [*DeviceD-igmp] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] igmp static-group 232.1.1.10 source dns-ssm-map
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/4
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/4] igmp static-group 232.1.1.5 source dns-ssm-map
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/4] quit
   ```
   ```
   [*DeviceD] commit
   ```
6. Verify the configuration.
   
   
   
   # Display DNS-based SSM mapping information on DeviceD.
   
   ```
   <DeviceD> display igmp dns-ssm-mapping
   ```
   ```
   IGMP SSM-Mapping conversion table of VPN-Instance: public net
   
    00001. Group: 232.1.1.5
             Domain: 5.1.1.232.huawei.com
             Number of sources: 2
             Source address list:
               10.0.1.11
               10.0.3.13
    00002. Group: 232.1.1.10
             Domain: 10.1.1.232.huawei.com
             Number of sources: 2
             Source address list:
               10.0.1.12
               10.0.3.14
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   ssm-policy 2000
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.3.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.3.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   ssm-policy 2000
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.3.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   ssm-policy 2000
  #
  return
  ```
* Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  acl number 2000
   rule permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.11.1 255.255.255.0
   isis enable 1
   pim sm
   igmp enable
   igmp version 3
   igmp ssm-mapping enable
   igmp static-group 232.1.1.10 source dns-ssm-map
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.0.10.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ip address 10.0.12.1 255.255.255.0
   isis enable 1
   pim sm
   igmp enable
   igmp version 3
   igmp ssm-mapping enable
   igmp static-group 232.1.1.5 source dns-ssm-map
  #
  igmp
   ssm-mapping query dns
   ssm-mapping domain huawei.com
  #
  dns resolve
  dns server 10.0.10.5
  #
  pim
   ssm-policy 2000
  #
  return
  ```