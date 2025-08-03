set flow-statistics include-interframe
======================================

set flow-statistics include-interframe

Function
--------



The **set flow-statistics include-interframe** command configures traffic statistics on an interface to contain the inter-frame gap and preamble.

The **undo set flow-statistics include-interframe** command configures traffic statistics on an interface not to contain the inter-frame gap and preamble.



By default, traffic statistics on an interface contain the inter-frame gap and preamble.


Format
------

**set flow-statistics include-interframe**

**undo set flow-statistics include-interframe**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run the **display interface** command to view the running status and traffic statistics on an interface. The Last 300 seconds input rate and Last 300 seconds output rate fields in the command output indicate the inbound and outbound traffic rates on the interface in the last 300 seconds.

To obtain the total number of bytes (including the number of packet bytes and the fixed lengths of the IFG and preamble) passing through an interface per second, configure collection of traffic statistics that include the IFG and preamble. The interface's traffic rate is then calculated as follows: Interface's traffic rate = (Original packet length + IFG length + Preamble length) x Number of packets passing through the interface per second

To obtain only the number of packet bytes (excluding the fixed lengths of the IFG and preamble) passing through an interface per second, configure collection of traffic statistics that exclude the IFG and preamble. The interface's traffic rate is then calculated as follows: Interface's traffic rate = Original packet length x Number of packets passing through the interface per second

By default, the IFG has a fixed value of 12 bytes and the preamble has a fixed value of 8 bytes. You can run the **ifg** command to configure the IFG.


Example
-------

# Configure traffic statistics on 100GE 1/0/1 to contain the inter-frame gap and preamble.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] set flow-statistics include-interframe

```