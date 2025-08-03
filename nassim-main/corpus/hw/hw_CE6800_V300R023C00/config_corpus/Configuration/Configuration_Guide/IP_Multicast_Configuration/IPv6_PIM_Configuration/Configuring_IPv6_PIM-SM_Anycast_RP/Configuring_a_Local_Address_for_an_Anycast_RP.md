Configuring a Local Address for an Anycast RP
=============================================

Configuring a Local Address for an Anycast RP

#### Context

When sending a Register message to an anycast RP peer, the local anycast RP needs to convert the source address of the message into the configured local address.

The devices functioning as anycast RPs can be identified by the same logical address so that the RP in the IPv6 PIM-SM domain is unique. The anycast RP-enabled devices, however, need to distinguish one another during communication. Therefore, the configured anycast RP address cannot be used in such communication. In this case, you need to configure a local address for each anycast RP and establish anycast RP peer relationships.


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
4. Configure a local address for the anycast RP.
   
   
   ```
   [local-address](cmdqueryname=local-address) local-address
   ```
   
   
   
   You are advised to use a loopback interface address as the local address of an anycast RP.
   
   The local address of an anycast RP cannot be the same as the anycast RP address.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```