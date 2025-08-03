isis lsp flood-control max-count
================================

isis lsp flood-control max-count

Function
--------



The **isis lsp flood-control max-count** command setd the maximum number of LSPs that IS-IS sends every second.

The **undo isis lsp flood-control max-count** command restores the maximum number of LSPs that IS-IS sends every second to the default value.



By default, IS-IS is enabled to adjust the flooding rate, and the maximum number of LSPs to be flooded per second is 3000.


Format
------

**isis lsp flood-control max-count** *max-count-value*

**undo isis lsp flood-control max-count** [ *max-count-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-count-value* | Specifies the maximum number of LSPs flooded by IS-IS per second. | The value is an integer that ranges from 1000 to 30000. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a scenario where a large number of LSPs need to be flooded at a time, for example, in a large-scale network topology, due to the limit on the maximum number of LSPs that can be sent by IS-IS every second, the time taken to flood a large number of LSPs may exceed the expected value, which affects the convergence efficiency of the entire network. You can run a command to adjust the maximum IS-IS flooding rate to increase the maximum number of LSPs that can be sent per second during IS-IS flooding. This improves IS-IS flooding efficiency and speeds up network convergence.When the flooding pressure on the network is heavy and flow control is required, you can run commands to reduce the maximum number of LSPs sent by IS-IS per second to slow down the IS-IS flooding rate and relieve the flooding pressure on nodes.


Example
-------

# Restore the IS-IS flooding rate to the default value, set the maximum number of LSPs to be sent per second to 3000, and configure the LSPs not to carry configuration data.
```
<HUAWEI> system-view
[~HUAWEI] undo isis lsp flood-control max-count

```

# Restore the IS-IS flooding rate to the default value, set the maximum number of LSPs to be sent per second to 3000, and configure the LSPs to carry configuration data.
```
<HUAWEI> system-view
[~HUAWEI] undo isis lsp flood-control max-count 5000

```

# Set the maximum number of LSPs that can be sent per second to 5000.
```
<HUAWEI> system-view
[~HUAWEI] isis lsp flood-control max-count 5000

```