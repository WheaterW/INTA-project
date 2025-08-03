Verifying the Tunnel Protection Group Configuration
===================================================

After configuring a tunnel protection group, run display commands to view information about the tunnel protection group and the binding between the working and protection tunnels.

#### Prerequisites

A tunnel protection group has been configured.
#### Procedure

1. Run the [**display mpls
   te protection tunnel**](cmdqueryname=display+mpls+te+protection+tunnel) { **all** | *tunnel-id* | **interface** *tunnel-interface-name* } [ **verbose** ] command to check information about a tunnel protection group.
2. Run the [**display mpls te protection binding protect-tunnel**](cmdqueryname=display+mpls+te+protection+binding+protect-tunnel) { *tunnel-id* | **interface** *tunnel-interface-name* } command to check the binding between the working and protection tunnels.