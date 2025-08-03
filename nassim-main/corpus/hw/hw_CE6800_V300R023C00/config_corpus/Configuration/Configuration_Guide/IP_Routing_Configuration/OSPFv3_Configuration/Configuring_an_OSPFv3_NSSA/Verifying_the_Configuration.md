Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3+routing+%28all+views%29) [ *process-id* ] **routing** [ [ *ipv6-address* *prefix-length* ] | **abr-routes** | **asbr-routes** | **ase-routes** | **inter-routes** | **intra-routes** | **nssa-routes** ] [ **verbose** ] command to check information about the OSPFv3 routing table.
  
  By comparing the OSPFv3 routing tables before and after the NSSA is configured, you can reach the following conclusions:
  + The NSSA can import AS external routes and advertise them to other OSPFv3 areas.
  + The NSSA does not learn external routes from other areas on the OSPFv3 network.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3+lsdb) [ *process-id* ] **lsdb** [ **area** *area-id* ] [ [ **originate-router** *advertising-router-id* | **hostname** *hostname* ] | **self-originate** ] [ { **grace** | **inter-prefix** | **inter-router** | **intra-prefix** | **link** | **network** | **router** | **router-information** | **nssa** } [*link-state-id* ] ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ] command to check information about the OSPFv3 LSDB.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3+routing+%28all+views%29)[ *process-id* ] **routing** **statistics** command to check OSPFv3 route statistics.