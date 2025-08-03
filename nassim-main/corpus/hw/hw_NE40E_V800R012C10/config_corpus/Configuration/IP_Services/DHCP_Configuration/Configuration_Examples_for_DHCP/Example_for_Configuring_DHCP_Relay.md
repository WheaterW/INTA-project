Example for Configuring DHCP Relay
==================================

This section provides an example for configuring a DHCP relay agent to forward DHCP messages between the DHCP clients and the DHCP server on different network segments. This configuration is available only on carrier IP devices.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172364738__fig_dc_vrp_dhcp_relay_cfg_001101), the DHCP clients reside on the network segment 10.100.0.0/16, and the DHCP server resides on the network segment 172.16.0.0/16. To allow the DHCP clients to obtain configuration information (including IP addresses) from the DHCP server, configure a DHCP relay agent to forward DHCP messages between the clients.

The network segment of the DHCP client is 10.100.0.0/16. The IP address of the DNS server is 10.100.1.2/16, the IP address of the NetBIOS server is 10.100.1.3/16, and the IP address of the gateway is 10.100.1.1. User packets carrying different Option 60 values use different gateways to apply for IP addresses and match the corresponding address pools. On the DHCP server, configure two address pools with different gateway addresses. The routing table on the server contains at least one reachable route to network segment 10.100.0.0.

**Figure 1** Configuring DHCP relay![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and interface 2 in this example represent GE0/1/0.1 and GE0/2/0.1, respectively.


  
![](images/fig_dc_vrp_dhcp_relay_cfg_001101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a DHCP relay agent.
   1. Configure an IP address for GE0/2/0.1.
   2. Configure the DHCP server address and enable DHCP relay on GE0/1/0.1.
   3. Configure GE0/1/0.1 to use different Giaddr values to apply for IP addresses for user packets with different Option 60 values (**abc** and **def**).
2. Configure the DHCP server.
   1. Configure a route from the DHCP server to GE0/1/0.1 on the DHCP relay agent.
   2. Configure an IP address for GE0/1/0.1.
   3. Configure IP addresses for the DNS server, NetBIOS server, and egress gateway.
   4. Configure two address pools with different gateway addresses on the DHCP server.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the interface to have DHCP relay enabled
* IP address of the DHCP server

#### Procedure

1. Configure a DHCP relay agent.
   
   
   
   # Configure an IP address for GE0/2/0.1.
   
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
   [~DeviceA] interface GigabitEthernet 0/2/0.1
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.1] ip address 172.16.1.1 255.255.0.0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.1] vlan-type dot1q 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.1] quit
   ```
   
   # Configure the DHCP server address and enable DHCP relay on GE0/1/0. Configure the device to use gateway 10.100.20.1 for user packets with Option 60 being **abc** and gateway 10.100.30.1 for user packets with Option 60 being **def**.
   
   ```
   [~DeviceA] dhcp enable
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0.1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] ip address 10.100.1.1 255.255.0.0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] ip address 10.100.20.1 255.255.255.0 sub
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] ip address 10.100.30.1 255.255.255.0 sub
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] ip relay address 172.16.1.2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] ip relay giaddr 10.100.20.1 dhcp-option 60 abc
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] ip relay giaddr 10.100.30.1 dhcp-option 60 def
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] vlan-type dot1q 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] dhcp select relay
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0.1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] quit
   ```
2. Configure the DHCP server.
   
   
   
   # Configure a route from the DHCP server to GE0/1/0.1 on the DHCP relay agent.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] ip route-static 10.100.1.1 16 172.16.1.1
   ```
   
   # Configure an IP address and enable the DHCP server function for GE 0/1/0.1.
   
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
   [~DeviceB] interface GigabitEthernet 0/1/0.1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0.1] ip address 172.16.1.2 255.255.0.0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0.1] vlan-type dot1q 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0.1] dhcp server enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0.1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0.1] quit
   ```
   
   # Configure two address pools with different gateway addresses on the DHCP server.
   
   ```
   [~DeviceB] ip pool pool1 server
   ```
   ```
   [*DeviceB-ip-pool-pool1] gateway 10.100.20.1 24
   ```
   ```
   [*DeviceB-ip-pool-pool1] section 0 10.100.20.2 10.100.20.255
   ```
   ```
   [*DeviceB-ip-pool-pool1] commit
   ```
   ```
   [~DeviceB-ip-pool-pool1] quit
   ```
   ```
   [*DeviceB] ip pool pool2 server
   ```
   ```
   [*DeviceB-ip-pool-pool2] gateway 10.100.30.1 24
   ```
   ```
   [*DeviceB-ip-pool-pool2] section 0 10.100.30.2 10.100.30.255
   ```
   ```
   [*DeviceB-ip-pool-pool2] commit
   ```
   ```
   [~DeviceB-ip-pool-pool2] quit
   ```
   
   # Configure the DNS and NetBIOS servers.
   
   ```
   [~DeviceB] ip pool pool1
   ```
   ```
   [~DeviceB-ip-pool-pool1] dns-server 10.100.1.2
   ```
   ```
   [*DeviceB-ip-pool-pool1] netbios-name-server 10.100.1.3
   ```
   ```
   [*DeviceB-ip-pool-pool1] commit
   ```
   ```
   [~DeviceB-ip-pool-pool1] quit
   ```
3. Verify the configuration.
   
   
   
   Run the **display dhcp relay address** command on the DHCP relay device to view configurations of the relay IP address.
   
   ```
   [~DeviceA] display dhcp relay address all
   ```
   ```
      ** GigabitEthernet0/1/0.1 DHCP Relay Address  **
   ```
   ```
             Dhcp Option          Relay Agent IP         Server IP
   ```
   ```
             *                    -                      172.16.1.2
   ```
   ```
             60(abc)              10.100.20.1            -  
   ```
   ```
             60(def)              10.100.30.1            -      
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
  dhcp enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0.1
  ```
  ```
   undo shutdown
  ```
  ```
   vlan-type dot1q 1
  ```
  ```
   ip address 10.100.1.1 255.255.0.0
  ```
  ```
   ip address 10.100.20.1 255.255.255.0 sub
  ```
  ```
   ip address 10.100.30.1 255.255.255.0 sub
  ```
  ```
   dhcp select relay
  ```
  ```
   ip relay address 172.16.1.2 
  ```
  ```
   ip relay giaddr 10.100.20.1 dhcp-option 60 abc
  ```
  ```
   ip relay giaddr 10.100.30.1 dhcp-option 60 def
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/2/0.1
  ```
  ```
   undo shutdown
  ```
  ```
   vlan-type dot1q 1
  ```
  ```
   ip address 172.16.1.1 255.255.0.0
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
  ip route-static 10.100.1.1 16 172.16.1.1
  #
  sysname DeviceB
  #
  dhcp enable
  #
  interface GigabitEthernet 0/1/0.1
   undo shutdown
   vlan-type dot1q 1
   ip address 172.16.1.2 255.255.0.0
   dhcp server enable
  #
  ip pool pool1 server
   gateway 10.100.20.1 255.255.255.0
   section 0 10.100.20.2 10.100.20.255
   dns-server 10.100.1.2 
   netbios-name-server 10.100.1.3 
  #
  ip pool pool2 server
   gateway 10.100.30.1 255.255.255.0
   section 0 10.100.30.2 10.100.30.255
  #
  return 
  ```