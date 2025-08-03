Adjusting C-BSR Parameters
==========================

At first, each Candidate-BootStrap Router (C-BSR) considers itself as a BSR and sends a Bootstrap message to all other Routers on the network. You can adjust the C-BSR hash mask length and Candidate-Rendezvous Point (C-RP) priority information carried by a Bootstrap message, interval for sending Bootstrap messages, and timeout period of a Bootstrap message on the Router configured as a C-BSR.

#### Context

BSR election rules are as follows:

* The C-BSR that has the highest priority wins.
* If C-BSRs have the same priority, the C-BSR that has the highest IP address wins.

Based on the BSR election result, a C-BSR performs the following operations:

* If the C-BSR wins the BSR election, it periodically sends Bootstrap messages to the network on which the C-BSR resides. The Bootstrap messages carry the IP addresses of the C-BSRs and the RP-Set information.
* If the C-BSR fails in the BSR election, it is suppressed from sending Bootstrap messages.
* When the current BSR becomes faulty, the C-BSRs automatically trigger a new round of BSR election to prevent service interruptions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
3. Run [**c-bsr hash-length**](cmdqueryname=c-bsr+hash-length) *hash-length*
   
   
   
   The global hash mask length is set for a C-BSR.
   
   The hash mask length carried by a Bootstrap message is used for RP calculation.
4. Run [**c-bsr priority**](cmdqueryname=c-bsr+priority) *priority*
   
   
   
   The global priority is set for a C-BSR.
   
   A larger *priority* value indicates a higher priority.
5. Run [**c-bsr interval**](cmdqueryname=c-bsr+interval) *interval*
   
   
   
   The interval at which a C-BSR sends Bootstrap messages is set.
6. Run [**c-bsr holdtime**](cmdqueryname=c-bsr+holdtime) *interval*
   
   
   
   The period during which the Router keeps the Bootstrap message received from a BSR is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The period during which the Router holds the Bootstrap message received from the BSR must be longer than the interval at which a C-BSR sends Bootstrap messages. Otherwise, BSR election is frequently performed.
   
   The BSR periodically sends Bootstrap messages over the network. After receiving the Bootstrap messages, the Routers hold the messages for a certain period during which the BSR election is suspended. After this period expires, the C-BSRs trigger a new round of BSR election.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.