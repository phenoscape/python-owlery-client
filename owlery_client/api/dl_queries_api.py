# coding: utf-8

"""
    Owlery API

    Owlery provides a web API for an [OWL API](http://owlapi.sourceforge.net)-based reasoner containing a configurable set of ontologies (a \"knowledgebase\").   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: balhoff@renci.org
    Generated by: https://openapi-generator.tech
"""

from owlery_client.api_client import ApiClient
from owlery_client.api.dl_queries_api_endpoints.kbs_kb_equivalent_get import KbsKbEquivalentGet
from owlery_client.api.dl_queries_api_endpoints.kbs_kb_instances_get import KbsKbInstancesGet
from owlery_client.api.dl_queries_api_endpoints.kbs_kb_satisfiable_get import KbsKbSatisfiableGet
from owlery_client.api.dl_queries_api_endpoints.kbs_kb_subclasses_get import KbsKbSubclassesGet
from owlery_client.api.dl_queries_api_endpoints.kbs_kb_superclasses_get import KbsKbSuperclassesGet
from owlery_client.api.dl_queries_api_endpoints.kbs_kb_types_get import KbsKbTypesGet


class DLQueriesApi(
    KbsKbEquivalentGet,
    KbsKbInstancesGet,
    KbsKbSatisfiableGet,
    KbsKbSubclassesGet,
    KbsKbSuperclassesGet,
    KbsKbTypesGet,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass