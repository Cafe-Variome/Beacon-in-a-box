import logging

LOG = logging.getLogger(__name__)


def get_filtering_terms():
    filtering_terms = [
        {
            "type": "alphanumeric",
            "id": "id",
            "label": "The id of the resource"
        },
        {
            "type": "alphanumeric",
            "id": "name",
            "label": "The resource name"
        },
        {
            "type": "alphanumeric",
            "id": "description",
            "label": "A description of the resource"
        },
        {
            "type": "alphanumeric",
            "id": "resourceTypes",
            "label": "Unique identifier of the resource"
        },
        {
            "type": "alphanumeric",
            "id": "apiVersions",
            "label": "apiVersion supported by this resource"
        }
    ]
    return filtering_terms
