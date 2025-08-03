Configuration Precautions for IPv6 NG MVPN
==========================================

Configuration Precautions for IPv6 NG MVPN

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| In an NG MVPN dual-root 1+1 scenario, different RDs must be configured in the VPN instance views of the two root nodes. Otherwise, dual roots cannot be formed. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In NG MVPNv6 dual-root 1+1 protection scenarios, a switchback takes effect by default. The default WTR time is 10 minutes, which can be changed using a command. This is because the WTR mechanism takes effect by default. Within 10 minutes after the primary link recovers and the BFD session for detecting the primary link goes Up, the egress selectively receives the backup traffic. After 10 minutes, the egress selectively receives the primary traffic. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In NG MVPNv6 dual-root 1+1 protection scenarios, the switchback process has the following restrictions:  1. If the backup link fails during the WTR period, fast switching is not supported. In this case, protocol convergence is required to selectively receive traffic from the primary link, which does not ensure switching performance.  2. If the standby link fails and then recovers during the WTR period, traffic needs to be switched to the standby link through protocol convergence. In this case, traffic cannot be received on the active link. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When NG-MVPNv6 dual-root 1+1 protection uses P2MP BFD to detect link faults, if the inbound interface of a leaf PE is a trunk interface, the BFD detection interval must be greater than or equal to 100 ms x 3 to prevent a false 1+1 switchover. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |