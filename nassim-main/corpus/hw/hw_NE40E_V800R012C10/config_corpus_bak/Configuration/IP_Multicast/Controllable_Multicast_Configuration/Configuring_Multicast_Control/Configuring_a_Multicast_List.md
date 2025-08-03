Configuring a Multicast List
============================

A multicast list consists of one or more multicast addresses that are used to define one or more channels or programs.

#### Context

A multicast list consists of one or more multicast addresses that are used to define one or more channels or programs.

Choose one of the following configurations as required:

* Configuring a multicast list on an IPv4 network
* Configuring a multicast list on an IPv6 network

#### Procedure

* Configuring a multicast list on an IPv4 network
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**multicast-list**](cmdqueryname=multicast-list) *list-name* [ **index** *list-index* ] [ **source-address** *source-address* [ *source-mask* | *source-mask-len* ] ] **group-address** *group-address* [ *group-mask* | *group-mask-length* ] [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     An IPv4 multicast list is configured.
     
     
     
     If neither group-mask nor group-mask-length is specified, by default, the system configures only one multicast list, with the group-mask being 255.255.255.255. That is, the group-mask-length is 32.
* Configuring a multicast list on an IPv6 network
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**multicast-list ipv6**](cmdqueryname=multicast-list+ipv6) *list-name* [ **index** *list-index* ] [ **source-ipv6-address** *ipv6-addr* [ *ipv6-prefix* ] ] **group-ipv6-address** *ipv6-addr* [ *group-ipv6-prefix* ] [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     An IPv6 multicast list is configured.