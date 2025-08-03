Example for Preventing Routing Loops
====================================

This section describes how to configure split horizon to prevent routing loops.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365883__fig_dc_vrp_rip_cfg_004901), IP addresses have been configured for interfaces on all Routers, RIP-2 has been configured on each Router, and RIP services are running properly. Classful summarization is enabled on RouterA and RouterC. It is required that split horizon be configured on RouterA and RouterC.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When configuring classful summarization on a RIP-2 network, you need to disable split horizon and poison reverse. After classful summarization is disabled, you need to reconfigure split horizon or poison reverse to prevent routing loops. This section uses split horizon as an example.


**Figure 1** Network diagram of configuring routing loop prevention![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, interface3, and interface4 in this example represent GE0/1/0, GE0/1/1, GE0/1/2, and GE0/1/3, respectively.


  
![](figure/en-us_image_0256711100.png)

#### Precautions

During the configuration, note the following:

If both split horizon and poison reverse are configured, only poison reverse takes effect.

To improve security, you are advised to configure RIP-2 packet authentication. For details, see "Improving RIP Network Security." The following example describes how to configure an authentication mode for RIP-2 packets. For details, see "Example for Configuring Basic RIP Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Disable route summarization.
2. Enable split horizon.

#### Data Preparation

To complete the configuration, you need the following data:

* RIP-enabled network segments 10.1.0.0, 10.2.0.0, 10.3.0.0, and 192.168.0.0 on DeviceA
* RIP-enabled network segment 192.168.0.0 on DeviceB
* RIP-enabled network segments 172.16.0.0, 172.17.0.0, 172.18.0.0, and 192.168.0.0 on DeviceC
* IP addresses of interfaces


#### Procedure

1. Disable route summarization.
   
   
   
   # Disable route summarization on DeviceA.
   
   ```
   [~DeviceA] rip 1
   ```
   ```
   [*DeviceA-rip-1] undo summary
   ```
   ```
   [*DeviceA-rip-1] commit
   ```
   ```
   [~DeviceA-rip-1] quit
   ```
   
   # Disable route summarization on DeviceB.
   
   ```
   [~DeviceB] rip 1
   ```
   ```
   [*DeviceB-rip-1] undo summary
   ```
   ```
   [*DeviceB-rip-1] commit
   ```
   ```
   [~DeviceB-rip-1] quit
   ```
2. Configure split horizon.
   
   
   
   Configure split horizon on the RIP interfaces of all Routers. The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For details, see configuration files.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] rip split-horizon
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] rip split-horizon
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] rip split-horizon
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] rip split-horizon
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceA] commit
   ```
3. Verify the configuration.
   
   
   
   # Run the [**display rip 1 interface verbose**](cmdqueryname=display+rip+1+interface+verbose) command on DeviceA and DeviceC to check the result after split horizon is configured. Use the command output on DeviceA as an example. If the value of the Split-Horizon field is Enabled, split horizon has been enabled.
   
   ```
   [~DeviceA] display rip 1 interface verbose
   ```
   ```
    GigabitEthernet0/1/0(192.168.1.1)
     State    : DOWN            MTU: 500
     Metricin : 0
     Metricout: 1
     Input    : Enabled         Output       : Enabled
     Protocol : RIPv2 Multicast
     Send     : RIPv2 Multicast Packets
     Receive  : RIPv2 Multicast and Broadcast Packets
     Poison-reverse                : Disabled
     Split-Horizon                 : Enabled
     Authentication type           : None
     Replay Protection             : Disabled
     Max Packet Length             : 512
    GigabitEthernet0/1/1(10.1.1.1)
     State    : DOWN            MTU: 500
     Metricin : 0
     Metricout: 1
     Input    : Enabled         Output       : Enabled
     Protocol : RIPv2 Multicast
     Send     : RIPv2 Multicast Packets
     Receive  : RIPv2 Multicast and Broadcast Packets
     Poison-reverse                : Disabled
     Split-Horizon                 : Enabled
     Authentication type           : None
     Replay Protection             : Disabled
     Max Packet Length             : 512
    GigabitEthernet0/1/2(10.2.1.1)
     State    : DOWN            MTU: 500
     Metricin : 0
     Metricout: 1
     Input    : Enabled         Output       : Enabled
     Protocol : RIPv2 Multicast
     Send     : RIPv2 Multicast Packets
     Receive  : RIPv2 Multicast and Broadcast Packets
     Poison-reverse                : Disabled
     Split-Horizon                 : Enabled
     Authentication type           : None
     Replay Protection             : Disabled
     Max Packet Length             : 512
    GigabitEthernet0/1/3(10.3.1.1)
     State    : DOWN            MTU: 500
     Metricin : 0
     Metricout: 1
     Input    : Enabled         Output       : Enabled
     Protocol : RIPv2 Multicast
     Send     : RIPv2 Multicast Packets
     Receive  : RIPv2 Multicast and Broadcast Packets
     Poison-reverse                : Disabled
     Split-Horizon                 : Enabled
     Authentication type           : None
     Replay Protection             : Disabled
     Max Packet Length             : 512
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
   rip version 2 multicast
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.0.0
  ```
  ```
   rip version 2 multicast
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.1 255.255.0.0
  ```
  ```
   rip version 2 multicast
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/3
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.1 255.255.0.0
  ```
  ```
   rip version 2 multicast
  ```
  ```
  #
  ```
  ```
  rip 1
  ```
  ```
   network 10.1.0.0
  ```
  ```
   network 10.2.0.0
  ```
  ```
   network 10.3.0.0
  ```
  ```
   network 192.168.0.0
  ```
  ```
   undo summary
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
   rip version 2 multicast
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
   rip version 2 multicast
  ```
  ```
  #
  ```
  ```
  rip 1
  ```
  ```
   network 192.168.0.0
  ```
  ```
   undo summary
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.2 255.255.255.0
  ```
  ```
   rip version 2 multicast
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.1 255.255.0.0
  ```
  ```
   rip version 2 multicast
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.17.1.1 255.255.0.0
  ```
  ```
   rip version 2 multicast
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/3
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.18.1.1 255.255.0.0
  ```
  ```
   rip version 2 multicast
  ```
  ```
  #
  ```
  ```
  rip 1
  ```
  ```
   network 172.16.0.0
  ```
  ```
   network 172.17.0.0
  ```
  ```
   network 172.18.0.0
  ```
  ```
   network 192.168.0.0
  ```
  ```
  return
  ```