tlv-fragments disable
=====================

tlv-fragments disable

Function
--------



The **tlv-fragments disable** command disables IS-IS TLV fragmentation.

The **undo tlv-fragments disable** command restores the default configuration.



By default, IS-IS TLV fragmentation is enabled.


Format
------

**tlv-fragments disable**

**undo tlv-fragments disable**


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

IS-IS TLV fragmentation is enabled by default. Due to the limitation on the packet format, an IS-IS LSP TLV can contain a maximum of 255 bytes (including the main TLV information). If the TLV fragmentation function is enabled, multiple TLVs carrying the same unit information can be advertised in the same LSP fragment.

**Precautions**

If the TLV fragmentation setting is changed, LSP information may change, causing a reset of the IS-IS instance.


Example
-------

# Disable IS-IS TLV fragmentation.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] tlv-fragments disable

```