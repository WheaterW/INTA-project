Logging Out Users
=================

In some scenarios, for example, when the online duration of a user expires, you can log out the user through AAA.

#### Procedure

* To log out users, run the following commands in the AAA view.
  
  
  + Run the [**cut access-user**](cmdqueryname=cut+access-user) **interface** { *interface-name* | *interface-type interface-number* } [ ****odd-mac**** | **even-mac** ] command to log out all users with odd or even MAC addresses on a specified interface.
  + Run the [**cut access-user**](cmdqueryname=cut+access-user) **mac-address** *mac-address* command to log out an online user based on a MAC address.
  + Run the [**cut access-user**](cmdqueryname=cut+access-user) **slot** *slot-id* command to log out online users based on a slot ID.
  + Run the [**cut access-user**](cmdqueryname=cut+access-user) **ip-address** *ip-address* [ *end-ip-address* ] [ **vpn-instance** *instance-name* ] command to log out online users based on IP addresses.
  + Run the [**cut access-user**](cmdqueryname=cut+access-user) **ipv6-address** *ipv6-address* [ **vpn-instance** *instance-name* ] command to log out an online user based on an IPv6 address.
  + Run the [**cut access-user**](cmdqueryname=cut+access-user) **username** *user-name* { **all** | **hwtacacs** | **local** | **none** | **radius** | **radius-proxy** } command to log out an online user based on a username.
  + Run the [**cut access-user**](cmdqueryname=cut+access-user) **domain** *domain-name* command to log out online users based on a domain name.
  + Run the [**cut access-user**](cmdqueryname=cut+access-user) **user-id** *start-num* [ *end-num* ] command to log out an online user based on a user ID.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    - If the connection is torn down based on the domain name, all online users in the domain are logged out.
    - When connections are torn down based on usernames or user IDs, if there are multiple connections satisfying the condition, they are torn down at the same time.