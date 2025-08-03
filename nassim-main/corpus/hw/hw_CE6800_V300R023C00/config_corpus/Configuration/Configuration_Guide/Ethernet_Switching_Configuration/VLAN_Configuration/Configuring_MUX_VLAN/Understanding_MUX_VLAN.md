Understanding MUX VLAN
======================

Understanding MUX VLAN

#### Background

Multiplex VLAN (MUX VLAN) provides a mechanism to control network resources based on VLANs.

For example, an enterprise network administrator allows both employees and customers to access servers on the network. Employees are allowed to communicate with each other, but customers are isolated from each other. In this case, inter-VLAN communication can be configured to allow all users to access servers on the enterprise network. If the enterprise has numerous users, many VLAN IDs need to be allocated to customers even though they cannot communicate with each other. This wastes VLAN IDs and complicates network maintenance.

MUX VLAN provides a Layer 2 traffic isolation mechanism to isolate customers from each other while still allowing employees to communicate with each other.


#### Basic Concepts

MUX VLAN involves the concepts of principal and subordinate VLANs. Subordinate VLANs are classified into separate VLANs and group VLANs. [Table 1](#EN-US_CONCEPT_0000001130782624__tab_dc_fd_vlan_001001) describes these concepts.

**Table 1** MUX VLAN concepts
| MUX VLAN | VLAN Type | Associated Port | Communication Permission |
| --- | --- | --- | --- |
| Principal VLAN | - | Principal port | A principal port can communicate with all ports in MUX VLAN. |
| Subordinate VLAN | Separate VLAN | Separate port | A separate port can communicate only with a principal port and is isolated from other types of ports.  Each separate VLAN must be bound to a principal VLAN. |
| Group VLAN | Group port | A group port can communicate with a principal port and other ports in the same group, but cannot communicate with ports in other groups or a separate port.  Each group VLAN must be bound to a principal VLAN. |