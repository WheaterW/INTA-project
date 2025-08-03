Clearing CMP Session Statistics
===============================

To re-collect CMP session statistics within a specific
period, clear existing CMP session statistics.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) CMP session statistics cannot be restored
after they are cleared. Exercise caution when running
the [**reset pki cmp
statistics**](cmdqueryname=reset+pki+cmp+statistics) command. Before running the [**reset pki cmp statistics**](cmdqueryname=reset+pki+cmp+statistics) command, run the [**display pki cmp statistics**](cmdqueryname=display+pki+cmp+statistics+session) **session** *session-name* command to
check whether the CMP session statistics to be cleared are still required.

#### Procedure

1. Run the [**reset pki cmp statistics**](cmdqueryname=reset+pki+cmp+statistics+session) **session** *session-name* command to clear CMP session statistics.