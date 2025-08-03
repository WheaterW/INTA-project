Verifying the Configuration
===========================

After configuring OSPF SR-MPLS Flex-Algo, you can check relevant information.

#### Prerequisites

All OSPF SR-MPLS Flex-Algo configurations are complete.


#### Procedure

1. Run the **display ospf** *process-id* **flex-algo** [ *flexAlgoIdentifier* ] [ **area** { *area-id-integer* | *area-id-ipv4* } ] command to check the preferred FAD in the LSDB.
2. Run the **display ospf** [ *process-id* ] **topology** [ **area** { *area-id* | *area-ipv4* } ] **flex-algo** [ *flex-algo-id* ] command to check information about the topology used for OSPF Flex-Algo to calculate routes.
3. Run the [**display segment-routing prefix mpls forwarding**](cmdqueryname=display+segment-routing+prefix+mpls+forwarding) **flex-algo** [ *flexAlgoId* ] [ **ip-prefix** *ip-prefix* *mask-length* | **label** *label* ] [ **verbose** ] command to check the Flex-Algo-based SR label forwarding table.
4. Run the [**display segment-routing state ip-prefix**](cmdqueryname=display+segment-routing+state+ip-prefix)*ip-prefix* *mask-length* **flex-algo** *flexAlgoId* command to check the SR status of a specified Flex-Algo based on a specified IP prefix.