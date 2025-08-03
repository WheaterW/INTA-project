Understanding BGP Recursion Suppression in Case of Next Hop Flapping
====================================================================

Understanding BGP Recursion Suppression in Case of Next Hop Flapping

#### Context

In some scenarios, a large number of routes may recurse to the same next hop. If the next hop flaps due to a device fault, the system will become occupied processing reselection and re-advertisement of each involved route, leading to excessive resource consumption and high CPU usage. To address this problem, enable BGP recursion suppression in case of next hop flapping.


#### Fundamentals

After BGP recursion suppression in case of next hop flapping is enabled, a BGP device determines whether to increase, retain, or reduce the penalty value by comparing the flapping interval with the configured interval. When the penalty value exceeds 10, the BGP device suppresses route recursion to the corresponding next hop. For example, if the intervals for increasing, retaining, and clearing the penalty value are T1, T2, and T3, respectively, a BGP device calculates the penalty value as follows:

* Increases the penalty value by 1 if the flapping interval is less than T1.
* Retains the penalty value if the flapping interval is greater than or equal to T1, but less than T2.
* Reduces the penalty value by 1 if the flapping interval is greater than or equal to T2, but less than T3.
* Clears the penalty value if the flapping interval is greater than or equal to T3.

When the penalty value exceeds 10, the system slows down how quickly it processes reselection and re-advertisement of the routes that are recursed to a flapping next hop.


#### Benefits

BGP recursion suppression in case of next hop flapping prevents the system from frequently processing reselection and re-advertisement of a large number of routes that are recursed to a flapping next hop, reducing system resource consumption and CPU usage.