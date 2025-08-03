Configuring ROA
===============

Resource Public Key Infrastructure (RPKI) can validate the origin of BGP routes, ensuring BGP security. Using RPKI, Route Origin Authorization (ROA) can validate and filter routes.

#### Usage Scenario

To solve the problem of BGP route hijacking, the industry proposes the RPKI solution that validates the origin ASs of BGP routes. Distributed RPKI servers are used to collect information such as the origin AS numbers, route prefixes, and masks of BGP routes initiated by each ISP. After a device sets up a connection with an RPKI cache server, the device saves a copy of ROA data locally. If no RPKI server is available, static ROA data can be configured on a device. Inbound ROA validation, which applies to the BGP routes received from peers, can be configured to control route selection. In addition, outbound ROA validation, which applies to the BGP routes to be advertised to peers, can be configured to control route advertisement. ROA validation ensures that hosts in an AS can securely access external services.


#### Pre-configuration Tasks

Before configuring ROA, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).

#### Procedure

1. Select one of the following configurations based on the usage scenario:
   
   
   * If the local device needs to obtain data from the ROA database through a connection to be established with an RPKI server, perform the following operations:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**rpki**](cmdqueryname=rpki)
        
        RPKI is started, and the RPKI view is displayed.
     3. Run [**session**](cmdqueryname=session) *ipv4-address*
        
        An address of the RPKI server is specified for a TCP connection to be set up between the device and the RPKI server.
     4. Run [**tcp**](cmdqueryname=tcp+port+password+md5+keychain) **port** *port-number* [ **password md5** *cipher-password* | **keychain***keychain-name* ]
        
        Parameters are configured for the TCP connection between the local device and the RPKI server.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
        
        The MD5 algorithm is not recommended if high security is required.
        
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + It is recommended that the new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
        + For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password.
     5. (Optional) Run [**timer**](cmdqueryname=timer+aging+refresh) { **aging** *aging-time* | **refresh** *refresh-time* }
        
        Timers are configured for the RPKI session.
        
        The *aging-time* parameter specifies a value of the validation data age timer, and the *refresh-time* parameter specifies a value of the session update timer. You can configure the timers based on actual requirements on BGP security. Small values are recommended if high BGP security is required. However, frequent data updates consume much network bandwidth.
     6. (Optional) Run [**rpki-limit**](cmdqueryname=rpki-limit+alert-only+idle-forever+idle-timeout) *limit* [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
        
        The maximum number of ROA entries that the device is allowed to accept in a session is configured.
        
        In most cases, a large number of ROA entries exist on an RPKI server. If the device receives a large number of ROA entries from the RPKI server, excessive system resources will be consumed. To prevent this problem, run the [**rpki-limit**](cmdqueryname=rpki-limit) command to configure the maximum number of ROA entries that the BGP device is allowed to accept in a session.
     7. (Optional) Run [**connect-interface**](cmdqueryname=connect-interface) { *interface-name* | *ipv4-source-address* | *interface-type* *interface-number* | *interface-type* *ipv4-source-address* | *interface-type* *interface-number* *ipv4-source-address* }
        
        The source interface for sending RPKI messages is specified.
     8. (Optional) Run [**ssl-policy**](cmdqueryname=ssl-policy) *policy-name*
        
        An SSL policy to be bound to the TCP connection between the device and RPKI server is configured.
     9. Run [**quit**](cmdqueryname=quit)
        
        The RPKI view is displayed.
     10. Run [**quit**](cmdqueryname=quit)
         
         The system view is displayed.
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
     4. Run [**static record**](cmdqueryname=static+record+max-length+origin-as) *ipv4-address* *mask-length* **max-length** *max-mask-length* **origin-as** *as-number*
        
        A record is configured for the static ROA database.
     5. Run [**quit**](cmdqueryname=quit)
        
        The RPKI view is displayed.
     6. Run [**quit**](cmdqueryname=quit)
        
        The system view is displayed.
     7. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Configure inbound or outbound ROA validation as required.
   
   
   * To configure inbound ROA validation (validation results not affecting route acceptance) for the routes received from an EBGP peer, perform the following operations:
     1. Run [**prefix origin-validation enable**](cmdqueryname=prefix+origin-validation+enable)
        
        Origin AS validation of RPKI is enabled.
        
        After origin AS validation is enabled, the device matches the origin AS of each received route against the origin AS data in the database and provides the validation result, which can be Valid, Not Found, or Invalid.
     2. (Optional) Run [**bestroute origin-as-validation**](cmdqueryname=bestroute+origin-as-validation+allow-invalid) [ **allow-invalid** ]
        
        The device is configured to apply origin AS validation results of RPKI to BGP route selection.
        
        BGP selects routes in descending order of Valid, Not Found, and Invalid after origin AS validation results are applied to route selection. If **allow-invalid** is not specified in the command, the BGP routes with the validation result being Invalid do not participate in route selection.
     3. (Optional) Run [**peer**](cmdqueryname=peer+advertise-ext-community) { *ipv4-address* | *group-name* } **advertise-ext-community**
        
        The device is configured to advertise extended community attributes to the specified peer.
     4. (Optional) Run [**peer**](cmdqueryname=peer+advertise+origin-as-validation) { *ipv4-address* | *group-name* } **advertise origin-as-validation**
        
        The device is enabled to advertise origin AS validation results of RPKI to the specified BGP peer or peer group.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        Origin AS validation results of RPKI can be advertised only to IBGP peers.
   * To configure outbound ROA validation for the routes to be advertised to an EBGP peer to control route advertisement, perform the following operations:
     
     Run [**peer**](cmdqueryname=peer+origin-validation+export+include-not-found+external) { *peerIpv4Addr* | *peerGroupName* } **origin-validation export** [ **include-not-found** [ **external** ] ]
     
     The local device is configured to perform outbound ROA validation on the routes to be advertised to the specified EBGP peer.
     
     After the local device is configured to perform outbound ROA validation on the routes to be advertised to a specified EBGP peer, the device matches the origin ASs of the routes against those of the matched routes recorded in the database. The validation result can be Valid, Not Found, or Invalid. By default, only the routes whose validation result is Valid are advertised. To configure the device to advertise the routes with the validation result being Valid or Not Found, specify the **include-not-found** keyword in the preceding command. To configure the device to advertise the routes with the validation result being Valid or Not Found (if the routes with the result being Not Found were received from another AS), specify the **include-not-found external** keyword in the preceding command.
4. (Optional) Run [**prefix origin-validation local-origin-as**](cmdqueryname=prefix+origin-validation+local-origin-as)
   
   
   
   The device is configured to use the locally configured AS number to validate routes when the AS\_Path attributes of the routes are empty.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the locally configured AS number is used for route validation, origin AS validation of RPKI needs to be enabled to validate routes from all origins using the [**prefix origin-validation all enable**](cmdqueryname=prefix+origin-validation+enable) command. Such validation applies only to routes received from IBGP peers, routes imported by the local instance, and summary routes.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display rpki session**](cmdqueryname=display+rpki+session+verbose) *ipv4-address* **verbose** command to check RPKI session configurations.
* Run the [**display rpki table**](cmdqueryname=display+rpki+table) command to check ROA information.