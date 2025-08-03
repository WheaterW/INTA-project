Verifying the Configuration of Controlling the Sending and Receiving of RIPng Packets
=====================================================================================

After controlling the sending and receiving of RIPng packets, verify the routing information in the RIPng database.

#### Prerequisites

Configurations have been performed to control the sending and receiving of RIPng packets.


#### Procedure

* Run the [**display ripng**](cmdqueryname=display+ripng) *process-id* **database** [ **verbose** ] [ **destination-address** *destination-address* [ *mask-length* ] ] [ **interface** *interface-type* *interface-number* [ **neighbor-address** *neighbor-address* ] ] command to check the routing information in the RIPng database.