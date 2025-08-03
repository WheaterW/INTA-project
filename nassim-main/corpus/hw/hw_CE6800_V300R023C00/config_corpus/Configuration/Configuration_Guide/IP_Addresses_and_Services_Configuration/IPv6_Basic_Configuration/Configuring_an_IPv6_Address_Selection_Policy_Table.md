Configuring an IPv6 Address Selection Policy Table
==================================================

Configuring an IPv6 Address Selection Policy Table

#### Context

IPv6 addresses can be classified into the following types based on applications:

* Link-local addresses and global unicast addresses based on the effective range of the IPv6 addresses
* Temporary addresses and public addresses based on security levels
* Home addresses and care-of addresses based on the application in the mobile IPv6 field
* Physical and logical interface addresses based on interface attributes

The preceding IPv6 addresses can be configured on the same interface of the device. In this case, the system must select a source address or a destination address from multiple addresses on the interface. If the system supports IPv4/IPv6 dual-stack, it must also select IPv4 or IPv6 addresses for communication. For example, if a domain name maps both an IPv4 address and an IPv6 address, the system must select an address to respond to the DNS request of the client.

An IPv6 address selection policy table solves the preceding problems by defining a group of address selection rules to specify or plan the source and destination addresses of packets. This table, similar to a routing table, can be queried by using the longest matching rule, where an address is selected based on the source and destination addresses.

* The *label* parameter can be used to determine the result of source address selection. The address with the same *label* value as that of the destination address is preferably selected as the source address.
* The destination address is selected based on both the *label* and *precedence* parameters. If *label* values of the candidate addresses are the same, the address with the largest *precedence* value is preferably selected as the destination address.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure source/destination address selection policies.
   
   
   ```
   [ipv6 address-policy](cmdqueryname=ipv6+address-policy+vpn-instance) [ vpn-instance vpn-instance-name ] ipv6-address prefix-length precedence label
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Example

As shown in [Figure 1](#EN-US_TASK_0000001176661709__fig_dc_vrp_ipv6_cfg_200201), the domain name (huawei.com) of ServerA maps multiple IPv6 addresses. When DeviceA, as an IPv6 DNS client, accesses ServerA by using the domain name (huawei.com), the DNS server sends all IPv6 addresses of ServerA to DeviceA. Then, DeviceA queries the IPv6 address selection policy table to select a proper IPv6 address as the destination address of ServerA.

**Figure 1** Network diagram of configuring an IPv6 address selection policy table![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001176741625.png)

Perform the following configurations on DeviceA:

# Configure IPv6 addresses for the interface.

```
<HUAWEI> system-view
[~HUAWEI] sysname DeviceA
[*HUAWEI] commit
[~DeviceA] interface 100ge 1/0/1
[~DeviceA-100GE1/0/1] undo portswitch
[*DeviceA-100GE1/0/1] ipv6 enable
[*DeviceA-100GE1/0/1] ipv6 address fe80::1 link-local
[*DeviceA-100GE1/0/1] ipv6 address 2001:db8:fed0:1::2 64
[*DeviceA-100GE1/0/1] ipv6 address 2001:db8:2::2 64
[*DeviceA-100GE1/0/1] ipv6 address 2001:db8:abcd::77 64
[*DeviceA-100GE1/0/1] quit
```

# Configure destination address selection policies.

```
[*DeviceA] ipv6 address-policy 2001:db8:fed0:1::2 128 100 100
[*DeviceA] ipv6 address-policy 2001:db8:1::1 128 100 100
```

# Configure dynamic IPv6 DNS services.

```
[*DeviceA] dns resolve
[*DeviceA] dns server ipv6 2001:db8:abcd::1234
[*DeviceA] dns domain com
[*DeviceA] commit
```
#### Verifying the Configuration

After configuring an IPv6 address selection policy table, verify the configuration.

Run the [**display ipv6 address-policy**](cmdqueryname=display+ipv6+address-policy+vpn-instance+all) [ **vpn-instance** *vpn-instance-name* ] { **all** | *ipv6-address* *prefix-length* } command to check the IPv6 address selection policy table.

```
<DeviceA> display ipv6 address-policy all
Policy Table :
             Total: 5                                                           
------------------------------------------------------------------------------- 
 Prefix     : ::                                      PrefixLength  : 0         
 Precedence : 40                                      Label         : 1         
 Default    : Yes                                                               

 Prefix     : ::1                                     PrefixLength  : 128       
 Precedence : 50                                      Label         : 0         
 Default    : Yes                                                               

 Prefix     : ::FFFF:0.0.0.0                          PrefixLength  : 96        
 Precedence : 10                                      Label         : 4         
 Default    : Yes                                                               

 Prefix     : 2002::                                  PrefixLength  : 16        
 Precedence : 30                                      Label         : 2         
 Default    : Yes                                                               

 Prefix     : FC00::                                  PrefixLength  : 7         
 Precedence : 20                                      Label         : 3         
 Default    : Yes                                                               

------------------------------------------------------------------------------- 
```