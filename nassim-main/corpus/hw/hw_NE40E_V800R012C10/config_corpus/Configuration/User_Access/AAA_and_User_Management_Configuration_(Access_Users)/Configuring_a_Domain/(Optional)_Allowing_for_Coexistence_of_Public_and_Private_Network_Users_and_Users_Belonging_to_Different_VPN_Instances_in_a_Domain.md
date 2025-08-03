(Optional) Allowing for Coexistence of Public and Private Network Users and Users Belonging to Different VPN Instances in a Domain
==================================================================================================================================

(Optional) Allowing for Coexistence of Public and Private Network Users and Users Belonging to Different VPN Instances in a Domain

#### Context

By default, a domain does not allow for the coexistence of public and private network users or the coexistence of users belonging to different VPN instances. To allow for such coexistence, configure the device to trust the VPN instances bound to the user access BAS interface or the VPN instances bound to the address pool or address pool group used by a RADIUS server to assign IP addresses. The configuration applies only to Layer 2 common users and static users.


#### Procedure

1. Allow for the coexistence of public and private network users and users belonging to different VPN instances when the BAS interfaces of such users are the same.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The domain view is displayed.
   4. Run [**trust vpn-instance access-interface**](cmdqueryname=trust+vpn-instance+access-interface)
      
      
      
      The device is configured to trust the VPN instance bound to the BAS interface.
      
      
      
      For VPN users, ensure that the VPN instance has been bound to the BAS interface using the [**vpn-instance**](cmdqueryname=vpn-instance) command in the BAS interface view and that the VPN instance bound to the BAS interface must be the same as that bound to the IP address pool.
      
      This command applies only to Layer 2 common users and static users.
2. Allow for the coexistence of public and private network users and users belonging to different VPN instances when the BAS interfaces of such users are different.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The domain view is displayed.
   4. Run either of the following commands to configure the device to trust the VPN instance bound to the address pool or address pool group used by the RADIUS server to assign IP addresses:
      
      
      * For IPv4 users, run the [**trust vpn-instance framed-pool**](cmdqueryname=trust+vpn-instance+framed-pool) command.
      * For IPv6 users, run the [**trust vpn-instance framed-ipv6-pool**](cmdqueryname=trust+vpn-instance+framed-ipv6-pool) command.
        
        This command applies only to Layer 2 common users and static users.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.