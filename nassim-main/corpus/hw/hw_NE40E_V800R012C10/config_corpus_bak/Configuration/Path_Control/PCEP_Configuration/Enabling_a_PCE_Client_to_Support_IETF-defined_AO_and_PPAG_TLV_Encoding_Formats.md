Enabling a PCE Client to Support IETF-defined AO and PPAG TLV Encoding Formats
==============================================================================

To facilitate interoperability tests, enable a PCE client to support IETF-defined Association Object (AO) and Path Protection Association Group (PPAG) TLV encoding formats.

#### Context

This function is mainly used in interoperability test scenarios. Devices can parse the AO and PPAG encoding formats defined in both RFC 8745 and RFC 8697 as well as those in the IETF draft. By default, devices use the encoding formats defined in the draft. You can adjust the encoding formats according to those used on the peer device.

If the peer controller or tester uses the formats defined in RFC 8745 and RFC 8697, enable the local device to use the RFC-defined AO and PPAG encoding formats by running the [**ppag standard enable**](cmdqueryname=ppag+standard+enable) command. The devices then can communicate with each other. If you do not run this command, the peer device cannot parse the PCRpt messages sent by the local device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The PCE client view is displayed.
3. Run [**ppag standard enable**](cmdqueryname=ppag+standard+enable)
   
   
   
   The PCE client is enabled to use the AO and PPAG TLV encoding formats defined in RFC 8697 and RFC 8745 in packets to be sent over a PCEP session.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.