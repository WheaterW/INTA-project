Creating an 802.1X Template
===========================

When 802.1X authentication is used, the NE40E and 802.1X clients perform authentication negotiation based on the parameters defined in an 802.1X template.

#### Context

To ensure that only authorized 802.1X users can access the network, you need to create an 802.1X template and enter the 802.1X template view. Then, authentication negotiation is performed based on the parameters defined in the 802.1X template to verify the consistency between parameters set by 802.1X users and those defined in the 802.1X template.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dot1x-template**](cmdqueryname=dot1x-template) *dot1x-template-number*
   
   
   
   An 802.1X template is created and the 802.1X template view is displayed.
   
   
   
   802.1X templates are identified by numbers. The NE40E has a default 802.1X template numbered 1. This template can be modified but cannot be deleted.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   All the parameters in the following optional steps have default values on the NE40E. Run corresponding commands to modify the default settings.
3. (Optional) Run [**authentication timeout**](cmdqueryname=authentication+timeout) *time*
   
   
   
   The timeout period of EAP authentication response packets is set.
4. (Optional) Run [**request**](cmdqueryname=request) { **retransmit** *times* | **interval** *time* } \*
   
   
   
   The timeout period and number of retransmission times of Request packets are set.
5. (Optional) Run [**keepalive**](cmdqueryname=keepalive) { **interval** *time* | **retransmit** *times* } \*
   
   
   
   The number of and timeout period for handshake packet retransmissions between the EAP client and server are set.
6. (Optional) Run [**reauthentication interval**](cmdqueryname=reauthentication+interval) *time*
   
   
   
   The interval for reauthentication of online 802.1X template users is set.
7. (Optional) Run [**eap-end**](cmdqueryname=eap-end) [ **chap** | **pap** ]
   
   
   
   The authentication method for EAP termination defined in the 802.1X template is configured.