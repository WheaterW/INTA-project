Enabling Layer 2 Proxy ARP
==========================

After Layer 2 proxy ARP is enabled, the ARP proxy responds to ARP request messages based on locally generated DHCP snooping or ARP snooping entries.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0240873513__fig_dc_vrp_arp_feature_000101), if proxy ARP is not enabled on the CEs, an ARP message sent by Host3 to request the MAC address of Host1 is broadcast in the BD through CE1. In this case, both Host1 and Host2 receive the ARP request message. Host1 finds that the destination of the message is itself, and so accepts the message. Host2, however, finds that the destination of the message is not itself, and so directly discards the message. This message forwarding mode brings the following problems:

(1) The IP address in the ARP message can be obtained by any user, posing security risks. For example, malicious users can use the IP address to initiate attacks (such as ping attacks) targeting authorized users.

(2) The ARP request message is broadcast to all users, including those that are not the destination, consuming excessive network resources. This causes network congestion and deteriorates network performance.

To solve the preceding problems, configure BD-based Layer 2 proxy ARP on the CEs. Layer 2 proxy ARP can relieve the pressure on processing ARP messages by isolating ARP BDs. With this function enabled, a device preferentially uses learned ARP snooping entries to respond to received ARP request messages. After receiving an ARP request message, the device with Layer 2 proxy ARP enabled checks whether the user information in the request message matches an ARP snooping binding entry. If a matching entry exists, the device sends an ARP reply message. If no matching entry exists, the device broadcasts the ARP request message.

**Figure 1** BD-based Layer 2 proxy ARP  
![](images/fig_dc_vrp_arp_feature_003703.png)
On the network shown in [Figure 2](#EN-US_TASK_0240873513__fig1428825633711), Layer 2 proxy ARP is not supported on the PE.**Figure 2** BD-based Layer 2 proxy ARP not supported  
![](figure/en-us_image_0000002084822782.png)

The users connected to the CE can communicate with each other in a Layer 2 BD, and the PE is connected to the BD. If Layer 2 proxy ARP is enabled in the BD:

1. When Host1 needs to communicate with Host2, it sends an ARP request message to Host2. The message enters the CE through Interface1. The CE then broadcasts the message to Host2 through Interface2 and to the PE's Interface4 through Interface3.

* The CE learns the MAC address of Host1 through Interface1.
* When the PE receives the ARP request message from Host1, Interface4 learns the ARP information sent by Host1 and adds a proxy ARP entry.

2. When Host2 needs to communicate with Host1, it sends an ARP request message to Host1. The message enters the CE through Interface2. The CE then broadcasts the message to Host1 through Interface1 and to the PE's Interface4 through Interface3.

* When Interface4 of the PE receives the ARP request message from Host2, the PE sends an ARP reply message to Host2 (Interface4 -> Interface3 -> Interface2) using the real MAC address of Host1 because the PE has a proxy ARP entry for Host1.
* After receiving the ARP reply message from the PE through Interface3, the CE learns the MAC address of Host1 through Interface3. As a result, the outbound interface of Host1's MAC address on the CE changes, affecting unicast traffic forwarding.

Therefore, when users connected to the CE communicate with each other in a Layer 2 BD, Layer 2 proxy ARP cannot be enabled in the BD connected to the PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The BD view is displayed.
3. Run [**arp l2-proxy enable**](cmdqueryname=arp+l2-proxy+enable)
   
   
   
   Layer 2 proxy ARP is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In a BD+L2VE+L3VE scenario, configuring this function prevents ARP entries from being learned.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.