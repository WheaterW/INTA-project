Configuring the TWAMP Light Controller
======================================

The TWAMP Light Controller integrates the Control-Client and Session-Sender functions in the standard model. The TWAMP Light Control-Client establishes, starts, and stops a test session. The TWAMP Light Session-Sender starts performance tests and sends test packets to the Responder, or stops performance tests.

#### Procedure

1. Configure a TWAMP Light Control-Client and create a test session.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**nqa twamp-light**](cmdqueryname=nqa+twamp-light)
      
      
      
      The TWAMP Light view is displayed.
   3. Run [**client**](cmdqueryname=client)
      
      
      
      The TWAMP Light Control-Client function is enabled, and its view is displayed.
   4. Create a test session on the Controller:
      
      
      * To create a test session in Eth-Trunk member interface-based test scenarios, run the [**test-session**](cmdqueryname=test-session) *session-id* { **sender-ip** *sender-ip-address* **reflector-ip** *reflector-ip-address* | [**sender-ipv6**](cmdqueryname=sender-ipv6) *sender-address-v6* [**reflector-ipv6**](cmdqueryname=reflector-ipv6) *reflector-address-v6* } **sender-port** *sender-port* **reflector-port** *reflector-port* [ **vpn-instance** *vpn-instance-name* ] **link-bundle-interface** { *link-bundle-interface-type* *link-bundle-interface-number* | *link-bundle-interface-name* } [ **dscp** *dscp-value* | **padding** *padding-length* | **padding-type** *padding-type* | **description** *description* ] \* command.
      * To create a session in other test scenarios, run the [**test-session**](cmdqueryname=test-session) *session-id* { **sender-ip** *sender-ip-address* **reflector-ip** *reflector-ip-address* | [**sender-ipv6**](cmdqueryname=sender-ipv6) *sender-address-v6* [**reflector-ipv6**](cmdqueryname=reflector-ipv6) *reflector-address-v6* } **sender-port** *sender-port* **reflector-port** *reflector-port* [ **vpn-instance** *vpn-instance-name* ] [ [ [ **dscp** *dscp-value* | **padding** *padding-length* | **padding-type** *padding-type* | **description** *description* ] \* command.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * After a test session is configured, its parameters cannot be modified. To modify parameters of a test session, delete the session and reconfigure it.
      * The IP address configured for a test session must be a unicast address.
      * The UDP port number of the Controller must be a port number not in use.
      * The VPN instance configured for a TWAMP Light test session must exist. This instance cannot be deleted after it is bound to a test session (the system displays a prompt if an attempt is made to delete the VPN instance).
      * To collect statistics of packets with multiple priorities in a single session, you can specify different UDP port numbers for the Session-Sender. For example:
        + Session 1: [**test-session**](cmdqueryname=test-session) 1 **sender-ip** 1.1.1.1 **reflector-ip** 2.2.2.2 **sender-port** 1025 **reflector-port** 1025 **dscp** 3
        + Session 2: [**test-session**](cmdqueryname=test-session) 2 **sender-ip** 1.1.1.1 **reflector-ip** 2.2.2.2 **sender-port** 1026 **reflector-port** 1025 **dscp** 6![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          When configuring a TWAMP Light client to send IPv6 packets, ensure that the length of the IPv6 packets to be sent is smaller than the smallest MTU configured on interfaces along the path. Otherwise, packets are discarded.
          
          Before the configuration, perform the ping test. Ensure that the source address, destination address, and packet length of the ping packet are the same as those of the TWAMP Light IPv6 packet. Then run the [**display ipv6 pathmtu**](cmdqueryname=display+ipv6+pathmtu) command to check the **PMTU** value of each interface along the path. For details, see [Path MTU Test](feature_0029040638.html).
   5. (Optional) Run [**test-session**](cmdqueryname=test-session) *session-id* [**ptp-compatible enable**](cmdqueryname=ptp-compatible+enable)
      
      
      
      The PTP compatible mode is enabled for the TWAMP Light test session.
      
      
      
      In the scenario where a Huawei device interworks with a non-Huawei device, if the non-Huawei device uses a PTP server as the clock source but the Huawei device uses an NTP server as the clock source, you can run this command to enable the PTP compatible mode on the Huawei device. This prevents inaccurate measurement data caused by asynchronous clocks (different primary reference clocks).
   6. (Optional) Run [**test-session**](cmdqueryname=test-session) *session-id* **bind interface** { *interface-type* *interface-number* | *interface-name* }
      
      
      
      An interface is bound to a TWAMP Light test session.
      
      
      
      After an interface is bound to a TWAMP Light test session, valid statistics are reported to the bound interface. Other functional modules can obtain the statistics from this interface.
2. Configure the TWAMP Light Session-Sender and start the TWAMP Light performance test.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**nqa twamp-light**](cmdqueryname=nqa+twamp-light)
      
      
      
      The TWAMP Light view is displayed.
   3. (Optional) Run [**one-way delay-measure enable**](cmdqueryname=one-way+delay-measure+enable)
      
      
      
      TWAMP Light one-way delay measurement is enabled.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Before configuring TWAMP Light one-way delay measurement, ensure that devices on the network have achieved PTP clock synchronization.
   4. Run [**sender**](cmdqueryname=sender)
      
      
      
      The TWAMP Light Session-Sender function is enabled, and its view is displayed.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   6. Start TWAMP Light performance measurement:
      
      
      * To perform one-off performance measurement, run the [**test start**](cmdqueryname=test+start) **test-session** *session-id* { **duration** *duration* | **packet-count** *packet-count* } [ **period** { **10** | **100** | **1000** | **30000** } ] [ **time-out** *time-out* ] command.
      * To perform continuous performance measurement, run the [**test start-continual**](cmdqueryname=test+start-continual) **test-session** *session-id* [ **period** { **10** | **100** | **1000** | **30000** } ] [ **time-out** *time-out* ] command.
      * To perform continuous performance measurement periodically, run the [**test start-regular**](cmdqueryname=test+start-regular) **test-session** *session-id* [ **regular-time** *timevalue* ] [ **packet-count** *packet-count* ] [ **time-out** *time-out* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Statistics collection automatically stops when the specified interval is reached or the specified number of sent packets is reached. You can also run the [**test stop**](cmdqueryname=test+stop) { **all** | **test-session** *session-id* } command to stop statistics collection.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.