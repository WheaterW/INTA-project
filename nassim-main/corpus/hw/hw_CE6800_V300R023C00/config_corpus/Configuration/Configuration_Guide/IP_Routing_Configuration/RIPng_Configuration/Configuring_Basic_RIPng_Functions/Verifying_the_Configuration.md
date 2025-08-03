Verifying the Configuration
===========================

Verifying the Configuration

#### Prerequisites

Basic RIPng functions have been configured.


#### Procedure

* Run the [**display ripng**](cmdqueryname=display+ripng) [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check the operating status and configuration of RIPng.
* Run the [**display ripng**](cmdqueryname=display+ripng) *process-id* **route** [ **destination-address** *destination-ipv6-address* [ *ipv6-mask-length* ] ] [ **interface** *interface-type* *interface-number* [ **neighbor-address** *neighbor-ipv6-address* ] ] command to check RIPng routes.