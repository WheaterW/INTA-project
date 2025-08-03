Configuring ASPA
================

RPKIv2-based ASPA validation verifies the AS\_Path attribute of routes, ensuring BGP4+ security.

#### Usage Scenario

RPKIv0-based ROA validation can detect unexpected path leaks, but it relies on the origin AS in the BGP attribute AS\_Path, which may be manipulated by attackers. As an inter-AS routing security mechanism, RPKIv0 provides only origin validation but not path validation.

ASPA can automatically detect invalid AS\_Paths in routes received from peers based on the customer-to-provider shared signature database constructed through RPKIv2.


#### Pre-configuration Tasks

Before configuring ASPA, complete the following task:

* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).

#### Procedure

1. Select one of the following configurations based on the usage scenario:
   
   
   * If the local device needs to obtain data in the ASPA database through a connection to be established with an RPKI server, perform the following operations:
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**rpki**](cmdqueryname=rpki) command to start RPKI and enter the RPKI view.
     3. Run the [**session**](cmdqueryname=session) *ipv6-address* command to configure session information for the TCP connection between the local device and the RPKI server.
     4. Run the [**tcp**](cmdqueryname=tcp+port+password+md5+keychain) **port** *port-number* [ **password md5** *cipher-password* | **keychain***keychain-name* ] command to configure parameters for the TCP connection between the local device and the RPKI server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
        
        The MD5 algorithm is not recommended if high security is required.
        
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + It is recommended that the new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
        + For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password.
     5. Run the **[**version**](cmdqueryname=version)** **version-num** command to configure an RPKI version. RPKIv2 allows a device to receive ASPA data on the condition that both the device and the RPKI server support RPKIv2.
     6. (Optional) Run the [**timer**](cmdqueryname=timer+aging+refresh) { **aging** *aging-time* | **refresh** *refresh-time* } command to configure timers for the RPKI session.
        
        The *aging-time* parameter specifies a value of the validation data aging timer, and the *refresh-time* parameter specifies a value of the session update timer. You can configure the timers based on actual requirements on BGP4+ security. Small values are recommended if high BGP4+ security is required. However, frequent data updates consume much network bandwidth.
     7. (Optional) Run the **[**aspa-limit**](cmdqueryname=aspa-limit)** **limit** [ **percentage** ] [ **alert-only** | ****idle-forever**** | ****idle-timeout**** **times** ] command to configure the maximum number of ASPA pairs that the device is allowed to accept in the session.
        
        In most cases, a large number of ASPA pairs exist on a server. If a BGP4+ device receives a large number of ASPA pairs from the server, excessive system resources will be consumed. To prevent this problem, run the **aspa-limit** command to configure the maximum number of ASPA pairs that the device is allowed to accept in the session.
     8. (Optional) Run the [**connect-interface**](cmdqueryname=connect-interface) { *interface-name* | *ipv4-source-address* | *interface-type* *interface-number* | *interface-type* *ipv4-source-address* | *interface-type* *interface-number* *ipv4-source-address* } command to specify the source interface for sending RPKI messages.
     9. (Optional) Run the [**ssl-policy**](cmdqueryname=ssl-policy) *policy-name* command to configure an SSL policy to be bound to the TCP connection between the device and the RPKI server.
     10. Run the [**quit**](cmdqueryname=quit) command to enter the RPKI view.
     11. Run the [**quit**](cmdqueryname=quit) command to enter the system view.
     12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If configurations of an RPKI session are changed and you want its new configurations to take effect immediately, run the [**reset rpki session**](cmdqueryname=reset+rpki+session) command to reset the RPKI session.
   * If a static ASPA database needs to be configured on the local device, perform the following operations:
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**rpki**](cmdqueryname=rpki) command to start RPKI and enter the RPKI view.
     3. Run the [**aspa-validation**](cmdqueryname=aspa-validation) command to create a static ASPA database and enter the RPKI ASPA-validation view.
     4. Run the **[**static record**](cmdqueryname=static+record)** **customer-as** ****provider**** **as-number**{ ****ipv4**** | ****ipv6**** } command to configure a static ASPA database.
     5. Run the [**quit**](cmdqueryname=quit) command to enter the RPKI view.
     6. Run the [**quit**](cmdqueryname=quit) command to enter the system view.
     7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
3. Configure inbound ASPA validation as required. To configure inbound ASPA validation (validation results not affecting route acceptance) for the routes received from an EBGP peer, perform the following operations:
   
   
   1. Run the **[**peer**](cmdqueryname=peer+role)** { **peerIpv4Addr** | **peerIpv6Addr** } **[**role**](cmdqueryname=peer+role)** { ****provider**** | ****rs**** | ****rs-client**** | ****customer**** | ****lateral-peer**** | ****sibling**** } command to configure a role for a BGP4+ peer.
   2. Run the [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast** command to enter the IPv6 unicast address family view.
   3. Run the **[**aspa-validation enable**](cmdqueryname=aspa-validation+enable)** command to enable RPKI-based ASPA validation. After ASPA validation is enabled, the device compares the AS\_Path of a route with the matching ASPA pair recorded in the database and provides the validation results: Valid, NotFound, or Invalid.
   4. (Optional) Run the [**bestroute aspa-validation**](cmdqueryname=bestroute+aspa-validation+allow-invalid) [ **allow-invalid** ] command to configure the device to apply ASPA validation results of RPKI to BGP4+ route selection. BGP selects routes in descending order of Valid, Not Found, and Invalid after ASPA validation results are applied to route selection. If **allow-invalid** is not specified in the command, the BGP routes with the validation result being Invalid do not participate in route selection.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display rpki aspa**](cmdqueryname=display+rpki+aspa) *ipv6* [**table**](cmdqueryname=table) command to check ASPA-related data.