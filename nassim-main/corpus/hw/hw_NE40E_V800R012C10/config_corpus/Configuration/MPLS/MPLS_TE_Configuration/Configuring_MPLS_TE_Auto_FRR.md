Configuring MPLS TE Auto FRR
============================

MPLS TE Auto FRR is a local protection mechanism that protects traffic on a link or a node of a CR-LSP.

#### Usage Scenario

On a network that requires high reliability, FRR is configured to improve network reliability. If the network topology is complex and a great number of links must be configured, the configuration procedure is complex.

Auto FRR automatically establishes an eligible bypass tunnel, reducing the configuration workload.

MPLS TE Auto FRR, similar to MPLS TE manual FRR, can be performed in the RSVP GR process. For details about MPLS TE manual FRR, see [Configuring MPLS TE Manual FRR](dc_vrp_te-p2p_cfg_0048.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only a primary CR-LSP supports MPLS TE Auto FRR.


In this example, a bypass tunnel with a higher priority is available on the NE40E. MPLS TE Auto FRR automatically deletes a binding between a primary tunnel and a bypass tunnel with a lower priority and binds the primary tunnel to another bypass tunnel with a higher priority. A bypass tunnel has a higher priority than another based on the following conditions in descending order:

* SRLG
  
  In MPLS TE Auto FRR, if the shared risk link group (SRLG) attribute is configured, the primary and bypass tunnels must be in different SRLGs. If they are in the same SRLG, the bypass tunnel cannot be established.
* Bandwidth protection takes precedence over non-bandwidth protection.
* Node protection takes precedence over link protection.
* Manual protection takes precedence over auto protection.


#### Pre-configuration Tasks

Before configuring MPLS TE Auto FRR, complete the following tasks:

* Set up a primary RSVP-TE tunnel.
* Enable MPLS, MPLS TE, and RSVP-TE in the system and interface views on every node along a bypass tunnel. (See [Enabling MPLS TE and RSVP-TE](dc_vrp_te-p2p_cfg_0004.html).)
* Enable CSPF on the ingress and transit nodes along a primary tunnel.
* (Optional) Configure the physical bandwidth for a bypass tunnel if the primary tunnel bandwidth needs to be protected. (See [(Optional) Configuring TE Attributes](dc_vrp_te-p2p_cfg_0006.html).)


[Enabling TE Auto FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0054.html)

TE Auto FRR must be enabled on the PLR of the bypass tunnel before the function is configured.

[Enabling TE FRR and Configuring Attributes for an Automatic Bypass LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0055.html)

After MPLS TE FRR is enabled on the ingress of a primary LSP, a bypass LSP is established automatically.

[(Optional) Configuring Auto Bypass Tunnel Re-Optimization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0185.html)

Auto bypass tunnel re-optimization allows paths to be recalculated at certain intervals for an auto bypass tunnel. If an optimal path is recalculated, a new auto bypass tunnel will be set up over this optimal path. In this manner, network resources are optimized.

[Verifying the MPLS TE Auto FRR Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0056.html)

After configuring MPLS TE Auto FRR, you can view detailed information about the bypass tunnel.