Configuration Precautions for MPLS OAM
======================================

Configuration_Precautions_for_MPLS_OAM

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Penultimate hop popping (PHP) cannot be configured in MPLS OAM scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MPLS OAM is configured for a tunnel, and bit-error-triggered protection switching is configured on an interface. The tunnel interface sends a backward defect indication (BDI) packet carrying defect information to the peer end through a reverse tunnel. After receiving the BDI packet, the peer end sets the status of all PWs in the tunnel to Down. As a result, service traffic is interrupted.  Suggestion 1:  1. If no protection is configured, do not enable bit-error-triggered switching on an interface.  2. In a scenario where protection is configured, bit-error-triggered protection switching is enabled only on the working path.  3. In APS non-revertive mode, bit errors may occur and traffic cannot be switched back to the working link even if the working link recovers. Therefore, you are not advised to deploy APS non-revertive mode.  Suggestion 2:  The OAM mode of the tunnel is set to 1731 (TPOAM). | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MPLS OAM single-ended frame loss measurement does not apply to the scenario where the service to be detected has multiple outbound interfaces and the outbound interfaces reside on different boards or chips. Typical scenarios: Public network load balancing or public network Eth-Trunk interfaces are used. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |