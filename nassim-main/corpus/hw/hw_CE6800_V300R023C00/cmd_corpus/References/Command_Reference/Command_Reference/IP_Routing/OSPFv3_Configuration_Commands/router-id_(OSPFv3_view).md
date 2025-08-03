router-id (OSPFv3 view)
=======================

router-id (OSPFv3 view)

Function
--------



The **router-id** command sets a router ID for the router that runs OSPFv3.

The **undo router-id** command deletes the router ID that is set for an OSPFv3 router.



By default, no router ID is configured for the router that runs OSPFv3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**router-id** *router-id*

**undo router-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *router-id* | Specifies a router ID. | The value is in dotted decimal notation. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The router ID of each OSPFv3 process is unique in an AS. If no router ID is set, no OSPFv3 process can be run.


Example
-------

# Set the router ID to 10.1.1.3 for OSPFv3 process 1.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] router-id 10.1.1.3

```