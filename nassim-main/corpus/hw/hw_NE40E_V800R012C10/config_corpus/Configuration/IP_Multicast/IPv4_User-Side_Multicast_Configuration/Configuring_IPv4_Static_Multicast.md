Configuring IPv4 Static Multicast
=================================

To allow IPv4 BAS users to receive the traffic of specific multicast groups without sending IGMP join messages, configure static multicast.

#### Usage Scenario

Configure static multicast when a program (such as an advertisement program) needs to be pushed to users, delivered to users' STBs before users join the program, or delivered to Layer 2 devices before users join the program. Static multicast helps shorten the program switching duration.


#### Pre-configuration Tasks

Before configuring static multicast, complete the tasks shown in [Figure 1](#EN-US_TASK_0172367660__fig2845416183017). For configuration details, see [Table 1](#EN-US_TASK_0172367660__table_dc_ne_bras-multicast_cac_cfg_000101).

**Figure 1** Pre-configuration tasks for static multicast configurations  
![](figure/en-us_image_0258916571.png)

**Table 1** Description of each pre-configuration task
| Item | Description |
| --- | --- |
|  | Configure an IPv4 Address Pool to Assign IP Addresses to Online Users. |
|  | Configure Authentication, Authorization and Accounting (AAA) schemes. |
|  | Configure a domain to implement AAA functions and manage access users. |
|  | Configure the PPPoE or IPoE access mode.   * [Configure the PPPoE access mode.](dc_ne_pppoe_cfg_0004.html) * Configure the IPoE access mode. |
|  | Configure basic multicast functions.   1. Configure multicast static routes. 2. Enable PIM-SM. 3. Enable IGMP. |
|  | Configure a BAS interface. |




#### Procedure

1. Configure a multicast program list
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**multicast-list**](cmdqueryname=multicast-list) *list-name* [ **index** *list-index* ] [ **source-address** *source-address* ] **group-address** *group-address* [ **vpn-instance** *vpn-instance-name* ]
      
      
      
      An IPv4 multicast program list is created.
2. Configure a multicast profile
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**multicast-profile**](cmdqueryname=multicast-profile) *profile-name*
      
      
      
      An IPv4 multicast profile is configured, and the profile view is displayed.
   4. Run [**multicast-list**](cmdqueryname=multicast-list) { **name** *list-name* | **list-index** *start-index* [ *end-index* ] } [ **static** ]
      
      
      
      The IPv4 multicast program list is bound to the IPv4 multicast profile.
   5. Run [**authentication**](cmdqueryname=authentication)
      
      
      
      Authentication is enabled for IPv4 multicast users.
3. Bind the multicast profile to the AAA domain.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   3. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The AAA domain view is displayed.
   4. Run [**multicast-profile**](cmdqueryname=multicast-profile) *profile-name*
      
      
      
      The IPv4 multicast profile is bound to the AAA domain.
   
   
   
   After a multicast profile is bound to a domain, users in this domain are allowed to access the programs defined in the multicast program list that is bound to the multicast profile. One domain can use only one multicast profile. If multiple multicast profiles are bound to a domain, the latest binding takes effect.

#### Checking the Configurations

Run the [**display multicast-profile**](cmdqueryname=display+multicast-profile) command to check information about a specified or all multicast profiles.

Run the [**display multicast-list**](cmdqueryname=display+multicast-list) command to check information about a specified or all multicast program lists.