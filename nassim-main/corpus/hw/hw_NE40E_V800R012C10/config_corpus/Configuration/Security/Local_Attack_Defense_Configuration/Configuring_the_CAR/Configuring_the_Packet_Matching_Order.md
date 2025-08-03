Configuring the Packet Matching Order
=====================================

After the packets to be sent to the CPU pass the GTSM check, set the matching sequence of packets: TCPSYN packets, packet fragments, dynamic link protection, whitelist, blacklist, and user-defined flow.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run **process-sequence** { **fragment-flood** | **tcpsyn-flood** | **dynamic-link-protection** | **whitelist** | **blacklist** | **user-defined-flow** | **management-acl** } &<7-7> or **process-sequence** { **blacklist** **whitelist** **user-defined-flow** | **blacklist** **user-defined-flow** **whitelist** | **user-defined-flow** **blacklist** **whitelist** | **user-defined-flow** **whitelist** **blacklist** | **whitelist** **blacklist** **user-defined-flow** | **whitelist** **user-defined-flow** **blacklist** } \*
   
   
   
   The matching sequence of packets to be sent to the CPU is set: TCPSYN packets, packet fragments, dynamic link protection, management protocol ACL, whitelist, blacklist, and user-defined flow.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The parameters in the command are mandatory. You can specify them as required.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.