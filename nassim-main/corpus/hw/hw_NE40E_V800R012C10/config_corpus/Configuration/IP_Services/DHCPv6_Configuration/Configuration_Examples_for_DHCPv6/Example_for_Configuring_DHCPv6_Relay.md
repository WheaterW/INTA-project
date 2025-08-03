Example for Configuring DHCPv6 Relay
====================================

This section provides an example for configuring DHCPv6 relay. This configuration example applies to IP devices.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001186994768__fig_dc_vrp_dhcpv6_relay_cfg_001101), DHCPv6 clients reside on the network segment 2001:db8:1::/64, and the DHCPv6 server resides on the network segment 2001:db8:2::/64. To allow the DHCPv6 clients to obtain IPv6 addresses and other configuration parameters from the DHCPv6 server, configure DHCPv6 relay on the device in between to relay DHCPv6 messages.

**Figure 1** Configuring DHCPv6 relay![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001187313242.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses for the relay agent's interfaces that connect to the server and clients.
2. Enable DHCPv6 on the relay agent.
3. Configure DHCPv6 relay forwarding on the relay agent's interface that connects to the clients.

#### Data Preparation

To complete the configuration, you need the following data:

* Number of the interface to have DHCPv6 relay enabled and IPv6 address of the interface
* IPv6 address of the DHCPv6 server

#### Procedure

1. Configure DHCPv6 relay.
   
   
   
   # Configure IPv6 addresses for interfaces.
   
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
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2/64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ipv6 address 2001:db8:2::1/64
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   # Enable DHCPv6.
   
   ```
   [~DeviceA] dhcpv6 enable
   ```
   
   # Configure DHCPv6 relay forwarding on GE 0/1/0.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] dhcpv6 relay destination 2001:db8:2::2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
2. Configure the DHCPv6 server.
   
   The configuration details are not provided. The DHCPv6 server must meet the following conditions:
   * An address pool is configured on the DHCPv6 server so that the DHCPv6 server can assign IPv6 addresses to DHCPv6 clients.
   * The address pool lease is configured to improve IP address utilization.
3. Verify the configuration.
   
   
   
   Run the [**display dhcpv6 relay statistics**](cmdqueryname=display+dhcpv6+relay+statistics) command on the DHCPv6 relay agent. The command output shows statistics about various DHCPv6 messages.
   
   ```
   [~DeviceA] display dhcpv6 relay statistics
   ```
   ```
     -------------------------------------------------------------------
     Bad Packets received                                :   0
     DHCPv6 packets received from clients                :   41357
            DHCPv6 SOLICIT packets received              :   41357
            DHCPv6 REQUEST packets received              :   0
            DHCPv6 CONFIRM packets received              :   0
            DHCPv6 RENEW packets received                :   0
            DHCPv6 REBIND packets received               :   0
            DHCPv6 DECLINE packets received              :   0
            DHCPv6 RELEASE packets received              :   0
            DHCPv6 INFORMATION-REQUEST packets received  :   0
            DHCPv6 UNKNOWN packets received              :   0
     DHCPv6 packets received from relay agents or servers:   6
            DHCPv6 RELAY-FORWARD packets received        :   6
            DHCPv6 RELAY-REPLY packets received          :   0
   
     DHCPv6 packets sent to clients                      :   0
            DHCPv6 ADVERTISE packets sent                :   0
            DHCPv6 REPLY packets sent                    :   0
            DHCPv6 RECONFIGURE packets sent              :   0
            DHCPv6 UNKNOWN packets sent                  :   0
     DHCPv6 packets sent to relay agents or servers      :   41333
            DHCPv6 RELAY-FORWARD packets sent            :   41333
            DHCPv6 RELAY-REPLY packets sent              :   0
   
     DHCPv6 packets dropped                              :   33
            Table Full                                   :   0
            General Error                                :   33
            IPSec Authentication Failed                  :   0
     -------------------------------------------------------------------
   
   ```

#### Configuration Files

* DHCPv6 relay agent configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
   dhcpv6 enable
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1::2/64
  ```
  ```
   dhcpv6 relay destination 2001:db8:2::2
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:2::1/64
  ```
  ```
   #
  ```
  ```
  return 
  ```