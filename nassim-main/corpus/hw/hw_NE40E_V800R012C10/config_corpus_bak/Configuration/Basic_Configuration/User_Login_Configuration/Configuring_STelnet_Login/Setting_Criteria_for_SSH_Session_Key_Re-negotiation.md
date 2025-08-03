Setting Criteria for SSH Session Key Re-negotiation
===================================================

Setting_Criteria_for_SSH_Session_Key_Re-negotiation

#### Context

When an SSH session meets one or more of the following criteria, the system re-negotiates a key and uses the new key to establish SSH session connections, improving system security.

* The number of interaction packets meets the configured key re-negotiation criterion.
* The accumulated packet data volume meets the configured key re-negotiation criterion.
* The session duration meets the configured key re-negotiation criterion.
* This command can be run on an IPv4 or IPv6 SSH client.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

A key re-negotiation request is initiated when either the SSH client or server meets the key re-negotiation criteria, and the other party responds.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Choose either of the following commands based on the SSH service type to configure criteria that trigger key re-negotiation.
   1. Run [**ssh client rekey**](cmdqueryname=ssh+client+rekey) { **data-limit** *data-limit* | **max-patchet** *max-packet* | **time** *minutes* } \*
      
      
      
      Parameters are configured for SSH client key re-negotiation.
   2. Run [**ssh server rekey**](cmdqueryname=ssh+server+rekey) { **data-limit** *data-limit* | **max-patchet** *max-packet* | **time** *minutes* } \*
      
      
      
      Parameters are configured for SSH server key re-negotiation.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

* Run the [**display ssh client**](cmdqueryname=display+ssh+client) **session** command to check the number of packets sent and received, data volume of packets sent and received, and online duration of the online session after SSH client key re-negotiation.