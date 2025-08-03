Configuring an Anycast RP Peer
==============================

Configuring an Anycast RP Peer

#### Context

When sending a Register message to an anycast RP peer, the local anycast RP needs to convert the destination address of the message into the local address of the anycast RP peer.

The devices functioning as anycast RPs can be identified by the same logical address so that the RP in the PIM-SM domain is unique. The anycast RP-enabled devices, however, need to distinguish one another during communication. Therefore, the configured anycast RP address cannot be used in such communication. In this case, you need to configure a local address for each anycast RP and establish anycast RP peer relationships.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IPv6 PIM view.
   
   
   ```
   [pim ipv6](cmdqueryname=pim+ipv6) [vpn-instance vpn-instance-name ]
   ```
3. Configure an anycast RP and enter its view.
   
   
   ```
   [anycast-rp](cmdqueryname=anycast-rp) rp-address
   ```
4. Configure an anycast RP peer.
   
   
   ```
   [peer](cmdqueryname=peer) peer-address
   ```
   
   
   
   *peer-address* specifies the local address of an anycast RP peer.
   
   In a PIM-SM domain, all anycast-RP-capable devices must be fully connected logically. That is, anycast RP peer relationships must be established between every two anycast RPs.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```