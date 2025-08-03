Example for Configuring a DHCP Server for Clients on the Same Network Segment
=============================================================================

This section provides an example for configuring a DHCP server for clients on the same network segment.

#### Networking Requirements

In a rather large network, if the PCs are connected to the routing device through other devices instead of being directly connected to the routing device through Ethernet interfaces, a network-side DHCP server needs to be configured so that the PCs can dynamically obtain IP addresses from the routing device.

On the network shown in [Figure 1](#EN-US_TASK_0172364741__fig_dc_vrp_dhcp_server_cfg_001901), the DHCP server assigns IP addresses to clients on the same network segment. The address pool resides in network segment 10.1.1.0/24 which is divided into two subnets: 10.1.1.0/25 and 10.1.1.128/25. The DHCP server has two GE interfaces whose IP addresses are 10.1.1.1/25 and 10.1.1.129/25, respectively.

The lease of the IP addresses on the network segment 10.1.1.0/25 is 10 days and 12 hours, and the domain name is **huawei.com**. The DNS server address is 10.1.1.2. There is no NetBIOS address. The gateway address is 10.1.1.1.

The lease of the IP addresses on the network segment 10.1.1.128/25 is 5 days, and the DNS suffix is **huawei.com**. The DNS server address is 10.1.1.2. The NetBIOS address is 10.1.1.4. The gateway address is 10.1.1.129.

**Figure 1** Networking diagram for configuring a DHCP server![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](images/fig_dc_vrp_dhcp_server_cfg_001901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses.
2. Configure an address pool.
   * Configure a gateway address, an address segment, and the IP addresses that do not take part in automatic assignment (including the DNS server address, NetBIOS server address, and gateway address).
   * Configure the NetBIOS server address, DNS server address, and DNS domain name suffix.
   * Configure an address lease.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IP addresses
* Gateway address
* Address segment number and range
* IP addresses prohibited from being assigned
* DNS domain name suffix and DNS server address
* Address lease

#### Procedure

1. Configure IP addresses for the interfaces on the DHCP server and enable the DHCP server function on them.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface gigabitethernet 0/1/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] ip address 10.1.1.1 255.255.255.128
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] dhcp server enable
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] quit
   ```
   ```
   [*HUAWEI] interface gigabitethernet 0/1/1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] ip address 10.1.1.129 255.255.255.128
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] dhcp server enable
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1] quit
   ```
   ```
   [*HUAWEI] commit
   ```
2. Configure address pool 1 on the DHCP server.
   
   
   
   # Configure a gateway address, an address segment, and the IP address that do not take part in automatic assignment.
   
   ```
   [~HUAWEI] dhcp enable
   ```
   ```
   [*HUAWEI] ip pool pool1 server
   ```
   ```
   [*HUAWEI-ip-pool-pool1] gateway 10.1.1.1 255.255.255.128
   ```
   ```
   [*HUAWEI-ip-pool-pool1] section 0 10.1.1.2 10.1.1.126
   ```
   ```
   [*HUAWEI-ip-pool-pool1] excluded-ip-address 10.1.1.2
   ```
   ```
   [*HUAWEI-ip-pool-pool1] excluded-ip-address 10.1.1.4
   ```
   
   # Configure the DNS server address and DNS domain name suffix.
   
   ```
   [*HUAWEI-ip-pool-pool1] dns-server 10.1.1.2
   ```
   ```
   [*HUAWEI-ip-pool-pool1] dns-suffix huawei.com
   ```
   
   # Configure an address lease.
   
   ```
   [*HUAWEI-ip-pool-pool1] lease 10 12
   ```
   ```
   [*HUAWEI-ip-pool-pool1] quit
   ```
   ```
   [*HUAWEI] commit
   ```
3. Configure address pool 2 on the DHCP server.
   
   
   
   # Configure a gateway address and an address segment.
   
   ```
   [~HUAWEI] ip pool pool2 server
   ```
   ```
   [*HUAWEI-ip-pool-pool2] gateway 10.1.1.129 255.255.255.128
   ```
   ```
   [*HUAWEI-ip-pool-pool2] section 0 10.1.1.130 10.1.1.254
   ```
   
   # Configure the NetBIOS server address, DNS server address, and DNS domain name suffix.
   
   ```
   [*HUAWEI-ip-pool-pool2] netbios-name-server 10.1.1.4
   ```
   ```
   [*HUAWEI-ip-pool-pool2] dns-server 10.1.1.2
   ```
   ```
   [*HUAWEI-ip-pool-pool2] dns-suffix huawei.com
   ```
   
   # Configure an address lease.
   
   ```
   [*HUAWEI-ip-pool-pool2] lease 5
   ```
   ```
   [*HUAWEI-ip-pool-pool2] quit
   ```
   ```
   [*HUAWEI] commit
   ```
4. Verify the configuration.
   
   
   
   # Run the [**display ip pool**](cmdqueryname=display+ip+pool) command on the DHCP server to check the IP address pool configuration.
   
   ```
   [~HUAWEI] display ip pool name pool1
   ```
   ```
   Pool-Name      : pool1
     Pool-No        : 1
     Pool-constant-index: -
     Lease          : 10 Days 12 Hours 0 Minutes
     NetBios Type   : N-Node
     Auto recycle   : 30
     Option 3       : Enable
     DNS-Suffix     : huawei.com
     Dom-Search-List0: -
     Dom-Search-List1: - 
     Dom-Search-List2: -
     Dom-Search-List3: -
     Option-Code 125 : enterprise-code : 2011, string: -
     DNS1         :10.1.1.2
     Position       : Server          Status           : Unlocked        
     RUI-Flag       : -
     Attribute      : Private         
     Gateway        : 10.1.1.1        Mask             : 255.255.255.128   
     Vpn instance   : --              Unnumbered gateway: -               
     Profile-Name   : -               Server-Name     : -               
     Total Idle     : 123             Have Dhcp IP     : 1
     Timeouts       : 0
     Timeout Count  : 0               Sub Option Count : 0               
     Option Count   : 0               Force-reply Count: 0               
     Codes: CFLCT(conflicted)
     ---------------------------------------------------------------------------------------
     ID           start             end total  used  idle CFLCT disable reserved static-bind
     ---------------------------------------------------------------------------------------
      0        10.1.1.2      10.1.1.126   125     0   123     0       2        0           0
     ---------------------------------------------------------------------------------------
   ```
   ```
   [~HUAWEI] display ip pool name pool2
   ```
   ```
   Pool-Name      : pool2
     Pool-No        : 2
     Pool-constant-index: -
     Lease          : 5 Days 0 Hours 0 Minutes
     NetBios Type   : N-Node
     Auto recycle   : 30
     Option 3       : Enable
     DNS-Suffix     : huawei.com
     Dom-Search-List0: -
     Dom-Search-List1: - 
     Dom-Search-List2: -
     Dom-Search-List3: -
     Option-Code 125 : enterprise-code : 2011, string: -
     DNS1         :10.1.1.2
     Position       : Server          Status           : Unlocked        
     RUI-Flag       : -
     Attribute      : Private         
     Gateway        : 10.1.1.129      Mask             : 255.255.255.128   
     Vpn instance   : --              Unnumbered gateway: -               
     Profile-Name   : -               Server-Name     : -               
     Total Idle     : 125             Have Dhcp IP     : 1
     Timeouts       : 0
     Timeout Count  : 0               Sub Option Count : 0               
     Option Count   : 0               Force-reply Count: 0               
     Codes: CFLCT(conflicted)
     ---------------------------------------------------------------------------------------
     ID           start             end total  used  idle CFLCT disable reserved static-bind
     ---------------------------------------------------------------------------------------
      0      10.1.1.130      10.1.1.254   125     0   125     0       0        0           0
     ---------------------------------------------------------------------------------------
   ```

#### Configuration Files

* DHCP server configuration file
  
  ```
  #
  dhcp enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.128
   dhcp server enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.129 255.255.255.128
   dhcp server enable
  #
  ip pool pool1 server
   gateway 10.1.1.1 255.255.255.128
   section 0 10.1.1.2 10.1.1.126
   excluded-ip-address 10.1.1.2
   excluded-ip-address 10.1.1.4
   dns-server 10.1.1.2
   dns-suffix huawei.com
   lease 10 12
  #
  ip pool pool2 server
   gateway 10.1.1.129 255.255.255.128
   section 0 10.1.1.130 10.1.1.254
   dns-server 10.1.1.2
   dns-suffix huawei.com
   netbios-name-server 10.1.1.4
   lease 5
  #
  return
  ```