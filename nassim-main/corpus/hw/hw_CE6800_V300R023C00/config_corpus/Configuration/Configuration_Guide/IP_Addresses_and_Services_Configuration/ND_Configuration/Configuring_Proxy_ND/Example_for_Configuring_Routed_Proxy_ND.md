Example for Configuring Routed Proxy ND
=======================================

Example for Configuring Routed Proxy ND

#### Networking Requirements

Hosts that belong to the same network segment but different physical networks are unable to communicate with each other if the gateways connected to them have different IPv6 addresses. In this case, you can enable routed proxy ND on a device's interface connected to the hosts to allow them to communicate.

As shown in [Figure 1](#EN-US_TASK_0000001130782302__fig7672135224615), DeviceA and DeviceB are connected to different networks, and DeviceA's interface 1 and DeviceB's interface 2 have different IPv6 addresses. Take HostA and HostB as an example. When HostA needs to communicate with HostB, it sends an NS message to request HostB's MAC address because the destination IPv6 address is on the same network segment as the local IPv6 address. However, as HostA and HostB are located on different physical networks, HostB cannot receive the NS message and therefore does not respond. To address this issue, enable routed proxy ND on interface 1 and interface 2.

**Figure 1** Network diagram of routed proxy ND![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001130622662.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses for interfaces.
2. Configure an IGP to implement IP interworking.
3. Enable routed proxy ND on interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IPv6 addresses
* Host IPv6 addresses

#### Procedure

1. Configure IPv6 addresses for interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [~DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:300:400::2 64
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:db8:300:600::1 64
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [~DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:300:600::2 64
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ipv6 enable
   [*DeviceB-100GE1/0/2] ipv6 address 2001:db8:300:500::2 64
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
2. Configure an IGP (for example, OSPFv3) to implement IP interworking.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   [*DeviceA-ospfv3-1] area 0
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] ospfv3 1 area 0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] ospfv3 1 area 0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   [*DeviceB-ospfv3-1] area 0
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] ospfv3 1 area 0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] ospfv3 1 area 0
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
3. Enable routed proxy ND on interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   0
   [~DeviceA-100GE1/0/1] ipv6 nd proxy route enable 
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] ipv6 nd proxy route enable 
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
4. Configure IPv6 addresses for hosts.
   
   
   
   # Set the IPv6 address of HostA to 2001:db8:300:400::1/48.
   
   # Set the IPv6 address of HostB to 2001:db8:300:500::1/48.

#### Verifying the Configuration

# After the configuration is complete, check that HostA and HostB can ping each other.

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
  #
  interface 100ge 1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:300:400::2/64
   ospfv3 1 area 0.0.0.0
   ipv6 nd proxy route enable
  #
  interface 100ge 1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:300:600::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #
  interface 100ge 1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:300:600::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100ge 1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:300:500::2/64
   ospfv3 1 area 0.0.0.0
   ipv6 nd proxy route enable
  #
  return
  ```