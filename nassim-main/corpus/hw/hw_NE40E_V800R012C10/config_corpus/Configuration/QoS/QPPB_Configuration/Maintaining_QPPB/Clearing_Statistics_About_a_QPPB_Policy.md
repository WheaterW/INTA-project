Clearing Statistics About a QPPB Policy
=======================================

This section describes how to clear statistics about a
QPPB policy on an interface.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) Once deleted, statistics cannot be restored.
Therefore, exercise caution when deleting statistics.

#### Procedure

1. Run the [**reset
   qppb local-policy statistics interface**](cmdqueryname=reset+qppb+local-policy+statistics+interface) *interface-type* *interface-number* [ **qos-local-id** *qos-local-id* ] { **inbound** | **outbound** } command in the user view
   to clear statistics about a QPPB local policy on the specified interface.