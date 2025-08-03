Disconnecting Online Users
==========================

Disconnecting_Online_Users

#### Context

The NE40E can be configured to disconnect online users by a condition, such as the IP address, MAC address, access interface, or domain, or a combination of conditions. If multiple connections meet a condition, the device disconnects the users at the same time. You can use a combination of the domain name, interface name, IP address pool, IPv6 address pool, and username to disconnect users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Disconnect online users as required.
   
   
   * To disconnect all online users with IPv6 prefixes within the address range, including the user addresses and prefixes, run the [**cut access-user ipv6-segment**](cmdqueryname=cut+access-user+ipv6-segment) *ipv6-prefix* [ **vpn-instance** *instance-name* ] command.
   * To disconnect online users based on IPv6 prefixes, run the [**cut access-user**](cmdqueryname=cut+access-user) **ipv6-prefix** *ipv6-prefix* [ **vpn-instance** *instance-name* ] command.
   * To disconnect an online user based on the username, run the [**cut access-user**](cmdqueryname=cut+access-user) **username** *user-name* { **all** | **hwtacacs** | **local** | **none** | **radius** | **radius-proxy** } command.
   * To disconnect online users based on a domain name, run the [**cut access-user**](cmdqueryname=cut+access-user) **domain** *domain-name* command.
   * To disconnect online users on an interface, run the [**cut access-user**](cmdqueryname=cut+access-user) **interface** *interface-type interface-number* [ **pevlan** *vlan-id* ] [ **cevlan** *vlan-id* ] command.
   * To disconnect online users based on an address pool, run the [**cut access-user**](cmdqueryname=cut+access-user) **ip-pool** *pool-name* command.
   * To disconnect online users based on an IPv6 address pool, run the [**cut access-user**](cmdqueryname=cut+access-user) **ipv6-pool** *ipv6-pool* command.
   * To disconnect online users based on an authentication mode, run the [**cut access-user**](cmdqueryname=cut+access-user) **authen-method** *authen-method-type* command.
   * To disconnect online users based on a QoS policy, run the [**cut access-user**](cmdqueryname=cut+access-user) { **qos-profile** *qos-profile-name* | **family-qos-profile** *family-qos-profile-name* | **resource-insufficient user-queue** } [ **inbound** | **outbound** | **both** ] command.
   * To disconnect online users based on a RADIUS server group, run the [**cut access-user**](cmdqueryname=cut+access-user) **radius-server-group** *radius-server-group* command.
   * To log out online users based on the specified combination of conditions, run the [**cut access-user**](cmdqueryname=cut+access-user) { **username** *user-name* { **all** | **hwtacacs** | **local** | **none** | **radius** | **radius-proxy** } | **domain** *domain-name* | **interface** *interface-type interface-number* [ **pevlan** *pevlan-id* [ **cevlan** *cevlan-id* ] ] | **ip-pool** *pool-name* | **ipv6-pool** *pool-name* | **authen-method** *authen-method-type* | { **qos-profile** *qos-profile-name* | **family-qos-profile** *family-qos-profile-name* | **resource-insufficient** **user-queue** } [ **inbound** | **outbound** | **both** ] | **radius-server-group** *radius-server-group* | }\* command.
   * To disconnect all users with odd or even MAC addresses on a specified interface, run the [**cut access-user**](cmdqueryname=cut+access-user) **interface** { *interface-name* | *interface-type interface-number* } [ ****odd-mac**** | **even-mac** ] command.
   * To disconnect an online user based on the user ID, run the [**cut access-user**](cmdqueryname=cut+access-user) **user-id** *start-num* [ *end-num* ] command.
   * To disconnect online users based on IP addresses, run the [**cut access-user**](cmdqueryname=cut+access-user) **ip-address** *ip-address* [ *end-ip-address* ] [ **vpn-instance** *instance-name* ] command.
   * To disconnect an online user with a specified IPv6 address, run the [**cut access-user**](cmdqueryname=cut+access-user) **ipv6-address** *ipv6-address* [ **vpn-instance** *instance-name* ] command.
   * To disconnect an online user based on a MAC address, run the [**cut access-user**](cmdqueryname=cut+access-user) **mac-address** *mac-address* command.
   * To disconnect online users based on a slot ID, run the [**cut access-user**](cmdqueryname=cut+access-user) **slot** *slot-id* command.
4. Run [**user-queue-resource allocate-fail offline**](cmdqueryname=user-queue-resource+allocate-fail+offline)
   
   
   
   A policy is configured to forcibly log out users when user queue resources fail to be allocated.
5. (Optional) Configure the device to forcibly log out a user if an IP address is released.
   1. (Optional) Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The domain view is displayed.
   2. (Optional) Run [**any-address-release offline**](cmdqueryname=any-address-release+offline)
      
      
      
      The device is configured to forcibly log out a user if any IP address is released by the user.
      
      
      
      This command applies only to PPPoX and L2TP users.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.