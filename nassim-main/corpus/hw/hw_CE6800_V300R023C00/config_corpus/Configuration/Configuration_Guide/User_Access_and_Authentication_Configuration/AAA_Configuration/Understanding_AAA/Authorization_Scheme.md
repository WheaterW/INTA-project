Authorization Scheme
====================

An authorization scheme defines the authorization methods used for user authorization and the order in which authorization methods take effect.

#### Authorization Methods Supported by a Device

* RADIUS authorization: A RADIUS server is used to authorize users. RADIUS combines authentication and authorization, which cannot be separated. If authentication succeeds, authorization also succeeds. When RADIUS authentication is used, no authorization scheme needs to be configured.
* HWTACACS authorization: An HWTACACS server is used to authorize users.
* LDAP authorization: An LDAP server is used to authorize users.
* Local authorization: The device functions as an authorization server to authorize users based on user information configured on the device.
* Non-authorization: Authenticated users have unrestricted access rights on a network.![](public_sys-resources/note_3.0-en-us.png) 
  
  For device or network security purposes, you are advised not to set the authorization mode to non-authorization.
* if-authenticated authorization: If passing authentication, a user passes authorization; otherwise, the user fails authorization. This method applies to scenarios where users must be authenticated and the authentication process can be separated from the authorization process.

In addition, the "authentication + privilege level" method is typically used to control access of the administrators (login users) to the device, improving device operation security. Authentication restricts the administrators' access to the device and the privilege level defines commands that the administrators can enter after logging in to the device. For details about this method, see "Logging In to the CLI" in the *Configuration Guide - Basic Configuration*.


#### Order in Which Authorization Methods Take Effect

An authorization scheme enables you to designate one or more authorization methods to be used, thus ensuring a backup system for authorization in case the initial method does not respond. The first method listed in the scheme is used to authorize users; if that method does not respond, the next authorization method in the authorization scheme is selected. If the initial method responds with an authorization failure message, the AAA server refuses to provide services for the user. In this case, authorization ends and the next listed method is not attempted.


#### Authorization Information

Authorization information can be delivered by a server or configured in a domain. For details about domains, see [Domain-based User Management](galaxy_aaa_cfg_0007.html). Whether a user obtains authorization information delivered by a server or configured in a domain depends on the authorization method configured in the authorization scheme. For details, see [Figure 1](#EN-US_CONCEPT_0000001564115685__en-us_concept_0176366033_fig_dc_cfg_aaa_602204).

* If local authorization is used, the user obtains authorization information from the domain.
* If server authorization is used, the user obtains authorization information from the server or domain. Authorization information configured in a domain has lower priority than that delivered by a server. If the two types of authorization information conflicts, authorization information delivered by the server takes effect. If no conflict occurs, the two types of authorization information take effect simultaneously. In this manner, you can increase authorization flexibility by means of domain management, regardless of the authorization attributes provided by the server.

**Figure 1** Two types of authorization information  
![](figure/en-us_image_0000001512836178.png)