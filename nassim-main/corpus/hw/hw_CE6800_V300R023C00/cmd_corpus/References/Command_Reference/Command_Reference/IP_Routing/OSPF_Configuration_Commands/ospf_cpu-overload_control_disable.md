ospf cpu-overload control disable
=================================

ospf cpu-overload control disable

Function
--------



The **ospf cpu-overload control disable** command disables OSPF CPU overload control.

The **undo ospf cpu-overload control disable** command restores the default configuration.



By default, OSPF CPU overload control is enabled.


Format
------

**ospf cpu-overload control disable**

**undo ospf cpu-overload control disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a device's CPU is overloaded, each module needs to take necessary measures to control its own CPU usage accordingly. Upon receiving a CPU overload notification from the system, the OSPF module controls the speeds of some internal computing processes and the establishment of neighbor relationships based on the CPU overload condition to enhance the resilience of OSPF. In this case, new neighbor relationships cannot be established. For original neighbor relationships, if a neighbor relationship is in the Full state, it will be retained; if a neighbor relationship is in a non-Full state, establishment of the neighbor relationship is paused and can continue only after the CPU recovers from overload.

**Precautions**

The ospf cpu-overload control disable command takes effect for both OSPF and OSPFv3.


Example
-------

# Disable OSPF CPU overload control.
```
<HUAWEI> system-view
[~HUAWEI] ospf cpu-overload control disable

```