Verifying the IPv4 IS-IS Route Convergence Speed Configuration
==============================================================

After configuring parameters to adjust the IPv4 IS-IS route convergence speed, check the configurations.

#### Procedure

* Run the [**display isis interface**](cmdqueryname=display+isis+interface) [ [ **verbose** | **traffic-eng** ] \* | **tunnel** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check IS-IS packet information.
* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **topology** *topology-name* ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] \* command to check the priority of IS-IS routes.