Configuration Precautions for SSL
=================================

Configuration Precautions for SSL

#### Licensing Requirements

SSL is not under license control.


#### Hardware Requirements

**Table 1** Hardware requirements
| Series | Models |
| --- | --- |
| CE6800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode) |
| CE8800 series | CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |



#### Feature Requirements

**Table 2** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Create an SSL policy. The default DH modulus is 3072, and the value can be 2048, 3072, or 4096. By default, ed25519, ed448, rsa-pss-pss-sha256, rsa-pss-pss-sha384, rsa-pss-pss-sha512, rsa-pss-rsae-sha256, rsa-pss-rsae-sha384 and rsa-pss-rsae-sha512 are enabled for signature algorithms, which can be configured separately to enhance security.  After an SSL policy is created, if the SSL handshake fails because the signature algorithm does not match or the DH modulus length is too long, run the diffie-hellman modulus command to adjust the DH modulus length or run the signature algorithm-list command to adjust the signature algorithm. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| The size of the SSL certificate file (identity certificate, CA, and CRL) cannot exceed 50 KB. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |
| When SSL certificates are used, a maximum of one certificate, four trust certificates, and two CRLs can be loaded to an SSL policy. Key files with the same name but different content cannot be loaded to different VSs.  When certificates in a PKI realm are used, an SSL policy can use a maximum of one certificate, 64 trust certificates, and 64 CRLs. | CE6800 series  CE8800 series | CE6820H-48S6CQ/CE6820S-48S6CQ/CE6820H-48S6CQ-K/CE6855-48XS8CQ/CE6860-SAN/CE6863H-48S6CQ/CE6863H-48S6CQ-K/CE6866-48S8CQ-K/CE6866-48S8CQ-P/CE6860-HAM/CE6881H-48S6CQ/CE6881H-48S6CQ-K/CE6881H-48T6CQ/CE6881H-48T6CQ-K/CE6885-48YS8CQ/CE6863E-48S8CQ/CE6885-48YS8CQ-T/CE6885-SAN-56F/CE6885-LL-56F (standard forwarding mode)/CE6885-LL-56F (low latency mode)  CE8850-SAN/CE8851-32CQ8DQ-K/CE8851-32CQ8DQ-P/CE8850-HAM/CE8855-32CQ4BQ/CE8851-32CQ4BQ |