Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3+lsdb) [ *process-id* ] **lsdb** command to check information about the OSPFv3 LSDB. The command output includes information such as the LSA type and link state ID.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3+routing) [ *process-id* ] **routing** command to check information about the OSPFv3 routing table. If the device resides in a common area, AS external routes exist in the routing table. After the area where the device resides is configured as a stub area, AS-external routes are no longer available on the device.