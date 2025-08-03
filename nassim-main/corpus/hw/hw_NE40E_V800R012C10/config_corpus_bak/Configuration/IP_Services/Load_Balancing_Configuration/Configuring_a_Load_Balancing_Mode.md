Configuring a Load Balancing Mode
=================================

Configuring_a_Load_Balancing_Mode

#### Configuring Per-packet Load Balancing

By default, the Huawei NE40E's control and forwarding planes both work in per-flow load balancing mode. You can configure the commands shown in [Table 1](#EN-US_CONCEPT_0172365000__table1934134692514) to change the mode to per-packet.

**Table 1** Configuring per-packet load balancing
| View | Command Format | Influence Scope | Description |
| --- | --- | --- | --- |
| System view | [**load-balance**](cmdqueryname=load-balance) **packet** { **slot** *slot-id* | **all** } | * Forwarding plane. This command takes effect only for MPLS packets on P nodes. * Control plane. This command takes effect for both IP and MPLS packets delivered by the CPU. | The load balancing mode is changed to per-packet. |
| Interface view | [**mpls l2vpn load-balance packet**](cmdqueryname=mpls+l2vpn+load-balance+packet) | LDP and SVC VLL traffic received by the interface | Before this command is run, configure an LDP or SVC VLL on the interface and configure a tunnel policy for the L2VPN. |



#### Configuring Per-flow Load Balancing

By default, the Huawei NE40E's control and forwarding planes both work in per-flow load balancing mode. You can configure the commands shown in [Table 2](#EN-US_CONCEPT_0172365000__tab_05002) to change the mode to per-flow if the mode has been changed to per-packet.

**Table 2** Configuring per-flow load balancing
| View | Command Format | Influence Scope | Description |
| --- | --- | --- | --- |
| System view | [**load-balance**](cmdqueryname=load-balance) **flow** { **slot** *slot-id* | **all** } | * Forwarding plane. This command takes effect only for MPLS packets on P nodes. * Control plane. This command takes effect for both IP and MPLS packets delivered by the CPU. | The load balancing mode is changed to per-flow. |
| Interface view | [**undo mpls l2vpn load-balance packet**](cmdqueryname=undo+mpls+l2vpn+load-balance+packet) | LDP and SVC VLL traffic received by the interface | Before this command is run, configure an LDP or SVC VLL on the interface and configure a tunnel policy for the L2VPN. |
| Layer 3 Eth-Trunk interface view | [**load-balance**](cmdqueryname=load-balance) **src-dst-ip** or **undo load-balance** | Traffic sent by the interface on which the command is run | By default, Layer 3 Eth-Trunk interfaces perform per-flow load balancing based on IP addresses. |



#### Configuring Load Balancing on a BAS Interface

**Table 3** Configuring load balancing on a BAS interface
| View | Command Format | Influence Scope |
| --- | --- | --- |
| Eth-Trunk interface view | [**bas-load-balance**](cmdqueryname=bas-load-balance) { **flow-mode** | **user-mode** | **real-flow-mode** } | BAS user online traffic |



#### Follow-up Procedure

Run the [**save**](cmdqueryname=save) command to save the current configuration to the configuration file when a set of configuration is finished and the expected functions have been achieved.