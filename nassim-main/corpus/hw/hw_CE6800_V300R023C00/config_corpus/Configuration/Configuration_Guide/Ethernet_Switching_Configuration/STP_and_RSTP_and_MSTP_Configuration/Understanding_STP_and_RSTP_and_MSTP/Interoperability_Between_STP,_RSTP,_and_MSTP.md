Interoperability Between STP, RSTP, and MSTP
============================================

Interoperability Between STP, RSTP, and MSTP

#### Interoperability Between STP and RSTP

RSTP can interoperate with STP, but in doing so RSTP compromises its fast convergence.

On a network where both an STP-enabled device and an RSTP-enabled device are deployed, the former device ignores RST BPDUs. If a port on the RSTP-enabled device receives a configuration BPDU from the STP-enabled device, the port switches to the STP mode and starts to send configuration BPDUs after two Hello timer intervals.

If the STP-device is disconnected, the ports on the RSTP-enabled device cannot automatically switch back to the RSTP mode. In order to do so, you need to run a command to configure the ports to work in RSTP mode.


#### Interoperability Between MSTP and STP/RSTP

On a network where both an MSTP-enabled device and an STP-enabled device are deployed, the ports connecting the devices switch to the STP mode.

If the STP-enabled device is disconnected, the ports on the MSTP-enabled device cannot automatically switch back to the MSTP mode. In order to do so, you need to run a command to configure the ports to work in MSTP mode.

MSTP- and RSTP- enabled devices can identify BPDUs received from each other.