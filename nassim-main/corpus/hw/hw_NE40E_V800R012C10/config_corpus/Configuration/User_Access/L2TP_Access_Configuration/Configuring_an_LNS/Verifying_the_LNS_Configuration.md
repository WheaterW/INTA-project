Verifying the LNS Configuration
===============================

This section describes how to verify the configurations of the L2TP group, session information, and the tunnel on the LNS after the LNS is configured and users go online.

#### Procedure

* Run the [**display l2tp-group**](cmdqueryname=display+l2tp-group) [ *group-name* ] command to check configurations of all L2TP groups or a specified one.
* Run the [**display lns-group**](cmdqueryname=display+lns-group) { **all** | **name** *lns-name* } command to check configurations of all L2TP groups or a specified one.
* Run the [**display l2tp session**](cmdqueryname=display+l2tp+session) **lns slot** *slot-id* [ **session-item** *session-id* | **source-ip** *source-ip-address* | **destination-ip** *destination-ip-address* ] command to check LNS session information.
* Run the [**display l2tp session-number**](cmdqueryname=display+l2tp+session-number) **lns** [ **source-ip** *source-ip-address* [ **vpn-instance** *vpn-instance-name* ] ] command to check the number of LNS sessions established based on a specified source IPv4 address.
* Run the [**display l2tp statistics lns tunnel-item**](cmdqueryname=display+l2tp+statistics+lns+tunnel-item) *tunnel-id* command to check statistics about LNS protocol packets based on a tunnel ID.
* Run the [**display l2tp session lns calling-num**](cmdqueryname=display+l2tp+session+lns+calling-num) *calling-num* command to check detailed information about a session based on a calling number.
* Run the [**display l2tp tunnel-limit**](cmdqueryname=display+l2tp+tunnel-limit) command to check the maximum number of L2TP tunnels.
* Run the [**display l2tp blocked-slot**](cmdqueryname=display+l2tp+blocked-slot) command to check blocked tunnel boards.
* Run the [**display l2tp tunnel**](cmdqueryname=display+l2tp+tunnel) **lns** **slot** *slot-id* [ **tunnel-item** *tunnel-id* | **tunnel-name** *remote-name* ] command to check LNS tunnel information.
* Run the [**display l2tp pim-sm tunnel**](cmdqueryname=display+l2tp+pim-sm+tunnel) [ **slot** *slot-id* | **tunnel-item** *tunnel-id* ] command to check information about users for whom PIM-SM multicast is enabled based on a specified tunnel or tunnel board.
* Run the [**display l2tp session rui**](cmdqueryname=display+l2tp+session+rui) command to check L2TP session backup statistics.