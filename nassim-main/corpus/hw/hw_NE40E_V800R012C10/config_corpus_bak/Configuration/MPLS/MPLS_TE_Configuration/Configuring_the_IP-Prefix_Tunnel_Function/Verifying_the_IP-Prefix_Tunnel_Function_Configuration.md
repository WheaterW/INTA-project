Verifying the IP-Prefix Tunnel Function Configuration
=====================================================

After configuring the IP-prefix tunnel function, verify the tunnel information, including the tunnel status, a P2P TE tunnel template used to establish tunnels, and IP prefix list.

#### Prerequisites

The IP-prefix tunnel function has been configured.
#### Operations

**Table 1** Items to be checked and related commands
| Operation | Command |
| --- | --- |
| Check the configuration of a P2P TE tunnel template. | [**display mpls te p2p-template**](cmdqueryname=display+mpls+te+p2p-template) |
| Check whether P2P TE tunnels are successfully established using the automatic primary tunnel function. | [**display mpls te tunnel**](cmdqueryname=display+mpls+te+tunnel) |
| Check detailed information about the automatic primary tunnel function. | [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) [ **auto-primary-tunnel** [ *tunnel-name* ] ] |