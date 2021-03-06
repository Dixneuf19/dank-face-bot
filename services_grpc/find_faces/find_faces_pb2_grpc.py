# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import find_faces_pb2 as find__faces__pb2


class FindFacesStub(object):
    """The findFaces service definition.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.FindFaces = channel.unary_unary(
            "/findFaces.FindFaces/FindFaces",
            request_serializer=find__faces__pb2.FindFacesRequest.SerializeToString,
            response_deserializer=find__faces__pb2.FindFacesResponse.FromString,
        )


class FindFacesServicer(object):
    """The findFaces service definition.
  """

    def FindFaces(self, request, context):
        """Find faces from a file
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FindFacesServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "FindFaces": grpc.unary_unary_rpc_method_handler(
            servicer.FindFaces,
            request_deserializer=find__faces__pb2.FindFacesRequest.FromString,
            response_serializer=find__faces__pb2.FindFacesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "findFaces.FindFaces", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
