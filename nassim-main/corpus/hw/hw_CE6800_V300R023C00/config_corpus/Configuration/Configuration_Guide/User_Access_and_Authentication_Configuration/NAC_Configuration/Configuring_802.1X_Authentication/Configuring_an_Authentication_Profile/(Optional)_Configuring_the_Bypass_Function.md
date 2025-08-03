(Optional) Configuring the Bypass Function
==========================================

(Optional) Configuring the Bypass Function

#### Prerequisites

Before configuring the bypass function for users, you need to complete the following configurations on the device:

* Configure a VLAN and associated network resources on the device.
* Configure a service scheme. For details, see [(Optional) Configuring a Service Scheme](galaxy_aaa_cfg_0014.html).

#### Context

Pre-connection users or users who fail authentication do not have network access rights. To meet the basic network access requirements of these users, such as updating the antivirus database and downloading the client, configure the bypass function on the device. The device will then authorize these users based on their authentication phase.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the authentication profile view.
   
   
   ```
   [authentication-profile](cmdqueryname=authentication-profile) name authentication-string
   ```
3. Configure the bypass function.
   
   
   
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure rights available to pre-connection users. | [**authentication event**](cmdqueryname=authentication+event) **pre-authen action authorize** { **vlan** *vlan-id* } | When users fail authentication, the authentication server is down, or the authentication server does not respond, the **response-fail** or **no-response** parameter can be configured on the device. * If neither of the two parameters is specified, the device sends an authentication success packet to users by default. As a result, the users are unaware of their authentication failures and authentication status. * If **response-fail** is specified, the device sends an authentication failure packet to the users. * If **no-response** is specified, the device does not send any response packet to the users. |
   | Configure rights available to users who fail authentication. | [**authentication event**](cmdqueryname=authentication+event) **authen-fail** **action authorize** { **vlan** *vlan-id* | **service-scheme** *scheme-name* } [ **response-fail** ] |
   | Configure rights available to users when the authentication server is down. | [**authentication event**](cmdqueryname=authentication+event) **authen-server-down** **action authorize** { **vlan** *vlan-id* | **service-scheme** *scheme-name* } [ **response-fail** ] |
   | Configure the device to retain the original rights of users when the authentication server is down. | [**authentication event**](cmdqueryname=authentication+event) **authen-server-down** **action authorize** **keep** [ **no-response** | **response-fail** ] | NA |
   | Configure the device to retain the original rights of users when the authentication server does not respond. | [**authentication event**](cmdqueryname=authentication+event) **authen-server-noreply** **action authorize** **keep** [ **no-response** | **response-fail** ] |
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The device grants rights to users based on the authentication server status or user status. If rights at a higher level are not configured, the rights at a lower level are assigned to users instead. Rights granted to users in pre-connection state are available only when the pre-connection function is enabled.
   
   * If the device detects that the authentication server is down, rights are assigned to users in descending order of priority as follows: rights available to users when the authentication server is down > rights available to users who fail authentication > rights available to users in pre-connection state.
   * If users fail authentication, rights are assigned to users in descending order of priority as follows: rights available to users who fail authentication > rights available to users in pre-connection state.
   * If users are in pre-connection state, rights available to users in pre-connection state are assigned to users.
   
   VLAN-based authorization does not apply to the authentication users who access the device through VLANIF interfaces.
   
   In 802.1X authentication for wired users, when the RADIUS server is down, some new clients will fail to go online because they do not have bypass rights. For example, when a Windows client receives a Success packet from the device, but does not receive the authentication packets exchanged with the RADIUS server, the client fails the authentication and cannot go online. Currently, the following clients have bypass rights when they go online after the user bypass function is configured: H3C iNode clients using Extensible Authentication Protocol (EAP)-message digest algorithm 5 (MD5) and Protected Extensible Authentication Protocol (PEAP), and Cisco AnyConnect clients using EAP-FAST and PEAP. For a Windows client (for example, Windows 7 client), choose **Local Area Connection** > **Properties** > **Authentication** > **Fallback to unauthorized network access** to grant bypass rights to the client.
4. (Optional) Configure the aging time for user entries.
   
   
   
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the aging time for entries of pre-connection users. | [**authentication timer pre-authen-aging**](cmdqueryname=authentication+timer+pre-authen-aging) *aging-time* | By default, the aging time for entries of pre-connection users is 23 hours. |
   | Configure the aging time for entries of the users who fail authentication. | [**authentication timer authen-fail-aging**](cmdqueryname=authentication+timer+authen-fail-aging) *aging-time* | By default, the aging time for entries of users who fail authentication is 23 hours.  This command can also be used to configure the aging time for entries of users whose authentication server is down. |
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```