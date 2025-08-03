Maintaining Routing Policies
============================

Maintaining Routing Policies

#### Context

Maintaining routing policies involves clearing statistics about IP prefix lists and the number of routes that match a specified route-policy.

![](public_sys-resources/notice_3.0-en-us.png) 

Statistics about routes matching IP prefix lists and the number of routes that match the specified route-policy cannot be restored after being cleared. Exercise caution when running the following commands.


**Table 1** Clearing statistics about routes matching IP prefix lists and a specified route-policy
| Operation | Command |
| --- | --- |
| Clear statistics about routes matching a specified IPv4 prefix list or all IPv4 prefix lists. | [**reset ip ip-prefix**](cmdqueryname=reset+ip+ip-prefix) [ *pfName* ] |
| Clear statistics about routes matching a specified IPv6 prefix list or all IPv6 prefix lists. | [**reset ip ipv6-prefix**](cmdqueryname=reset+ip+ipv6-prefix) [ *pf6name* ]  NOTE:  The CE6885-LL does not support this command. |
| Clear statistics about routes matching a specified route-policy. | [**reset route-policy**](cmdqueryname=reset+route-policy) *route-policy-name* **counters** |