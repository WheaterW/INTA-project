route-policy
============

route-policy

Function
--------



The **route-policy** command creates a route-policy and displays the Route-policy view.

The **undo route-policy** command deletes the created route-policy.



By default, no route-policy is created.


Format
------

**route-policy** *route-policy-name* *matchMode* **node** *node*

**undo route-policy** *route-policy-name* [ **node** *node* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *route-policy-name* | Specifies the name of the route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *matchMode* | Specifies the matching mode of the route-policy. | The value is an enumerated type:   * permit: Specifies the matching mode of the route-policy as permit. * deny: Specifies the matching mode of the route-policy as deny. |
| **node** *node* | Specifies the index of the node in the route-policy. | The value is an integer ranging from 0 to 65535. When the route-policy is used to filter routes, the node with the smaller value is matched against first. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A route-policy is used to filter routes and set route attributes for the routes that pass the filtering. A route-policy can contain multiple nodes. One node can be configured with multiple if-match and apply clauses. The if-match clauses define matching rules for this node, and the apply clauses define behaviors for the routes that match the rules.The relationship among if-match clauses that are based on different route attributes is AND in the same route-policy node. Specifically, a route is considered to match a node only when it matches all the if-match clauses of the node. The relationship among if-match clauses that are based on the same route attribute is OR in the same route-policy node. Specifically, a route is matched against the if-match clauses in order; if the route matches an if-match clause, the route is considered to match the route-policy and will not be matched against the rest if-match clauses. For example, node 10 has two if-match clauses: if-match community-filter 1 and if-match as-path-filter 1. The two if-match clauses are based on different route attributes. Therefore, the relationship between them is AND. Node 20 also has two if-match clauses: if-match community-filter 1 and if-match community-filter 2. The two if-match clauses are both based on the community attribute. Therefore, the relationship between them is OR. If no if-match clause is specified, all the routes are matched.The relationship between the nodes in a route-policy is "OR". That is, if a route matches one node in a route-policy, the route matches this route-policy; if a route does not match any node in a route-policy, the route fails to match this route-policy.

Generally, you are not advised to use the same route-policy to filter both IPv4 and IPv6 routes.For example, for BGP, if both IPv4 and IPv6 peer relationships exist, you are advised to use different route-policies for IPv4 and IPv6 peers. The configuration is as follows:

#bgp 65001peer x.x.x.x as-number 65001peer x::x as-number 65001#ipv4-family unicastpeer x.x.x.x enablepeer x.x.x.x route-policy policyV4 export#ipv6-family unicastpeer x.x.x.x enablepeer x::x route-policy policyV6 export

In this scenario, you are advised to use one route-policy for IPv4 peer x.x.x.x and another route-policy for IPv6 peer x::x.

The following example describes the use of the same route-policy to filter both IPv4 and IPv6 routes.Scenario 1: In the same deny node of a route-policy, some if-match clauses match IPv4 routes, and other if-match clauses match IPv6 routes.

#route-policy policy1 deny node 10if-match ip-prefix prefix-aif-match ipv6 address prefix-list prefix-a-v6#route-policy policy1 permit node 30

Explanation:If a node contains multiple if-match clauses for different attributes, the node can pass the matching test only when all the matching conditions specified by the if-match clauses are met.By default:a. In an IPv4 scenario, node 10 is preferentially matched based on the route-policy. The IPv4 routes that match ip-prefix prefix-a match the if-match clause and are denied by node 10. The routes are matched based on the unique matching rule of the route-policy and are not matched against other nodes. Therefore, these routes cannot match the route-policy. Other IPv4 routes that do not match ip-prefix prefix-a continue to be matched against node 30. Node 30 does not have if-match clauses for IPv4 routes. By default, all IPv4 routes match the if-match clauses. The mode of node 30 is permit, and IPv4 routes that are not in the ip-prefix prefix-a range are also permitted.b. In the IPv6 scenario, node 10 is preferentially matched based on the route-policy. The IPv6 routes that match prefix-list prefix-a-v6 match the if-match clause and are denied by node 10. The routes are matched based on the unique matching rule of the route-policy and are not matched against other nodes. Therefore, these routes cannot match the route-policy. Other IPv6 routes that do not match prefix-list prefix-a-v6 continue to be matched against node 30. Node 30 does not have any if-match clause for IPv6 routes. By default, all IPv6 routes match the if-match clause. The mode of node 30 is permit, and all IPv6 routes that are not in the prefix-list prefix-a-v6 range are permitted.By default, the IPv4 routes that match ip-prefix prefix-a and IPv6 routes that match prefix-list prefix-a-v6 are denied, and the other routes are permitted.

Scenario 1 (a): If node 20 is added to the route-policy to match only IPv4 or IPv6 routes, unexpected results may occur.In this example, IPv4 route filtering conditions need to be added due to service changes. Therefore, node 20 is added and prefix-a-2 is used to filter IPv4 routes.

#route-policy policy1 deny node 10if-match ip-prefix prefix-aif-match ipv6 address prefix-list prefix-a-v6#route-policy policy1 deny node 20if-match ip-prefix prefix-a-2#route-policy policy1 permit node 30

Explanation:a. In the IPv4 scenario, node 10 is preferentially matched based on the route-policy. The IPv4 routes that match ip-prefix prefix-a match the if-match clause and are denied by node 10. The routes are matched based on the unique matching rule of the route-policy and are not matched against other nodes. Therefore, these routes cannot match the route-policy. Other IPv4 routes that do not match ip-prefix prefix-a continue to match node 20. IPv4 routes that match ip-prefix prefix-a-2 match the if-match clause and are denied. The mode of node 30 is permit. Therefore, all IPv4 routes beyond the range of ip-prefix prefix-a and ip-prefix prefix-a-2 are permitted.b. In IPv6 scenarios, node 10 is preferentially matched based on the route-policy. The IPv6 routes that match prefix-list prefix-a-v6 match the if-match clause and are denied by node 10. The routes are matched based on the unique matching rule of the route-policy and are not matched against other nodes. Therefore, these routes cannot match the route-policy. Other IPv6 routes that do not match prefix-list prefix-a-v6 continue to match node 20. Node 20 does not have any if-match clause for IPv6 routes. By default, all IPv6 routes match the if-match clause. The mode of node 20 is deny, and all IPv6 routes that are not in the prefix-list prefix-a-v6 group address range are denied. In this scenario, node 30 is not executed based on the unique matching rule of the route-policy. The final result is that no IPv6 route matches the route-policy.By default, only the IPv4 routes that are not in the range specified by ip-prefix prefix-a and ip-prefix prefix-a-2 are permitted, and the other IPv4 routes and all IPv6 routes are denied.According to the analysis in scenario 1, the user intends to filter out some IPv4 routes (matching prefix-a-2) based on the original filter. However, all IPv6 routes fail to pass the filtering of the route-policy.

Scenario 2: In the same permit node of a route-policy, some if-match clauses match IPv4 routes, and other if-match clauses match IPv6 routes.

#route-policy policy1 permit node 10if-match ip-prefix prefix-aif-match ipv6 address prefix-list prefix-a-v6#route-policy policy1 deny node 30

Explanation:If a node contains multiple if-match clauses for different attributes, the node can pass the matching test only when all the matching conditions specified by the if-match clauses are met.By default:a. In an IPv4 scenario, node 10 is preferentially matched based on the route-policy. The IPv4 routes that match ip-prefix prefix-a match the if-match clause and are permitted by node 10. Therefore, these routes match the route-policy. Other IPv4 routes that do not match ip-prefix prefix-a continue to match node 30. Node 30 does not have an if-match clause for IPv4 routes. By default, all IPv4 routes match the if-match clause, but the mode of node 30 is deny, IPv4 routes that are not in the ip-prefix prefix-a range are also denied.b. In IPv6 scenarios, node 10 is preferentially matched based on the route-policy. The IPv6 routes that match prefix-list prefix-a-v6 match the if-match clause and are permitted by node 10. Therefore, these routes match the route-policy. Other IPv6 routes that do not match prefix-list prefix-a-v6 continue to match node 30. Node 30 does not have an if-match clause for IPv6 routes. By default, all IPv6 routes match the if-match clause, but node 30 is in deny mode, IPv6 routes beyond the prefix-list prefix-a-v6 range are also denied.By default, IPv4 routes that match ip-prefix prefix-a and IPv6 routes that match prefix-list prefix-a-v6 are permitted, and other routes are denied.

Scenario 2 (a): If node 20 is added to the route-policy to match only IPv4 or IPv6 routes, unexpected results may occur.In this example, IPv6 route filtering conditions need to be added due to service changes. Therefore, node 20 is added and prefix-a-v6-2 is used to filter IPv6 routes.

#route-policy policy1 permit node 10if-match ip-prefix prefix-aif-match ipv6 address prefix-list prefix-a-v6#route-policy policy1 permit node 20if-match ipv6 address prefix-list prefix-a-v6-2#route-policy policy1 deny node 30

Explanation:a. In the IPv4 scenario, node 10 is preferentially matched based on the route-policy. The IPv4 routes that match ip-prefix prefix-a match the if-match clause and are permitted by node 10. These routes match the route-policy. Other IPv4 routes that do not match ip-prefix prefix-a continue to match node 20. Node 20 does not have if-match clauses for IPv4 routes. By default, all IPv4 routes match the if-match clauses. The mode of node 20 is permit, all IPv4 routes that are not in the ip-prefix prefix-a range are permitted. In this scenario, node 30 is not executed based on the unique matching rule of the route-policy. All IPv4 routes can match the route-policy.b. In IPv6 scenarios, node 10 is preferentially matched based on the route-policy. The IPv6 routes that match prefix-list prefix-a-v6 match the if-match clause and are permitted by node 10. These routes match the route-policy. Other IPv6 routes that do not match prefix-list prefix-a-v6 continue to match node 20. The IPv6 routes that match iprefix-list prefix-a-v6-2 match the if-match clause, and are permitted. The mode of node 30 is deny. Therefore, IPv6 routes beyond the prefix-list prefix-a-v6 and iprefix-list prefix-a-v6-2 ranges are denied.By default, in this scenario, only the IPv6 routes beyond the prefix-list prefix-a-v6 and iprefix-list prefix-a-v6-2 ranges are denied, and the other IPv6 routes and all IPv4 routes are permitted.According to the analysis in scenario 2, the user intends to filter out some IPv6 routes (matching prefix-a-v6-2) based on the original filter and permit these routes to match the route-policy. However, all IPv4 routes accidentally match the route-policy.

In the preceding scenarios, if the same route-policy is used to filter both IPv4 and IPv6 routes, the expected result can be obtained. However, if you keep this configuration habit for a long time, services may be interrupted due to improper use of services.

In some scenarios, the same route-policy is used to filter both IPv4 and IPv6 routes. However, some nodes have only IPv4 if-match clauses, and some nodes have only IPv6 if-match clauses. As a result, unexpected results are more likely to occur. A typical application scenario is as follows:

Scenario 3: A route-policy matches only IPv4 routes, but the route-policy is referenced by IPv6.For example:

#route-policy policy1 deny node 10if-match ip-prefix prefix-a#route-policy policy1 permit node 30

Explanation:a. In an IPv4 scenario, node 10 is preferentially matched based on the route-policy. IPv4 routes that match ip-prefix prefix-a are denied. The IPv4 routes that do not match ip-prefix prefix-a match node 30 and are permitted. This problem does not occur in all IPv4 scenarios.b. In the IPv6 scenario, node 10 is preferentially matched based on the route-policy. There is no if-match clause for IPv6 routes on node 10. By default, all IPv6 routes match the if-match clause. However, the mode of node 10 is deny. Therefore, all IPv6 routes are denied. In this scenario, node 30 is not executed based on the unique matching rule of the route-policy. The final result is that no IPv6 route matches the route-policy.In conclusion, the IPv4 routes that do not match ip-prefix prefix-a are permitted, and the other IPv4 routes and all IPv6 routes are denied.

Scenario 4: A route-policy matches only IPv6 routes, but the route-policy is referenced by IPv4.For example:

#route-policy policy1 deny node 20if-match ipv6 address prefix-list prefix-a-v6#route-policy policy1 permit node 30

Explanation:a. In IPv6 scenarios, node 20 is preferentially matched based on the route-policy. IPv6 routes that match prefix-list prefix-a-v6 are denied. The IPv6 routes that do not match prefix-list prefix-a-v6 are matched against node 30 and are permitted. This problem does not occur in all IPv6 scenarios.b. In an IPv4 scenario, node 20 is preferentially matched based on the route-policy. There is no if-match clause for IPv4 routes on node 20. By default, all IPv4 routes match the if-match clause. However, the mode of node 20 is deny. Therefore, all IPv4 routes are denied. In this scenario, node 30 is not executed based on the unique matching rule of the route-policy. The final result is that no IPv4 route matches the route-policy.In conclusion, the IPv6 routes that do not match prefix-list prefix-a-v6 are permitted, and the other IPv4 routes and all IPv6 routes are denied.

Scenario 5: In the same route-policy, some nodes match IPv4 routes, and some nodes match IPv6 routes. Some routes that are expected to be permitted are blocked by the deny node in advance because they do not match the address family.For example:

#route-policy policy1 deny node 10if-match ip-prefix prefix-a#route-policy policy1 deny node 20if-match ipv6 address prefix-list prefix-a-v6#route-policy policy1 permit node 30

Explanation:a. In an IPv4 scenario, node 10 is preferentially matched based on the route-policy. IPv4 routes that match ip-prefix prefix-a are denied. The IPv4 routes that do not match ip-prefix prefix-a are matched against node 20. Node 20 does not have if-match clauses for IPv4 routes. By default, all IPv4 routes match the if-match clauses. However, the mode of node 20 is deny, IPv4 routes that are not in the ip-prefix prefix-a range are also denied. In this scenario, node 30 is not executed based on the unique matching rule of the route-policy. The final result is that no IPv4 route matches the route-policy.b. In an IPv6 scenario, node 10 is preferentially matched based on the route-policy. Node 10 does not have an if-match clause for IPv6 routes. By default, all IPv6 routes match the if-match clause. However, the mode of node 10 is deny, all IPv6 routes are denied. According to the unique matching rule of the route-policy, node 20 and node 30 are not executed in this scenario. The final result is that no IPv6 route matches the route-policy.In conclusion, all IPv4 or IPv6 routes are denied in this scenario.

Scenario 6: In the same route-policy, some nodes match IPv4 routes, and some nodes match IPv6 routes. Some routes that are expected to be denied are blocked by the permit node in advance because they do not match the address family.For example:

#route-policy policy1 permit node 10if-match ip-prefix prefix-a#route-policy policy1 permit node 20if-match ipv6 address prefix-list prefix-a-v6#route-policy policy1 deny node 30

Explanation:a. In an IPv4 scenario, node 10 is preferentially matched based on the route-policy. IPv4 routes that match ip-prefix prefix-a are permitted. IPv4 routes that do not match ip-prefix prefix-a are matched against node 20. Node 20 does not have if-match clauses for IPv4 routes. By default, all IPv4 routes match the if-match clauses. The mode of node 20 is permit, IPv4 routes that are not in the ip-prefix prefix-a range are also permitted. In this scenario, node 30 is not executed based on the unique matching rule of the route-policy. All IPv4 routes can match the route-policy.b. In IPv6 scenarios, node 10 is preferentially matched based on the route-policy. Node 10 does not have if-match clauses for IPv6 routes. By default, all IPv6 routes match the if-match clauses. The mode of node 10 is permit, all IPv6 routes are permitted. According to the unique matching rule of the route-policy, node 20 and node 30 are not executed in this scenario. All IPv6 routes can match the route-policy.In conclusion, all IPv4 or IPv6 routes are permitted in this scenario.The preceding analysis shows that when IPv4 and IPv6 use the same route-policy, unexpected results may occur due to the default matching rule of the if-match clause. Therefore, you are advised to use different route-policies for IPv4 and IPv6.

In some special service scenarios, only one route-policy can be used. In this case, you are advised to run the **route-policy address-family mismatch-deny** command before running the route-policy command.For example, in a BGP EVPN scenario, BGP EVPN peers do not distinguish between IPv4 and IPv6. A peer relationship can transmit both IPv4 and IPv6 routes. In this case, only one route-policy can be used.

In this scenario, to prevent service interruption caused by improper configurations, you are advised to use the following configuration methods:

#route-policy policy1 permit node 10if-match ip-prefix prefix-a#route-policy policy1 permit node 20if-match ipv6 address prefix-list prefix-a-v6#route-policy policy1 deny node 30#route-policy policy1 address-family mismatch-deny

Explanation:After the **route-policy address-family mismatch-deny** command is run, if the address family of a route does not match the address family specified in the if-match clause of the routing policy, the matching fails.a. In an IPv4 scenario, node 10 is preferentially matched based on the route-policy. The IPv4 routes that match ip-prefix prefix-a match the if-match clause, and therefore are permitted. Other IPv4 routes that do not match ip-prefix prefix-a continue to match node 20. There is no matching rule for IPv4 routes on node 20. In addition, these IPv4 routes fail to match node 20 because the **route-policy address-family mismatch-deny** command is run. Then, the IPv4 routes that do not match ip-prefix prefix-a continue to match node 30. Node 30 does not have matching rules for IPv4 routes. In addition, these IPv4 routes fail to match node 30 because the **route-policy address-family mismatch-deny** command is run. In conclusion, the other IPv4 routes that do not match ip-prefix prefix-a are denied by Route-Policy policy1.b. In IPv6 scenarios, node 10 is preferentially matched based on the route-policy. There is no matching rule for IPv6 routes on node 10. In addition, these IPv6 routes fail to match node 10 because the **route-policy address-family mismatch-deny** command is configured. Then, all IPv6 routes continue to match node 20. The IPv6 routes that match prefix-list prefix-a-v6 match the if-match clause, and are permitted by node 20. Then, other IPv6 routes that do not match ip-prefix prefix-a-v6 continue to match node 30. Node 30 does not have matching rules for IPv6 routes. In addition, these IPv6 routes fail to match node 30 because the **route-policy address-family mismatch-deny** command is run. In conclusion, the other IPv6 routes that do not match ip-prefix prefix-a-v6 are denied by Route-Policy policy1.The preceding analysis shows that in the BGP EVPN scenario, routes can be accurately filtered based on the preceding configuration. To add IPv4 filtering conditions in subsequent service expansion, you can add an if-match clause under node 10 or add an IPv4 filtering node. To add an IPv6 filtering condition, add an if-match clause under node 20 or add an IPv6 filtering node.



**Precautions**

* You can run the **display route-policy** command to check the number of routes permitted and denied by the filter.
* If a route-policy clause contains only ip-prefix matching conditions, only IPv4 prefixes are checked. If no IPv6 prefix matching condition is specified, all routes are permitted by default. If IPv6 prefixes also need to be filtered, add an if-match clause to filter IPv6 prefixes. Similarly, if a route-policy clause contains an ipv6-prefix matching condition, only IPv6 prefixes are checked. If the IPv4 prefix matching condition is empty, all routes pass the check by default. If IPv4 prefixes also need to be filtered, add an if-match clause to filter IP prefixes.
* When a route-policy is used to control the advertisement or receiving of BGP routes, the priority of the peer-specific configuration is higher than that of a peer group-specific configuration.
* In the scenario where an if-match clause references a matching rule, if the referenced matching rule contains only the deny index, the current policy node is skipped and routes are matched against the next route-policy node.
* The device considers that each unmatched route fails to match the route-policy by default. If more than one node is defined in a route-policy, at least one node must be in permit mode.If a policy node is not configured with any if-match or goto clause, the subsequent policy node with a larger index cannot be executed. As a result, the configuration may be incorrect. Example:route-policy test permit node 10apply community 100route-policy test permit node 20apply community 200In this case, the node 20 cannot be executed.If a route-policy is configured with multiple policy nodes with the same configuration, the configuration may be incorrect. Example:route-policy test permit node 10apply community 100route-policy test permit node 20apply community 100

The following if-match clauses may be used to filter both IPv4 and IPv6 routes in a route-policy: if-match clauses for prefix matching, nexthop matching, source matching, and ACL matching. The following uses prefix-based if-match clauses as an example to describe unexpected situations that may occur when a route-policy filters both IPv4 and IPv6 routes. The method of configuring other if-match clauses is similar to that of configuring prefix-based if-match clauses. The configuration principles are as follows:

1. It is not recommended that you use the same route-policy to filter both IPv4 and IPv6 routes.
2. In service scenarios where only one route-policy can be used, you are advised to run the **route-policy address-family mismatch-deny** command before running the route-policy command.

After a route-policy node is created, deleted, or configured, if all nodes in the route-policy are permit nodes and if-match is not configured, the route-policy is a permit-all policy. If the permit-all policy is applied, all routes may pass the policy, which may cause problems such as overload.After a route-policy node is created, deleted, or configured, if all nodes in the route-policy are deny nodes, this policy is a deny-all policy. If this policy is applied, all routes fail to pass the policy. As a result, routes may be unreachable.



Example
-------

# Configure the route-policy named policy1 whose node number is 10 and matching mode is permit.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix-a index 10 permit 172.17.1.0 24
[*HUAWEI] route-policy policy1 permit node 10
[*HUAWEI-route-policy] if-match ip-prefix prefix-a
[*HUAWEI-route-policy] apply cost 100

```