AAA and User Management Configuration (Access Users)
====================================================

AAA configuration allows local or remote authentication, authorization, and accounting to be performed for access users.The NE40E-M2E does not support this feature.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this feature is supported only by the admin VS.



[Overview of AAA](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0036.html)



[Configuration Precautions for AAA and User Management (Access Users)](../../../../software/nev8r10_vrpv8r16/user/spec/AAA_and_User_Management_limitation.html)



[Configuring AAA Schemes](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0515.html)

Configure AAA schemes to determine user authentication, authorization, and accounting modes.

[Configuring a Device as a RADIUS Client](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0600.html)

When a device functions as a RADIUS client to perform authentication, authorization, and accounting for users through a remote RADIUS server, you need to configure RADIUS information on the device.

[Configuring the Function to Locally Generate and Store User Bills](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_09002.html)

If RADIUS is used to implement accounting, configure the function to locally generate and store user bills, so that user accounting information is still correct if an interworking RADIUS server fails to respond upon user login or logout.

[Configuring a Device as a Diameter Client](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0050.html)

A Diameter client must be configured if service policies need to be delivered through the server.

[Configuring a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0111.html)

The NE40E supports domain-based management for local users and access users.

[Configuring and Managing Users](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0270.html)

The BRAS manages users either through the domain to which users belong or user accounts.

[Maintaining AAA](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0039.html)

This section describes how to maintain AAA by clearing HWTACACS statistics and debugging RADIUS or HWTACACS.

[Configuration Examples for AAA and User Management](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0057.html)

This section provides configuration examples for AAA and user management.