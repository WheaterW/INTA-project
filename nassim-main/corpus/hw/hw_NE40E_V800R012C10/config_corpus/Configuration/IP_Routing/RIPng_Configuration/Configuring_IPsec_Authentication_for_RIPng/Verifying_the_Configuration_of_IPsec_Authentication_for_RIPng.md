Verifying the Configuration of IPsec Authentication for RIPng
=============================================================

After IP security (IPsec) authentication for RIPng is configured, you can check the security association (SA) used in IPsec authentication and statistics on the RIPng packets that failed authentication.

#### Prerequisites

After IPsec authentication is enabled in a RIPng process or on a RIPng interface, the configuration takes effect immediately. There is no need to restart the RIPng process.


#### Procedure

* Run the [**display ripng**](cmdqueryname=display+ripng) *process-id* **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command to check the SA used in IPsec authentication.
* Run the [**display ripng**](cmdqueryname=display+ripng) *process-id* **statistics** **interface** { **all** | *interface-type interface-number* [ **verbose** | **neighbor** *neighbor-ipv6-address* ] } command to check the number of RIPng packets that failed authentication.