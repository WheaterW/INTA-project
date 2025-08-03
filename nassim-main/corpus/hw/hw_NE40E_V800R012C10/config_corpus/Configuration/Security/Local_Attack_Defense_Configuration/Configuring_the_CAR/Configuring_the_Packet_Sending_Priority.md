Configuring the Packet Sending Priority
=======================================

This section describes how to prioritize packets to be sent to the CPU. Sending higher-priority packets preferentially can protect the CPU when the queues are full of packets to be sent to the CPU.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run [**priority**](cmdqueryname=priority+index+whitelist+whitelist-v6+blacklist+tcpsyn+fragment) { *protocol-name* | **index** *index* | **whitelist** | **whitelist-v6** | **blacklist** | **tcpsyn** | **fragment** | **user-defined-flow** *flow-id* } { **high** | **middle** | **low** | **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** | **cs7** }
   
   
   
   The packet sending priority is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.