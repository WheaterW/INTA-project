Configuring the TWAMP Light Responder
=====================================

The TWAMP Light Responder responds to TWAMP test packets sent by the TWAMP Light Controller.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa twamp-light**](cmdqueryname=nqa+twamp-light)
   
   
   
   The TWAMP Light view is displayed.
3. Run [**responder**](cmdqueryname=responder)
   
   
   
   The TWAMP Light Responder is enabled, and its view is displayed.
4. Run either of the following commands to create a test session on the Responder as required.
   
   
   * To create a test session in Eth-Trunk member interface-based test scenarios, run the [**test-session**](cmdqueryname=test-session) *session-id* { **local-ip** *local-ip-address* **remote-ip** *remote-ip-address* | [**local-ipv6**](cmdqueryname=local-ipv6) *local-ipv6-address* [**remote-ipv6**](cmdqueryname=remote-ipv6) *remote-ipv6-address* } **local-port** *local-port* **remote-port** *remote-port* [ **vpn-instance***vpn-instance-name* ] **link-bundle-interface** { *link-bundle-interface-type* *link-bundle-interface-number* | *link-bundle-interface-name* } [ **anti-loop-on** ] [ **description** *description* ] command.
   * To create a test session in other test scenarios, run the [**test-session**](cmdqueryname=test-session) *session-id* { **local-ip** *local-ip-address* **remote-ip** *remote-ip-address* | [**local-ipv6**](cmdqueryname=local-ipv6) *local-ipv6-address* [**remote-ipv6**](cmdqueryname=remote-ipv6) *remote-ipv6-address* } **local-port** *local-port* **remote-port** *remote-port* [ **interface** { *interface-type* *interface-number* | *interface-name* } | **vpn-instance** *vpn-instance-name* ] [ **anti-loop-on** ] [ **description** *description* ] command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * After a test session is configured, its parameters cannot be modified. To modify parameters of a test session, delete the session and reconfigure it.
   * The IP address configured for a test session must be a unicast address.
   * The UDP port number of the Responder must be a port number not in use.
   * The VPN instance configured for a TWAMP Light test session must exist. This instance cannot be deleted after it is bound to a test session (the system displays a prompt if an attempt is made to delete the VPN instance).
   * In Layer 2 and Layer 3 hybrid networking scenarios where the base station is offline, you need to configure static ARP on the Layer 3 virtual interface of the network device that connects Layer 3 to Layer 2.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.