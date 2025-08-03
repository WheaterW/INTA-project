Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] **v-stp** command to check the V-STP status and statistics.
* Run the [**display dfs-group**](cmdqueryname=display+dfs-group) *dfs-group-id* **node** *node-id* **stp** { **brief** | **global** | **m-lag** *m-lag-id* [ **brief** ] } command to check STP information about all nodes in a DFS group.
* Run the [**display dfs-group**](cmdqueryname=display+dfs-group) [ *dfs-group-id* ] [ **node** *node-id* ] **m-lag** **brief** command to check information about an M-LAG.
* Run the [**display dfs-group**](cmdqueryname=display+dfs-group) *dfs-group-id* [**peer-link**](cmdqueryname=peer-link) command to check information about the peer-link in an M-LAG.
* Run the [**display dfs-group**](cmdqueryname=display+dfs-group) *dfs-group-id* **lacp system-id m-lag** *m-lag-id* command to check M-LAG LACP system ID and priority information.
* Run the [**display dfs-group consistency-check**](cmdqueryname=display+dfs-group+consistency-check) { **global** | **interface** { **m-lag** *m-lag-id* | **peer-link** *peer-linkid* } | **static-arp** | **static-mac** } command to check the configuration of the M-LAG master and backup devices.
* Run the [**display dfs-group consistency-check status**](cmdqueryname=display+dfs-group+consistency-check+status) command to check the running status of M-LAG configuration consistency check.
* Run the [**display dfs-group consistency-check packet configuration**](cmdqueryname=display+dfs-group+consistency-check+packet+configuration) command to check the status of packet sending and receiving for M-LAG consistency check.
* Run the **[**display m-lag consistency-check whitelist status**](cmdqueryname=display+m-lag+consistency-check+whitelist+status)** command to check the whitelist for M-LAG configuration consistency check.
* Run the [**display dfs-group**](cmdqueryname=display+dfs-group) *dfs-group-id* **m-lag check stp** command to check whether the STP configurations on the local and peer M-LAG member devices are consistent.
* Run the [**display dfs-group**](cmdqueryname=display+dfs-group) *dfs-group-id* **heartbeat** command to check the HB DFS information negotiated by M-LAG member devices through the DAD link.
* Run the [**display dfs packet statistics**](cmdqueryname=display+dfs+packet+statistics) command to check the number of received and sent packets about M-LAG interface status changes.
* Run the [**display dfs partner**](cmdqueryname=display+dfs+partner) command to check the PID, status and other information about the external components interacting with the DFS module.