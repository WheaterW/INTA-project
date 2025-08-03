Creating a Dot1x Template
=========================

When 802.1X authentication is used, an authentication server and 802.1X client perform authentication negotiation based on parameters defined in a dot1x template.

#### Context

After a dot1x template is created, configure parameters for the dot1x template:

* Run the [**eap-end**](cmdqueryname=eap-end) command to specify the authentication method for 802.1X users using the dot1x template. Choose EAP termination mode or EAP relay mode as required.
* Run the [**authentication timeout**](cmdqueryname=authentication+timeout) command in the template view to set the timeout period for the BRAS to wait for an EAP Response packet from the authentication server. If the BRAS does not receive an EAP Response packet from the authentication server within a specified timeout period, the BRAS considers that a user goes offline and logs out the user.
* During 802.1X authentication, the BRAS sends an EAP-Request/Identity packet to the client. If you want the BRAS to retransmit the packet when the client does not respond, run the [**request**](cmdqueryname=request) command to set the timeout period for the BRAS to wait for an EAP-Response/Identity packet from the client and the number of retransmissions of EAP-Request/Identity packets. If the client does not respond with an EAP-Response/Identity packet within the timeout period and after packet retransmissions reach the specified number, the user is logged out.
* If users go online through 802.1X authentication, run the [**reauthentication interval**](cmdqueryname=reauthentication+interval) command to set the interval for the BRAS to send re-authentication request packets. If re-authentication fails, the users are logged out to ensure that only authorized users can access the network.
* In some cases, accounting continues after 802.1X users go offline. To resolve such issues, run the [**keepalive**](cmdqueryname=keepalive) command to set the number of and timeout period for handshake packet retransmissions between the EAP client and server. If the client does not respond within the timeout period and after handshake packet retransmissions reach the specified number, the user is logged out.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dot1x-template**](cmdqueryname=dot1x-template) *dot1x-template-number*
   
   
   
   A dot1x template is created and the dot1x template view is displayed.
   
   
   
   Dot1x templates are identified by numbers. The Router has a default dot1x template numbered 1. This template can be modified but cannot be deleted.
3. (Optional) Run [**eap-end**](cmdqueryname=eap-end) [ [**chap**](cmdqueryname=chap) | [**pap**](cmdqueryname=pap) ]
   
   
   
   The EAP authentication method is set for 802.1X users.
4. (Optional) Run [**authentication timeout**](cmdqueryname=authentication+timeout) *time*
   
   
   
   The timeout period for the BRAS to wait for an EAP Response packet from the authentication server is set.
5. (Optional) Run [**request**](cmdqueryname=request) { [**interval**](cmdqueryname=interval) *time* | [**retransmit**](cmdqueryname=retransmit) *times* } \*
   
   
   
   The timeout period for the BRAS to wait for an EAP-Response/Identity packet from the client and the number of retransmissions of EAP-Request/Identity packets is set.
6. (Optional) Run [**reauthentication interval**](cmdqueryname=reauthentication+interval) *time*
   
   
   
   The interval for the BRAS to send re-authentication request packets is set.
7. (Optional) Run [**keepalive**](cmdqueryname=keepalive) { [**interval**](cmdqueryname=interval) *time* | [**retransmit**](cmdqueryname=retransmit) *times* } \*
   
   
   
   The number of and timeout period for handshake packet retransmissions between the EAP client and server is set.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.