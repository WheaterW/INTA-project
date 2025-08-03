(Optional) Configuring RADIUS CAR
=================================

(Optional) Configuring RADIUS CAR

#### Context

By default, RADIUS packets are sent to the CPU of a device through the CPCAR channel. If a packet is valid (the Authenticator field value is correct and authentication or accounting has been successfully performed), the device adds the source and destination IP addresses and port number carried in the packet to a whitelist. If the source and destination IP addresses and port number of subsequently received packets match those in the whitelist, the packets are sent to the CPU through the whitelist channel. If the device does not receive packets from the same server or device within 1 hour after a whitelist entry is generated, the entry ages out. When passing through the whitelist channel, packets pass through the following CAR channels in sequence: RADIUS whitelist session-CAR channel, RADIUS whitelist CAR channel, and total CAR channel. Passing through the RADIUS whitelist session-CAR channel is optional.

Adjust bandwidth parameters if the defaults do not meet service requirements.

In RADIUS proxy authentication, you need to comprehensively consider the following factors when estimating the RADIUS whitelist bandwidth:

* Suppression threshold for the number of active RADIUS proxy sessions. It can be configured using the [**access-speed adjustment system-state radius-proxy active-session threshold**](cmdqueryname=access-speed+adjustment+system-state+radius-proxy+active-session+threshold) command. The default value is 250.
* Load balancing mode for user-to-network traffic and forwarding mode for network-to-user traffic. User-to-network RADIUS packets can be load balanced among multiple interface boards for processing. However, RADIUS packets sent from a RADIUS server to a BRAS cannot be load balanced among multiple interface boards. Instead, they are processed only on one interface board. As such, you are advised to use different interface boards for user-to-network RADIUS packets and network-to-user RADIUS packets. For example, a BRAS has three interface boards: boards 3, 4, and 5. Board 3 and 4 load balance user-to-network RADIUS packets, and board 5 processes network-to-user RADIUS packets.
* Number of RADIUS packets that the BRAS needs to process each time a user goes online. Assume that an 802.1X user requests to go online. During authentication, the BRAS needs to interact with the RADIUS server 22 times. The AC sends 11 Access-Request packets to the BRAS, and the RADIUS server sends 10 Access-Challenge packets and one Access-Accept packet to the BRAS.
* User access rate. Assume that the default suppression threshold for the number of active RADIUS proxy sessions (250) is used. If it takes 1s for each user to go online, the BRAS processes access for 250 users per second. If it takes 100 ms for each user to go online, the BRAS processes access for 2500 users per second.

Assume that a BRAS has three interface boards: boards 3, 4, and 5. User-to-network RADIUS packets are load balanced among two interface boards (boards 3 and 4). RADIUS packets sent from a RADIUS server to a BRAS are processed on board 5. The suppression threshold for the number of active RADIUS proxy sessions is 250. It takes 1s for each user to go online.

Each of the boards in slots 3 and 4 processes user-to-network RADIUS packets of 125 users per second.

CIR of board 3 and board 4 = 125 active sessions per second x 11 packets x 128 bytes x 8 = 1,408,000 bits per second = 1408 kbps

CBS of board 3 and board 4 = 125 active sessions x 11 packets x 128 bytes = 176,000 bytes

Board 5 processes network-to-user RADIUS packets of 250 users per second.

CIR of board 5 = 250 active sessions per second x 11 packets x 128 bytes x 8 = 2,816,000 bits per second = 2816 kbps

CBS of board 5 = 250 active sessions x 11 packets x 128 bytes = 352,000 bytes

After the RADIUS whitelist bandwidth is changed, the total CAR bandwidth needs to be adjusted accordingly.


#### Procedure

* Configure whitelist session-CAR for RADIUS.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**whitelist session-car radius**](cmdqueryname=whitelist+session-car+radius) { **cir** *cir-value* | **pir** *pir-value* | **cbs** *cbs-value* | **pbs** pbs-value } \*
     
     
     
     Whitelist session-CAR parameters are configured for RADIUS.
  3. (Optional) Run [**whitelist session-car radius disable**](cmdqueryname=whitelist+session-car+radius+disable)
     
     
     
     Whitelist session-CAR is disabled for RADIUS.
     
     
     
     Whitelist session-CAR can be disabled for RADIUS only when this function is abnormal. Under normal circumstances, enabling whitelist session-CAR for RADIUS is recommended.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure whitelist CAR for RADIUS.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
     
     
     
     An attack defense policy is configured.
  3. Run [**car whitelist radius**](cmdqueryname=car+whitelist+radius) { ****cir**** **cir-value** | ****cbs**** **cbs-value** } \*
     
     
     
     The bandwidth for incoming packets to be sent to the CPU is configured for the whitelist.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the policy view.
  6. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  7. Run [**cpu-defend-policy**](cmdqueryname=cpu-defend-policy) *policy-number*
     
     
     
     The attack defense policy is bound to the interface board.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure total CAR.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
     
     
     
     An attack defense policy is configured.
  3. Run [**car total-packet**](cmdqueryname=car+total-packet) { ****high**** | ****middle**** | ****low**** | *total-packet-rate*
     
     
     
     A total rate is set for sending packets to the CPU.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the policy view.
  6. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The interface board view is displayed.
  7. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
     
     
     
     The attack defense policy is bound to the interface board.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If an attack defense policy is bound to an interface board, run the [**display this**](cmdqueryname=display+this) command in the slot view to check the policy. Then, enter the attack defense policy view and modify CAR parameters.