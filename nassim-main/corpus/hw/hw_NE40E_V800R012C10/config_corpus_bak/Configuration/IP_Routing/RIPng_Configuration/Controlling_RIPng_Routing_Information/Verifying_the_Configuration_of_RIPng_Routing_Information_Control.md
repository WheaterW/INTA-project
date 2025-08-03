Verifying the Configuration of RIPng Routing Information Control
================================================================

After controlling RIPng routing information, verify all
activated routes in the RIPng database.

#### Prerequisites

Configurations have been performed to control RIPng routing
information.
#### Procedure

* Run the [**display ripng**](cmdqueryname=display+ripng) *process-id* **database** [ **verbose** ] [ **destination-address** *destination-address* [ *mask-length* ] ] [ **interface** *interface-type* *interface-number* [ **neighbor-address** *neighbor-address* ] ] command to check routes in the RIPng database.