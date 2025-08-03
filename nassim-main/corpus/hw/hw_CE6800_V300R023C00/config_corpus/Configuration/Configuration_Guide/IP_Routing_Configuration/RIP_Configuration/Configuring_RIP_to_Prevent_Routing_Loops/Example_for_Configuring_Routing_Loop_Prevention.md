Example for Configuring Routing Loop Prevention
===============================================

Example for Configuring Routing Loop Prevention

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130623174__fig_dc_vrp_rip_cfg_004901), IP addresses have been configured for interfaces on all devices, RIP-2 has been configured on each device, and RIP services are running properly. Classful summarization has been enabled on DeviceA and DeviceC. Split horizon must also be configured on DeviceA and DeviceC.

![](public_sys-resources/note_3.0-en-us.png) 

If classful summarization is configured on a RIP-2 network, you must disable split horizon and poison reverse. After classful summarization is canceled, you must configure split horizon or poison reverse to prevent routing loops. This example uses split horizon.


**Figure 1** Network diagram of configuring routing loop prevention![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001130782990.png)

#### Precautions

When configuring routing loop prevention, consider the following factors:

If both split horizon and poison reverse are configured, only poison reverse takes effect.

To improve security, you are advised to configure RIP-2 packet authentication. For details, see "Improving RIP Network Security." The following example describes how to configure an authentication mode for RIP-2 packets. For details, see "Example for Configuring Basic RIP Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Disable route summarization.
2. Enable split horizon.

#### Procedure

1. Assign an IP address to each interface. For configuration details, see Configuration Script in this section.
2. Disable route summarization.
   
   
   
   # Disable route summarization on DeviceA.
   
   ```
   [~DeviceA] rip 1
   [*DeviceA-rip-1] undo summary
   [*DeviceA-rip-1] quit
   [*DeviceA] commit
   ```
   
   # Disable route summarization on DeviceB.
   
   ```
   [~DeviceB] rip 1
   [*DeviceB-rip-1] undo summary
   [*DeviceB-rip-1] quit
   [*DeviceB] commit
   ```
3. Configure split horizon.
   
   
   
   Configure split horizon on the RIP interfaces of all routing devices.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge1/0/1
   [~DeviceA-100GE1/0/1] rip split-horizon
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge1/0/2
   [*DeviceA-100GE1/0/2] rip split-horizon
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge1/0/3
   [*DeviceA-100GE1/0/3] rip split-horizon
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge1/0/4
   [*DeviceA-100GE1/0/4] rip split-horizon
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.

#### Verifying the Configuration

# Run the [**display rip 1 interface verbose**](cmdqueryname=display+rip+1+interface+verbose) command on DeviceA and DeviceC to check whether split horizon is enabled. The following example uses the command output on DeviceA. If **Split-Horizon** is displayed as **Enabled**, split horizon has been enabled.

```
[~DeviceA] display rip 1 interface verbose
 100GE1/0/1(192.168.1.1)
 
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
 100GE1/0/2(10.1.1.1)
 
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
 100GE1/0/3(10.2.1.1)
 
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
 100GE1/0/4(10.3.1.1)
 
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
   rip version 2 multicast
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.1 255.255.0.0
   rip version 2 multicast
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.2.1.1 255.255.0.0
   rip version 2 multicast
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.3.1.1 255.255.0.0
   rip version 2 multicast
  #
  rip 1
   undo summary
   network 10.1.0.0
   network 10.2.0.0
   network 10.3.0.0
   network 192.168.0.0
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
   rip version 2 multicast
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   rip version 2 multicast
  #
  rip 1
   undo summary
   network 192.168.0.0
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   rip version 2 multicast
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.1 255.255.0.0
   rip version 2 multicast
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 172.17.1.1 255.255.0.0
   rip version 2 multicast
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 172.18.1.1 255.255.0.0
   rip version 2 multicast
  #
  rip 1
   network 172.16.0.0
   network 172.17.0.0
   network 172.18.0.0
   network 192.168.0.0
  #
  return
  ```