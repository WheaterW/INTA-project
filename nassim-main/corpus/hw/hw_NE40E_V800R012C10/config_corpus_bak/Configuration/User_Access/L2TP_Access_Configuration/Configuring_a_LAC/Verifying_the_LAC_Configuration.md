Verifying the LAC Configuration
===============================

This section describes how to verify the configurations of the L2TP group, session information, and the tunnel on the LAC after the LAC is configured and users go online.

#### Procedure

* Run the [**display l2tp-group**](cmdqueryname=display+l2tp-group) [ *group-name* ] command to check the L2TP group configuration.
* Run the [**display l2tp session**](cmdqueryname=display+l2tp+session) **lac** [ **session-item** *session-id* | **source-ip** *source-ip-address* | **destination-ip** *destination-ip-address* ] command to check information about the current LAC session.
* Run the [**display l2tp tunnel**](cmdqueryname=display+l2tp+tunnel) **lac** [ **tunnel-item** *tunnel-id* | **tunnel-name** *remote-name* ] command to check information about the tunnel on the LAC.
* Run the [**display l2tp session-number**](cmdqueryname=display+l2tp+session-number) **lac** [ **source-ip** *source-ip-address* [ **vpn-instance** *vpn-instance-name* ] ] command to check the number of LAC sessions established based on a specified source IPv4 address.
* Run the [**display l2tp statistics lac tunnel-item**](cmdqueryname=display+l2tp+statistics+lac+tunnel-item) *tunnel-id* command to check statistics about LAC protocol packets based on a tunnel ID.