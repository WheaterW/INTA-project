Example for Configuring Routed Proxy ARP
========================================

Example for Configuring Routed Proxy ARP

#### Networking Requirements

Two hosts on the same network segment but on different physical networks need to communicate with each other.

As shown in [Figure 1](#EN-US_TASK_0000001176743505__fig_dc_vrp_arp_cfg_206201), two devices are connected using a serial link. No default gateways are set for HostA and HostB. To enable HostA and HostB to communicate with each other, configure routed proxy ARP on the two devices.

**Figure 1** Network diagram of configuring routed proxy ARP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001130783864.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for the interfaces to which hosts are connected, ensuring that the links between the hosts and interfaces are working properly.
2. Configure routed proxy ARP on the interfaces. After receiving an ARP request (for the destination host's MAC address) sent by the host, the device that has routed proxy ARP enabled responds to the request with its own MAC address. The host then forwards data to the device.
3. Configure a default route between two devices so that data can be transmitted along the route.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the interface that connects DeviceA to HostA: 172.16.1.1/24; IP address of the interface that connects DeviceB to HostB: 172.16.2.1/24
* Default route on each device
* IP address of HostA: 172.16.1.2/16; IP address of HostB: 172.16.2.2/16

#### Procedure

1. Configure DeviceA.
   
   
   
   # Configure an IP address for 100GE 1/0/1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 172.16.1.1 255.255.255.0
   [*DeviceA] commit
   ```
   
   # Enable routed proxy ARP.
   
   ```
   [~DeviceA-100GE1/0/1] arp proxy enable
   [~DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure a static route.
   
   ```
   [~DeviceA] ip route-static 0.0.0.0 0 100ge 1/0/2 172.17.3.2
   [*DeviceA] commit
   ```
   
   # Configure an IP address for 100GE 1/0/2.
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 172.17.3.1 255.255.255.0
   [*DeviceA-100GE1/0/2] undo shutdown
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
2. Configure DeviceB.
   
   
   
   # Configure an IP address for 100GE 1/0/1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*DeviceB] commit
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 172.16.2.1 255.255.255.0
   [*DeviceB] commit
   ```
   
   # Enable routed proxy ARP.
   
   ```
   [~DeviceB-100GE1/0/1] arp proxy enable
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure a static route.
   
   ```
   [~DeviceB] ip route-static 0.0.0.0 0 100ge 1/0/2 172.17.3.1
   [*DeviceB] commit
   ```
   
   # Configure an IP address for 100GE 1/0/2.
   
   ```
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 172.17.3.2 255.255.255.0
   [*DeviceB-100GE1/0/2] undo shutdown
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
3. Configure hosts.
   
   
   
   # Configure IP address 172.16.1.2/16 for HostA.
   
   # Configure IP address 172.16.2.2/16 for HostB.

#### Verifying the Configuration

# Ping HostB from HostA. The ping is successful.

# Check ARP entries on HostA. The command output shows that the MAC address of HostB is the MAC address of 100GE 1/0/1 on DeviceA.

```
C:\Documents and Settings\Administrator>arp -a
Interface: 172.16.1.2 --- 0x2
  Internet Address      Physical Address      Type
  172.16.2.2            00e0-fc39-80aa        dynamic
```
#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  ip route-static 0.0.0.0 0.0.0.0 100GE1/0/2 172.17.3.2
  #
  interface 100ge 1/0/1
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
   arp proxy enable
  #
  interface 100ge 1/0/2
   undo portswitch
   ip address 172.17.3.1 255.255.255.0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  ip route-static 0.0.0.0 0.0.0.0 100GE1/0/2 172.17.3.1
  #
  interface 100ge 1/0/2
   undo portswitch
   ip address 172.16.2.1 255.255.255.0
   arp proxy enable
  #
  interface 100ge 1/0/2
   undo portswitch
   ip address 172.17.3.2 255.255.255.0
  
  #
  return
  ```