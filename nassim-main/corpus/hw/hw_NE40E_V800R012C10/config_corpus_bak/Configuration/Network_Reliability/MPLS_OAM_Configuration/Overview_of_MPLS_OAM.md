Overview of MPLS OAM
====================

MPLS OAM can effectively detect, identify, and locate faults at the MPLS client layer and quickly switch traffic if links or nodes fail.

#### Definition

As a
key technology used on scalable next generation networks, Multiprotocol
Label Switching (MPLS) provides multiple services with quality of
service (QoS) guarantee. MPLS, however, introduces a unique network
layer, which causes faults. Therefore, MPLS networks must obtain operation,
administration and maintenance (OAM) capabilities.

OAM is an
important means to reduce network maintenance costs. The MPLS OAM
mechanism manages operation and maintenance of MPLS networks.

For details about the MPLS OAM background, see ITU-T Recommendation
Y.1710. For details about the MPLS OAM implementation mechanism, see
ITU-T Recommendation Y.1711.


#### Purpose

The server-layer
protocols, such as Synchronous Optical Network (SONET)/Synchronous
Digital Hierarchy (SDH), is below the MPLS layer; the client-layer
protocols, such as IP, FR, and ATM, is above the MPLS layer. These protocols have their
own OAM mechanisms. Failures in the MPLS network cannot be rectified
completely through the OAM mechanism of other layers. In addition,
the network technology hierarchy also requires MPLS to have its independent
OAM mechanism to decrease dependency between layers on each other.

The MPLS OAM mechanism can detect, identify, and locate a defect
at the MPLS layer effectively. Then, the MPLS OAM mechanism reports
and handles the defect. In addition, if a failure occurs, the MPLS
OAM mechanism triggers protection switching.

MPLS offers an
OAM mechanism totally independent of any upper or lower layer. The
following OAM features are enabled on the MPLS user plane:

* Monitors links connectivity.
* Evaluates network usage and performance.
* Performs a traffic switchover if a fault occurs so that services
  meet service level agreements (SLAs).

#### Benefit

* MPLS OAM can rapidly detect link faults or monitor the connectivity
  of links, which helps measure network performance and minimizes OPEX.
* If a link fault occurs, MPLS OAM rapidly switches traffic to the
  standby link to restore services, which shortens the defect duration
  and improves network reliability.


#### Basic Detection Functions

MPLS OAM can be used to check the connectivity
of an LSP.

[Figure 1](#EN-US_CONCEPT_0172362319__en-us_concept_0172351536_fig_dc_vrp_mplsoam_cfg_000301) shows
connectivity monitoring for an LSP.

**Figure 1** Connectivity monitoring for an LSP
  
![](images/fig_dc_vrp_mplsoam_cfg_000301.png)  

The working process of MPLS OAM is as follows:

1. The ingress sends a connectivity verification (CV) or fast
   failure detection (FFD) packet along an LSP to be monitored. The packet
   passes through the LSP and arrives at the egress.
2. The egress compares the packet type, frequency, and trail termination
   source identifier (TTSI) in a received packet with the locally configured
   values to verify the packet. In addition, the egress collects the
   numbers of correct and incorrect packets within a detection interval.
3. If the egress detects an LSP defect, it analyzes the defect
   type and sends a backward defect indication (BDI) packet carrying
   defect information to the ingress along a reverse tunnel. The ingress
   can then obtain the defect. If a protection group is correctly configured,
   the ingress switches traffic to a backup LSP.

#### Reverse Tunnel

A reverse tunnel is bound to an LSP that is monitored using MPLS
OAM. The reverse tunnel can transmit BDI packets to notify the ingress
of an LSP defect.

A reverse tunnel and the LSP to which the
reverse tunnel is bound must have the same endpoints.

The reverse
tunnel transmitting BDI packets can be either of the following types:

* Private reverse LSP
* Shared reverse LSP

#### MPLS OAM Auto Protocol

ITU-T Recommendation Y.1710 has some drawbacks,
for example:

* If OAM is enabled on the ingress of an LSP later than that
  on the egress or if OAM is enabled on the egress but disabled on the
  ingress, the egress generates a loss of connectivity verification
  defect (dLOCV) alarm.
* Before the OAM detection packet type or the interval at which
  detection packets are sent are changed, OAM must be disabled on the
  ingress and egress.
* OAM parameters (such as a detection packet type and an interval
  at which detection packets are sent) must be set on both the ingress
  and egress, which may cause parameter inconsistency.

The NE40E implements the OAM auto protocol to resolve these drawbacks.

The OAM auto protocol is configured on the egress. With this protocol,
the egress can automatically start OAM functions after receiving the
first OAM packet. In addition, the egress can dynamically stop running
the OAM state machine after receiving an FDI packet sent by the ingress.