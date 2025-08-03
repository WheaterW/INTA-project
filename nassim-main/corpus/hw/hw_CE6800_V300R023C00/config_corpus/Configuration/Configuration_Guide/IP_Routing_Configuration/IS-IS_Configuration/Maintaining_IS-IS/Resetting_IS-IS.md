Resetting IS-IS
===============

Resetting IS-IS

#### Context

Resetting IS-IS includes restarting IS-IS processes, resetting IS-IS neighbor relationships, and clearing IS-IS packet information. For details, see [Table 1](#EN-US_TASK_0000001130624344__table1451120547137).

![](public_sys-resources/note_3.0-en-us.png) 

If an IS-IS process is restarted, all involved neighbor relationships and structure information are reset. Therefore, exercise caution when restarting an IS-IS process.

Resetting an IS-IS neighbor relationship interrupts it. Therefore, exercise caution when resetting an IS-IS neighbor relationship.


**Table 1** Resetting IS-IS
| Operation | Command |
| --- | --- |
| Restart an IS-IS process. | [**reset isis all**](cmdqueryname=reset+isis+all) [ *process-id* | **vpn-instance** *vpn-instance-name* ]  [**reset isis**](cmdqueryname=reset+isis) *process-id* **all** |
| Reset an IS-IS neighbor relationship. | [**reset isis peer**](cmdqueryname=reset+isis+peer) *system-id* [ *process-id* | **vpn-instance** *vpn-instance-name* ]  [**reset isis**](cmdqueryname=reset+isis) *process-id* **peer** *system-id* |
| Clear information about error LSPs and error Hello packets received by a specified interface or process. | [**reset isis error**](cmdqueryname=reset+isis+error) [ *process-id* | **vpn-instance** *vpn-instance-name* ]  [**reset isis error**](cmdqueryname=reset+isis+error) **interface** *interface-type* *interface-number* |
| Clear IS-IS statistics on a specified interface. | [**reset isis statistics**](cmdqueryname=reset+isis+statistics) { **packet** | **socket** } [ **interface** [ *interface-type* *interface-number* ] ] |
| Clear IS-IS statistics on a specified process. | [**reset isis**](cmdqueryname=reset+isis) [ *process-id* ] **statistics packet** [ **lsp** ]  [**reset isis statistics**](cmdqueryname=reset+isis+statistics) **packet** **lsp** [ *process-id* ] |
| Configure an interface to exit IS-IS neighbor relationship flapping suppression. | [**reset isis**](cmdqueryname=reset+isis) *process-id* **suppress-flapping peer** [ *interface-type* *interface-number* ] [ **notify-peer** ] |