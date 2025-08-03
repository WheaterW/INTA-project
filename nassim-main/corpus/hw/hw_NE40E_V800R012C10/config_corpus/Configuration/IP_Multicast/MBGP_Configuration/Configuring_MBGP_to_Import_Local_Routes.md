Configuring MBGP to Import Local Routes
=======================================

MBGP can import routes from other protocols. When routes are imported from dynamic routing protocols, the process IDs of the routing protocols must be specified.

#### Usage Scenario

MBGP cannot discover routes by itself. Instead, it imports routes discovered by an IGP or static routes into the MBGP routing table.

Routes imported into the MBGP table can be:

* Routes statically imported by using the [**network**](cmdqueryname=network) command
* Routes imported by using the [**import-route**](cmdqueryname=import-route) command

At least one type of routes need to be imported into the MBGP routing table.

#### Pre-configuration Tasks

Before configuring MBGP to import routes, [configure an MBGP peer](dc_vrp_multicast_cfg_1003.html).

Perform the following steps on the Routers that are configured as MBGP peers:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
4. Run [**network**](cmdqueryname=network) *ip-address* [ *mask-length* | *mask* ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
   
   
   
   MBGP is configured to import routes from the local routing table into the MBGP routing table and then advertise the MBGP routes on the local network.
   
   
   
   * *ip-address* [ *mask-length* | *mask* ]: specifies the IP address, mask length, or mask information of the imported routes.
   * **route-policy** *route-policy-name*: specifies a routing policy to control which routes can be imported.
   
   The destination address and mask length specified in the [**network**](cmdqueryname=network) command must be the same as those of the entry in the local IP routing table. Otherwise, the specified routes will not be imported.
5. Run [**import-route**](cmdqueryname=import-route) { **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** | **unr** } [ **med** *med-value* | [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] ] \*
   
   
   
   IGP routes are imported into the MBGP routing table.
   
   
   
   * **med** *med-value*: specifies the MED value assigned to imported routes.
   * **route-policy** *route-policy-name* and **route-filter** *route-filter-name* are used to filter routes. Only the routes that match the specified rule can be imported.
6. (Optional) Run [**default-route imported**](cmdqueryname=default-route+imported)
   
   
   
   Default routes are imported into the MBGP routing table.
   
   
   
   To import default routes, run the [**import-route**](cmdqueryname=import-route) command and the [**default-route imported**](cmdqueryname=default-route+imported) command. If only the [**import-route**](cmdqueryname=import-route) command is used, default routes will not be imported. In addition, the [**default-route imported**](cmdqueryname=default-route+imported) command is used to import only the default routes that exist in the local routing table.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After the configuration is complete, verify the configuration.

* Run the [**display bgp multicast network**](cmdqueryname=display+bgp+multicast+network) command to check routing information advertised by MBGP.
* Run the [**display bgp multicast routing-table**](cmdqueryname=display+bgp+multicast+routing-table) command to check the MBGP routing table.