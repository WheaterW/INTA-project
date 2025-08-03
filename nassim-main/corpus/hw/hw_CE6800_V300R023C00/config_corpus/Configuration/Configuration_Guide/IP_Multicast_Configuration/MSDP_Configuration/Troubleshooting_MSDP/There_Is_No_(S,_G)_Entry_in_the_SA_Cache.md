There Is No (S, G) Entry in the SA Cache
========================================

There Is No (S, G) Entry in the SA Cache

#### Fault Symptom

MSDP fails to send (S, G) entries through SA messages.

#### Possible Causes

* If two MSDP peers do not have a route to each other, the TCP connection cannot be established, and no (S, G) entry is available on the device.
* If the local interface address differs from the MSDP peer address configured on the remote device, the TCP connection cannot be established, and no (S, G) entry is available on the device.
* The [**import-source**](cmdqueryname=import-source) command configures a policy for filtering active sources that can be advertised using SA messages. If the **acl** parameter is not specified, all (S, G) entries are filtered out by default. In other words, all (S, G) entries in the local domain are not advertised.
* If the [**import-source**](cmdqueryname=import-source) command is not run, the device sends all (S, G) entries in the local domain. If MSDP fails to send (S, G) entries in the local domain through SA messages, check whether the [**import-source**](cmdqueryname=import-source) command configuration is correct.


#### Procedure

1. Check whether the two devices that will become MSDP peers have learned ARP entries from each other.
   
   
   ```
   [display arp](cmdqueryname=display+arp)
   ```
2. Check whether there are reachable unicast routes between the two devices that will be configured as MSDP peers.
   
   
   ```
   [display ip routing-table](cmdqueryname=display+ip+routing-table)
   ```
3. Check whether the address of the local interface is the same as the address of the remote MSDP peer.
   
   
   ```
   [display current-configuration interface](cmdqueryname=display+current-configuration+interface) [ interface-type [ interface-number ]| interface-number ] [ include-default ]
   ```
4. Check whether the [**import-source**](cmdqueryname=import-source) command is run in the MSDP view of the public network instance or the VPN instance on the local device, and whether the **acl** parameter is correctly configured. Ensure that the ACL rule can properly filter (S, G) information.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```