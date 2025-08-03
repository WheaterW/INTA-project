Configuration Precautions for iNOF
==================================

Configuration Precautions for iNOF

#### Licensing Requirements

iNOF is under license control (CE-LIC-iNOF).


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6860-SAN/CE6885-SAN-56F/CE6860-HAM/CE6866-48S8CQ-K/CE6866-48S8CQ-P |
| CE8800 series | CE8850-SAN/CE8850-HAM/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |



#### Feature Requirements

**Table 2** Feature requirements
| Feature | Feature Requirements | Series | Models |
| --- | --- | --- | --- |
| RPFR | 1. If the Layer 3 logical interfaces corresponding to the access interfaces fail at the same time, there is a high probability that RPFR proxy fails.  2. There is a 5% probability that RPFR proxy fails. | CE6800 series  CE8800 series | CE6860-SAN/CE6885-SAN-56F  CE8850-SAN |
| RPFR | RPFR and NPCC are mutually exclusive. | CE6800 series  CE8800 series | CE6860-SAN  CE8850-SAN |
| Plug-and-Play Storage Service | The communication port number of the iNOF function must be the same on the entire network. The default TCP listening port number is 19516. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Plug-and-Play Storage Service | If two iNOF reflectors exist in an iNOF system, they must be specified as each other's client. In addition, other clients configured using the peer reflect-client command on the two reflectors must be the same. In this way, the two reflectors can back up each other to enhance the reliability of the iNOF system. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Plug-and-Play Storage Service | 1. If traffic matches both the iNOF zone isolation function and NPCC, the iNOF zone isolation function takes effect preferentially.  2. The client does not support the hard zoning function. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Plug-and-Play Storage Service | The global configurations of IPv4 iNOF and IPv6 iNOF are independent of each other. The data synchronized from the respective reflector prevails. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Plug-and-Play Storage Service | The AI Fabric feature package contains the AI ECN and iNOF features, which are included in the basic software package. By default, the basic software package contains the AI ECN and iNOF features. The AI Fabric feature package cannot be installed using the install feature-software command or uninstalled using the uninstall feature-software command. The AI Fabric feature package can be upgraded. To upgrade it, log in to the Huawei technical support website, search for the corresponding product and version in the software download zone, and download the AI Fabric feature package and corresponding documentation. For details about how to install and upgrade the feature package, see "Upgrade Maintenance Configuration" in Configuration Guide > System Management Configuration. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |
| Plug-and-Play Storage Service | The IPv4 address of the iNOF cannot be set to a non-class A/B/C address or a loopback address.  The IPv6 address of the iNOF cannot be set to a link-local address, multicast address, unspecified address, or loopback address. | CE6800 series  CE8800 series | CE6860-HAM/CE6860-SAN/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6885-SAN-56F  CE8850-HAM/CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P |