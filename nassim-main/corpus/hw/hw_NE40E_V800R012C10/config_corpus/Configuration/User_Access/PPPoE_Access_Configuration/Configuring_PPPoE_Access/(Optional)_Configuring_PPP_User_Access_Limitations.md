(Optional) Configuring PPP User Access Limitations
==================================================

To prevent unauthorized users from initiating a brute force attack to crack the password of an authorized user or the number of access users, configure the maximum number of users allowed to go online through a board or MAC address.

#### Context

On live networks, unauthorized users may use a brute force attack to crack the password of an authorized user or the number of access users. To prevent this problem, configure the maximum number of users allowed to go online through a board.

Multiple users may use the same MAC address for network access. To allow PPPoE users to use the same MAC address to go online through the same device, configure the maximum number of users allowed to go online through a MAC address.

When PPPoE users are online, a downstream device failure causes the NE40E to receive a large number of NCP negotiation requests from some users, resulting in high CPU usage. Therefore, the number of NCP negotiations must be limited.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pppoe-server**](cmdqueryname=pppoe-server) *slot-number* **max-sessions** *session-number*
   
   
   
   The maximum number of users allowed to go online through a board is configured.
3. Run [**pppoe-server max-sessions remote-mac**](cmdqueryname=pppoe-server+max-sessions+remote-mac) *session-number* [ **with-check-location** [ **padi-mac-check** ] ]
   
   
   
   The maximum number of users allowed to go online through a MAC address at different geographical locations is configured. Only one access user is allowed at the same physical location.
4. Run [**pppoe-server negotiation times limit**](cmdqueryname=pppoe-server+negotiation+times+limit)
   
   
   
   The number of NCP negotiations is limited.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.