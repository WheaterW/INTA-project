isis srlg
=========

isis srlg

Function
--------

The **isis srlg** command adds an interface to a shared risk link group (SRLG).

The **undo isis srlg** command deletes an interface from an SRLG.

By default, an interface is not added to any SRLG.



Format
------

**isis srlg** *srlg-value*

**undo isis srlg** [ *srlg-value* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *srlg-value* | Specifies an SRLG ID. | The value is an integer ranging from 0 to 4294967295. |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

An SRLG is a set of links that share a common physical resource, such as an optical fiber. These links share the same risk level. If one of the links fails, all the other links in the SRLG may also fail.

If two links have the same risk of failure, you can run the isis srlg command on each of the links' interfaces to add the links to the same SRLG. Then, configure IS-IS to preferentially select a backup link not in the same SRLG as the specified link during route calculation in Auto FRR, reducing the possibility of network traffic interruption.

**Prerequisites**

IS-IS has been enabled on the interface using the **isis enable** command in the interface view.

**Follow-up Procedure**

Run the **tiebreaker srlg-disjoint preference** command to configure IS-IS to preferentially select a backup link not in the same SRLG during route calculation in Auto FRR.



Example
-------

# Add
100GE
1/0/1 to SRLG1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis srlg 1

```