Verifying the Configuration of RIPng Route Selection
====================================================

After adjusting RIPng route selection, verify the running
status of RIPng, information about interfaces, and RIPng routing information.

#### Prerequisites

RIPng route selection has been adjusted.
#### Procedure

* Run the [**display ripng**](cmdqueryname=display+ripng) [ *process-id* | **vpn-instance** *vpn-instance-name* ]
  command to check the current operating status and configuration of
  RIPng.
* Run the [**display ripng**](cmdqueryname=display+ripng) *process-id* **route** [ **destination-address** *destination-address* [ *mask-length* ] ] [ **interface** *interface-type* *interface-number* [ **neighbor-address** *neighbor-address* ] ] command to check RIPng routes.
* Run the [**display ripng**](cmdqueryname=display+ripng) *process-id* **interface** command to check information
  about RIPng interfaces.