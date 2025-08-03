Configuring AAA Schemes
=======================

This section describes how to configure authentication, authorization, and accounting (AAA) schemes.

#### Context

Configuring AAA schemes include:

* [Configure an authentication scheme.](#EN-US_TASK_0172371787__step_dc_vrp_aaa_cfg_100401)
* [Configure an authorization scheme.](#EN-US_TASK_0172371787__step_dc_vrp_aaa_cfg_100402)
* [Configure an accounting scheme.](#EN-US_TASK_0172371787__step_dc_vrp_aaa_cfg_100403)

#### Procedure

* Configure an authentication scheme.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**authentication-scheme**](cmdqueryname=authentication-scheme) *scheme-name*
     
     
     
     An authentication scheme is created, and its view is displayed.
     
     
     
     A maximum of 32 authentication schemes can be configured.
  4. Run [**authentication-mode**](cmdqueryname=authentication-mode) { **hwtacacs** | **radius** | **local** }\*
     
     
     
     An authentication mode is configured.
     
     
     
     The **radius** parameter can be specified only for the admin VS.
     
     If multiple authentication modes are configured in an authentication scheme, authentication modes are used in the sequence in which they are configured.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The next configured authentication mode is used only when the current one does not take effect (for example, the server does not respond). If the current authentication succeeds or fails, the next authentication mode is not used.
     
     In the scenario where HWTACACS authentication and then local authentication are configured, after the [**authentication-reliability auto-change-next**](cmdqueryname=authentication-reliability+auto-change-next) command is run, a user is automatically switched to local authentication if HWTACACS remote authentication fails.
  5. (Optional) Run [**authentication-reliability auto-change-next**](cmdqueryname=authentication-reliability+auto-change-next)
     
     
     
     The device is configured to automatically perform local authentication for users who fail HWTACACS remote authentication.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an authorization scheme.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**authorization-scheme**](cmdqueryname=authorization-scheme) *authorization-scheme-name*
     
     
     
     An authorization scheme is created, and its view is displayed.
     
     
     
     A maximum of 32 authorization schemes can be configured.
  4. Run [**authorization-mode**](cmdqueryname=authorization-mode) *authorization-mode1* [ *authorization-mode2* [ *authorization-mode3* [ *authorization-mode4* ] ] ]
     
     
     
     An authorization mode is configured.
     
     
     
     If multiple authorization modes are configured in an authorization scheme, the authorization modes are used in the sequence in which they are configured.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The next configured authorization mode is used only when the current one does not take effect (for example, the server does not respond). If the current authorization succeeds or fails, the next authorization mode is not used.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an accounting scheme.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**accounting-scheme**](cmdqueryname=accounting-scheme) *acct-scheme-name*
     
     
     
     An accounting scheme is created, and its view is displayed.
     
     
     
     A maximum of 256 accounting schemes can be configured.
  4. Run [**accounting-mode**](cmdqueryname=accounting-mode) { **hwtacacs** | **radius** | **none** }
     
     
     
     An accounting mode is configured.
     
     
     
     The **radius** parameter can be specified only for the admin VS.
  5. (Optional) Run [**accounting interim interval**](cmdqueryname=accounting+interim+interval) *interval* [ **second** ] [ **traffic** ] [ **hash** ]
     
     
     
     The interval for real-time accounting and conditions for sending real-time accounting packets are configured, and real-time accounting packets are hashed.
     
     
     
     Real-time accounting indicates that the NE40E periodically generates accounting packets and send them to the remote accounting server when a user is online. Real-time accounting minimizes loss of accounting information when the communication between the NE40E and the remote server is interrupted.
     
     The interval for real-time accounting can be set to minutes or seconds.
  6. (Optional) Run [**accounting start-fail**](cmdqueryname=accounting+start-fail) { **offline** | **online** [ **keep-accounting** ] }
     
     
     
     A policy is configured for handling accounting start failures.
     
     
     
     If the NE40E does not receive any response after sending an Accounting Start packet to the remote accounting server, the NE40E adopts the configured policy for handling the failure. This policy may keep the user online or log the user out.
  7. (Optional) Run [**accounting interim-fail**](cmdqueryname=accounting+interim-fail) [ **max-times** *times* ] { **offline** | **online** }
     
     
     
     A policy is configured for processing real-time accounting failures.
     
     
     
     If the NE40E does not receive any response after re-sending the real-time accounting packets to the remote accounting server for a specified number of times, the NE40E adopts the configured policy for handling the failure. This policy may keep the user online or log the user out.
     
     When RADIUS/HWTACACS accounting is used, it is recommended that the number of retransmissions of real-time accounting packets be greater than the number of retransmissions of RADIUS/HWTACACS packets.
  8. (Optional) Run [**accounting send-update**](cmdqueryname=accounting+send-update)
     
     
     
     The device is configured to send real-time accounting packets immediately after receiving response packets to Accounting Start packets.
     
     
     
     After receiving a response packet from the accounting server, the NE40E determines whether to send a real-time accounting packet immediately according to the configuration.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Follow-up Procedure

Perform one of the following operations based on the configured authentication, authorization, and accounting modes:

* [Configure a local user.](dc_vrp_aaa_cfg_1005.html)
* [Configure an HWTACACS server template.](dc_vrp_aaa_cfg_1006.html)
* [Configuring a Device as a RADIUS Client](../ne/dc_ne_aaa_cfg_1600.html)