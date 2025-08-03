Configuring a Static User
=========================

A user requiring a fixed IP address can be configured as a static user.

#### Prerequisites

Before configuring an access interface for a static user, configure the interface as a BAS interface.


#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

* The IPv4 address assigned to a Layer 2 or Layer 3 static user must belong to a configured address pool. If the address pool is a local address pool, you must run the [**excluded-ip-address**](cmdqueryname=excluded-ip-address) command to disable a specified range of IP addresses. This prevents these IP addresses from being dynamically assigned to other users.
* If an IPv6 address or IPv6 delegation prefix needs to be assigned from a local address pool to a Layer 2 or Layer 3 static user, you must configure a local address pool first and run the [**excluded-ipv6-address**](cmdqueryname=excluded-ipv6-address) command to disable the specified IPv6 address segment or prefix segment. If an IPv6 address or IPv6 delegation prefix needs to be assigned from a remote address pool, the local device does not need to be configured with a remote address pool, and the remote server must ensure that the address or address segment is not occupied by other users.
* If the IPv6 address/delegation prefix of a Layer 2 static user is not assigned from the local or remote address pool, ensure that the IPv6 address/delegation prefix is not occupied by other users or services.

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Add an interface to the access interface list of static users.
   
   
   1. Run the [**static-user interface-list**](cmdqueryname=static-user+interface-list) *list-name* command to configure an access interface list for static users.
   2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to add an interface to the access interface list of static users.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
3. Run either of the following commands to create a static user:
   
   
   * Run the [**static-user**](cmdqueryname=static-user) [ *description* ] { *start-ip-address* [ *end-ip-address* ] [ **gateway** *gateway-ip-address*] | *start-ipv6-address* [ *end-ipv6-address* ] [ **delegation-prefix** *start-ipv6-prefix* [ *end-ipv6-prefix* ] *prefix-length* ] **ipv6âgateway** *ipv6-address*} \* [ **vpn-instance** *instance-name* ] [ **interface** { *interface-name* | *interface-type* *interface-number* } [ **vlan** *vlan-id* [ **qinq** *qinq-vlan* ] ] | **mac-address** *mac-address* | **detect** | **keep-online** | **domain-name** *domain-name* | **export** | **user-name** *user-name* ] \* command to create a static user. The static user can go online through a specified interface.
     
     If **detect** is configured, the device initiates ARP/IPv4 packets or NS/NA/IPv6 packets for static users to trigger user login. If **detect** is not configured:
     
     + Run the [**ip-trigger**](cmdqueryname=ip-trigger) or [**arp-trigger**](cmdqueryname=arp-trigger) command in the BAS interface view so that IPv4 static users are triggered to go online only after they send ARP/IPv4 packets.
     + Run the [**ipv6-trigger**](cmdqueryname=ipv6-trigger) or [**nd-trigger**](cmdqueryname=nd-trigger) command in the BAS interface view so that IPv6 users are triggered to go online only after they send NS/NA/IPv6 packets.
   * Run the [**static-user**](cmdqueryname=static-user) [ *description* ] *start-ip-address* [ *end-ip-address* ] [ **gateway** *gateway-ip-address* ] [ **vpn-instance** *instance-name* ] [ **domain-name** *domain-name* | **interface-list** *list-name* | **mac-address** *mac-address* | **export** | **keep-online** | **user-name** *user-name* ] \* command to create a static user. The user can go online through an interface of the specified interface list.
   
   When creating a static user, you can specify an IP address (including the VPN instance to which the IP address belongs), an interface through which the user is connected to the NE40E, a domain to which the user belongs, and a MAC address for the user.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * IPv4 single-stack static users can go online through multiple interfaces bound to an interface list. However, the device cannot initiate ARP or IPv4 packets for the static users for login. When you configure IPv4 single-stack static users to go online through interfaces bound to an interface list using the [**static-user**](cmdqueryname=static-user) command, the **detect** and **vlan** keywords cannot be configured.
   * The interface through which IPv6 static users go online cannot be bound to an interface list.
   * If a client needs to ping the IPv6 gateway address of a Layer 2 IPv6 static user, the gateway address must be configured on any interface of the BRAS.
   * If the **vpn-instance** keyword is configured, the same VPN instance must be configured on the BAS interface so that users can go online through this interface.
   * If an IPv4/IPv6 address and **keep-online** are configured for a static user and this user goes online but fails to be detected multiple times, the device periodically broadcasts detection packets to the user client, allowing the user to go online again using the IPv4/IPv6 address after a MAC address change. In this case, ensure that the access interface and VLAN remain unchanged. To prevent the static user from going online again after changing the MAC address, you can specify the MAC address in the static user configuration. If a dual-stack static user changes the MAC address, the user is logged out from both stacks. After the user is allowed to change the MAC address, the user goes online again using the original IPv4 and IPv6 addresses. In this case, ensure that the access interface and VLAN remain unchanged.
   * If the MAC address of a static user is changed before the roaming process ends, the user cannot go online again using the IPv4 address.
4. (Optional) Run [**static-user detect interval**](cmdqueryname=static-user+detect+interval) *interval-value*
   
   
   
   The interval at which the Router detects whether static users are online is configured.
5. (Optional) Run [**static-user datacheck trust bas**](cmdqueryname=static-user+datacheck+trust+bas)
   
   
   
   The static user detection behavior when users send traffic is configured to be the same as that configured on the BAS interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**static-user datacheck trust bas**](cmdqueryname=static-user+datacheck+trust+bas) command is run, the **user detect datacheck** command configuration in the BAS interface view determines whether the device detects static users.
6. Run [**layer3-subscriber**](cmdqueryname=layer3-subscriber) { *start-ip-address* [ *end-ip-address* ] | *start-ipv6-address* [ *end-ipv6-address* ] | **delegation-prefix** *start-ipv6-prefix* [ *end-ipv6-prefix* ] *prefix-length* } \* [ **vpn-instance** *instance-name* ] **domain-name** *domain-name*
   
   
   
   The IP address segment to which the Layer 3 static users belong and the name of the associated authentication domain are specified.
   
   
   
   The number of address segments that can be configured on a device is limited. When there are a large number of address segments on a network, you are advised to run the [**layer3-subscriber ip-address any**](cmdqueryname=layer3-subscriber+ip-address+any) **domain-name** *domain-name* command. If no address segment is matched, users go online based on the domain configured using this command. If this command is not run, IPv4 packets that do not match the address segment are discarded, and users fail to go online.
7. (Optional) Run [**layer3-subscriber ipv4 vpn-instance switch enable**](cmdqueryname=layer3-subscriber+ipv4+vpn-instance+switch+enable) [ **export host-route** ]
   
   
   
   Dynamic VPN instance switching is enabled for Layer 3 static users.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This function takes effect only in IPoEv4 access scenarios.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.