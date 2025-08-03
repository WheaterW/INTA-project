(Optional) Configuring Attack Detection for ND Messages with a Fixed Source MAC Address
=======================================================================================

(Optional) Configuring Attack Detection for ND Messages with a Fixed Source MAC Address

#### Context

ND has powerful functions. However, if there is no security mechanism, attackers may use ND to attack network devices. The system collects statistics about ND messages sent to the CPU based on the source MAC addresses of the messages. If the number of ND messages with the same source MAC address received within 5 seconds exceeds a specified threshold, the system considers that an attack occurs and adds the MAC address to an attack entry. Before the attack entry ages out, the following actions are performed based on the configured detection mode:

* If the detection mode is set to filter, log information is generated and ND messages sent from the source MAC address are filtered out.
* If the detection mode is set to monitor, only log information is generated and ND messages sent from the source MAC address are not filtered out.

If a MAC address is added to an ND attack entry with a fixed source MAC address, this MAC address is deleted after the aging time expires. Some important servers may send a large number of ND messages. To prevent these messages from being filtered out, you can configure the MAC addresses of these servers as protected ones.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**ipv6 nd source-mac detect-mode**](cmdqueryname=ipv6+nd+source-mac+detect-mode) { **filter** | **monitor** }
   
   Attack detection for ND messages with a fixed source MAC address is enabled and a detection mode is specified.
3. (Optional) Run [**ipv6 nd source-mac aging-time**](cmdqueryname=ipv6+nd+source-mac+aging-time)  *aging-value*
   
   The aging time of ND attack entries with a fixed source MAC address is set.
4. (Optional) Run [**ipv6 nd source-mac threshold**](cmdqueryname=ipv6+nd+source-mac+threshold) *threshold-value*
   
   An attack detection threshold is configured for ND messages with fixed source MAC addresses. If the number of ND messages with the same source MAC address received within 5 seconds exceeds the configured threshold, the system considers that an attack occurs and adds the MAC address to an attack entry.
5. (Optional) Run [**ipv6 nd source-mac exclude-mac**](cmdqueryname=ipv6+nd+source-mac+exclude-mac) *mac-address*
   
   The MAC address of the device to be protected is configured.
6. (Optional) Run [**ipv6 nd source-mac max-detect-number**](cmdqueryname=ipv6+nd+source-mac+max-detect-number) *max-detect-value*
   
   The maximum number of ND messages with fixed source MAC addresses that can be detected is configured.
7. (Optional) Run [**ipv6 nd source-mac max-entry-number**](cmdqueryname=ipv6+nd+source-mac+max-entry-number) *max-entry-value*
   
   The maximum number of ND attack entries with fixed source MAC addresses is configured.
8. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.