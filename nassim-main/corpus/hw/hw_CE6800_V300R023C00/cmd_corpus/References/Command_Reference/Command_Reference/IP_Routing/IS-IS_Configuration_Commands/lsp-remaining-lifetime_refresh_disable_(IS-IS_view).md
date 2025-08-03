lsp-remaining-lifetime refresh disable (IS-IS view)
===================================================

lsp-remaining-lifetime refresh disable (IS-IS view)

Function
--------



The **lsp-remaining-lifetime refresh disable** command disables automatic IS-IS LSP Remaining Lifetime adjustment.

The **undo lsp-remaining-lifetime refresh disable** command enables automatic IS-IS LSP Remaining Lifetime adjustment.



By default, automatic IS-IS LSP Remaining Lifetime adjustment is enabled.


Format
------

**lsp-remaining-lifetime refresh disable**

**undo lsp-remaining-lifetime refresh disable**


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

If the Remaining Lifetime field of LSPs is abnormal, LSP flapping or a route calculation error may occur. For example, if the abnormal Remaining Lifetime is 500s and the actual Remaining Lifetime is 1200s, LSPs are aged prematurely. To address this problem, automatic IS-IS LSP Remaining Lifetime adjustment is enabled by default. If the Remaining Lifetime in a received LSP is less than the locally configured maximum LSP age, IS-IS changes the Remaining Lifetime in the LSP to the locally configured maximum LSP age by default until the Remaining Lifetime values of all LSPs in the area become the same. In this case, routes can be calculated correctly.


Example
-------

# Disable automatic IS-IS LSP Remaining Lifetime adjustment.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] lsp-remaining-lifetime refresh disable

```