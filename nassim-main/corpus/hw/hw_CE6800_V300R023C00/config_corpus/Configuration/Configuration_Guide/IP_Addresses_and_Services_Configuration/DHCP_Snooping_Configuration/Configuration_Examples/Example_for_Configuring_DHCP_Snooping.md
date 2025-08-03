Example for Configuring DHCP Snooping
=====================================

Example for Configuring DHCP Snooping

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_XTASK_0000001563760673__fig435655411611), users access DeviceC through DeviceA and DeviceB. DeviceC is the user gateway that functions as the DHCP relay agent to forward DHCP messages to the DHCP server, so that DHCP clients can obtain IP addresses and related configurations from the DHCP server.

The network may encounter the following DHCP attacks:

* Bogus DHCP server attack: An attacker deploys a DHCP server on the network to allocate IP addresses and other network parameters to clients. If the DHCP server allocates incorrect IP addresses and other network parameters to clients, the network will be greatly affected.
* DHCP flood attack: If an attacker sends a large number of DHCP messages to a device in a short period, device performance is impacted, and the device may stop working.
* Bogus DHCP message attack: If an attacker pretends to be an authorized user and continuously sends DHCPREQUEST messages to the DHCP server to renew the IP address lease, the expired IP addresses cannot be reclaimed. As a result, authorized users can no longer obtain IP addresses. If an attacker pretends to be an authorized user and sends a DHCPRELEASE message to the DHCP server, the authorized user will be disconnected unexpectedly.
* DHCP server DoS attack: If a large number of attackers apply for IP addresses or an attacker continuously changes the CHADDR field to apply for IP addresses from the DHCP server, IP addresses on the DHCP server are quickly exhausted and authorized users can no longer obtain IP addresses.

To defend against DHCP attacks and provide a high-quality service for DHCP users, configure the DHCP snooping function.

**Figure 1** Network diagram of configuring DHCP snooping attack defense![](public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1, 2, and 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001512681270.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DHCP relay so that DeviceC forwards DHCP messages from different network segments to the DHCP server.
2. Configure the basic DHCP snooping functions to prevent bogus DHCP server attacks. Enable association between ARP and DHCP snooping to ensure that the binding table is updated in real time when DHCP users are disconnected unexpectedly. Configure the device to discard DHCP messages in which the GIADDR field value is not 0 to prevent attacks initiated by unauthorized users.
3. Set the maximum rate of DHCP messages sent to the DHCP message processing unit to prevent DHCP flood attacks. Enable the packet discarding alarm function so that an alarm is generated when the number of discarded DHCP messages reaches the alarm threshold.
4. Enable the device to check DHCP messages against the binding table to prevent bogus DHCP message attacks. Configure the device to generate an alarm when the number of DHCP messages discarded because they do not match the binding table reaches the threshold.
5. Configure the maximum number of access users and enable the device to check whether the CHADDR field value is the same as the source MAC address in the header of a DHCPREQUEST message to prevent DHCP server DoS attacks.

In this example, only the configuration on DeviceC is provided. The example does not include detailed configurations for the DHCP server.



#### Procedure

1. Configure DHCP relay.
   
   # Configure DHCP relay.
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname DeviceC
   [*DeviceC] commit 
   [~DeviceC] vlan batch 10 20 
   [*DeviceC] interface 100GE 1/0/1 
   [*DeviceC-100GE1/0/1] portswitch 
   [*DeviceC-100GE1/0/1] port link-type access 
   [*DeviceC-100GE1/0/1] port default vlan 10 
   [*DeviceC-100GE1/0/1] quit 
   [*DeviceC] interface 100GE 1/0/2 
   [*DeviceC-100GE1/0/2] portswitch 
   [*DeviceC-100GE1/0/2] port link-type access 
   [*DeviceC-100GE1/0/2] port default vlan 10 
   [*DeviceC-100GE1/0/2] quit 
   [*DeviceC] interface 100GE 1/0/3 
   [*DeviceC-100GE1/0/3] portswitch 
   [*DeviceC-100GE1/0/3] port link-type access 
   [*DeviceC-100GE1/0/3] port default vlan 20 
   [*DeviceC-100GE1/0/3] quit 
   [*DeviceC] dhcp enable 
   [*DeviceC] interface vlanif 10 
   [*DeviceC-Vlanif10] ip address 10.0.0.1 255.255.255.0 
   [*DeviceC-Vlanif10] dhcp select relay  
   [*DeviceC-Vlanif10] quit 
   [*DeviceC] interface vlanif 20 
   [*DeviceC-Vlanif20] ip address 10.1.1.1 255.255.255.0
   [*DeviceC-Vlanif20] dhcp select relay
   [*DeviceC-Vlanif20] quit 
   [*DeviceC] ip route-static 0.0.0.0 0.0.0.0 10.1.1.1
   [*DeviceC] commit
   ```
   
   Set the IP address of the DHCP server to 10.2.1.2/24, configure the address pool with the network segment 10.0.1.0/24, and set the gateway address of the address pool to 10.0.0.1.
2. Enable basic DHCP snooping functions.
   
   # Enable DHCP snooping globally.
   
   ```
   [~DeviceC] dhcp snooping enable
   [*DeviceC] commit
   ```
   
   # Enable DHCP snooping on the user-side interface. The following uses 100GE 1/0/1 as an example. The configuration of 100GE 1/0/2 is the same as that of 100GE 1/0/1.
   
   ```
   [~DeviceC] interface 100GE 1/0/1
   [*DeviceC-100GE1/0/1] dhcp snooping enable 
   ```
   
   # Enable association between ARP and DHCP snooping.
   
   ```
   [*DeviceC-100GE1/0/1] [dhcp snooping user-bind arp-detect enable](cmdqueryname=dhcp+snooping+user-bind+arp-detect+enable) 
   ```
   
   # Enable the device to check whether the GIADDR field value in a DHCPREQUEST message is not 0.
   
   ```
   [*DeviceC-100GE1/0/1] dhcp snooping check dhcp-giaddr enable 
   ```
3. Enable the device to check DHCP messages against the binding table.
   
   # Configure the user-side interface.
   
   ```
   [*DeviceC-100GE1/0/1] dhcp snooping check dhcp-request enable 
   ```
4. Configure the maximum number of access users allowed on the interface and enable the device to check the CHADDR field.
   
   # Configure the user-side interface.
   
   ```
   [*DeviceC-100GE1/0/1] dhcp snooping user-bind max-number 20 
   [*DeviceC-100GE1/0/1] dhcp snooping check dhcp-chaddr enable 
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
5. Verify the configuration.# Check the DHCP snooping configuration.
   ```
   [~DeviceC] display dhcp snooping configuration 
   # 
   dhcp snooping enable 
   # 
   interface 100GE1/0/1  
    dhcp snooping enable  
    dhcp snooping check dhcp-giaddr enable  
    dhcp snooping check dhcp-request enable  
    dhcp snooping check dhcp-chaddr enable
    dhcp snooping user-bind max-number 20
   # 
   interface 100GE1/0/2  
    dhcp snooping enable  
    dhcp snooping check dhcp-giaddr enable  
    dhcp snooping check dhcp-request enable  
    dhcp snooping check dhcp-chaddr enable
    dhcp snooping user-bind max-number 20
   #
   ```
   
   # Check DHCP snooping running information on an interface. The command output shows that the values of **Check dhcp-giaddr**, **Check dhcp-chaddr**, and **Check dhcp-request** fields are all **Enable**. The following uses the command output on 100GE 1/0/1 as an example:
   
   ```
   [~DeviceC] display dhcp snooping interface 100GE 1/0/1 
   DHCP snooping running information for interface 100GE1/0/1 :  
   DHCP snooping                            : Enable  
   Trusted interface                        : No  
   Dhcp user max number                     : 20  
   Current dhcp and nd user number          : 0  
   Check dhcp-giaddr                        : Enable  
   Check dhcp-chaddr                        : Enable  
   Check dhcp-request                       : Enable  
   ```


#### Configuration Scripts

DeviceC
```
# 
sysname DeviceC 
# 
vlan batch 10 20 
# 
dhcp enable 
# 
dhcp snooping enable
#
interface Vlanif 10  
 ip address 10.0.0.1 255.255.255.0   
 dhcp select relay  
# 
interface Vlanif 20 
 ip address 10.1.1.1 255.255.255.0 
# 
interface 100GE 1/0/1   
 portswitch 
 port default vlan 10  
 dhcp snooping enable  
 dhcp snooping check dhcp-giaddr enable
 dhcp snooping check dhcp-request enable
 dhcp snooping check dhcp-chaddr enable
 dhcp snooping user-bind max-number 20 
# 
interface 100GE 1/0/2    
 portswitch 
 port default vlan 10  
 dhcp snooping enable  
 dhcp snooping check dhcp-giaddr enable
 dhcp snooping check dhcp-request enable
 dhcp snooping check dhcp-chaddr enable
 dhcp snooping user-bind max-number 20

# 
interface 100GE 1/0/3   
 portswitch 
 port default vlan 20
# 
ip route-static 0.0.0.0 0.0.0.0 10.1.1.1 
# 
return
```