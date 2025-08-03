Enabling a Device Not to Verify UDP6 Packets with the Checksum Value of 0
=========================================================================

Enabling_a_Device_Not_to_Verify_UDP6_Packets_with_the_Checksum_Value_of_0

#### Context

By default, a receiver verifies the checksum of UDP6 packets. The receiver accepts such packets only if the checksum verification succeeds. If a sender sends such packets with the checksum value fixed at 0, run the [**ipv6 udp zero-checksum ignore**](cmdqueryname=ipv6+udp+zero-checksum+ignore) command on the receiver so that it does not verify these packets, thereby improving network compatibility.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 udp zero-checksum ignore**](cmdqueryname=ipv6+udp+zero-checksum+ignore)
   
   
   
   The device is enabled not to verify UDP6 packets with the checksum value of 0.
   
   
   
   In VS mode, this command is supported only by the admin VS.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.