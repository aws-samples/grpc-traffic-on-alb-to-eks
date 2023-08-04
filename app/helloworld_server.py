# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import grpc
from concurrent import futures
import time
import helloworld_pb2_grpc as pb2_grpc
import helloworld_pb2 as pb2
from grpc_reflection.v1alpha import reflection


class helloworldService(pb2_grpc.helloworldServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'Thanks for talking to gRPC server!!! Welcome to hello world. Received message is {message}'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_helloworldServicer_to_server(helloworldService(), server)
    SERVICE_NAMES = (
        pb2.DESCRIPTOR.services_by_name['helloworld'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:9000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()