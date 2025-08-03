Configuring a Bridge Domain-based MAC Address Table
===================================================

A MAC address table contains static, blackhole, and dynamic MAC address entries. A MAC address table can be correctly configured to help a device to forward traffic.

#### Usage Scenario

Each device maintains a MAC address table, also called a MAC table, which is used to forward traffic. EVC devices learn MAC addresses based on bridge domains.

On virtual private LAN service (VPLS) networks, multiple bridge domains can transmit traffic of the same virtual switch instance (VSI), and traffic in various bridge domains are distinguished using bridge domain IDs. Bridge domain-based MAC address learning helps devices isolate broadcast domains in a VSI and prevents the learned MAC address entries from changing in the VSI.

* MAC address table generation
  
  + Automatically generated MAC address entries
    
    A device learns source MAC addresses, generates MAC address entries, and adds the entries to a MAC address table. To adapt to a changing network, the MAC address table needs to be updated constantly. The entries automatically generated in a MAC address table are not always valid. Each entry has a life cycle. The entry that is not updated till its life cycle ends will be deleted. This life cycle is called aging time. If the entry is updated before its life cycle expires, the aging time of the entry restarts.
  + Manually configured MAC address entries
    
    When a device automatically learns all source MAC addresses carried in packets to build a MAC address table, it does not check whether the packets are sent by authorized users or hackers, which poses security threats. If hackers set the source MAC addresses of attack packets to the MAC addresses of authorized users and access a device through interfaces different from the interfaces that authorized users access, the device learns incorrect MAC address entries. As a result, the packets that should be forwarded to authorized users are forwarded to hackers. To improve interface security, a network administrator can manually add specified MAC address entries to the MAC address table. The MAC addresses of user devices are bound to access interfaces to prevent unauthorized users from obtaining data. Manually configured MAC address entries take precedence over dynamically generated entries.
* MAC address entry types
  
  + Dynamic entries: learned and stored by interface boards. Dynamic entries age after a specified period of time elapses. After a device resets, an interface board is hot swapped, or the interface board resets, dynamic MAC address entries are lost.
    
    A device automatically learns source MAC addresses and adds them to a MAC address table. The device must be enabled to learn source MAC addresses.
  + Static entries: configured manually and delivered to interface boards. Static entries do not age. The configured static MAC address entries will not be lost even if the device is reset, an interface board on the device is hot swapped, or the interface board is reset.
    
    On a network with unchanged users or a device is connected to an important server, to prevent hacker attacks on devices or the server, a static MAC address can be configured and added to a MAC address table.
  + Static blackhole MAC address entries: configured manually and delivered to interface boards. Blackhole MAC address entries are used to discard frames with specified destination MAC addresses. Blackhole entries do not age. The configured blackhole MAC address entries will not be lost even if the device is reset, an interface board on the device is hot swapped, or the interface board is reset.
    
    To prevent invalid MAC address entries (unauthorized users, for example) from using the MAC address table space and prevent hackers from attacking a device or network using forged MAC addresses, configure MAC addresses of untrusted users as blackhole MAC addresses. A device discards packets destined for static blackhole MAC addresses.
  + Dynamic blackhole entries: learned and stored by interface boards. These address entries do not age out. After a device resets, an interface board is hot swapped, or the interface board resets, MAC address entries are lost.
    
    On an EVPN network, to prevent MAC address entries from frequently flapping, the MAC address entries can be set to dynamic blackhole entries, so that related interfaces are blocked, and loops are rapidly eliminated.
* Limit on MAC address learning
  
  If hackers forge MAC addresses to attack user devices or networks through a device, the device learns the forged MAC address entries and adds the entries to the MAC address table, which causes a MAC address table overflow. As a result, the device cannot learn MAC address entries of authorized users. The MAC address learning limit function allows you to set the maximum number of MAC addresses that a device can learn and the rate at which a device learns MAC addresses. This function helps prevent attacks using forged MAC addresses and limit the number of users who can access the device.
* Aging time for dynamically learned MAC addresses
  
  As the network topology changes, devices keep learning MAC addresses. To prevent a MAC address table overflow, an aging time can be set for dynamically learned MAC address entries. Dynamically learned MAC addresses are deleted if they are not updated after the specified aging time elapses.

Manually configured MAC address entries take precedence over dynamically generated entries. Manually configured MAC address entries take precedence over dynamically generated entries. Static and static blackhole MAC address entries can overwrite dynamic MAC address entries, but cannot be overwritten by dynamic MAC address entries.

#### Pre-configuration Tasks

Before configuring a bridge domain-based MAC address table, [create a bridge domain](dc_vrp_evc_cfg_0004.html).



[Configuring a Static MAC Address Entry](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0008.html)

On a network with unchanged users or a device is connected to an important server, to prevent hacker attacks on devices or the server, a static MAC address can be configured and added to a MAC address table.

[Configuring a Static Blackhole MAC Address Entry](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0009.html)

To prevent invalid MAC address entries (unauthorized users, for example) from using the MAC address table space and prevent hackers from attacking a device or network using forged MAC addresses, configure MAC addresses of untrusted users as blackhole MAC addresses. A device discards packets destined for static blackhole MAC addresses.

[Adjusting Dynamic MAC Address Learning Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0010.html)

Dynamic MAC address learning parameters can be adjusted to improve device security.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0011.html)

After configuring a bridge domain-based MAC address table, you can check the configurations, including the aging time for dynamic MAC addresses in the bridge domain and the limit on the number of MAC addresses that a device can learn.