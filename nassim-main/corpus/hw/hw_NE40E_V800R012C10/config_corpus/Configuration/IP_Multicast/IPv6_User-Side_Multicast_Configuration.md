IPv6 User-Side Multicast Configuration
======================================

Configuring IPv6 user-side multicast on a BRAS enables the BRAS to identify users and to implement user-based multicast service control and management.

#### Context

IPv6 user-side multicast enables the BRAS to identify users and the programs they join or leave, which help carriers better manage and control online users.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This feature is supported only on the Admin-VS.



[Overview of IPv6 User-Side Multicast](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6bras-multicast_cfg_0001.html)

This section describes the definition and purpose of IPv6 user-side multicast.

[Configuration Precautions for IPv6 user-side multicast](../../../../software/nev8r10_vrpv8r16/user/spec/IPv6_user-side_multicast_limitation.html)



[Configuring IPv6 User-Side Multicast](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6bras-multicast_cfg_0003.html)

User-side multicast enables a BRAS on an IPv6 network to identify users who have joined or left a multicast group, implementing user-based multicast service control and management.

[Configuring IPv6 Static Multicast](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_bras-multicast_cac_cfg_ipv6_0005.html)

To allow IPv6 BAS users to receive the traffic of specific multicast groups without sending MLD join messages, configure static multicast.

[Maintaining IPv6 User-Side Multicast](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6bras-multicast_cfg_0004.html)

IPv6 User-side multicast maintenance includes checking multicast group joining information for online users and statistics about MLD messages, and deleting statistics about MLD messages on BAS interfaces.

[Configuration Examples for IPv6 User-Side Multicast](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv6bras-multicast_cfg_0007.html)

This section provides IPv6 user-side multicast configuration examples, including networking requirements, precautions and configuration roadmap.