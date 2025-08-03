IPv4 User-Side Multicast Configuration
======================================

Configuring IPv4 user-side multicast on a BRAS enables the BRAS to identify users, so that the BRAS can replicate the data flow of a multicast program only for users who are requiring the multicast program. User-side multicast implements user-based multicast service control and management for carriers.

#### Context

IPv4 user-side multicast enables the BRAS to identify users as they join or leave multicast groups, which helps carriers better manage and control the users.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This feature is supported only on the Admin-VS.



[Overview of IPv4 User-Side Multicast](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bras-multicast_cfg_0001.html)

This section describes the definition and purpose of user-side multicast.

[Configuration Precautions for IPv4 user-side multicast](../../../../software/nev8r10_vrpv8r16/user/spec/IPv4_user-side_multicast_limitation.html)



[Configuring IPv4 User-Side Multicast](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bras-multicast_cfg_0003.html)

User-side multicast enables a BRAS to identify users who have joined or left a multicast group, implementing user-based multicast service control and management.

[Configuring IPv4 User-Side Multicast for a VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bras-multicast_cfg_0010.html)

To enable a device to identify users of multicast programs in a VPN and to implement refined management of users in the VPN, configure IPv4 user-side multicast for the VPN.

[Configuring IPv4 User-side Multicast CAC](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_bras-multicast_cac_cfg_0001.html)

To implement refined bandwidth control for users, configure user-side multicast CAC, which helps improve multicast service quality.

[Configuring IPv4 Static Multicast](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_bras-multicast_cac_cfg_0005.html)

To allow IPv4 BAS users to receive the traffic of specific multicast groups without sending IGMP join messages, configure static multicast.

[Maintaining IPv4 User-Side Multicast](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bras-multicast_cfg_0004.html)

User-side multicast maintenance includes checking multicast group joining information for online users and statistics about IGMP messages, and deleting statistics about IGMP messages on BAS interfaces.

[Configuration Examples for User-Side Multicast](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bras-multicast_cfg_0007.html)

This section provides user-side multicast configuration examples, including networking requirements, precautions and configuration roadmap.