Configuring IPv6 Static Multicast
=================================

To allow IPv6 BAS users to receive the traffic of specific multicast groups without sending MLD join messages, configure static multicast.

#### Usage Scenario

Configure static multicast when a program (such as an advertisement program) needs to be pushed to users, delivered to users' STBs before users join the program, or delivered to Layer 2 devices before users join the program. Static multicast helps shorten the program switching duration.


#### Pre-configuration Tasks

Before configuring static multicast, complete the tasks shown in [Figure 1](#EN-US_TASK_0172367703__fig9701546163711). For configuration details, see [Table 1](#EN-US_TASK_0172367703__table_dc_ne_bras-multicast_cac_cfg_000101).

**Figure 1** Pre-configuration tasks for static multicast configurations  
![](figure/en-us_image_0258918782.png)

**Table 1** Pre-configuration Tasks
| Task | Link |
| --- | --- |
|  | Configure an IPv6 address pool to assign IPv6 addresses to access users. |
|  | Configure AAA authentication and accounting schemes. |
|  | Configure a domain to implement AAA functions and manage access users. |
|  | Configure the PPPoE or IPoE access mode.   * [Configuring the PPPoXv6 Access Service](dc_ne_pppoxv6_cfg_0012.html) * [Configuring the IPoEv6 Access Service](dc_ne_ipoxv6_cfg_0004.html) |
|  | Enable multicast routing, PIM, and MLD.   1. [Enable IPv6 multicast routing.](../vrp/dc_vrp_multicast_cfg_2006.html) 2. [Enable IPv6 PIM-SM.](../vrp/dc_vrp_multicast_cfg_2007.html) 3. [Enable MLD.](../vrp/dc_vrp_multicast_cfg_2074.html) |
|  | Configure a BAS interface. |




#### Procedure

1. Configure an IPv6 static multicast program list.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**multicast-list**](cmdqueryname=multicast-list) **ipv6** *list-name* [ **index** *list-index* ] [ **source-ipv6-address** *source-ipv6-address* [ *source-ipv6-prefix-length* ] ] **group-ipv6-address** *group-ipv6-address* [ *group-ipv6-prefix-length* ] [ **vpn-instance** *vpn-instance-name* ]
      
      
      
      An IPv6 multicast program list is configured.
2. Configure an IPv6 multicast profile.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**multicast-profile**](cmdqueryname=multicast-profile) **ipv6** *profile-name*
      
      
      
      An IPv6 multicast profile is created, and the profile view is displayed.
   4. Run [**multicast-list**](cmdqueryname=multicast-list) **ipv6** { **name** *list-name* | **list-index** *start-index* [ *end-index* ] } [ **static**]
      
      
      
      The IPv6 multicast program list is bound to the IPv6 multicast profile.
   5. Run [**authentication**](cmdqueryname=authentication)
      
      
      
      Authentication is enabled for IPv6 multicast users.
3. Bind the multicast profile to the AAA domain.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The AAA domain view is displayed.
   4. Run [**multicast-profile**](cmdqueryname=multicast-profile) [ **ipv6** ] *profile-name*
      
      
      
      The IPv6 multicast profile is bound to the AAA domain.
   
   
   
   After a multicast profile is bound to a domain, users in this domain are allowed to access the programs defined in the multicast program list that is bound to the multicast profile. One domain can use only one multicast profile. If multiple multicast profiles are bound to a domain, the latest binding takes effect.

#### Checking the Configurations

Run the [**display multicast-profile ipv6**](cmdqueryname=display+multicast-profile+ipv6) command to check information about a specified or all IPv6 multicast profiles.

Run the [**display multicast-list ipv6**](cmdqueryname=display+multicast-list+ipv6) command to check information about a specified or all IPv6 multicast program lists.