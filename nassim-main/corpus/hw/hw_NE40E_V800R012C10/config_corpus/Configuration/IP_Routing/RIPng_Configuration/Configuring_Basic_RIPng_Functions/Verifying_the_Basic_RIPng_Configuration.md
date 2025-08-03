Verifying the Basic RIPng Configuration
=======================================

After configuring basic RIPng functions, verify the current
operating status and routing information of RIPng.

#### Prerequisites

Basic RIPng functions have been configured.
#### Procedure

* Run the [**display ripng**](cmdqueryname=display+ripng) [ *process-id* | **vpn-instance** *vpn-instance-name* ]
  command to check the operating status and configuration of RIPng.
* Run the [**display ripng**](cmdqueryname=display+ripng) *process-id* **route** [ **destination-address** *destination-address* [ *mask-length* ] ] [ **interface** *interface-type* *interface-number* [ **neighbor-address** *neighbor-address* ] ] command to check RIPng routes.