Configuring a Multicast Profile
===============================

To authorize multicast users, you must bind a configured multicast list to a created multicast profile.

#### Context

You can bind a configured multicast list to a created multicast profile and configure authentication for multicast users.

Choose one of the following configurations as required:

* Configuring a multicast profile on an IPv4 network
* Configuring a multicast profile on an IPv6 network

#### Procedure

* Configuring a multicast profile on an IPv4 network
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**multicast-profile**](cmdqueryname=multicast-profile) *profile-name*
     
     
     
     An IPv4 multicast profile is configured and the IPv4 multicast profile view is displayed.
  4. Run [**multicast-list**](cmdqueryname=multicast-list) { **name** *list-name* | **list-index** *start-index* *end-index* }
     
     
     
     An IPv4 multicast list is bound to the IPv4 multicast profile.
  5. Run [**authentication**](cmdqueryname=authentication)
     
     
     
     IPv4 multicast user authentication is enabled.
* Configuring a multicast profile on an IPv6 network
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**multicast-profile ipv6**](cmdqueryname=multicast-profile+ipv6) *profile-name*
     
     
     
     An IPv6 multicast profile is configured and the IPv6 multicast profile view is displayed.
  4. Run [**multicast-list ipv6**](cmdqueryname=multicast-list+ipv6) { **name** *list-name* | **list-index** *start-index* [ *end-index* ] }
     
     
     
     An IPv6 multicast list is bound to the IPv6 multicast profile.
  5. Run [**authentication**](cmdqueryname=authentication)
     
     
     
     IPv6 multicast user authentication is enabled.