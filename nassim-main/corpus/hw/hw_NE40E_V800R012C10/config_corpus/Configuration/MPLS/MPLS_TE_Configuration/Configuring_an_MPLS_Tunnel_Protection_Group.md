Configuring an MPLS Tunnel Protection Group
===========================================

This section describes how to configure a tunnel protection group. A protection tunnel can be bound to a working tunnel to form a tunnel protection group. If the working tunnel fails, traffic switches to the protection tunnel. The tunnel protection group helps improve tunnel reliability.

#### Usage Scenario

A tunnel protection group provides end-to-end protection for traffic transmitted along TE tunnel. If a working tunnel fails, bidirectional automatic protection switching switches traffic to the protection tunnel.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In an MPLS OAM for associated or co-routed LSP scenario where tunnel APS is configured, if the primary and backup tunnels use the same path and the path fails, both the tunnels are affected, and services may be interrupted.

A protected tunnel is called a working tunnel. A tunnel that protects the working tunnel is called a protection tunnel. The working and protection tunnels form a tunnel protection group. A tunnel protection group works in 1:1 mode. In 1:1 mode, one protection tunnel protects only one working tunnel.

* Working and protection tunnels
  
  Tunnel-specific attributes in a tunnel protection group are independent from each other. For example, a protection tunnel with bandwidth 50 Mbit/s can protect a working tunnel with 100 Mbit/s bandwidth.
  
  TE FRR can be enabled to protect the working tunnel.
  
  A protection tunnel cannot be protected by other tunnels or have TE FRR enabled.
* Protection switching mechanism
  
  The NE40E performs protection switching based on the following rules.
  
  **Table 1** Switching rules
  | Switching Request | Priority | Description |
  | --- | --- | --- |
  | Clear | Highest | Clears all switching requests initiated manually, including forcible and manual switch requests. A signal failure will trigger traffic switching. |
  | Lockout of protection | â | Prevents traffic from switching to a protection tunnel even if a working tunnel fails. |
  | Signal Fail for Protection | â | Switches traffic from a protection tunnel to a working tunnel if the protection tunnel fails. |
  | Forcible switch | â | Forcibly switches traffic from a working tunnel to a protection tunnel, regardless of whether the protection tunnel functions properly (unless a higher priority switch request takes effect). |
  | Signal Fail for Working | â | Switches traffic from a working tunnel to a protection tunnel if the working tunnel fails. |
  | Manual switch | â | Switches traffic from a working tunnel to a protection tunnel only when the protection tunnel functions properly or switches traffic from the protection tunnel to the working tunnel only when the working tunnel functions properly. |
  | Wait to restore | â | Switches traffic from a protection tunnel to a working tunnel after the working tunnel recovers, which happens after the wait-to-restore (WTR) timer elapses. |
  | No request | Lowest | There is no switching request. |

#### Pre-configuration Tasks

Before configuring an MPLS TE tunnel protection group, create an MPLS TE working tunnel and a protection tunnel.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* A tunnel protection group uses a configured protection tunnel to protect a working tunnel, which improves tunnel reliability. Configuring working and protection tunnels over separate links is recommended.
* The working and protection tunnels must be bidirectional. The following types of bidirectional tunnels are supported:
  
  + Static bidirectional associated LSPs
  + Dynamic bidirectional associated LSPs
  + Static bidirectional co-routed LSPs


[Creating a Tunnel Protection Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0163.html)

A configured protection tunnel can be bound to a working tunnel to form a tunnel protection group. If the working tunnel fails, traffic switches to the protection tunnel, which improves tunnel reliability.

[(Optional) Configuring the Protection Switching Trigger Mechanism](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0166.html)

This section describes how to configure the protection switching trigger mechanism for a tunnel protection group to forcibly switch traffic to the working or protection tunnel. Alternatively, you can perform a traffic switchover manually.

[Verifying the Tunnel Protection Group Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0167.html)

After configuring a tunnel protection group, run display commands to view information about the tunnel protection group and the binding between the working and protection tunnels.