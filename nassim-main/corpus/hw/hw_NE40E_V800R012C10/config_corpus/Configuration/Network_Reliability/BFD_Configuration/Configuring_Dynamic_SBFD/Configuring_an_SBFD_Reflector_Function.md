Configuring an SBFD Reflector Function
======================================

This section describes how to configure a Seamless Bidirectional Forwarding Detection (SBFD) reflector function. An SBFD reflector can work with an initiator to quickly detect link faults.

#### Usage Scenario

SBFD is a simplified BFD mechanism, which involves an initiator and reflector.

* The initiator provides an SBFD state machine and detection mechanism to protect services.
* The reflector loops back SBFD packets sent by the initiator without providing an SBFD state machine or detection mechanism or associating with services.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**sbfd**](cmdqueryname=sbfd)
   
   
   
   SBFD is enabled.
5. Run [**reflector discriminator**](cmdqueryname=reflector+discriminator) { *unsigned-integer-value* | *ip-address-value* }
   
   
   
   A discriminator is configured for the SBFD reflector.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.