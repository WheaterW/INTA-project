(Optional) Configuring IPv4 Address Reservation
===============================================

(Optional) Configuring IPv4 Address Reservation

#### Context

You can configure an IPv4 address pool in which the reserved addresses can be queried and reclaimed. After a user goes online and then offline using an IP address in the address pool, you can view information about reserved addresses in the address pool and reclaim the reserved addresses. This section describes two reservation modes for an IPv4 address pool: MAC address-based reservation and lease-based reservation.

Perform the following steps on the device functioning as a DHCPv4 server:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip pool**](cmdqueryname=ip+pool) *pool-name* **bas local**
   
   
   
   A local IPv4 address pool is created.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed, and the address pool view is displayed.
4. Configure address reservation in either of the following modes:
   * MAC address-based reservation: Run the [**reserved ip-address mac**](cmdqueryname=reserved+ip-address+mac) command to configure MAC address-based reservation.
   * Lease-based reservation: Run the [**reserved ip-address lease**](cmdqueryname=reserved+ip-address+lease) command to configure lease-based reservation. You can choose whether to configure a lease using the [**lease**](cmdqueryname=lease) *Days* *Hours* *Minutes* command. If such a lease is not configured, the default lease (3 days) is used.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. (Optional) Run [**recycle reserved ip-address**](cmdqueryname=recycle+reserved+ip-address)
   
   
   
   Reserved addresses are reclaimed.

#### Result

After assignable addresses are configured in the IPv4 address pool view, IPoEv4 users can go online using IP addresses in this address pool. After users go offline, you can view information about reserved IP addresses in the address pool and reclaim the reserved IP addresses. You can also view reserved IPv4 addresses in the diagnostic view and reclaim the reserved addresses.