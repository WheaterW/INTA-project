Resetting IPv6 IS-IS
====================

Resetting IPv6 IS-IS

#### Context

Resetting IPv6 IS-IS includes restarting IPv6 IS-IS processes, resetting IPv6 IS-IS neighbor relationships, and clearing IPv6 IS-IS packet information. For details, see [Table 1](#EN-US_TASK_0000001130622646__table1451120547137).

![](public_sys-resources/note_3.0-en-us.png) 

If IPv6 IS-IS is reset, all involved neighbor relationships and LSDBs are re-established. Therefore, exercise caution when resetting IPv6 IS-IS.

Resetting an IPv6 IS-IS neighbor relationship interrupts it. Therefore, exercise caution when resetting an IPv6 IS-IS neighbor relationship.


**Table 1** Resetting IPv6 IS-IS
| Operation | Command |
| --- | --- |
| Restart an IPv6 IS-IS process. | [**reset isis all**](cmdqueryname=reset+isis+all) [ *process-id* | **vpn-instance** *vpn-instance-name* ]  [**reset isis**](cmdqueryname=reset+isis) *process-id* **all** |
| Reset an IPv6 IS-IS neighbor relationship. | [**reset isis peer**](cmdqueryname=reset+isis+peer) *system-id* [ *process-id* | **vpn-instance** *vpn-instance-name* ]  [**reset isis**](cmdqueryname=reset+isis) *process-id* **peer** *system-id* |
| Clear information about error LSPs and error Hello packets received by a specified interface or process. | [**reset isis error**](cmdqueryname=reset+isis+error) [ *process-id* | **vpn-instance** *vpn-instance-name* ]  [**reset isis error**](cmdqueryname=reset+isis+error) **interface** *interface-type* *interface-number* |
| Clear IPv6 IS-IS statistics on a specified interface. | [**reset isis statistics**](cmdqueryname=reset+isis+statistics) { **packet** | **socket** } [ **interface** [ *interface-type* *interface-number* ] ] |
| Clear IPv6 IS-IS statistics on a specified process. | [**reset isis**](cmdqueryname=reset+isis) [ *process-id* ] **statistics packet** [ **lsp** ]  [**reset isis statistics**](cmdqueryname=reset+isis+statistics) **packet** **lsp** [ *process-id* ] |
| Configure an interface to exit IPv6 IS-IS neighbor relationship flapping suppression. | [**reset isis**](cmdqueryname=reset+isis) *process-id* **suppress-flapping peer** [ *interface-type* *interface-number* ] [ **notify-peer** ] |