adjacency-strict-check
======================

adjacency-strict-check

Function
--------



The **adjacency-strict-check enable** command enables IS-IS neighbor strict-check.

The **undo adjacency-strict-check enable** command disables IS-IS neighbor strict-check.

The **adjacency-strict-check disable** command disables IS-IS neighbor strict-check.



By default, IS-IS neighbor strict-check is disabled when IS-IS is establishing neighbor relationships.


Format
------

**adjacency-strict-check enable**

**adjacency-strict-check disable**

**undo adjacency-strict-check** [ **enable** ]


Parameters
----------

None

Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During the establishment of IS-IS neighbor relationships, if both IPv4 and IPv6 are configured at both ends, both IPv4 and IPv6 neighbors are established. By default, IPv4 and IPv6 share the standard topology. If the link between the two ends fails and then recovers, IPv4 goes Up faster than IPv6. When one end receives a message indicating that IPv4 goes Up, it considers that both IPv4 and IPv6 neighbors are restored. If the end sends IPv6 packets to the other end, these IPv6 packets are discarded.To resolve this problem, run the **adjacency-strict-check enable** command to enable IS-IS adjacency strict-check to ensure that an IS-IS neighbor is established only when both IPv4 and IPv6 go Up.

**Prerequisites**

An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.The command must be used with the ipv6 enable topology standard command.

**Configuration Impact**

After you run the **adjacency-strict-check enable** command on a broadcast network, the base topology becomes Down by not publishing the neighbor information, if the IP protocol enabled on the local router is different from that on its neighbors.After you run the **adjacency-strict-check enable** command on a P2P network, neighbor relationships cannot be established if the IP protocol enabled on the local router is different from that on its neighbors and only the base topology is available on the local router.

**Precautions**

The undo adjacency-strict-check [ enable ] and undo adjacency-strict-check commands have the same function.


Example
-------

# Enable neighbor strict-check for IS-IS process 1.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] adjacency-strict-check enable

```