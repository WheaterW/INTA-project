Configuring ROA
===============

Resource Public Key Infrastructure (RPKI) can be configured to validate the origin of BGP4+ routes to ensure BGP4+ security. Route Origin Authorization (ROA) uses RPKI to validate and filter routes.

#### Usage Scenario

To solve the problem of BGP4+ route hijacking, the industry proposes the RPKI solution that validates the origin ASs of BGP4+ routes. Distributed RPKI servers are used to collect information such as the origin AS numbers, route prefixes, and masks of BGP4+ routes initiated by each ISP. After a device sets up a connection with an RPKI cache server, the device saves a copy of Route Origin Authorization (ROA) data locally. If no RPKI server is available, static ROA data can be configured on a device. Inbound ROA validation, which applies to the BGP4+ routes received from peers, can be configured to control route selection. In addition, outbound ROA validation, which applies to the BGP4+ routes to be advertised to peers, can be configured to control route advertisement. ROA validation ensures that hosts in an AS can securely access external services.


#### Pre-configuration Tasks

Before configuring ROA, complete the following tasks:

* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).

#### Procedure

1. Select one of the following configurations based on the usage scenario:
   
   
   * If the local device needs to obtain data from the ROA database through a connection to be established with an RPKI server, perform the following operations:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**rpki**](cmdqueryname=rpki)
        
        RPKI is started, and the RPKI view is displayed.
     3. Run [**session**](cmdqueryname=session) *ipv6-address*
        
        An IPv6 address is specified for a TCP connection to be set up between the device and the RPKI server.
     4. Run [**tcp**](cmdqueryname=tcp+port+password+md5+keychain) **port** *port-number* [ **password md5** *cipher-password* | **keychain***keychain-name* ]
        
        Parameters are configured for the TCP connection between the local device and the RPKI server.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
        
        The MD5 algorithm is not recommended if high security is required.
        
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + It is recommended that the new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
        + For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password.
     5. (Optional) Run [**timer**](cmdqueryname=timer+aging+refresh) { **aging** *aging-time* | **refresh** *refresh-time* }
        
        RPKI session timers are configured.
        
        The *aging-time* parameter specifies a value of the validation data age timer, and the *refresh-time* parameter specifies a value of the session update timer. You can configure the timers based on actual requirements on BGP4+ security. Small values are recommended if high BGP4+ security is required. However, frequent data updates consume much network bandwidth.
     6. (Optional) Run [**rpki-limit**](cmdqueryname=rpki-limit+alert-only+idle-forever+idle-timeout) *limit* [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
        
        The maximum number of ROA entries that the device is allowed to accept in a session is configured.
        
        In most cases, a large number of ROA entries exist on a server. If the device receives a large number of ROA entries from the server, excessive system resources will be consumed. To prevent this problem, run the [**rpki-limit**](cmdqueryname=rpki-limit) command to configure the maximum number of ROA entries that the BGP4+ device is allowed to accept in a session.
     7. (Optional) Run [**connect-interface**](cmdqueryname=connect-interface) { *interface-name* | *ipv6-source-address* | *interface-type* *interface-number* | *interface-type* *ipv6-source-address* | *interface-type* *interface-number* *ipv6-source-address* }
        
        The source interface for sending RPKI packets is specified.
     8. (Optional) Run [**ssl-policy**](cmdqueryname=ssl-policy) *policy-name*
        
        An SSL policy to be bound to the TCP connection between the device and RPKI server is configured.
     9. Run [**quit**](cmdqueryname=quit)
        
        Exit the RPKI session view.
     10. Run [**quit**](cmdqueryname=quit)
         
         Exit the RPKI view.
     11. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If configurations of an RPKI session are changed and you want its new configurations to take effect immediately, run the [**reset rpki session**](cmdqueryname=reset+rpki+session) command to reset the RPKI session.
   * If a static ROA database needs to be configured on the local device, perform the following operations:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**rpki**](cmdqueryname=rpki)
        
        RPKI is started, and the RPKI view is displayed.
     3. Run [**origin-validation**](cmdqueryname=origin-validation)
        
        A static ROA database is created, and the RPKI origin-validation view is displayed.
     4. Run [**static record**](cmdqueryname=static+record+max-length+origin-as) *ipv6-address* *ipv6-mask-length* **max-length** *ipv6-max-mask-length* **origin-as** *as-number*
        
        A record is configured for the static ROA database.
     5. Run [**quit**](cmdqueryname=quit)
        
        The RPKI view is displayed.
     6. Run [**quit**](cmdqueryname=quit)
        
        The system view is displayed.
     7. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Configure inbound or outbound ROA validation as required.
   
   
   * To configure inbound ROA validation (validation results not affecting route acceptance) for the routes received from an EBGP peer, perform the following operations:
     1. Run [**prefix origin-validation enable**](cmdqueryname=prefix+origin-validation+enable)
        
        Origin AS validation of RPKI is enabled. After origin AS validation is enabled, the device matches the origin AS of each received route against the origin AS data in the database and provides the validation result, which can be Valid, Not Found, or Invalid.
     2. (Optional) Run [**bestroute origin-as-validation**](cmdqueryname=bestroute+origin-as-validation+allow-invalid) [ **allow-invalid** ]
        
        The device is configured to apply origin AS validation results of RPKI to BGP4+ route selection.
        
        BGP4+ selects routes in descending order of Valid, Not Found, and Invalid after origin AS validation results are applied to route selection. If **allow-invalid** is not specified in the command, the BGP4+ routes with the validation result being Invalid do not participate in route selection.
     3. (Optional) Run [**peer**](cmdqueryname=peer+advertise-ext-community) { *ipv6-address* | *group-name* } **advertise-ext-community**
        
        The device is configured to advertise extended community attributes to the specified peer.
     4. (Optional) Run [**peer**](cmdqueryname=peer+advertise+origin-as-validation) { *ipv6-address* | *group-name* } **advertise origin-as-validation**
        
        The device is enabled to advertise BGP4+ origin AS validation results of RPKI to the specified peer or peer group.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        BGP4+ origin AS validation results of RPKI can be advertised only to IBGP peers.
   * To configure outbound ROA validation for the routes to be advertised to an EBGP peer to control route advertisement, perform the following operations:
     
     Run [**peer**](cmdqueryname=peer+origin-validation+export+include-not-found+external) { *peerIpv6Addr* | *peerGroupName* } **origin-validation export** [ **include-not-found** [ **external** ] ]
     
     The local device is configured to perform outbound ROA validation on the routes to be advertised to the specified EBGP peer.
     
     After the local device is configured to perform outbound ROA validation on the routes to be advertised to a specified EBGP peer, the device matches the origin ASs of the routes against those of the matched routes recorded in the database. The validation result can be Valid, Not Found, or Invalid. By default, only the routes whose validation result is Valid are advertised. To configure the device to advertise the routes with the validation result being Valid or Not Found, specify the **include-not-found** keyword in the preceding command. To configure the device to advertise the routes with the validation result being Valid or Not Found (if the routes with the result being Not Found were received from another AS), specify the **include-not-found external** keyword in the preceding command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display rpki session**](cmdqueryname=display+rpki+session+verbose) *ipv6-address* **verbose** command to check RPKI session configurations.
* Run the [**display rpki table**](cmdqueryname=display+rpki+table) command to check ROA information.