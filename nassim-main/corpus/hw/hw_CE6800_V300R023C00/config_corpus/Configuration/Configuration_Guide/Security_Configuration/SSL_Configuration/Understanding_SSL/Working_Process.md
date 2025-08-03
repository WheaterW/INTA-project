Working Process
===============

Working Process

#### **Handshake Process**

A client and server set up a session using the SSL handshake protocol to verify each other's identities, as well as negotiate the keys and cipher suite. [Figure 1](#EN-US_CONCEPT_0000001513152546__fig26514918416) shows the SSL handshake process. In this process, the ChangeCipherSpec message is exchanged through the SSL change cipher spec protocol, while other messages are exchanged through the SSL handshake protocol.

The SSL server may choose not to verify the identity of the SSL client, meaning steps 4, 6, and 8 (colored blue) in [Figure 1](#EN-US_CONCEPT_0000001513152546__fig26514918416) are optional.

**Figure 1** SSL handshake process  
![](figure/en-us_image_0000001563992813.png)

1. The SSL client sends a ClientHello message carrying information, such as the supported SSL versions and cipher suites, to the SSL server beginning a handshake.
2. The SSL server sends a ServerHello message to the SSL client with the selected SSL version and cipher suite. If the SSL server allows the SSL client to reuse the current session in subsequent communication, the SSL server allocates a session ID to this session.
3. The SSL server sends a digital certificate carrying its public key to the SSL client so that the client can authenticate the server.
4. (Optional) The SSL server requires the SSL client to provide a certificate for identity authentication.
5. The server sends a ServerHelloDone message, which means the SSL version and cipher suite negotiation has finished and key information exchange can begin.
6. (Optional) The SSL client sends its own certificate to the SSL server.
7. The SSL client verifies the authenticity of the SSL server certificate, encrypts the randomly generated key using the public key in the certificate, and sends the encrypted key to the SSL server.
   
   The randomly generated key (premaster secret) cannot be directly used to encrypt data or compute MACs. It is used to compute the symmetric key for encryption and decryption and MACs for data integrity verification. The SSL client and server use the premaster secret to compute the same master secret, and then based on this, use a symmetric key algorithm to compute the symmetric key and MACs. Therefore, the premaster secret plays a crucial role in calculating the symmetric key and MACs.
8. (Optional) The SSL client sends its certificate to the server for identity authentication.
   
   The client computes a hash value for the master secret over exchanged handshake messages, encrypts the hash value using its private key, and then sends a CertificateVerify message to the server. The server computes a hash value for the master secret over exchanged handshake messages, decrypts the received CertificateVerify message using the public key in the client's certificate, and compares the decrypted result with the computed hash value. If the two values are the same, client authentication succeeds.
9. The SSL client notifies the SSL server that subsequent packets will be encrypted and MACs will be computed using the negotiated key (generated based on the master secret) and cipher suite.
10. The client instructs the server to verify that the SSL negotiation has been successful.
    
    The client computes a hash value over exchanged handshake messages, uses the negotiated key and cipher suite to process the hash value, and sends a Finished message containing the hash value and MACs to the server. The server computes a hash value in the same way, decrypts the received Finished message, and verifies the hash value and MACs. If the verification succeeds, the key and cipher suite negotiation is successful.
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    Computing a hash value means that a hash algorithm (MD5 or SHA) is used to convert an arbitrary-length message to a fixed-length message.
11. The SSL server notifies the SSL client that subsequent packets will be encrypted and MACs will be computed using the negotiated key (generated based on the master secret) and cipher suite.
12. The server instructs the client to verify that the SSL negotiation has been successful.
    
    The server computes a hash value over exchanged handshake messages, uses the negotiated key and cipher suite to process the hash value, and sends a Finished message containing the hash value and MACs to the client. The client computes a hash value in the same way, decrypts the received Finished message, and verifies the hash value and MACs. If the verification succeeds, the key and cipher suite negotiation is successful.

Successful SSL negotiation indicates that the SSL server passes the SSL client's identity authentication. The SSL server can decrypt the ClientKeyExchange message to obtain the premaster secret only after it obtains the private key of the client.

In the SSL handshake process, an asymmetric key algorithm is used to encrypt keys and authenticate the identities of the communicating parties. It involves heavy computation workload and consumes a lot of system resources. To simplify the SSL handshake process, SSL allows resumed sessions, as shown in [Figure 2](#EN-US_CONCEPT_0000001513152546__fig19637162412434).

**Figure 2** SSL handshake process for resuming a session  
![](figure/en-us_image_0000001513152562.png)

1. The SSL client sends a ClientHello message to the SSL server. The session ID in this message is set to the ID of the session to be resumed.
2. If the server allows this session to be resumed, it replies with a ServerHello message with the same session ID. After that, the client and server can use the key and cipher suite of the resumed session without further negotiation.
3. The client sends a ChangeCipherSpec message to notify the server that subsequent messages will be encrypted and MACs will be computed based on the key and cipher suite negotiated for the resumed session.
4. The client computes a hash value over exchanged handshake messages, uses the key and cipher suite negotiated for the resumed session to process the hash value, and then sends a Finished message to the server so that it can check whether the key and cipher suite are correct.
5. Similarly, the server sends a ChangeCipherSpec message to notify the client that subsequent messages will be encrypted and MACs will be computed based on the key and cipher suite negotiated for the resumed session.
6. The server computes a hash value over exchanged handshake messages, uses the key and cipher suite negotiated for the resumed session to process the hash value, and then sends a Finished message to the client so that it can check whether the key and cipher suite are correct.

#### Data Transmission Process

After the handshake is complete, the client and server can exchange application layer data. Data transmission is implemented using the SSL record protocol.

[Figure 3](#EN-US_CONCEPT_0000001513152546__fig465814964414) shows the data transmission process. The SSL record protocol fragments the application data to be transmitted into manageable blocks, compresses the data (optional), adds a MAC to the end of each block, encrypts the block using an encryption algorithm, and then adds an SSL record header to the encrypted block. In reverse order, the receiver decrypts, verifies, decompresses, and reassembles the received message to obtain clear-text data.

**Figure 3** Data transmission process  
![](figure/en-us_image_0000001563752909.png)