Example for Configuring DHCPv6 Relay
====================================

Example for Configuring DHCPv6 Relay

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001564130489__fig758173185111), the DHCPv6 clients' network address and DHCPv6 server address are fc00:2::/64 and fc00:3::3/64, respectively. The clients want to obtain IPv6 addresses through DHCPv6. The clients and server are on different network segments; therefore, a DHCPv6 relay agent is required to forward DHCPv6 messages.

DeviceA needs to be configured as a DHCPv6 relay agent to forward DHCPv6 messages between the clients and server. In addition, DeviceA functions as the gateway of the clients. The flags in RA messages can be specified to allow the clients to obtain IPv6 addresses and other network configuration parameters through DHCPv6.

**Figure 1** Network diagram of configuring DHCPv6 relay![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001513050450.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses for interfaces to implement IPv6 communication.
2. Configure DHCPv6 relay so that DeviceA forwards DHCPv6 messages between the DHCPv6 server and clients.


#### Procedure

1. Add interfaces to VLANs.
   
   
   
   # Add 100GE 1/0/1 and 100GE 1/0/2 to VLAN 10 and VLAN 11, respectively.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 10 11
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 11
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Configure IPv6 addresses for VLANIF interfaces.
   
   
   
   # Configure an IPv6 address for VLANIF 10.
   
   ```
   [~DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ipv6 enable
   [*DeviceA-Vlanif10] ipv6 address fc00:2::1 64
   [*DeviceA-Vlanif10] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure an IPv6 address for VLANIF 11.
   
   ```
   [~DeviceA] interface vlanif 11
   [*DeviceA-Vlanif11] ipv6 enable
   [*DeviceA-Vlanif11] ipv6 address fc00:3::1 64
   [*DeviceA-Vlanif11] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure DHCPv6 relay.
   
   
   ```
   [~DeviceA] dhcp enable
   [~DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] dhcpv6 relay destination fc00:3::3
   [*DeviceA-Vlanif10] commit
   ```
4. Configure DeviceA to advertise RA messages and set their flags.
   
   
   ```
   [~DeviceA-Vlanif10] ipv6 nd ra halt disable
   [*DeviceA-Vlanif10] ipv6 nd autoconfig managed-address-flag
   [*DeviceA-Vlanif10] ipv6 nd autoconfig other-flag
   [*DeviceA-Vlanif10] commit
   [~DeviceA-Vlanif10] quit
   ```

#### Verifying the Configuration

# Run the [**display dhcpv6 relay statistics**](cmdqueryname=display+dhcpv6+relay+statistics) command to check statistics on DHCPv6 messages forwarded by the DHCPv6 relay agent.

```
[~DeviceA] display dhcpv6 relay statistics
 MessageType              Receive          Send             Error                                                                   
 Solicit                  41357            0                24                                                                       
 Advertise                0                6                0                                                                       
 Request                  0                0                0                                                                       
 Confirm                  0                0                0                                                                       
 Renew                    0                0                0                                                                       
 Rebind                   0                0                0                                                                       
 Reply                    0                0                0                                                                       
 Release                  0                0                0                                                                       
 Decline                  0                0                0                                                                       
 Reconfigure              0                0                0                                                                       
 Information-request      0                0                0                                                                       
 Relay-forward            6                41333            0                                                                       
 Relay-reply              0                0                0                                                                       
 UnknownType              0                0                0    
-------------------------------------------------------------------
```
#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 10 11
#
dhcp enable
#
interface Vlanif10
 ipv6 enable
 ipv6 address FC00:2::1/64
 ipv6 nd ra halt disable
 ipv6 nd autoconfig managed-address-flag
 ipv6 nd autoconfig other-flag
 dhcpv6 relay destination FC00:3::3
#
interface Vlanif11
 ipv6 enable
 ipv6 address FC00:3::1/64
# 
interface 100GE1/0/1
 port default vlan 10
#
interface 100GE1/0/2
 port default vlan 11
#
return
```