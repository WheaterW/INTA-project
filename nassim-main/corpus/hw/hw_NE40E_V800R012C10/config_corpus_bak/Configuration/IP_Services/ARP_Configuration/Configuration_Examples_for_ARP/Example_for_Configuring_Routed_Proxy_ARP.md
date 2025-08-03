Example for Configuring Routed Proxy ARP
========================================

This example provides an example for configuring routed proxy ARP.

#### Networking Requirements

Two hosts on the same network segment but on different physical networks need to communicate with each other.

As shown in [Figure 1](#EN-US_TASK_0172364517__fig_dc_vrp_arp_cfg_206201), two routers are connected by serial links. No default gateways are set for Host A and Host B that reside on different physical networks. To enable Host A and Host B to communicate with each other, configure routed proxy ARP on Routers.

**Figure 1** Configuring routed proxy ARP![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_arp_cfg_206201.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| Device A | GE 0/1/0 | 172.16.1.1/24 |
| GE 0/2/0 | 172.17.3.1/24 |
| Device B | GE 0/1/0 | 172.16.2.1/24 |
| GE 0/2/0 | 172.17.3.2/24 |



#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for the interface that connects each Router to a host, ensuring that the link between each host and each Router is working properly.
2. Configure routed proxy ARP on the interface that connects each Router to a host. After receiving an ARP request (for the destination host's MAC address) sent by the host, the Router that has routed proxy ARP enabled responds to the request with its own MAC address. The host then forwards data to the Router.
3. Configure a default route between two Routers so that data can be transmitted along the route.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the interface that connects Device A to Host A: 172.16.1.1/24; IP address of the interface that connects Device B to Host B: 172.16.2.1/24
* Default route on each Router
* IP address of Host A: 172.16.1.2/16; IP address of Host B: 172.16.2.2/16

#### Procedure

1. Configure the Router Device A.
   
   
   
   # Configure an IP address for GE 0/1/0.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device A
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device A] interface gigabitethernet 0/1/0
   ```
   ```
   [~Device A-GigabitEthernet0/1/0] ip address 172.16.1.1 255.255.255.0
   ```
   
   # Enable routed proxy ARP.
   
   ```
   [*Device A-GigabitEthernet0/1/0] arp-proxy enable
   ```
   ```
   [*Device A-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*Device A-GigabitEthernet0/1/0] quit
   ```
   
   # Configure a static route.
   
   ```
   [*Device A] ip route-static 0.0.0.0 0 gigabitethernet 0/2/0 172.17.3.2
   ```
   
   # Configure an IP address for GE 0/2/0.
   
   ```
   [*Device A] interface gigabitethernet 0/2/0
   ```
   ```
   [*Device A-GigabitEthernet0/2/0] ip address 172.17.3.1 255.255.255.0
   ```
   ```
   [*Device A-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*Device A-GigabitEthernet0/2/0] quit
   ```
   ```
   [*Device A] commit
   ```
2. Configure the Router Device B.
   
   
   
   # Configure an IP address for GE 0/1/0.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device B] interface gigabitethernet 0/1/0
   ```
   ```
   [~Device B-GigabitEthernet0/1/0] ip address 172.16.2.1 255.255.255.0
   ```
   
   # Enable routed proxy ARP.
   
   ```
   [*Device B-GigabitEthernet0/1/0] arp-proxy enable
   ```
   ```
   [*Device B-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*Device B-GigabitEthernet0/1/0] quit
   ```
   
   # Configure a static route.
   
   ```
   [*Device B] ip route-static 0.0.0.0 0 gigabitethernet 0/2/0 172.17.3.1
   ```
   
   # Configure an IP address for GE 0/2/0.
   
   ```
   [*Device B] interface gigabitethernet 0/2/0
   ```
   ```
   [*Device B-GigabitEthernet0/2/0] ip address 172.17.3.2 255.255.255.0
   ```
   ```
   [*Device B-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*Device B-GigabitEthernet0/2/0] quit
   ```
   ```
   [*Device B] commit
   ```
3. Configure hosts.
   
   
   
   # Set the IP address of Host A to 172.16.1.2/16.
   
   # Set the IP address of Host B to 172.16.2.2/16.
4. Verify the configuration.
   
   
   
   # Ping Host B from Host A, and the ping is successful.
   
   # Check ARP entries on Host A. The command output shows that the MAC address of Host B is the MAC address of GE 0/1/0 on Device A.
   
   ```
   C:\Documents and Settings\Administrator>arp -a
   ```
   ```
   Interface: 172.16.1.2 --- 0x2
   ```
   ```
     Internet Address      Physical Address      Type
   ```
   ```
     172.16.2.2            00e0-fc39-80aa        dynamic
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  ```
  ```
  sysname Device A
  ```
  ```
  #
  ```
  ```
  ip route-static 0.0.0.0 0.0.0.0 GigabitEthernet0/2/0 172.17.3.2
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
   ip address 172.16.1.1 255.255.255.0
  ```
  ```
   arp-proxy enable
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
   ip address 172.17.3.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device B configuration file
  
  ```
  #
  ```
  ```
  sysname Device B
  ```
  ```
  #
  ```
  ```
  ip route-static 0.0.0.0 0.0.0.0 GigabitEthernet0/2/0 172.17.3.1
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
   ip address 172.16.2.1 255.255.255.0
  ```
  ```
   arp-proxy enable
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
   ip address 172.17.3.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```