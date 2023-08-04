# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import grpc
import helloworld_pb2_grpc as pb2_grpc
import helloworld_pb2 as pb2


class helloworldClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'www.example.com'
        self.server_port = 443
		
		# instantiate a secure channel		
        credentials = grpc.ssl_channel_credentials()
        self.channel = grpc.secure_channel(
            '{}:{}'.format(self.host, self.server_port) , credentials)

        # bind the client and the server
        self.stub = pb2_grpc.helloworldStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = helloworldClient()
    result = client.get_url(message="Hello to gRPC server from Client")
    print(f'{result}')