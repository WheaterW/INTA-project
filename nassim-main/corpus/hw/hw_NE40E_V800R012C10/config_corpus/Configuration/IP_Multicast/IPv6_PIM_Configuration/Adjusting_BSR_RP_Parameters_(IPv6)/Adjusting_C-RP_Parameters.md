Adjusting C-RP Parameters
=========================

A Candidate-Rendezvous Point (C-RP) periodically sends BootStrap router (BSR) Advertisement messages that carry the C-RP's priority information. You can adjust the priority of a C-RP, interval for sending Advertisement messages, and timeout period of an Advertisement message sent by a device that has C-RPs configured.

#### Context

RP election rules are as follows:

* The C-RP with the highest priority wins.
* If C-RPs have the same priority, hash functions are started. The C-RP that has the greatest calculated value wins.
* If the preceding rules cannot determine an RP, the C-RP with the highest address wins.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
3. Run [**c-rp priority**](cmdqueryname=c-rp+priority) *priority*
   
   
   
   The global priority is set for a C-RP.
   
   A higher *priority* value indicates a lower priority.
4. Run [**c-rp advertisement-interval**](cmdqueryname=c-rp+advertisement-interval) *interval*
   
   
   
   The interval at which a C-RP sends Advertisement messages is set.
5. Run [**c-rp holdtime**](cmdqueryname=c-rp+holdtime) *interval*
   
   
   
   The period during which a BSR keeps the Advertisement message from a C-RP is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The period during which a BSR keeps the Advertisement message from a C-RP must be longer than the interval at which a C-RP sends Advertisement messages.
   
   C-RPs periodically send Advertisement messages to the current BSR. The BSR extracts **Holdtime** from the messages and starts a timer. If the BSR does not receive any Advertisement message from a C-RP within the timeout period of the timer, the BSR considers the C-RP invalid or inaccessible.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.